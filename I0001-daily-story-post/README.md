# I0001｜日常故事貼文助手（KM 3001）

這支技能協助把真實日常小事寫成 A 反轉、B 感受、C 日常三種 FB／IG 貼文。使用者選定貼文並提供有權使用的原始照片後，再製作 9:16 繁體中文標題花字封面；重要文字需留在 IG／FB 縮圖可見範圍。

## 技能檔案

- [技能主檔](skills/daily-story-post/SKILL.md)
- [詳細執行指令](skills/daily-story-post/references/current-instructions.md)
- [中文顯示名稱](skills/daily-story-post/agents/openai.yaml)
- [獨立 Plugin 範例設定](plugin.json)

要加入**自己可編輯的現有 Plugin**，請複製整個 `skills/daily-story-post/` 資料夾到原 Plugin 的 `skills/`；保留原有技能、素材與 `plugin.json`，更新原 Plugin 版本後重新封裝與測試。不要用這裡的範例 `plugin.json` 覆蓋原 Plugin。

## 來源與驗證狀態

此 GitHub 副本取自 P013 的正式 Skill 主檔及其 2026-09-29 使用者指定新版參考指令。I0001 盤點資料夾的「03_知識庫與附件」目前是空的，未另加不存在的知識檔。原 GPT 的線上已發布版本、Actions 與實際照片封面效果仍待核對；GitHub 上傳不代表技能已安裝到學生帳號。

## GitHub 單頁匯入測試（2026-10-03）

- [三個技能檔案的完整匯入頁](IMPORT.md)：內容版本 0.2.2，識別碼 I0001-0.2.2-20b66fbba4a4。
- [完整學生測試提示詞](INSTALL-PROMPT.md)：到自己外掛的「編輯外掛程式」貼上。

單頁由 P013 正式來源自動產生；原三檔全文都保留，安裝後仍還原三檔，相對引用不變。修改正式來源後須重新產生單頁與 ZIP。此頁是匯入來源，不是直接掛上 GitHub 就持續同步；已安裝技能需要另行更新。

本次核對：三檔內容與目前 GitHub、ZIP 在統一換行後一致。網頁工具可讀一般檔案頁，但 I0001 兩個 main 頁面回傳舊規則；Raw、固定提交網址及新匯入頁出現 Cache miss。**單頁只能降低跨檔漏讀，不能保證網頁工具可取得來源；學生免費手機匯入／儲存／新對話待測。**
