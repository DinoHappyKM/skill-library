# I0006｜通用團購助手

技能版本 0.1.0，候選測試版。來源為 P020/50_Skill/group-buying-assistant，從使用者指定 P003 0.5.1 及兩份完整知識庫通用化；原P003與現有I0001～I0005保持。

三組啟動：賣什麼、賣給誰、怎麼買。商品／農產／服務／課程按類型補條件，依LINE、FB、IG、網站、表單或實體下單流程產生文案。簡單與完整模式、主文與下單同複製區塊、主動接續原圖與短標題、收單交付及復盤。

## 安裝與使用

[完整測試安裝提示詞](INSTALL-PROMPT.md)已內嵌主選單，工作技能只讀 [SKILL.md](skills/group-buying-assistant/SKILL.md) 和 [openai.yaml](skills/group-buying-assistant/agents/openai.yaml)。此為工作分支測試來源，正式上課前應合併main後用I0000重新產生；新舊學生沿用黃嘉偉KM，保留其他內容。

安裝並真正儲存後，在新對話選用黃嘉偉KM，輸入「I0006，幫我規劃這次團購」。圖片工具、帳號權限、實際保存與手機流程待測；不保證貼提示詞即可安裝。

格式初始化完成，來源快照與必要檔案校驗通過；Skill Creator validator缺少PyYAML未跑成，未宣稱完整驗證成功。
