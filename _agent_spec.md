# CSCS 章節摘要 — 代理作業規格(每個代理只負責一章)

## 任務
你負責把 CSCS 教材(NSCA《力量與體能訓練基礎》中文版,**簡體機翻**,DeepL 文筆生硬)的**一章**改寫成一份「ELI5 式系統學習摘要」,輸出為單一 HTML 檔案。讀者是今年要考 CSCS 的備考生,不是五歲小孩本身——ELI5 是**講解手法**(比喻、短句、零術語門檻),內容深度必須達到**考試可用**。

## 輸入(必讀,順序不可省)
1. `D:\dgx-spark\cscs-exam-prep\raw\chXX.txt` — 本章全文(簡體)。檔案大,用 Read 的 offset/limit 分段讀,**必須讀到檔案末尾**,不準只讀前半。
2. `D:\dgx-spark\cscs-exam-prep\_template.html` — HTML 樣板。`<style>` 區塊**原樣複製**到你的輸出,一個字都不改。

## 輸出
- 路徑:`D:\dgx-spark\cscs-exam-prep\html\chXX.html`(XX=两位数章節号)
- 完整 HTML(<!DOCTYPE html> 到 </html>),UTF-8,無 BOM 亦可,自包含。

## 語言(硬性)
- 正文**繁體中文**。用語自然流暢,不要照抄簡體機翻的怪句式。
- 每個專業術語**首次**出現時附英文原文括號,例:三磷酸腺苷(adenosine triphosphate, ATP)。此後可用中文或縮寫。
- 數字、單位照教材。教材沒寫、但你以 CSCS 常識補的數字,確保是業界共識值,不要憑空發明。

## ELI5 手法(硬性)
- 每個抽象機制配一個生活比喻(廚房、零用錢、交通、操場、水塔…)。比喻放 `.analogy` 框。
- 一個句子只講一件事。短句。主動語態。不用「賦能、抓手、閉環、不僅僅、總而言之、深入探討、無縫」這類八股詞。
- 先講「這是什麼、為什麼要管它」,再講細節。

## 章節結構(按順序,標題用 <h2>,小節用 <h3>)
1. `<h1>` 章號+章名;下方 `.subtitle` 放英文章名(對照用)+ 原文頁碼(見下方對照表)
2. **一、本章一句話** — 一句話總結全章
3. **二、學完本章你會** — 3–6 條,改寫自章首目標
4. **三、把核心概念講給你聽(ELI5)** — 主體,按原書知識區塊分 <h3> 小節;每節含比喻框;關鍵機制講到「能回答考試出題」的精度
5. **四、考点速記** — 高頻死數字/死規則集中列(休息間隔、%1RM、次数範圍、心率區間、維生素 mineral 建議量…依章節而異),用表格或 `.exam` 框
6. **五、術語速查(中英對照)** — 表格 ≥10 行:中文術語 | English | 一句話定義
7. **六、圖表** — **≥2 個內嵌 SVG** + **≥2 個表格**。SVG 規格見下
8. **七、易混陷阱** — ≥3 組「長得像但不同」的對比(例:變向能力 vs 敏捷性),用 `.trap` 框或對比表格
9. **八、自我檢測** — 6–10 題混合是非題/選擇題,`.qa` 框,答案附一句話理由;考點落在本章死數字與定義

## SVG 規格(硬性)
- 純原生 `<svg><rect><line><circle><path><text>`,零外部依賴、零 `<image>`、零 `<script>`。
- 寬 ≤660,高自定(建議 120–420);字級 ≥10;文字用繁體中文。
- 配色只用模板色系:#0f3460(深藍) #e94560(紅) #e6b800(黃) #3d7a3d(綠) #16213e #f4f7fa。
- 圖型選對內容:時間/時序→時間軸或甘特;成分佔比→長條圖;分類→層級方塊圖;流程→箭頭方塊;強度–次数→雙軸對照長條。每圖下方 `.figcap` 標「圖X.N 說明」。
- 不要畫需要精确解剖知識的圖;画不準就改表格,寧缺勿醜。

## 長度
正文(不含表格、列表、題目)約 2,500–4,500 中文字。整份 HTML 印出約 6–12 頁 A4。技巧類章節(16/17)動作步驟用表格,正文可靠下限。

## 禁止
- `<script>`、外部 CSS/字型/圖片、markdown 殘留(`**文字**`、`- 列表`)、`<br>` 堆疊排版
- 開頭客套(「讓我們開始探索…」)、結尾總結套話
- 把整段機翻原文直接貼上——必須重新組織成自己的講解

## 章節對照表(章號 | 輸出檔名用繁體章名 | 原文起訖頁 | 英文章名僅供術語對照)
1. 第1章 人体系统的结构与功能 | p38–103 | Structural and Functional Foundations of Human Movement
2. 第2章 阻力训练的生物力学 | p104–173 | Biomechanics of Resistance Exercise
3. 第3章 运动与训练的生物能量学 | p174–226 | Bioenergetics of Exercise and Training
4. 第4章 阻力训练的内分泌反应 | p227–280 | Endocrine Responses to Exercise and Training
5. 第5章 对无氧训练的适应(神经肌肉适应) | p281–338 | Neuromuscular Adaptations to Resistance Training and Detraining
6. 第6章 对有氧训练的适应 | p339–383 | Aerobic Exercise Adaptations
7. 第7章 年龄差异及其对阻力训练的影响 | p384–437 | Age-Related Differences and Their Impact on Resistance Training
8. 第8章 性别差异及其对阻力训练的影响 | p438–464 | Sex-Related Differences and Their Impact on Resistance Training
9. 第9章 表演的心理基础 | p465–535 | Psychological Foundations of Performance
10. 第10章 影响健康的基本营养因素 | p536–612 | Basic Nutritional Factors for Health
11. 第11章 提升运动表现的营养策略 | p613–658 | Advanced Nutrition Strategies for Sport Performance
12. 第12章 提高运动表现的物质和方法 | p659–728 | Substances and Methods to Enhance Performance (Ergogenic Aids)
13. 第13章 测试选择与管理原则 | p729–763 | Testing Selection and Administration Principles
14. 第14章 特定测试的管理、评分和解释 | p764–853 | Administration, Scoring, and Interpretation of Specific Tests
15. 第15章 表现准备、机动性和灵活性 | p854–946 | Performance Preparation, Mobility, and Flexibility
16. 第16章 自由重量和器械训练的运动技巧 | p947–1087 | Exercise Technique: Free Weights and Machines
17. 第17章 替代模式和非传统器械训练的练习技巧 | p1088–1185 | Exercise Technique: Alternative Modes and Nontraditional Equipment
18. 第18章 阻力训练计划设计 | p1186–1259 | Resistance Training Program Design
19. 第19章 增强式训练的方案设计与技巧 | p1260–1397 | Plyometric Program Design and Technique
20. 第20章 速度和敏捷性训练的方案设计与技巧 | p1398–1511 | Speed and Agility Program Design and Technique
21. 第21章 有氧耐力和代谢训练的计划设计与技巧 | p1512–1578 | Aerobic Endurance and Metabolic Program Design and Technique
22. 第22章 周期化 | p1579–1629 | Periodization
23. 第23章 康复、再训练和医疗问题 | p1630–1678 | Rehabilitation, Retraining, and Medical Issues
24. 第24章 过度训练、过度运动和恢复 | p1679–1726 | Overtraining, Overreaching, and Recovery
25. 第25章 设施设计、布局和组织 | p1727–1774 | Facility Design, Layout, and Organization
26. 第26章 设施政策、程序和法律问题 | p1775–1820 | Facility Policies, Procedures, and Legal Issues

## 交貨自檢(寫完 HTML 後逐項確認)
- [ ] 讀完了 raw 檔全文(最後一段有讀到)
- [ ] style 區塊與模板逐字一致
- [ ] 繁體中文;術語首現附英文
- [ ] ≥2 個 SVG、≥2 個表格、≥10 行術語表、≥6 題自我檢測
- [ ] 死數字全部保留且正確(重讀你写的表格核對)
- [ ] 無 script/外部資源/markdown 殘留
- [ ] 檔案已寫入 D:\dgx-spark\cscs-exam-prep\html\chXX.html
