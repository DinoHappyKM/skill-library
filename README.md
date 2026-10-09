# 黃嘉偉KM｜技能資料庫

技能庫0.3.2｜2026-10-10。請以目前檢視的 GitHub 分支與 PR 狀態判斷是否已發布到 main。

老師發給學生的Plugin名稱固定「黃嘉偉KM」，自己的私人KM獨立保留。先建立主選單，再分批加入；也可直接貼任一完整提示詞，由它建立缺少的外掛與主選單。

## 學生安裝

|代號|技能|原文版本|分類|安裝|
|---|---|---|---|---|
|I0001|日常故事貼文助手|0.2.3|文案|[提示詞](I0001-daily-story-post/INSTALL-PROMPT.md)|
|I0002|直播企劃與開播助手|0.1.1|影音|[提示詞](I0002-live-stream-planning/INSTALL-PROMPT.md)|
|I0003|公仔表情設計|0.1.0|圖像|[提示詞](I0003-figurine-expression-design/INSTALL-PROMPT.md)|
|I0004|單圖動態影片提示詞助手|0.1.0|影音|[提示詞](I0004-image-to-video-prompt/INSTALL-PROMPT.md)|
|I0005|標題花字產生器|0.1.0|圖像|[提示詞](I0005-title-lettering-generator/INSTALL-PROMPT.md)|

[00建立](0000-km-menu/00_建立黃嘉偉KM外掛.txt)｜[00更新主選單](0000-km-menu/00_更新既有黃嘉偉KM主選單.txt)｜[I0000老師工具](I0000-install-prompt-generator/README.md)｜[版本目錄](skills-catalog.json)｜[測試說明](tests/README.md)

## 版本、完整性與權限

缺少新增；相同保留；可核對未客製舊版才更新；較新版、同版異文、未知基準或個人修改先確認。保留其他技能、設定、檔案與ID，不用老師manifest覆蓋現有外掛。

I0003、I0004首次於SKILL.md宣告技能版0.1.0；舊無版本官方兩檔校驗值列於目錄供保守升級。其餘正式工作檔不變；歷史references、IMPORT仍保留，學生每支工作技能只要兩檔。不是宣稱工具只能讀二個檔案。

帳號須實際有Plugin Creator權限；貼提示詞不能增加權限。學生讀GitHub失敗，可由老師I0000產生完整原文模式，不要ZIP；原文不足則停止，不猜免費額度原因。

GitHub/G槽路徑是資料位置，不是Plugin安裝網址；更新不自動同步已安裝外掛。主選單是聊天文字導航，不承諾原生按鈕或自訂字型。

## 維護與驗證

[版本目錄規格](docs/技能版本目錄.md)。先改原專案主檔，再重建部署；不能反向改正式技能。

`python -m unittest discover -s tests -v`執行離線檢查。ChatGPT儲存、免費帳號、iPhone／安卓及電腦實測待驗證；本機結果不能稱安裝成功。
