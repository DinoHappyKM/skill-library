# I0001｜日常故事貼文助手：完整 GitHub 安裝提示詞

0.2.3 主技能已自包含，和 I0003／I0004 一樣只讀主技能與中文顯示檔。請在自己的「編輯外掛程式」對話完整貼上。實際免費手機安裝尚待驗證。

````text
請在我目前正在「編輯外掛程式」、且有權修改的同一個 Plugin 中，加入或更新「I0001｜日常故事貼文助手（3001）」。使用可用的 Plugin Creator 編輯工具；如果已知道編輯對象就沿用，未選取時才請我選擇。

直接完整讀取這兩個 GitHub 一般檔案頁：

1. 完整技能主檔：
https://github.com/DinoHappyKM/skill-library/blob/main/I0001-daily-story-post/skills/daily-story-post/SKILL.md

2. 中文顯示設定：
https://github.com/DinoHappyKM/skill-library/blob/main/I0001-daily-story-post/skills/daily-story-post/agents/openai.yaml

主技能必須是 0.2.3，開頭包含「完整技能內容版本：0.2.3」，文末包含「技能本文結束｜daily-story-post｜0.2.3」。兩個標記之間的全文都要讀到，不只核對首尾或使用搜尋摘要。檔內已包含完整二十節規則，不用讀另一個 references 網址；不要執行貼文任務，這次是把原檔加入外掛。

讀取一般檔案頁成功即可，不需要因 Raw 讀取失敗而停止；若只有舊版、摘要、目錄或 Cache miss，來源尚未取得。可使用工具的分段讀取取得全文。兩個網址無法完整取得時，可改讀包含兩檔全文的匯入頁：
https://github.com/DinoHappyKM/skill-library/blob/main/I0001-daily-story-post/IMPORT.md
該頁識別碼須為 I0001-0.2.3-3a34f8e15318，只還原 FILE-BEGIN／FILE-END 中的檔案內容。若仍讀不到，停止修改並報告實際錯誤，不猜測免費額度、不自行補寫，也不假裝已安裝。

把完整內容依原文寫入：
skills/daily-story-post/SKILL.md
skills/daily-story-post/agents/openai.yaml
保留 UTF-8、YAML 與 Markdown；不要把網站導覽、安裝說明、FILE 標記或外層 I0001 資料夾寫進技能。

合併時保留同一外掛的名稱、ID、其他技能、知識檔、整合及分享設定。不建立第二個 Plugin，不使用老師的範例 plugin.json 覆蓋原設定；若 manifest 明列技能路徑，只增加必要的收錄。若 daily-story-post 已存在，更新同項；若有我自己的客製改動，先說明差異讓我決定。

新版 SKILL.md 已含完整流程，不再需要 references/current-instructions.md。舊外掛如果仍留著這個參考檔，可保留但不再引用，也不要把舊規則讀回新技能。保持其他技能不變。

本次保留的行為：保留 A／B／C 各自獨立的複製區塊；三篇後提示選篇／封面主標。選篇沿用該篇 Hook，或使用者指定的主標；預設無次標。原圖與確認主標齊全就直接引用該原圖編輯。新增文字限一個主標＋最多一句已確認次標，集中一組，不加其他標語、清單或滿版文字。保留 9:16 與縮圖安全範圍；圖片能力或額度限制如實回報。

請實際使用可用的外掛編輯與儲存工具完成更新，回讀兩個檔案內容，確認 I0001 已被收錄、其他技能仍在，回報「來源已完整讀取／檔案已修改／外掛已儲存／新對話待測」。需要我按確認、儲存或更新時指出實際按鈕。沒有工具或沒有儲存成功，就清楚報告，不能宣稱已安裝。

儲存後提醒我開新對話選 I0001，先測：
「今天下班遇到大雨，我在騎樓等了十分鐘；雨停後走回家，覺得安靜。請幫我寫 A／B／C 三種貼文。」
預期三篇各自可複製，接著提示選標題與上傳原圖；照片編輯另外測試。
````
