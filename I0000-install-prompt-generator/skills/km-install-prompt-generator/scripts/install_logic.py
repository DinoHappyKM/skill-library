"""離線可執行的保守合併判斷；不是 ChatGPT 帳號 API。"""
import hashlib, re
from functools import cmp_to_key
PLUGIN_NAME = "黃嘉偉KM"
def sha(data):
    return hashlib.sha256(data).hexdigest()
def normalized_sha(data):
    return sha(data.decode("utf-8-sig").replace("\r\n","\n").replace("\r","\n").encode("utf-8"))
def semver(v):
    m=re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?(?:\+([0-9A-Za-z.-]+))?",v or "")
    if not m: raise ValueError("不是有效的版本號："+str(v))
    pre=m[4].split(".") if m[4] else []
    if any(not x or (x.isdigit() and len(x)>1 and x[0]=="0") for x in pre): raise ValueError("預發行版本不合法")
    if m[5] and any(not x for x in m[5].split(".")): raise ValueError("建置版本不合法")
    return tuple(map(int,m.group(1,2,3))),pre
def compare(a,b):
    aa,ap=semver(a); bb,bp=semver(b)
    if aa!=bb: return (aa>bb)-(aa<bb)
    if not ap or not bp: return (bool(bp)>bool(ap))-(bool(bp)<bool(ap))
    for x,y in zip(ap,bp):
        if x==y: continue
        if x.isdigit() and y.isdigit(): return (int(x)>int(y))-(int(x)<int(y))
        if x.isdigit()!=y.isdigit(): return -1 if x.isdigit() else 1
        return (x>y)-(x<y)
    return (len(ap)>len(bp))-(len(ap)<len(bp))
def decide(target,actual,receipt=None):
    """actual/receipt：version、hashes。hashes 是必要檔案的實際 SHA256。"""
    if actual is None: return "add"
    same=actual["hashes"]==target["hashes"]
    if same:
        if actual.get("version") not in (None,target.get("version")): return "confirm"
        return "keep"
    # 公開記錄的官方無版號舊檔，可用完整兩檔SHA核對後安全升級。
    if any(actual.get("version")==p.get("version") and actual["hashes"]==p.get("hashes") for p in target.get("official_predecessors",[])):
        return "update"
    if not receipt or actual["hashes"]!=receipt.get("installed_hashes",receipt.get("hashes")) or actual.get("version")!=receipt.get("version"):
        return "confirm"
    old,new=actual.get("version"),target.get("version")
    if old is None or new is None: return "confirm"
    return "update" if compare(old,new)<0 else "confirm"
def plan(plugins,selected,capabilities,inventory_complete=True):
    if not inventory_complete or not capabilities.get("list") or not capabilities.get("read"):
        return {"status":"blocked","reason":"無法完整核對帳號外掛與內容"}
    matches=[x for x in plugins if x.get("display_name")==PLUGIN_NAME]
    if len(matches)>1: return {"status":"confirm","reason":"有多個同名外掛，須指定 ID"}
    plugin=matches[0] if matches else None
    if not capabilities.get("creator"):
        return {"status":"blocked","reason":"帳號沒有 Plugin Creator 建立／編輯能力"}
    if plugin and not plugin.get("can_edit"):
        return {"status":"blocked","reason":"沒有目標外掛編輯權限"}
    if not plugin and not capabilities.get("create"):
        return {"status":"blocked","reason":"沒有建立權限"}
    actions={}
    for target in selected:
        if target["role"]!="student_skill": raise ValueError("學生選取不得包含教師工具或主選單")
        actions[target["id"]]=decide(target,(plugin or {}).get("skills",{}).get(target["slug"]),(plugin or {}).get("receipts",{}).get(target["slug"]))
    if "confirm" in actions.values(): return {"status":"confirm","plugin_id":(plugin or {}).get("id"),"actions":actions}
    changes=not plugin or any(x!="keep" for x in actions.values()) or not plugin.get("menu_ok",False)
    if changes and (not capabilities.get("save") or (plugin and not capabilities.get("edit"))):
        return {"status":"blocked","reason":"沒有更新／儲存權限","actions":actions}
    return {"status":"ready" if changes else "unchanged","plugin_id":(plugin or {}).get("id"),"create":not bool(plugin),"actions":actions}

def merge_registry(existing,selected):
    """保留自訂項目；同id異slug或同slug異id必須先確認。"""
    import copy
    result=copy.deepcopy(existing)
    for item in selected:
        hits=[i for i,x in enumerate(result) if x.get("id")==item["id"] or x.get("skill_slug")==item["slug"]]
        if len(hits)>1 or (hits and (result[hits[0]].get("id")!=item["id"] or result[hits[0]].get("skill_slug")!=item["slug"])):
            raise ValueError("主選單代號／slug衝突")
        row={"id":item["id"],"name":item["name"],"skill_slug":item["slug"],"category_id":item["category"]["id"],
             "subcategory_id":None,"summary":item.get("summary",item["name"]),"tags":item.get("tags",[]),
             "source_version":item["version"],"registration":"已核對"}
        if hits: result[hits[0]].update(row) # 自訂擴充欄位保留
        else: result.append(row)
    return result
def simulate_apply(plugin,selected,decision,source_files,menu_files,expected_release):
    """離線交易模型；不呼叫雲端，不把此結果視為Plugin已儲存。"""
    import copy,json
    if decision["status"] not in ("ready","unchanged"): raise ValueError("尚未取得可執行計畫")
    if plugin and plugin["release"]!=expected_release: raise ValueError("release已改變，須重新比較")
    # 全部來源核對完成才產生新樹；失敗不修改輸入。
    for item in selected:
        for path,digest in item["hashes"].items():
            if path not in source_files or sha(source_files[path])!=digest: raise ValueError("來源缺漏或校驗不一致")
    if decision["status"]=="unchanged":return copy.deepcopy(plugin)
    result=copy.deepcopy(plugin) if plugin else {"id":"local-simulation-only","display_name":PLUGIN_NAME,"release":"new-local","can_edit":True,"version":"0.0.0","files":{},"settings":{},"skills":{},"receipts":{},"registry":[]}
    result["registry"]=merge_registry(result.get("registry",[]),selected)
    for item in selected:
        if decision["actions"][item["id"]]=="keep":continue
        for path in item["hashes"]:result["files"][path]=source_files[path]
        actual={"version":item["version"],"hashes":item["hashes"]}
        result["skills"][item["slug"]]=copy.deepcopy(actual)
        result["receipts"][item["slug"]]=copy.deepcopy(actual)
    # 主選單以JSON（有效YAML）快照嵌入，避免空模板覆蓋既有清單。
    for path,data in menu_files.items():
        if path.endswith("SKILL.md"):
            text=data.decode("utf-8")
            snap={"menu_version":"0.4.0","plugin_display_name":PLUGIN_NAME,"skills":result["registry"]}
            pat=r"<!-- KM-REGISTRY-BEGIN -->.*?<!-- KM-REGISTRY-END -->"
            text,n=re.subn(pat,"<!-- KM-REGISTRY-BEGIN -->\n~~~yaml\n"+json.dumps(snap,ensure_ascii=False,indent=2)+"\n~~~\n<!-- KM-REGISTRY-END -->",text,flags=re.S)
            if n!=1:raise ValueError("主選單模板快照區不存在或重複")
            data=text.encode("utf-8")
        result["files"][path]=data
    result["menu_ok"]=True
    version,pre=semver(result["version"])
    if pre:raise ValueError("預發行Plugin版本須由實際平台確認")
    result["version"]=".".join(map(str,(version[0],version[1],version[2]+1)))
    result["release"]="local-simulation:"+result["version"]
    return result
