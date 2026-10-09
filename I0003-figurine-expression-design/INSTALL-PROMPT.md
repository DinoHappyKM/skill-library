# I0003｜公仔表情設計：黃嘉偉KM學生安裝

2026-10-09｜測試分支。帳號須有Plugin Creator權限；手機實測待驗證。複製下方完整區塊。

~~~~~~~~text
此為測試分支安裝入口，main尚未合併。先解析下方source_ref的目前commit，將全部來源網址固定到同一commit再讀取；若校驗不一致須請老師重新產生，不能直接換版本。

請使用本帳號實際可用的 Plugin Creator，建立或更新「黃嘉偉KM」，安裝下方選取的工作技能。這次是安裝，不要執行貼文、直播或產圖。

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
{
  "plugin_display_name": "黃嘉偉KM",
  "source_repository": "DinoHappyKM/skill-library",
  "source_commit": "resolve-ref-before-install",
  "source_ref": "upgrade/huang-jia-wei-km-installer",
  "live_install_tested": false,
  "menu": {
    "id": "0000",
    "name": "主選單",
    "slug": "km-menu",
    "role": "menu",
    "version": "0.4.0",
    "category": {
      "id": null,
      "name": null,
      "subcategory": null
    },
    "summary": "依代號與分類找到已收錄技能",
    "tags": [],
    "files": [
      {
        "source_url": "https://github.com/DinoHappyKM/skill-library/blob/upgrade/huang-jia-wei-km-installer/0000-km-menu/skills/km-menu/SKILL.md",
        "target_path": "skills/km-menu/SKILL.md",
        "sha256": "17424e4ad875ff124de32373c197db7394dc2f2bf28826a7757d8f97a98c6781",
        "bytes": 8083,
        "normalized_text_sha256": "17424e4ad875ff124de32373c197db7394dc2f2bf28826a7757d8f97a98c6781",
        "content": "---\nname: km-menu\ndescription: 黃嘉偉KM的0主選單。在已選用此外掛時，使用者輸入0、主選單、目錄、分類或C代號、詢問有哪些技能，或用I料號選技能及不確定該用哪支技能時使用；已在工作技能內回答選項則沿用該流程。\nmetadata:\n  version: \"0.4.0\"\n---\n\n# 0｜主選單\n\n選單內容版本：0.4.0。協助已選用此外掛的使用者，以代號、分類或一句需求找到同外掛的工作技能。採繁體中文、手機單欄、短段落與簡潔目錄；實際工作沿用對應技能的完整指令。\n\n## 收錄資料與可信範圍\n\n「已核對收錄快照」是編輯外掛時確認的資料，不是執行時掃描帳號的 API。只顯示其中 registration 為「已核對」的工作技能；老師對照表只是分類依據，不是已安裝清單。初始 skills 為空。\n\n本教師外掛標頭固定「黃嘉偉KM」；學生自己的私人KM是另一個獨立外掛，不以本選單改名或合併。不要每次開目錄讀 GitHub。看目錄、介紹、搜尋都不安裝技能、不修改快照。GitHub 改版也不自動更新學生外掛。\n\n選定後取得同外掛 skill_slug 對應的可用 Skill 指令，再依其正式流程處理；沒有可用技能讀取或選用能力時，說明未取得工作技能，不能只憑摘要重寫流程或假裝已呼叫。圖片與影片能力以當前工具、使用者素材和帳號額度為準。\n\n## 入口與數字優先順序\n\n1. 單獨輸入 0、00、0000、主選單、目錄、有哪些技能：顯示主選單。正文、程式碼、檔名或資料中的 0 不作導航。返回目錄保留同對話可見的工作草稿。\n2. 明確 I 代號忽略大小寫與前導零：I003、i3、0003 在明確選技能的脈絡下對應 I0003。料號至少補足四位，不截斷更長料號；排序、分類與分頁永遠不重編料號。\n3. 裸數字 3 只在「選單等候選工作技能」時代表 I0003，不是畫面第 3 列。分類清單中裸數字 4 不代表 C04；選分類用中文名稱或 C 代號。\n4. 工作技能正等候 A／B／C、21～24、91～93、步驟數字、數量等回答時，該技能的解讀優先。明確 I 代號仍可表示切換工作；用途不清的裸數字只補問一次。\n5. 3001 僅在快照已核對它對應 daily-story-post／I0001 時作為相容入口；其他既有 3001 或 K01 不自動改號或覆蓋。\n\n## 主選單與空清單\n\n標頭固定使用「黃嘉偉KM」，下一行「想完成哪件事？」。按主要分類分組，以固定 I 代號排序，每筆兩行：\n\n**I0003｜公仔表情設計**\n公仔表情、動作與純色素材\n\n這是排版示例，不代表已安裝 I0003。用粗體標題、段落和少量分隔線；不要用大表格、整段程式碼框或假按鈕呈現選單。平台文字畫面不承諾自訂宋體、金色或點按事件。\n\n結尾固定引導：「輸入技能代號或直接說需求。找分類輸入『分類』；看全部輸入『全部』；0 回主選單。」\n\nskills 為空時：「目前尚未加入工作技能。請到此外掛的『編輯外掛程式』，貼上老師本次提供的加入技能提示詞；完成儲存後，在新對話輸入 0。」不列老師五支為可用技能，不自行建立技能。\n\n## 分類、分頁與返回\n\n- 「分類／找分類」：只列有已核對工作技能的大分類，顯示 C 代號、中文名稱及筆數。明確輸入分類名稱或 C04，可直接查看該分類；完整工作需求有「圖片」等詞時先辨識任務，不誤當分類指令。\n- 分類內顯示該分類名稱、技能筆數、每筆固定代號／中文名稱／一句用途。結尾：「輸入技能代號；返回回分類目錄；0 回主選單。」\n- 「全部」：列此外掛已核對的所有工作技能，包含保留的自訂項目，不改用老師總庫。\n- 分類與技能列表各自每頁最多八項。下一頁／上一頁保持目前分類及固定代號；到首尾清楚說明。不產生任意新項目填滿一頁。\n- 單獨「返回」依目錄層級處理：分類內技能 → 分類清單 → 主選單。工作流程已接續時，沿用工作技能自己的返回規則；單獨 0 仍回主選單。\n- 在分類內選到其他分類的裸數字：若該料號已收錄，先指出所屬分類與用途，提示用完整 I 代號明確切換；未收錄則說明尚未收錄。\n- 已知但空的分類：「此外掛的這個分類尚未收錄技能。」附分類／全部／0。未知分類給現有分類名稱；不虛構項目。\n- category_id 為 null 的已核對自訂技能，列在「待分類」下，仍可用原代號或名稱查找；不擅自另編料號。\n\n## 名稱、需求與接續工作\n\n中文名稱、代號、用途與 tags 都可用來找已收錄技能。明確選用一支技能或只有一支符合需求時，直接取得正式技能並接續，不再多問「是否開始」。例如「用 I0003，先讓我選模式」應依公仔技能列出 A／B／C；不只再顯示介紹。\n\n「介紹 I0003」只說用途、需要資料與如何開始，不產圖。模糊需求最多列三個已收錄候選與不同用途，等使用者選擇。I0099 等未收錄料號清楚說明並提供分類／全部／0；不冒充可執行。快照存在但實際技能不可取得時，說明「目錄有登錄，但目前未取得對應技能，請核對外掛版本」。\n\n在同一對話記住目錄頁、分類、頁碼及可見的工作進度；繼續任務只使用可見資料，必要時補問缺少資料。不承諾新對話能接續舊對話的草稿。\n\n## 大分類與老師料號對照\n\n主要分類：C01 策略；C02 文案；C03 編劇；C04 圖像；C05 影音；C06 LINE；C07 網站；C08 GPT 與 AI 工具；C09 語法；C10 專案。小分類暫為 null；日後調整分類不改 I 料號。\n\n以下用於編輯時登錄，不能當成學生已安裝：\n- I0001｜日常故事貼文助手｜daily-story-post｜C02｜三種貼文、原圖標題｜日常、故事、貼文。\n- I0002｜直播企劃與開播助手｜live-stream-planning｜C05｜直播企劃、開播準備｜直播、企劃、開播。\n- I0003｜公仔表情設計｜figurine-expression-design｜C04｜公仔表情、動作與純色素材｜公仔、表情、動作。\n- I0004｜單圖動態影片提示詞助手｜image-to-video-prompt｜C05｜圖片動畫英文提示詞｜圖片、動畫、影片提示詞。\n- I0005｜標題花字產生器｜title-lettering-generator｜C04｜繁體標題、花字與透明素材｜標題、花字、透明PNG。\n\n## 編輯時登錄與更新\n\nPlugin Creator 在加入／更新工作技能後，讀取同一外掛檔案，核對主檔與 slug，再合併下方快照。每筆保留 id、name、skill_slug、category_id、subcategory_id、summary、tags、source_version、registration；未知版本填 null，只有確定存在的技能標為「已核對」。對照表沒有的自訂技能保留原名稱與原代號，分類未知填 null；未確認料號不要自行發明。\n\n保留其他已核對項目與自訂資料，此外掛名稱固定黃嘉偉KM；新版空模板不能清空舊快照。重複 id／slug 或同用途異名有疑義時先核對，不擅自覆蓋。必要欄位與格式修正可合併；不能以選單升級為由改寫其他工作技能。\n\n同一版本中保存工作技能及選單快照後，回讀確認清單；儲存失敗不可宣稱已更新。技能已刪除時同步移除對應登錄；尚待核對者改為「待核對」並在一般目錄隱藏。第二階段 MCP 可沿用相同欄位，第一階段沒有 MCP 依賴。\n\n## 已核對收錄快照\n\n<!-- KM-REGISTRY-BEGIN -->\n~~~yaml\nmenu_version: \"0.4.0\"\nplugin_display_name: \"黃嘉偉KM\"\nskills: []\n~~~\n<!-- KM-REGISTRY-END -->\n\n## 教師工具界線\n\n裸0、00、0000是本主選單。I0000是老師專用安裝產生器，不列入學生工作技能。編輯時核對安裝版本與校驗值，本選單不在使用時連GitHub更新；個人修改及版本衝突先確認。\n\n技能本文結束｜km-menu｜0.4.0\n"
      },
      {
        "source_url": "https://github.com/DinoHappyKM/skill-library/blob/upgrade/huang-jia-wei-km-installer/0000-km-menu/skills/km-menu/agents/openai.yaml",
        "target_path": "skills/km-menu/agents/openai.yaml",
        "sha256": "ae7f10241660711b29b57520dce360063920f0d56e641f47a9bdf447820e7083",
        "bytes": 212,
        "normalized_text_sha256": "ae7f10241660711b29b57520dce360063920f0d56e641f47a9bdf447820e7083",
        "content": "interface:\n  display_name: \"0｜主選單\"\n  short_description: \"依代號、分類或需求找到黃嘉偉KM已收錄技能\"\n  default_prompt: \"使用 $km-menu，顯示黃嘉偉KM已核對的技能與分類。\"\n"
      }
    ]
  },
  "selected_skills": [
    {
      "id": "I0003",
      "name": "公仔表情設計",
      "slug": "figurine-expression-design",
      "role": "student_skill",
      "version": null,
      "category": {
        "id": "C04",
        "name": "圖像",
        "subcategory": null
      },
      "summary": "公仔表情、動作與純色素材",
      "tags": [
        "公仔",
        "表情",
        "動作"
      ],
      "files": [
        {
          "source_url": "https://github.com/DinoHappyKM/skill-library/blob/upgrade/huang-jia-wei-km-installer/I0003-figurine-expression-design/skills/figurine-expression-design/SKILL.md",
          "target_path": "skills/figurine-expression-design/SKILL.md",
          "sha256": "8b526c06c203b2a2079997bd5e71acc1e2937075cb3f427fe3ab15899c97a015",
          "bytes": 8989,
          "normalized_text_sha256": "610e96c8a200d69ac0ba432524fa428daa77ec6036c0baeddc9fb0037188b574"
        },
        {
          "source_url": "https://github.com/DinoHappyKM/skill-library/blob/upgrade/huang-jia-wei-km-installer/I0003-figurine-expression-design/skills/figurine-expression-design/agents/openai.yaml",
          "target_path": "skills/figurine-expression-design/agents/openai.yaml",
          "sha256": "ae429e65737a5cb5c72b9aa5ae9c28f6d1b0757f8342c855f4273d00f9c8adc7",
          "bytes": 296,
          "normalized_text_sha256": "ad67836f81f95e8a834466923c94993ab86ab6fba458d08c851aed3d985c7090"
        }
      ]
    }
  ]
}
~~~~~~~~
