# I0004｜單圖動態影片提示詞助手

使用者提供一張圖片與想要的動感後，本技能撰寫一份可貼入圖片轉影片工具的英文提示詞，並用繁體中文說明主體、鏡頭與背景將如何動。英文提示詞會獨立放在 Markdown 程式碼區塊，方便手機複製。

未指定工具時使用通用寫法。若指定 Google Flow、Midjourney、Grok 或其他工具，只在已核實用法時調整；本技能不會代替使用者上傳圖片或生成影片。

## 檔案

- [技能主檔](skills/image-to-video-prompt/SKILL.md)
- [繁體中文顯示設定](skills/image-to-video-prompt/agents/openai.yaml)
- [獨立 Plugin 範例設定](plugin.json)

## 加入自己可編輯的現有 Plugin

把整個 `skills/image-to-video-prompt/` 資料夾放入原 Plugin 的 `skills/`，保留原有技能及原 Plugin 的 `plugin.json`。本資料夾的 `plugin.json` 只是獨立範例，**不要覆蓋**已存在的外掛設定。若使用 ChatGPT 的 Edit Plugin，需確認編輯器確實讀到技能主檔與顯示設定，完成後在新對話測試。

GitHub 上有檔案不等於學員已安裝技能。外掛安裝、手機複製按鈕，以及 Google Flow／Midjourney 等工具實際生成結果，仍需在相應帳號測試。