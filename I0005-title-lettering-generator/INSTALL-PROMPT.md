# I0005｜GitHub 完整學生提示詞

請使用可用的 Plugin Creator 更新工具，在我目前選取且有權編輯的私人 KM 外掛中，加入或更新「I0005｜標題花字產生器」。本次安裝技能，不要現在分析圖片或生成花字。

一、沿用修改對象
先讀取已選取外掛的實際 ID、版本與檔案清單。沒有選取才讓我選一次，不猜 ID、不另外建立外掛。

二、完整取得來源
完整讀取兩個檔案：
https://github.com/DinoHappyKM/skill-library/blob/main/I0005-title-lettering-generator/skills/title-lettering-generator/SKILL.md
https://github.com/DinoHappyKM/skill-library/blob/main/I0005-title-lettering-generator/skills/title-lettering-generator/agents/openai.yaml
主技能內容版本須為 0.1.0，完整至「技能本文結束｜title-lettering-generator｜0.1.0」。
若分頁、Raw 或讀取工具失敗，可改讀：
https://github.com/DinoHappyKM/skill-library/blob/main/I0005-title-lettering-generator/IMPORT.md
只還原 FILE-BEGIN／FILE-END 中的檔案內容，不將外層反引號、標記或安裝說明寫入技能。有可用計算工具時，依 IMPORT 頁中的完整性雜湊核對兩個檔案；沒有計算工具時，不假稱雜湊通過，仍須取得兩檔全文、核對版本與首尾及所有段落。不能因缺少計算工具就直接要求我上傳附件。
來源仍不完整時停止，外掛保持原狀，回報實際工具錯誤；不得用摘要、舊快取或自行補寫代替來源。

三、合併到原外掛
原文寫入：
skills/title-lettering-generator/SKILL.md
skills/title-lettering-generator/agents/openai.yaml
保留 UTF-8、YAML、Markdown。不要加入外層 I0005-title-lettering-generator，不用老師的範例 manifest 覆蓋我的外掛。
保留原外掛名稱、ID、其他技能、知識、附件、整合、啟動器及私人設定；僅更新本技能收錄及工具要求的外掛版本。同名技能已與來源相同則不重複新增；若有我的客製內容，先提出差異。已有 km-menu 時追加 I0005 名稱與 title-lettering-generator 指向，保留原項目；沒有目錄也可獨立加入。

四、保留兩階段啟動
先索取風格參考圖與必要資訊，分析並讓我確認，再等我給新文字；此時不提前生成。內容齊全且已授權直接製作時可繼續。透明 PNG、字形及 OCR 的檢查狀態依實際結果回報，不宣稱永久學會字體或 100% 筆順。

五、儲存與新對話驗收
使用真正編輯與儲存工具完成，回讀兩檔與收錄結果，確認原有技能仍在。回報「來源已完整讀取／檔案已修改或原已相同／外掛已儲存／新對話待測」，附實際外掛連結及版本。需要我按確認、儲存或更新時指出實際按鈕；未儲存成功不能稱已安裝。

新對話測試句：
「使用 I0005 標題花字產生器。請先向我索取風格參考圖片與必要資訊，分析後等我確認，再等我給新文字；先不要生成圖片。」
預期：先收集參考圖；取得圖片後分析並等待，直到我確認風格及提供新文字才製作。圖片工具、額度、手機與新對話效果依實際帳號確認。
