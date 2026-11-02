"""Offline lookup of the preserved I0009 marketing library; no external services."""
from pathlib import Path
import argparse,json,re,sys
LIBRARY=Path(__file__).resolve().parents[1]/'references/decision-library.json'

def normalize_module(value):
 token=value.strip().upper()
 if not re.fullmatch(r'(?:MK|M)(?:0[1-9]|[1-3][0-9]|40)',token):raise ValueError('請使用MK01～MK40；本工具不解析KMW流程M代號')
 return 'MK'+token.lstrip('MK')

def load_library(path=LIBRARY):return json.loads(Path(path).read_text(encoding='utf-8'))

def validate(lib):
 errors=[];modules={r['fields']['模組ID'] for r in lib['modules']};cases={r['fields']['案例ID'] for r in lib['cases']}
 if modules!={f'MK{i:02}' for i in range(1,41)} or len(lib['modules'])!=40:errors.append('module IDs must be unique MK01..MK40')
 if len(cases)!=len(lib['cases']):errors.append('duplicate case IDs')
 for link in lib['case_links']:
  f=link['fields']
  if f['模組ID'] not in modules or f['案例ID'] not in cases:errors.append('orphan '+str(link['source']))
 for kind in ('cases','strategy_templates','day90_template'):
  for r in lib[kind]:
   for value in r['fields'].values():
    for code in re.findall(r'(?<![A-Za-z0-9])MK\d{2}(?!\d)',value):
     if code not in modules:errors.append('unknown '+code)
    if re.search(r'(?<![A-Za-z0-9])M\d{2}(?!\d)',value):errors.append('unconverted legacy ID '+str(r['source']))
 return errors

def query_module(lib,value):
 code=normalize_module(value);record=next(r for r in lib['modules'] if r['fields']['模組ID']==code)
 links=[r for r in lib['case_links'] if r['fields']['模組ID']==code];ids={r['fields']['案例ID'] for r in links}
 return {'module':record,'case_links':links,'cases':[r for r in lib['cases'] if r['fields']['案例ID'] in ids],'strategy_templates':[r for r in lib['strategy_templates'] if code in re.findall(r'MK\d{2}',r['fields']['模組組合'])],'evidence_status':lib['case_evidence_status']}

def main():
 parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group(required=True)
 group.add_argument('--module');group.add_argument('--case');group.add_argument('--strategy');group.add_argument('--check',action='store_true');args=parser.parse_args();lib=load_library()
 try:
  if args.check:
   errors=validate(lib);result={'passed':not errors,'errors':errors,'counts':{k:len(lib[k]) for k in ('modules','cases','case_links','strategy_templates','day90_template')}}
   print(json.dumps(result,ensure_ascii=False,indent=2));return int(bool(errors))
  if args.module:result=query_module(lib,args.module)
  else:
   key,field,value=('cases','案例ID',args.case.upper()) if args.case else ('strategy_templates','模板ID',args.strategy.upper())
   result=next((r for r in lib[key] if r['fields'][field]==value),None)
   if result is None:raise ValueError('資料庫沒有這個編號：'+value)
  print(json.dumps(result,ensure_ascii=False,indent=2));return 0
 except (ValueError,StopIteration) as exc:
  print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
