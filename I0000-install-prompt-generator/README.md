# I0000｜安裝提示詞產生器（老師專用）

版本0.1.1。P012/50_Skill/km-install-prompt-generator是正式主檔；這裡是部署副本。學生不安裝I0000，裸0是主選單。

呼叫：`使用I0000，產生I0001、I0003、I0005的黃嘉偉KM學生安裝提示詞。` 可用中文名稱。學生讀不到GitHub時指定「完整原文模式」，不摘要、不傳ZIP。

## 老師首次安裝

教師 Plugin 的正式顯示名稱為「黃嘉偉KMT教師工具」，搜尋代碼 KMT；其中 I0000 仍是固定技能代號。

1. 開啟 Plugin Creator 的建立外掛，或既有教師工具的編輯外掛程式。
2. [複製完整老師安裝提示詞](INSTALL-PROMPT.txt)，貼進建立／編輯對話。
3. 依工具指示儲存。已存在教師工具時沿用同一 Plugin ID；舊名稱「黃嘉偉KM教師工具」先核對原名稱、新名稱、ID 與內碼影響並確認，再調整顯示名稱，不因更名建立副本。
4. 在新對話選用「黃嘉偉KMT教師工具」，輸入本文的 I0000 呼叫範例。

安裝提示詞內嵌六個完整來源檔案；學生主平台名稱仍為「黃嘉偉KM」。既有 ID、內碼、技能代號與原始功能保持不變；帳號的實際儲存與手機搜尋仍待實測。

[Notion 老師安裝教學](https://app.notion.com/p/3f704b753fe08172a4edfd0a00d8f1fd)

## 可執行方法

Python3.10以上與標準函式庫，網路須能讀GitHub，不需模型API金鑰。

```text
python I0000-install-prompt-generator/skills/km-install-prompt-generator/scripts/generate_install_prompt.py --skills "I0001,I0003,I0005" --output 學生安裝.txt
```

追加`--mode embedded`為完整原文模式。每次解析最新來源commit再讀取及校驗；預設來源依 assets/source-config.json；發布狀態須即時核對。TXT結尾兩次Enter。

倉庫不是可直接上傳的整包Plugin。老師可在教師工具外掛加入本Skill全部檔案（scripts、assets也是必要），或本機執行。雲端能否執行Python／讀GitHub須實測；不能完整取得來源就停止。
