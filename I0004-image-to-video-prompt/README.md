# I0004｜單圖動態影片提示詞助手

## 現行安裝（2026-10-10）

老師發給學生的外掛固定命名「黃嘉偉KM」。請使用[完整學生安裝提示詞](INSTALL-PROMPT.md)；提示詞會核對來源版本及既有外掛。缺少技能時新增；可核對的舊版才更新；個人修改先確認。學生自己的私人 KM 保持獨立。

技能正文未修改；SKILL.md前言首次宣告技能版本0.1.0，舊無版號兩檔SHA256留作保守更新；不以範例Plugin版本代替。手機／帳號待測，GitHub更新不自動同步。

## 原有教材與歷史說明

以下保留历史資料；與現行規則衝突時以以上入口為準。

# I0004｜單圖動態影片提示詞助手

使用者提供一張圖片與想要的動感後，本技能撰寫一份可貼入圖片轉影片工具的英文提示詞，並用繁體中文說明主體、鏡頭與背景將如何動。英文提示詞會獨立放在 Markdown 程式碼區塊，方便手機複製。

未指定工具時使用通用寫法。若指定 Google Flow、Midjourney、Grok 或其他工具，只在已核實用法時調整；本技能不會代替使用者上傳圖片或生成影片。

## 檔案

- [技能主檔](skills/image-to-video-prompt/SKILL.md)
- [繁體中文顯示設定](skills/image-to-video-prompt/agents/openai.yaml)
- [獨立 Plugin 範例設定](plugin.json)

## 加入黃嘉偉KM

請先使用[完整學生安裝提示詞](INSTALL-PROMPT.md)。若採手動 ZIP 備援，把 `skills/image-to-video-prompt/` 放入「黃嘉偉KM」的 `skills/`，保留原有技能及原 Plugin 的 `plugin.json`。本資料夾的 `plugin.json` 只是獨立範例，**不要覆蓋**已存在的外掛設定。完成後在新對話測試。

GitHub 上有檔案不等於學員已安裝技能。外掛安裝、手機複製按鈕，以及 Google Flow／Midjourney 等工具實際生成結果，仍需在相應帳號測試。