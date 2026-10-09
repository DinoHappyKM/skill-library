# I0000｜安裝提示詞產生器（老師專用）

版本0.1.1。P012/50_Skill/km-install-prompt-generator是正式主檔；這裡是部署副本。學生不安裝I0000，裸0是主選單。

呼叫：`使用I0000，產生I0001、I0003、I0005的黃嘉偉KM學生安裝提示詞。` 可用中文名稱。學生讀不到GitHub時指定「完整原文模式」，不摘要、不傳ZIP。

## 可執行方法

Python3.10以上與標準函式庫，網路須能讀GitHub，不需模型API金鑰。

```text
python I0000-install-prompt-generator/skills/km-install-prompt-generator/scripts/generate_install_prompt.py --skills "I0001,I0003,I0005" --output 學生安裝.txt
```

追加`--mode embedded`為完整原文模式。每次解析最新來源commit再讀取及校驗；預設來源依 assets/source-config.json；發布狀態須即時核對。TXT結尾兩次Enter。

倉庫不是可直接上傳的整包Plugin。老師可在教師工具外掛加入本Skill全部檔案（scripts、assets也是必要），或本機執行。雲端能否執行Python／讀GitHub須實測；不能完整取得來源就停止。
