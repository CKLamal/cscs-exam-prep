# 5e 漂移審計報告（AUDIT_5e）

- 掃描日期：2026-09-09
- 掃描工具：`tools\scan_5e_drift.py`（唯讀，不修改題庫）
- 掃描對象：`bank\merged.json`（3205 題，question / explanation_en / explanation_zh / answer_text 四個欄位）
- merged.json sha256（掃描前後相同）：`cb34ac1c26b640415e2ce99c6f08d0832b4f3fd2361257d5b1c31b35e141fe0c`

## 目的

題庫來源是 5e 之前的網路來源（liftaroo、Brainscape、Cram、packman、Quizlet、Trainer Academy、certprep、NSCA 樣本、practicetestgeeks）。這些題目以第 4 版（4e）時代的說法為主，可能與第 5 版《Essentials of Strength Training and Conditioning》（5e）不同。`scan_5e_drift.py` 以 8 組 regex 掃過全庫，列出「可能漂移」的題目與命中上下文。掃描本身不改題。後續的判定階段只修改「依 5e 內文客觀錯誤」的題目。灰色地帶（措辭新舊、資訊性命中）維持原題，只在判定表標記。

## 掃描統計

| 群組 | 掃描內容 | 命中題數（unique qid） |
|---|---|---|
| G1 | 僅用 female athlete triad 舊框架、同欄未提 RED-s（5e 改採 RED-s） | 4 |
| G2 | 提及 RED-s／relative energy deficiency（一致性檢查） | 2 |
| G3 | vaping／電子煙（5e 第 6 章新增，資訊性） | 1 |
| G4 | 傷害心理相關詞，且在傷害上下文（5e 第 9 章擴充） | 1 |
| G5 | overtraining／overreaching 用語（依 5e 第 24 章逐題核對定義） | 52 |
| G6 | 舊章節名稱出現在題幹（實測 0 命中，舊章名未入題） | 0 |
| G7 | 指南數字陷阱：休息間隔、48/72 小時、1-3 天、2-5 分鐘、30 秒、80/85% 1RM、220−年齡 | 66 |
| G8 | 停經／estrogen 說法（5e 擴大為 RED-s、兩性皆適用） | 3 |
| 合計 | 命中至少一組的題目 | **123**（佔全庫 3.8%） |

一題可命中多組，故各組之和（129）大於 123。完整命中報告（qid｜來源｜部分｜模式｜±80 字元上下文）由 `python -X utf8 tools\scan_5e_drift.py` 輸出。

已知誤中（判定時可直接標「無漂移」）：q2067 的 triad 指肌漿網三聯體（T 小管＋終池），非女運動員三聯症。q1252 為 "stress and injury" 字面誤配（落地力學題），非傷害心理概念。

## 判定表（123 題骨架）

規則：每列一題。「判定（5e 頁碼引用）」與「處置」留空，由判定階段填寫。「處置」已填「僅記錄」者為資訊性命中（G3/G6 類），不需改題。建議先處理下方「高風險優先順序」的 20 題。

| qid | 命中模式 | 疑似問題 | 判定（5e 頁碼引用） | 處置 |
|---|---|---|---|---|
| q0015 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0021 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0023 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0024 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0027 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q0063 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q0072 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0104 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q0118 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0143 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0144 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0164 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q0193 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q0195 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0196 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0234 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q0240 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q0249 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0250 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0296 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q0297 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q0302 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0354 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0425 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q0435 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0436 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0440 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0442 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0452 | G3-vaping | 涉及vaping/電子煙（5e第6章新增內容） |  | 僅記錄 |
| q0477 | G8-amenorrhea-estrogen | 停經/雌激素說法（5e擴大為RED-s、兩性皆適用） |  |  |
| q0550 | G2-red-s | 提及RED-s/能量可用性，核對用詞與數值一致性 |  |  |
| q0563 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0694 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q0708 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q0741 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0742 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0748 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0758 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0783 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q0795 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0796 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0797 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0798 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0799 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0800 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0801 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0802 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0803 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0805 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0806 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0807 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0808 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0809 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0810 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0813 | G2-red-s, G5-overtraining | 提及RED-s/能量可用性，核對用詞與數值一致性；過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0814 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0913 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q0915 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q0922 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q0923 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q1019 | G7a-rest-interval-units | 休息間隔數值 |  |  |
| q1188 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1189 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1194 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1213 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1247 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1252 | G4-injury-psych | 傷害心理相關措辭（5e第9章擴充）。誤中：落地力學題 |  |  |
| q1255 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1391 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1405 | G7c-1-3-days | 1-3天數值 |  |  |
| q1408 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1413 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q1444 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1445 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1447 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1454 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1456 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1458 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1463 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1467 | G5-overtraining, G7b-48-72h-recovery | 過度訓練/過度負荷用語，依5e第24章核對定義；48/72小時恢復數值 |  |  |
| q1474 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1481 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1510 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1515 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1516 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1519 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1520 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1542 | G7a-rest-interval-units | 休息間隔數值 |  |  |
| q1563 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1581 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1592 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1650 | G8-amenorrhea-estrogen | 停經/雌激素說法（5e擴大為RED-s、兩性皆適用） |  |  |
| q1676 | G1-triad-only, G5-overtraining, G8-amenorrhea-estrogen | 以 female athlete triad 舊框架陳述、未提 RED-s（5e 改採 RED-s）；過度訓練/過度負荷用語，依5e第24章核對定義；停經/雌激素說法（5e擴大為RED-s、兩性皆適用） |  |  |
| q1677 | G1-triad-only | 以 female athlete triad 舊框架陳述、未提 RED-s（5e 改採 RED-s） |  |  |
| q1693 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q1725 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q1844 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q1873 | G7a-rest-interval-units | 休息間隔數值 |  |  |
| q1894 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1909 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q1917 | G7a-rest-interval-units | 休息間隔數值 |  |  |
| q1955 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q1957 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q2001 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2013 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2037 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2067 | G1-triad-only | 以 female athlete triad 舊框架陳述、未提 RED-s（5e 改採 RED-s）。誤中：肌漿網三聯體 |  |  |
| q2158 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2205 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q2287 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2288 | G1-triad-only | 以 female athlete triad 舊框架陳述、未提 RED-s（5e 改採 RED-s） |  |  |
| q2289 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q2301 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q2308 | G7f-80-85pct-1RM | 80/85% 1RM強度數值 |  |  |
| q2439 | G5-overtraining, G7f-80-85pct-1RM | 過度訓練/過度負荷用語，依5e第24章核對定義；80/85% 1RM強度數值 |  |  |
| q2442 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2451 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q2453 | G7d-2-5-minutes | 2-5分鐘組間休息數值 |  |  |
| q2608 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |
| q2703 | G5-overtraining, G7g-220-age-hrmax | 過度訓練/過度負荷用語，依5e第24章核對定義；220減年齡最大心率公式 |  |  |
| q2815 | G5-overtraining | 過度訓練/過度負荷用語，依5e第24章核對定義 |  |  |
| q2849 | G7b-48-72h-recovery | 48/72小時恢復數值 |  |  |
| q3204 | G7g-220-age-hrmax | 220減年齡最大心率公式 |  |  |

### 高風險優先順序（前 20 題）

掃描過程中風險最高、建議最先判定的題目：

1. q1676 — 女運動員三聯症卡片，純 4e 線性三聯框架，無 RED-s（G1+G8）
2. q2288 — 「What is the female triad? Male?」舊框架、題幹不規則
3. q1677 — 三聯症成因題，舊框架
4. q0802 — 副交感神經過訓／Addisonoid 舊分類，5e 第 24 章是否保留待查
5. q0803 — 腎上腺耗竭說法，舊文獻用語
6. q0196 — 交感／副交感過訓二分題
7. q0249 — 交感型過訓屬性題
8. q0801 — 交感興奮 presentation 題
9. q0250 — FOR／NFOR／OTS 時間數字（數天-數週／數週-數月）
10. q1515 — FOR 與 NFOR 恢復時程數字
11. q1725 — NFOR 生理特徵（題幹來源為舊考題庫）
12. q0795 — OTS 診斷必要條件
13. q0796 — overtraining（過程）與 OTS（結果）區分
14. q2849 — 答案「48 hours (24-48)」與慣常 48-72 小時不一致
15. q0193 — 發炎期「約 72 小時」（5e 第 9 章傷害反應）
16. q0783 — 同上，發炎期約 72 小時
17. q0027 — 高血壓客戶阻力訓練 48-72 小時（對照 5e/ACSM 建議）
18. q1693 — 同 q0027 題組（quizlet 來源）
19. q0550 — 能量可用性 45/30 kcal/kg FFM 數值（5e RED-s 章節核對）
20. q0741 — Fox 公式 220−年齡作為考答案（5e 對該公式的定位）

## pdf\ 目錄未重建說明

`pdf\*.pdf` 仍由舊 html 產生，內嵌的英文章副標是舊版（5e 已改章名，例如第 5/6 章為 Adaptations to Anaerobic/Aerobic Training）。repo 內沒有 PDF 建置腳本。html\ 是唯一權威來源：html 內容已完成 5e 驗證，PDF 尚未跟隨重建。要重建 PDF 需先補建置腳本，再批次重印。在此之前，請以 html 為準。

## 重新執行 merge_bank.py 的警告

`merge_bank.py` 從 `bank\*.json` 原始來源檔重建 `merged.json`。重建結果只有原始來源內容。它會蓋掉兩類之後附加的修改：

1. `explanation_zh` 中文翻譯（存在 `bank\zh\patch_*.json`，由 `apply_zh_patches.py` 套用了 3000+ 題）。
2. 之後以 `tools\apply_5e_fixes.py` 打入的 5e 修正（若有）。

因此重建後必須依序重新執行：`merge_bank.py` → `apply_zh_patches.py` → `apply_5e_fixes.py`。最後 `tools\bank-data.js` 一律用 `make_bank_data.py` 重新產生（html 只讀 bank-data.js）。順序錯或漏跑，練習工具會顯示未翻譯或未修正的題目。

## 重新執行掃描

```
python -X utf8 tools\scan_5e_drift.py          # 完整命中報告＋統計＋sha256 自我檢查
python -X utf8 tools\scan_5e_drift.py --rows   # 判定清單 TSV（qid、命中模式、來源、部分）
```

腳本結尾比較 merged.json 掃描前後 sha256。不同則 assert 失敗（理論上不可能，掃描唯讀）。
