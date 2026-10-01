# I0002｜直播企劃與開播助手

這支技能由 I0002 的「01_GPT指令與畫面」完整指令及「03_知識庫與附件」K01 轉製；兩份內容與本地 P009 正式主檔一致。技能提供簡易與完整直播規劃、YouTube 標題／描述／16:9 封面、直播提示、開播導流及直播後復盤。

## 單獨分享

- [技能主檔](skills/live-stream-planning/SKILL.md)
- [詳細流程與輸出規範](skills/live-stream-planning/references/K01_直播工作流程與輸出規範.md)
- [技能選單顯示設定](skills/live-stream-planning/agents/openai.yaml)
- [獨立 Plugin 範例設定](plugin.json)

要把這支技能加入**自己可編輯的現有 Plugin**，請複製整個 `skills/live-stream-planning/` 資料夾到原 Plugin 的 `skills/`，保留原 Plugin 設定及其他技能，更新版本後重新封裝與上傳。不要用這份範例 `plugin.json` 覆蓋原 Plugin。

## 驗證狀態

已完成原始指令與 K01 的靜態比對，以及 GitHub 檔案上傳。原 GPT 的發布／草稿狀態、Plugin 安裝後的實際觸發、手機複製、封面圖片生成及 YouTube 後台操作仍待實測。圖片生成是否可用，依學員帳號與當次環境的工具而定。
