# DinoH 黃嘉偉 KM｜技能資料庫

這個公開倉庫提供課堂練習用的技能原始檔。目前收錄 **I0002｜直播企劃與開播助手** 與 **I0003｜公仔表情設計**。GitHub 用來保存與下載檔案；把 GitHub 網址貼進 ChatGPT 對話，**不等於安裝到 Plugin**。

## 目前收錄

| 編號 | 技能 | 用途 | 原始檔 |
| --- | --- | --- | --- |
| I0002 | I0002｜直播企劃與開播助手 | 簡易／完整直播規劃、YouTube 標題描述與封面、開播導流 | [開啟 SKILL.md](I0002-live-stream-planning/skills/live-stream-planning/SKILL.md) |
| I0003 | I0003｜公仔表情設計 | A 公仔表情／動作合成；B 真人公仔化；C 公仔純色背景 | [開啟 SKILL.md](I0003-figurine-expression-design/skills/figurine-expression-design/SKILL.md) |

每支技能各有獨立資料夾與 Plugin 範例設定檔。I0002 依盤點資料中的完整指令與知識庫轉製；其原 GPT 目前發布／草稿狀態及實際操作結果仍待核對。I0003 是從既有技能 ZIP 展開的副本，**不是原 GPT 的完整原始備份**。兩者都尚未代表學員帳號已安裝或實測。

## 學員已有自己的 Plugin：如何加入單一技能

以下步驟只適用於你**自己建立並有權修改**的 Plugin。若只是安裝別人的 Plugin，不能改它的技能內容。

1. 在本倉庫右上角按「Code → Download ZIP」，下載後解壓縮。
2. 選擇要加入的技能資料夾：I0002 是 `I0002-live-stream-planning/skills/live-stream-planning/`，I0003 是 `I0003-figurine-expression-design/skills/figurine-expression-design/`。整個技能資料夾都要保留，包含 `SKILL.md`、`agents/openai.yaml` 及其 `references/`（若有）。
3. 打開你現有 Plugin 的原始資料夾，將這個技能資料夾複製到原有的 `skills/` 內。例如加入 I0002 後應有 `你的Plugin/skills/live-stream-planning/SKILL.md`。
4. **保留**原 Plugin 的名稱、`plugin.json`、原有技能及素材。不要用本倉庫的範例 `plugin.json` 覆蓋你的 Plugin。若原 manifest 明列技能路徑，確認新增技能也會被包含；更新原 Plugin 的版本號。
5. 重新壓縮**整個原 Plugin 資料夾**，上傳到原 Plugin 的更新入口。請先檢查 ZIP 結構與平台自動檢查結果；公開 Plugin 的新技能版本可能還需審查。
6. 更新生效後開新對話測試，不要只看「上傳成功」就當作已安裝完成。

如果你的 Plugin 是在 ChatGPT 內建立、介面提供 **Edit Plugin**，也可以從該入口要求加入這支技能，提供所選技能的 `SKILL.md` 與其參考檔，並明確要求保留原有技能。儲存前逐項檢查，之後同樣用新對話測試。每位學員可用的編輯／發布入口以其帳號畫面為準。

## 課堂測試

- I0002：輸入「我想直播談第一次創業常見錯誤」；應預設簡易做法，不重問模式，且先整理內容再進入封面製作。
- I0002：輸入「改用完整做法」；應保留已確認資料，逐階段繼續。
- 輸入「公仔表情設計」：應先辨識 A／B／C 模式。
- 輸入「A 公仔合成」：應要求公仔照、表情或動作參考圖、背景代號及比例代號；資料不足時不能假裝已生成圖片。
- 輸入「C 公仔純色背景」：應要求公仔與動作參考圖及比例；不應再要求背景代號。

實際生成圖片還取決於帳號可用的圖片工具與額度。本文只是安裝教學，**尚未代表學生帳號已通過實測**。

## 製作者與更新

製作者：DinoH 黃嘉偉 KM。課堂使用前，請確認倉庫最新內容與老師展示的版本一致。若要將這份技能納入正式公開 Plugin，須依該 Plugin 的完整套件與審查流程更新。

參考：[OpenAI Plugin 封裝說明](https://developers.openai.com/plugins/build/plugins)｜[Plugin 更新與送審](https://developers.openai.com/plugins/deploy/submission)｜[在 ChatGPT 編輯自己的 Plugin](https://learn.chatgpt.com/docs/build-plugins)