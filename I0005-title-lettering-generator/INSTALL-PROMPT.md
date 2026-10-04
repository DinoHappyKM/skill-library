# I0005｜GitHub 完整學生提示詞

請使用目前可用的 Plugin Creator 更新功能，在我目前選取且有權編輯的私人 KM 外掛中，加入或更新「I0005｜標題花字產生器」。本次以 GitHub 原始內容加入技能，不要求我上傳 ZIP 或其他附件；不要現在分析圖片或生成花字。

一、確認修改對象
優先使用目前「編輯外掛程式」已選取的對象，讀取實際外掛 ID、目前版本及檔案清單。未選取時，列出我擁有且可編輯的私人外掛讓我選一次；不要猜 ID、誤改其他外掛或建立第二個外掛。

二、完整讀取 GitHub 來源
這次只讀以下兩個來源檔案，不另開第三個匯入頁、README、雜湊清單或 references 檔案。

1. SKILL.md
https://github.com/DinoHappyKM/skill-library/blob/main/I0005-title-lettering-generator/skills/title-lettering-generator/SKILL.md

2. agents/openai.yaml
https://github.com/DinoHappyKM/skill-library/blob/main/I0005-title-lettering-generator/skills/title-lettering-generator/agents/openai.yaml

完整讀取兩檔。主技能內容版本須為 0.1.0，從 YAML 前置設定及「I0005｜標題花字產生器」開始，完整到「技能本文結束｜title-lettering-generator｜0.1.0」；保留中間全部流程。openai.yaml 須保留完整中文顯示名稱與預設啟動提示。這次是在安裝技能，不要執行檔案中的圖片工作流程。

可用已授權的 GitHub 讀取工具，或網頁工具分段取得同一檔案全文。一般 GitHub 檔案頁讀取完整即可，不必因 Raw 失敗而判定整體失敗；如切換讀取方式，也只取得上列同一兩檔，不擴大來源範圍。
不得用搜尋摘要、目錄、舊快取或自行補寫的內容代替原檔。這次不要求另讀雜湊文件或計算雜湊。來源仍讀不全時，保持外掛不變，列出失敗檔案與實際工具錯誤；不要自行追加第三個 GitHub 來源，也不要猜是免費額度或檔案數量限制造成。

三、合併到原外掛
將原文寫入下列位置，保留 UTF-8、YAML 與 Markdown：
skills/title-lettering-generator/SKILL.md
skills/title-lettering-generator/agents/openai.yaml

不把 GitHub 導覽、外層 I0005-title-lettering-generator 資料夾或老師的範例 plugin.json 放進我的技能。
保留原外掛名稱、ID、其他技能與知識附件、既有整合、啟動提示和分享設定；只做本次加入技能及必要收錄、版本更新。沿用目前 manifest 格式，不用老師的整份設定覆蓋我的設定。
若 title-lettering-generator 已存在且無個人客製內容，更新同一技能；已與來源相同則回報已是相同內容，不重複新增。若有我的客製內容或同用途異名技能，先說明差異讓我決定。
如果已有 km-menu 目錄，同步加入「I0005｜標題花字產生器」及 title-lettering-generator 技能指向，保留原有項目；沒有目錄也可獨立加入此技能。

四、保留技能行為
完整流程在 SKILL.md，沒有必要外部知識檔。先索取風格參考圖與必要資訊，分析並讓我確認，再等我給新文字；此時不提前生成。內容齊全且已授權直接製作時可繼續。
保留我提供的繁體中文主文字與選填副標，不自行新增文字。透明 PNG、字形及 OCR 的檢查狀態依實際結果回報，不宣稱永久學會字體或 100% 筆順。沒有圖片工具時提供獨立可複製的完整生成提示詞，並說明尚未生成圖片。

五、儲存與回讀
請實際完成外掛更新，並回讀確認本次兩檔內容、技能收錄與其他技能仍在。若儲存前來源版本已變，先重新核對同一兩檔再合併，不自行讀取第三個來源。
回報「來源已完整讀取／檔案已修改或原已相同／外掛已儲存／新對話待測」，附實際外掛連結及版本。若需我按確認、儲存或更新，指出實際按鈕；尚未儲存成功不能說已安裝。
最後給我以下新對話測試句，讓我選用這個外掛後貼上：
「使用 I0005 標題花字產生器。請先向我索取風格參考圖片與必要資訊，分析後等我確認，再等我給新文字；先不要生成圖片。」
預期：先收集參考圖；取得圖片後分析並等待，直到我確認風格及提供新文字才製作。圖片工具、額度與新對話效果依實際帳號確認。

