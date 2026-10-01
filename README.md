# DinoH 黃嘉偉 KM｜技能資料庫

這個公開倉庫提供課堂練習用的技能原始檔。目前先收錄 **I0003 公仔表情設計**。GitHub 用來保存與下載檔案；把 GitHub 網址貼進 ChatGPT 對話，**不等於安裝到 Plugin**。

## 目前收錄

| 編號 | 技能 | 用途 | 原始檔 |
| --- | --- | --- | --- |
| I0003 | 公仔表情設計 | A 公仔表情／動作合成；B 真人公仔化；C 公仔純色背景 | [開啟 SKILL.md](figurine-expression-design/skills/figurine-expression-design/SKILL.md) |

本資料夾另有 [I0003 獨立 Plugin 範例 manifest](figurine-expression-design/plugin.json) 與技能選單顯示檔。這是從既有技能 ZIP 展開的副本，**不是原 GPT 的完整原始備份**；原 GPT 的設定、知識檔及真實測試結果仍待核對。

## 學員已有自己的 Plugin：如何加入 I0003

以下步驟只適用於你**自己建立並有權修改**的 Plugin。若只是安裝別人的 Plugin，不能改它的技能內容。

1. 在本倉庫右上角按「Code → Download ZIP」，下載後解壓縮。
2. 找到 `figurine-expression-design/skills/figurine-expression-design/`，整個技能資料夾都要保留，包含 `SKILL.md` 和 `agents/openai.yaml`。
3. 打開你現有 Plugin 的原始資料夾，將這個技能資料夾複製到原有的 `skills/` 內。完成後應有 `你的Plugin/skills/figurine-expression-design/SKILL.md`。
4. **保留**原 Plugin 的名稱、`plugin.json`、原有技能及素材。不要用 I0003 範例的 `plugin.json` 覆蓋你的 Plugin。若原 manifest 明列技能路徑，確認新增技能也會被包含；更新原 Plugin 的版本號。
5. 重新壓縮**整個原 Plugin 資料夾**，上傳到原 Plugin 的更新入口。請先檢查 ZIP 結構與平台自動檢查結果；公開 Plugin 的新技能版本可能還需審查。
6. 更新生效後開新對話測試，不要只看「上傳成功」就當作已安裝完成。

如果你的 Plugin 是在 ChatGPT 內建立、介面提供 **Edit Plugin**，也可以從該入口要求加入這支技能，提供本頁的 `SKILL.md`，並明確要求保留原有技能。儲存前逐項檢查，之後同樣用新對話測試。每位學員可用的編輯／發布入口以其帳號畫面為準。

## 課堂測試

- 輸入「公仔表情設計」：應先辨識 A／B／C 模式。
- 輸入「A 公仔合成」：應要求公仔照、表情或動作參考圖、背景代號及比例代號；資料不足時不能假裝已生成圖片。
- 輸入「C 公仔純色背景」：應要求公仔與動作參考圖及比例；不應再要求背景代號。

實際生成圖片還取決於帳號可用的圖片工具與額度。本文只是安裝教學，**尚未代表學生帳號已通過實測**。

## 製作者與更新

製作者：DinoH 黃嘉偉 KM。課堂使用前，請確認倉庫最新內容與老師展示的版本一致。若要將這份技能納入正式公開 Plugin，須依該 Plugin 的完整套件與審查流程更新。

參考：[OpenAI Plugin 封裝說明](https://developers.openai.com/plugins/build/plugins)｜[Plugin 更新與送審](https://developers.openai.com/plugins/deploy/submission)｜[在 ChatGPT 編輯自己的 Plugin](https://learn.chatgpt.com/docs/build-plugins)