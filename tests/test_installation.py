import copy,hashlib,importlib.util,json,re,sys,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
S=R/"I0000-install-prompt-generator/skills/km-install-prompt-generator/scripts"
sys.path.insert(0,str(S))
from install_logic import sha,normalized_sha,compare,decide,plan,merge_registry,simulate_apply
from generate_install_prompt import load,select,generate,safe_path,files_for
CAT=json.loads((R/"skills-catalog.json").read_text(encoding="utf-8"))
WORK=[x for x in CAT["skills"] if x["role"]=="student_skill"]
MENU=next(x for x in CAT["skills"] if x["role"]=="menu")
CAP={x:True for x in ("list","read","creator","create","edit","save")}
def target(i=0):return copy.deepcopy(WORK[i])
def installed(e,version=None,hashes=None):
    return {"version":e["version"] if version is None else version,"hashes":copy.deepcopy(e["hashes"] if hashes is None else hashes)}
def plugin():
    e=target();actual=installed(e)
    return {"id":"existing-target","display_name":"黃嘉偉KM","can_edit":True,"menu_ok":True,"version":"1.0.1","release":"release-original",
      "skills":{e["slug"]:actual},"receipts":{e["slug"]:copy.deepcopy(actual)},
      "registry":[{"id":"K01","name":"自訂直播","skill_slug":"custom-live","category_id":"C05","registration":"已核對","custom":"keep"}],
      "files":{"assets/photo.png":b"\x00original-photo","skills/custom-live/SKILL.md":b"custom original","plugin.json":b'{"name":"existing-name","defaultPrompt":["keep"]}'},
      "settings":{"scope":"USER","visibility":"PRIVATE","integrations":["original"],"defaultPrompt":["custom startup"]}}
def sources(es):
    return {f["target_path"]:(R/f["path"]).read_bytes() for e in es for f in e["required_files"]}
class Scenarios(unittest.TestCase):
    def test_01_no_plugin_create(self):
        out=plan([], [target()], CAP)
        self.assertEqual(out["status"],"ready");self.assertTrue(out["create"])
        p=simulate_apply(None,[target()],out,sources([target()]),sources([MENU]),None)
        self.assertEqual(p["display_name"],"黃嘉偉KM");self.assertEqual(len(p["registry"]),1)
    def test_02_existing_same_id(self):
        p=plugin();out=plan([p],[target(2)],CAP)
        self.assertEqual(out["plugin_id"],p["id"])
        applied=simulate_apply(p,[target(2)],out,sources([target(2)]),sources([MENU]),p["release"])
        self.assertEqual(applied["id"],p["id"]);self.assertEqual(applied["settings"],p["settings"])
        for f in p["files"]:self.assertEqual(applied["files"][f],p["files"][f])
        self.assertEqual(applied["registry"][0],p["registry"][0])
    def test_03_only_missing_subset(self):
        p=plugin();out=plan([p],[target(),target(2)],CAP)
        self.assertEqual(out["actions"],{"I0001":"keep","I0003":"add"})
    def test_04_old_official(self):
        p=plugin();slug=target()["slug"];old={"version":"0.2.2","hashes":{"old":"verified-baseline"}}
        p["skills"][slug]=copy.deepcopy(old);p["receipts"][slug]=copy.deepcopy(old)
        out=plan([p],[target()],CAP);self.assertEqual(out["actions"]["I0001"],"update")
    def test_05_latest_noop(self):
        p=plugin();out=plan([p],[target()],CAP)
        self.assertEqual(out["status"],"unchanged")
        self.assertEqual(simulate_apply(p,[target()],out,sources([target()]),sources([MENU]),p["release"]),p)
    def test_06_separate_private_km(self):
        private=plugin();private["id"]="personal";private["display_name"]="王同學私人KM";original=copy.deepcopy(private)
        out=plan([private,plugin()],[target(2)],CAP)
        self.assertEqual(out["plugin_id"],"existing-target");self.assertEqual(private,original)
        self.assertTrue(plan([private],[target()],CAP)["create"])
    def test_07_no_creator(self):
        cap=dict(CAP,creator=False);self.assertEqual(plan([], [target()],cap)["status"],"blocked")
        self.assertEqual(plan([plugin()],[target()],cap)["status"],"blocked")
    def test_personal_modified(self):
        p=plugin();p["skills"][target()["slug"]]["hashes"]={"changed":"personal"}
        self.assertEqual(plan([p],[target()],CAP)["status"],"confirm")
    def test_same_version_different_content(self):
        t=target();a=installed(t,hashes={"modified":"different"})
        self.assertEqual(decide(t,a,a),"confirm")
    def test_newer_not_downgraded(self):
        t=target();a=installed(t,version="9.0.0",hashes={"newer":"different"})
        self.assertEqual(decide(t,a,a),"confirm")
    def test_unknown_baseline(self):
        t=target();a=installed(t,version="0.2.2",hashes={"unknown":"old"})
        self.assertEqual(decide(t,a,None),"confirm")
    def test_unversioned_mismatch(self):
        t=target(2);a=installed(t,hashes={"unknown":"different"})
        self.assertIsNone(t["version"]);self.assertEqual(decide(t,a,a),"confirm")
    def test_duplicate_target(self):
        self.assertEqual(plan([plugin(),plugin()],[target()],CAP)["status"],"confirm")
    def test_incomplete_inventory(self):
        self.assertEqual(plan([], [target()],CAP,False)["status"],"blocked")
    def test_no_edit_permission(self):
        p=plugin();p["can_edit"]=False
        self.assertEqual(plan([p],[target(2)],CAP)["status"],"blocked")
    def test_no_save_permission(self):
        self.assertEqual(plan([], [target()],dict(CAP,save=False))["status"],"blocked")
    def test_optimistic_release_guard(self):
        p=plugin();before=copy.deepcopy(p);out=plan([p],[target(2)],CAP)
        with self.assertRaises(ValueError):simulate_apply(p,[target(2)],out,sources([target(2)]),sources([MENU]),"other")
        self.assertEqual(p,before)
    def test_source_failure_atomic(self):
        p=plugin();before=copy.deepcopy(p);out=plan([p],[target(2)],CAP)
        with self.assertRaises(ValueError):simulate_apply(p,[target(2)],out,{},sources([MENU]),p["release"])
        self.assertEqual(p,before)
    def test_registry_conflict(self):
        with self.assertRaises(ValueError):merge_registry([{"id":"I0003","skill_slug":"some-personal-skill"}],[target(2)])
    def test_semver_numeric_and_prerelease(self):
        self.assertGreater(compare("0.1.10","0.1.9"),0)
        self.assertLess(compare("1.0.0-alpha.2","1.0.0-alpha.10"),0)
        self.assertLess(compare("1.0.0-rc.1","1.0.0"),0)
        self.assertEqual(compare("1.0.0+build.1","1.0.0+build.2"),0)
        with self.assertRaises(ValueError):compare("01.0.0","1.0.0")
class Artifacts(unittest.TestCase):
    def test_original_ten_files_preserved(self):
        fixture=json.loads((R/"tests/fixtures/original-skill-hashes.json").read_text(encoding="utf-8"))
        self.assertEqual(len(fixture["protected"]),10)
        for f,h in fixture["protected"].items():self.assertEqual(sha((R/f).read_bytes()),h,f)
    def test_all_original_paths_retained(self):
        fixture=json.loads((R/"tests/fixtures/original-skill-hashes.json").read_text(encoding="utf-8"))
        self.assertEqual(len(fixture["retained_paths"]),36)
        for f in fixture["retained_paths"]:self.assertTrue((R/f).is_file(),f)
    def test_catalog_all_content_hashes(self):
        ids=set();slugs=set()
        for e in CAT["skills"]:
            self.assertNotIn(e["id"],ids);self.assertNotIn(e["slug"],slugs);ids.add(e["id"]);slugs.add(e["slug"])
            self.assertEqual(e["version_status"],"unversioned" if e["version"] is None else "declared")
            for f in e["required_files"]:
                data=(R/f["path"]).read_bytes()
                self.assertEqual(sha(data),f["sha256"]);self.assertEqual(normalized_sha(data),f["normalized_text_sha256"]);self.assertEqual(len(data),f["bytes"])
        self.assertEqual(len(WORK),5);self.assertTrue(all(len(e["required_files"])==2 for e in WORK))
    def test_versions_from_original_not_manifest(self):
        self.assertEqual([e["version"] for e in WORK],["0.2.3","0.1.1",None,None,"0.1.0"])
        self.assertEqual(MENU["version"],"0.4.0")
    def test_aliases_chinese_no_teacher(self):
        self.assertEqual([x["id"] for x in select(CAT,"I1,I003,標題花字產生器")],["I0001","I0003","I0005"])
        for key in ("I0000","0","不存在"):
            with self.assertRaises(ValueError):select(CAT,key)
    def test_embedded_roundtrip_original_bytes(self):
        c,r,commit,ref=load(R)
        text,payload=generate(c,r,commit,ref,"I0001,I0002,I0003,I0004,I0005","embedded")
        parsed=json.loads(text.split("【老師核對的本次來源快照】\n",1)[1])
        for e in [parsed["menu"]]+parsed["selected_skills"]:
            for f in e["files"]:self.assertEqual(sha(f["content"].encode("utf-8")),f["sha256"])
        self.assertNotIn("I0000",[e["id"] for e in parsed["selected_skills"]])
    def test_paths_only_two_work_sources(self):
        c,r,commit,ref=load(R);text,payload=generate(c,r,commit,ref,"I0003")
        self.assertEqual(len(payload["selected_skills"][0]["files"]),2)
        self.assertTrue(all("content" not in f for f in payload["selected_skills"][0]["files"]))
        self.assertTrue(all("content" in f for f in payload["menu"]["files"]))
    def test_truncated_source_rejected(self):
        with self.assertRaises(ValueError):files_for(target(),lambda f:(R/f).read_bytes()[:-1],"local","branch",False)
    def test_unsafe_path_rejected(self):
        for p in ("../secret","C:/secret","/etc/passwd","a\\b"):
            with self.assertRaises(ValueError):safe_path(p)
    def test_eol_normalization_keeps_body_spaces(self):
        self.assertEqual(normalized_sha(b"\xef\xbb\xbfa\r\nb\r"),normalized_sha(b"a\nb\n"))
        self.assertNotEqual(normalized_sha(b"a  \nb\n"),normalized_sha(b"a\nb\n"))
    def test_install_prompt_contracts(self):
        for e in WORK:
            text=(R/e["skill_path"].split("/")[0]/"INSTALL-PROMPT.md").read_text(encoding="utf-8")
            for keyword in ("黃嘉偉KM","release","km-installed-skills.json","版本較舊","先確認","私人 KM","selected_skills"):
                self.assertIn(keyword,text)
            self.assertNotIn("加入或更新「XXX私人KM」",text)
    def test_manifest_display_not_skill_name(self):
        for f in R.glob("I000*/plugin.json"):
            obj=json.loads(f.read_text(encoding="utf-8"));self.assertEqual(obj["extensions"]["com.openai"]["interface"]["displayName"],"黃嘉偉KM")
    def test_menu_preserves_navigation_contract(self):
        text=(R/MENU["skill_path"]).read_text(encoding="utf-8")
        for word in ("C01 策略","C10 專案","每頁最多八項","A／B／C","21～24","91～93","初始 skills 為空","空模板不能清空","0｜主選單","I0000","黃嘉偉KM"):
            self.assertIn(word,text)
    def test_00_txt_two_enters(self):
        for f in (R/"0000-km-menu").glob("*.txt"):
            data=f.read_bytes();self.assertTrue(data.endswith(b"\r\n\r\n"));self.assertFalse(data.endswith(b"\r\n\r\n\r\n"))
if __name__=="__main__":unittest.main()
