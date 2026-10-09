# I0003｜公仔表情設計

## 現行安裝（2026-10-10）

外掛固定「黃嘉偉KM」；自己的私人KM獨立保留。[完整學生提示詞](INSTALL-PROMPT.md)使用測試分支，main未合併。缺少新增，可核對未客製舊版才更新，相同保留；個人修改先確認。

技能正文未修改；SKILL.md前言首次宣告技能版本0.1.0，舊無版號兩檔SHA256留作保守更新；不以範例Plugin版本代替。手機／帳號待測，GitHub更新不自動同步。

## 原有教材與歷史說明

以下保留历史資料；與現行規則衝突時以以上入口為準。

# I0003｜公仔表情設計

這支技能提供三種模式：A 公仔表情與動作合成、B 真人公仔化、C 公仔純色背景素材。使用者提供參考照片與指定選項後，再依可用圖片工具製作素材。

## 技能檔案

- [技能主檔](skills/figurine-expression-design/SKILL.md)
- [中文顯示名稱](skills/figurine-expression-design/agents/openai.yaml)
- [獨立 Plugin 範例設定](plugin.json)

要加入**自己可編輯的現有 Plugin**，請複製整個 `skills/figurine-expression-design/` 資料夾到原 Plugin 的 `skills/`。保留原 Plugin 的其他技能與 `plugin.json`，更新版本後重新封裝、上傳並測試。

此資料夾是既有技能 ZIP 展開後的副本，不代表原 GPT 的設定與全部知識檔已完成比對，也不代表學生帳號已安裝或實測。
