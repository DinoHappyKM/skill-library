# 黃嘉偉KM｜技能資料庫

## 完整ZIP安裝｜手機優先

**[下載黃嘉偉KM完整外掛 v0.1.4](https://github.com/DinoHappyKM/skill-library/raw/refs/heads/main/downloads/huang-jia-wei-km-v0.1.4.zip)** · [安裝步驟](INSTALL-ZIP.md) · [Notion手機教學](https://app.notion.com/p/3f404b753fe08030a598cdde79ee41b3)

內含主選單、I0001～I0006與DINO Logo。新同學：ChatGPT外掛頁→新增→上傳外掛程式封存檔→選ZIP→確認。已有外掛者先閱讀更新分流；自訂內容須備份合併。原生上傳與手機仍待學生實測。


技能庫0.3.4｜2026-10-12。請以目前檢視的 GitHub 分支與 PR 狀態判斷是否已發布到 main。

老師發給學生的Plugin名稱固定「黃嘉偉KM」，自己的私人KM獨立保留。先建立主選單，再分批加入；也可直接貼任一完整提示詞，由它建立缺少的外掛與主選單。

## 學生安裝

[一次安裝 I0001～I0006｜完整學生提示詞](INSTALL-I0001-I0006.txt)


|代號|技能|原文版本|分類|安裝|
|---|---|---|---|---|
|I0001|日常故事貼文助手|0.2.3|文案|[提示詞](I0001-daily-story-post/INSTALL-PROMPT.md)|
|I0002|直播企劃與開播助手|0.1.1|影音|[提示詞](I0002-live-stream-planning/INSTALL-PROMPT.md)|
|I0003|公仔表情設計|0.1.0|圖像|[提示詞](I0003-figurine-expression-design/INSTALL-PROMPT.md)|
|I0004|單圖動態影片提示詞助手|0.1.0|影音|[提示詞](I0004-image-to-video-prompt/INSTALL-PROMPT.md)|
|I0005|標題花字產生器|0.1.0|圖像|[提示詞](I0005-title-lettering-generator/INSTALL-PROMPT.md)|
|I0006|通用團購助手|0.1.1|文案|[提示詞](I0006-group-buying-assistant/INSTALL-PROMPT.md)|

[00建立](0000-km-menu/00_建立黃嘉偉KM外掛.txt)｜[00更新主選單](0000-km-menu/00_更新既有黃嘉偉KM主選單.txt)｜[KMT教師工具教學](I0000-install-prompt-generator/README.md)｜[I0000老師完整安裝提示詞](I0000-install-prompt-generator/INSTALL-PROMPT.txt)｜[版本目錄](skills-catalog.json)｜[測試說明](tests/README.md)

## 教師工具

教師 Plugin 名稱為「黃嘉偉KMT教師工具」（KMT），內部安裝技能代號 I0000；學生主平台固定為「黃嘉偉KM」。先複製上方老師完整安裝提示詞，安裝並儲存教師工具，再以 I0000 產生課堂需要的學生提示詞。已有教師工具沿用原 Plugin ID，舊名稱更名先核對及確認，不建立重複外掛。

## 版本、完整性與權限

缺少新增；相同保留；可核對未客製舊版才更新；較新版、同版異文、未知基準或個人修改先確認。保留其他技能、設定、檔案與ID，不用老師manifest覆蓋現有外掛。

I0003、I0004首次於SKILL.md宣告技能版0.1.0；舊無版本官方兩檔校驗值列於目錄供保守升級。其餘正式工作檔不變；歷史references、IMPORT仍保留，學生每支工作技能只要兩檔。不是宣稱工具只能讀二個檔案。

帳號須實際有Plugin Creator權限；貼提示詞不能增加權限。學生讀GitHub失敗，可由老師I0000產生完整原文模式，不要ZIP；原文不足則停止，不猜免費額度原因。

GitHub/G槽路徑是資料位置，不是Plugin安裝網址；更新不自動同步已安裝外掛。主選單是聊天文字導航，不承諾原生按鈕或自訂字型。

## 維護與驗證

[版本目錄規格](docs/技能版本目錄.md)。先改原專案主檔，再重建部署；不能反向改正式技能。

`python -m unittest discover -s tests -v`執行離線檢查。ChatGPT儲存、免費帳號、iPhone／安卓及電腦實測待驗證；本機結果不能稱安裝成功。

## I0006 通用團購助手

main 已發布 I0006 0.1.1：商品、農產、服務與課程開團，三組啟動問題，依實際下單管道交付文案、原圖與收單流程。[直接複製正式安裝提示詞](I0006-group-buying-assistant/INSTALL-PROMPT.md)到Plugin Creator，實際使用結果待老師驗收。原已安裝教師工具的查目錄程式可依新目錄選取 I0006，實際帳號呼叫仍待測。

I0006 0.1.1 修正：LINE團購主文預設附「接龍／1.／2.／3.」，主文與接龍同一複製區塊；明確不要接龍或只用表單／私訊時省略。

## 新增技能

| I0007 | 1Shop容器HTML產生器 | 0.1.0 | 網站 | [提示詞](I0007-one-shop-html-block/INSTALL-PROMPT.md) |
