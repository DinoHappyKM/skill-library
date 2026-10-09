"""從最新 GitHub commit 或已核對本機資料庫產生手機提示詞。"""
import argparse,base64,json,re,sys,urllib.request,urllib.parse
from pathlib import Path
from install_logic import sha,semver
REPO="DinoHappyKM/skill-library"
CONFIG=Path(__file__).resolve().parents[1]/"assets/source-config.json"
def request(path):
    req=urllib.request.Request("https://api.github.com/repos/"+REPO+"/"+path,headers={"User-Agent":"Huang-KM-installer","Accept":"application/vnd.github+json"})
    with urllib.request.urlopen(req,timeout=45) as f: return json.load(f)
def safe_path(path):
    pp=Path(path)
    if path.startswith("/") or pp.is_absolute() or "\\" in path or ".." in pp.parts or ":" in path: raise ValueError("不安全來源路徑")
    return path
def read_remote(path,ref):
    obj=request("contents/"+urllib.parse.quote(safe_path(path),safe="/")+"?ref="+urllib.parse.quote(ref,safe=""))
    if obj.get("encoding")!="base64": raise ValueError("無法取得完整 GitHub 內容："+path)
    data=base64.b64decode(obj["content"])
    if len(data)!=obj["size"]: raise ValueError("來源長度不一致："+path)
    return data
def load(repo_root=None,ref=None):
    cfg=json.loads(CONFIG.read_text(encoding="utf-8"))
    ref=ref or cfg["default_ref"]
    if repo_root:
        root=Path(repo_root).resolve()
        def reader(path):
            q=(root/safe_path(path)).resolve()
            if not q.is_relative_to(root): raise ValueError("來源超出資料庫")
            return q.read_bytes()
        commit="local-unpublished"
    else:
        commit=request("commits/"+urllib.parse.quote(ref,safe=""))["sha"]
        if not re.fullmatch("[0-9a-f]{40}",commit): raise ValueError("commit 不合法")
        reader=lambda path:read_remote(path,commit)
    catalog=json.loads(reader("skills-catalog.json"))
    if catalog.get("schema_version")!="1.0.0" or catalog.get("plugin_display_name")!="黃嘉偉KM":
        raise ValueError("不支援的目錄或外掛名稱")
    return catalog,reader,commit,ref
def select(catalog,query):
    result=[]
    for token in re.split(r"[,，、\n]+",query):
        token=token.strip()
        if not token: continue
        m=re.fullmatch(r"[iI]?(\d+)",token)
        key="I"+m[1].zfill(4) if m else token
        hits=[e for e in catalog["skills"] if e["role"]=="student_skill" and key in (e["id"],e["name"],e["slug"])]
        if len(hits)!=1: raise ValueError("未知或不唯一的學生技能："+token)
        if hits[0] not in result: result.append(hits[0])
    if not result: raise ValueError("請選取至少一支工作技能")
    return result
def files_for(entry,reader,commit,ref,embedded):
    files=[]
    for item in entry["required_files"]:
        path=safe_path(item["path"]); data=reader(path)
        if len(data)!=item["bytes"] or sha(data)!=item["sha256"]: raise ValueError("來源校驗失敗："+path)
        file={"source_url":"https://github.com/"+REPO+"/blob/"+(commit if commit!="local-unpublished" else ref)+"/"+path,
              "target_path":item["target_path"],"sha256":item["sha256"],"bytes":item["bytes"],
              "normalized_text_sha256":item["normalized_text_sha256"]}
        if embedded: file["content"]=data.decode("utf-8")
        files.append(file)
    return {"id":entry["id"],"name":entry["name"],"slug":entry["slug"],"role":entry["role"],
            "version":entry["version"],"official_predecessors":entry.get("official_predecessors",[]),"category":entry["category"],"summary":entry.get("summary",entry["name"]),"tags":entry.get("tags",[]),"files":files}
RULES="""請使用本帳號實際可用的 Plugin Creator，建立或更新「黃嘉偉KM」，安裝下方選取的工作技能。這次是安裝，不要執行貼文、直播或產圖。

【一、權限與正確對象】
先完整列出可用外掛，讀取實際外掛 ID、外掛層級 displayName、目前 release、版本、完整檔案及權限。名稱一律為「黃嘉偉KM」；「0｜主選單」只是技能標籤，不能當外掛名稱。
沒有黃嘉偉KM且有建立／儲存權限：建立此名稱的新 Plugin，加入本提示詞的主選單及指定技能。
已有黃嘉偉KM：沿用同一 ID。多個同名：只問一次讓我指定 ID。目前編輯的是另一個私人 KM 時，切換正確目標；不得修改或覆蓋我的私人 KM。
清單讀不到不能當成「沒有」。缺少建立、編輯、讀取或儲存能力時，明確回報工具及權限限制，不宣稱已安裝，不猜免費版是否支援。
初建可依當前 Creator 支援的 manifest 建立；外掛人類顯示名稱須是黃嘉偉KM，內部 name 使用有效小寫識別字。root plugin.json 的標準欄位及 extensions.com.openai.interface.displayName 依工具格式處理，不把技能 YAML 的 display_name 當外掛名稱。

【二、取得完整正式內容】
下方 JSON 是本次已由老師核對的來源快照。主選單兩檔已內嵌，不必另抓選單網址。工作技能若含 content，原樣取用完整文字；若只有 source_url，完整讀取該支的 SKILL.md 與 agents/openai.yaml 兩檔。依固定 commit 取得，禁止自行改用其他版本。多支可依支次序取得；不是限制帳號只能讀二個檔案的宣稱。
GitHub 檔案頁全文讀得到即可；Raw 失敗可用已授權 GitHub 工具或同一檔案分段讀取。不要為補資料去找第三個 IMPORT、references、README 或老師的範例 plugin.json。不要用搜尋摘要、舊對話、目錄或自行補寫的技能代替原文。
先取得所有本次必要檔案才開始合併。可計算 SHA256 時校對 JSON 中 bytes 與原始校驗值；若網頁只轉換換行或 BOM，使用 normalized_text_sha256（只去 UTF8 BOM、CRLF/CR轉LF，不刪其他空白）。不能計算就清楚標記「完整內容回讀核對，雜湊待驗證」，不得聲稱校驗已通過。來源截斷、缺檔或內容不符：停止儲存，說明實際失敗；請老師用 I0000 產生「完整原文模式」同一提示詞直接貼文字，不要求 ZIP，不強迫學生讀第三份檔案。

【三、比較版本並保留個人內容】
技能版本以 SKILL.md 的宣告為準；version:null 代表未宣告，不能借外掛版本或範例 manifest 猜一個。
不存在：新增到 JSON 的 target_path。
內容相同且版本一致或原文未宣告：保留同一技能，不新增副本。
版本較舊且能確認仍是老師原版：更新同一 slug。確認方式是實際檔案符合 km-installed-skills.json 的原版安裝校驗值，或已完整核對相應歷史官方版本；單看舊版本號不足以確認未客製。
對首次補版本的技能，若已安裝檔案的完整兩檔 SHA256 與本次 official_predecessors 中同一筆舊官方版完全相同，即可視為可核對舊版更新；任一檔不同或無法完整讀取，先確認，不以外掛版本推定。
版本相同但內容不同、比老師更新、版本未知且內容不同、缺少可信原版基準、同代號／slug 衝突、個人修改：列差異先確認，不覆蓋。比較使用語意版本，0.1.10 高於 0.1.9。
先讀實際檔案，安裝紀錄不能代替回讀。不得把規則、正式原文或 YAML 簡化成摘要。保留原本所有其他技能、附件、資產、整合、外掛 ID、scope、分享、作者及啟動設定。沿用現有 manifest，不用老師整份範例覆蓋；若舊 manifest 需遷移，先保留有效設定並核對，不能用空白新 manifest 遮蔽原有設定。不要改動自己私人 KM。

【四、主選單與合併】
主選單固定 skills/km-menu，名稱「0｜主選單」，標頭「黃嘉偉KM」；裸數字0/00/0000是主選單，I0000是老師工具且不安裝給學生。
主選單模板的 skills:[] 只是初始空範本，不能清空已安裝快照。讀原 KM-REGISTRY-BEGIN／END 區與實際工作檔，保留所有自訂及其他已核對項目，只合併本次實際加入的技能；版本取本次原文，未知填 null，已寫入且回讀成功才標 registration:已核對。
已有舊版主選單且是可核對官方規則：更新官方規則，保留快照與自訂資料。主選單有個人改寫或無法解析快照時先確認，不能清空。模板中的中文分類和 I 代號保持固定；只列實際收錄，不能把老師總庫當作全已安裝。
依每筆 id/name/slug/category/summary/tags/version 登錄 id、name、skill_slug、category_id、subcategory_id:null、summary、tags、source_version、registration。只改本次必要主選單資料。
建立或更新 root km-installed-skills.json，合併其他既有紀錄，記下每支的 id、slug、version、來源 commit、來源校驗值與實際安裝內容校驗值。主選單因快照合併而異於空模板時分別記下模板與安裝後校驗值；不把版本目錄等同安裝紀錄。

【五、儲存及驗證】
儲存前重新確認目標 ID 和 release 未變；有並行修改就重新比較，禁止覆蓋他人更新。同一個新 release 一起保存本次必要檔案、合併後主選單和安裝紀錄；有實際修改才依有效語意版本提高 Plugin 版本，完全相同則不儲存不升版。
如需我按確認／儲存／更新，指出實際按鈕。依工具結果回讀已儲存的 release、檔案內容、外掛名稱、主選單登錄，確認其他技能及原有設定保留。草稿／檔案生成不是已儲存；驗證失敗要據實回報。
最後分別回報：來源完整性與校驗狀態、每支新增/更新/保留/待確認、外掛實際 ID/名稱/版本、儲存狀態、待測項目。
提供新對話測試：選用黃嘉偉KM後分次輸入0、分類、分類代號及本次 I 代號，確認接續正式技能流程；未在本帳號實測就標「待測」。不承諾 GitHub 更新自動同步或手機安裝成功。

【老師核對的本次來源快照】
"""
def generate(catalog,reader,commit,ref,query,mode="paths"):
    chosen=select(catalog,query)
    menus=[e for e in catalog["skills"] if e["role"]=="menu"]
    if len(menus)!=1: raise ValueError("需要唯一主選單")
    payload={"plugin_display_name":"黃嘉偉KM","source_repository":REPO,"source_commit":commit,
             "source_ref":ref,"live_install_tested":False,
             "menu":files_for(menus[0],reader,commit,ref,True),
             "selected_skills":[files_for(e,reader,commit,ref,mode=="embedded") for e in chosen]}
    return RULES+json.dumps(payload,ensure_ascii=False,indent=2),payload
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--skills",required=True)
    ap.add_argument("--repo-root"); ap.add_argument("--ref")
    ap.add_argument("--mode",choices=["paths","embedded"],default="paths")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    catalog,reader,commit,ref=load(a.repo_root,a.ref)
    text,payload=generate(catalog,reader,commit,ref,a.skills,a.mode)
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes((text.rstrip()+"\n\n").replace("\r\n","\n").replace("\n","\r\n").encode("utf-8"))
    print(json.dumps({"output":str(out),"source_commit":commit,"ids":[x["id"] for x in payload["selected_skills"]],"mode":a.mode},ensure_ascii=False))
if __name__=="__main__": main()
