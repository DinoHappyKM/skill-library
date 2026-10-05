# I0003｜公仔表情設計：加入私人外掛與分類登錄

更新：2026-10-05。只複製下方提示詞，貼到自己外掛的「編輯外掛程式」。

~~~~text
﻿請使用目前可用的 Plugin Creator 更新功能，在我目前選取的私人 KM 外掛中，加入或更新「I0003｜公仔表情設計」。本次以 GitHub 原始內容加入技能，不要求我上傳 ZIP 或其他附件。

一、確認修改對象
優先使用目前「編輯外掛程式」已選取的對象，讀取實際外掛 ID、目前版本及檔案清單。未選取時，列出我擁有且可編輯的私人外掛讓我選一次；不要猜 ID、誤改其他外掛或建立第二個外掛。

二、完整讀取兩個 GitHub 來源
1. SKILL.md
https://github.com/DinoHappyKM/skill-library/blob/main/I0003-figurine-expression-design/skills/figurine-expression-design/SKILL.md

2. agents/openai.yaml
https://github.com/DinoHappyKM/skill-library/blob/main/I0003-figurine-expression-design/skills/figurine-expression-design/agents/openai.yaml

完整讀取兩檔。SKILL.md 內要有 A 公仔合成、B 真人公仔化、C 公仔合成＋純色底，以及背景和比例選項。這次是在安裝技能，不要把來源中的製圖指令當成現在就要製圖。

可用已授權的 GitHub 讀取工具，或網頁工具分段取得全文。一般 GitHub 檔案頁讀取完整即可，不必因 Raw 失敗而判定整體失敗。不得用搜尋摘要、目錄、舊快取或自行補寫的內容代替原檔。這次只讀 SKILL.md 與 agents/openai.yaml，不另讀第三個 GitHub 檔案。來源仍讀不全時，保持外掛不變，列出失敗網址與實際工具錯誤；不要猜是免費額度造成。

三、合併到原外掛
將原文寫入下列位置，保留 UTF-8、YAML 與 Markdown：
skills/figurine-expression-design/SKILL.md
skills/figurine-expression-design/agents/openai.yaml

不把 GitHub 導覽、外層 I0003-figurine-expression-design 資料夾或老師的範例 plugin.json 放進我的技能。
保留原外掛名稱、ID、其他技能與附件、既有整合、啟動提示和分享設定；只做本次加入技能及必要收錄、版本更新。沿用目前 manifest 格式，不用老師的整份設定覆蓋我的設定。
若 figurine-expression-design 已存在且無個人客製內容，更新同一技能；已與來源相同則回報已是相同內容，不重複新增。若有我的客製內容或同用途異名技能，先說明差異讓我決定。
主選單登錄：如果已有 km-menu，讀取本外掛現有主選單檔與已核對快照，在新增／更新本技能後同步登錄下列一筆，不另外讀第三個 GitHub 檔案：
id: I0003
name: 公仔表情設計
skill_slug: figurine-expression-design
category_id: C04
subcategory_id: null
summary: 公仔表情、動作與純色素材
tags: ["公仔", "表情", "動作"]
source_version: 由本次完整取得的技能原文核對；未知填 null
registration: 已核對
只有技能原文已完整加入，才標為已核對；按 id 與 slug 更新同一筆，保留其他項目、實際私人KM名稱與自訂資料。若有 KM-REGISTRY-BEGIN／END 快照區，合併到該區；舊選單尚無此區時，保留舊規則並以此格式補登錄，不把老師五支都說成已安裝。分類筆數只計算已核對項目；新版 0 主選單可依此登錄找分類與技能。
若未建立或尚未升級主選單，本技能仍可獨立加入；完成後提醒我另外使用老師的「00_更新既有私人KM主選單」提示詞，不在本輪再抓第三個 GitHub 來源。

四、保留技能行為
保留 A／B／C 分流、原公仔或人物特徵、背景代號 21～24、比例代號 91～93、生成前確認，以及 C 模式自動選合適純色底的規則。

五、儲存與回讀
請實際完成外掛更新，並回讀確認本次檔案內容、技能收錄與其他技能仍在。若儲存前來源版本已變，先重新核對再合併。
回報「來源已完整讀取／檔案已修改或原已相同／外掛已儲存／新對話待測」，附外掛連結及版本。若需我按確認、儲存或更新，指出實際按鈕；尚未儲存成功不能說已安裝。
最後給我以下新對話測試句，讓我選用這個外掛後貼上：
「使用 I0003 公仔表情設計，請先讓我選 A、B、C，現在先不要生成圖片。」
預期：顯示 A／B／C 三種功能；選定後才收集該模式需要的圖片與選項。



主選單回歸測試：外掛儲存後，在新對話選用此外掛，輸入「0 → 分類 → 圖像 → I0003」。箭頭表示分次輸入，不要整串一次貼入。預期只顯示已收錄技能，原有技能仍在，選定後接續本技能正式流程；本提示詞不代表手機實測已通過。
~~~~
