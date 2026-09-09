# CSCS Exam Prep — NSCA-CSCS 考試準備資料

針對 NSCA《CSCS 体能訓練專家》考試的中文自學工具。教材依據：《Essentials of Strength Training and Conditioning》第 5 版（英文原文，簡體機翻版僅作術語參考）。

包含三類產出：

1. **26 章研讀摘要**（繁體中文，淺白講解風格）→ 輸出為 `pdf/` 內 26 個章節 PDF。
2. **題庫與模擬考工具**（3205 題，完全離線）→ 見 `mock-exams/README.md`。
3. **校對與建置腳本** → 見下方「工作流程」。

## 目錄結構

| 路徑 | 內容 |
|---|---|
| `html_v2/` | 現行 26 章研讀摘要原始檔（PDF 的產生來源） |
| `pdf/` | 成品：26 個章節 PDF（由 `_scripts/build_chapter_pdfs.py` 產生） |
| `mock-exams/` | 題庫（`bank/`）、練習與模擬考工具（`tools/practice-tool.html`） |
| `raw_en/` | 5e 英文原文逐章全文（`chNN_en.txt`），校對時的唯一事實依據 |
| `raw/` | 陸版簡體機翻全文，僅用於仲裁中文術語，不作為數字依據 |
| `_scripts/` | 建置、抽取、驗證腳本（見下） |
| `_agent_spec.md` | 摘要寫作規格（章節页碼對照、必答要點、格式） |
| `_review_spec.md` | 先前風格校對規格 |
| `html/`、`html_prereview/`、`html_v2_backup_pre_proofread/`、`pdf_demo/`、`fig_inventory.txt` | 歷史迭代與校對前備份，不参与建置 |

## 工作流程（Windows + Chrome + Python）

全部指令在 repo 根目錄執行，需先設定 UTF-8：

```powershell
chcp 65001 > $null; $env:PYTHONIOENCODING = 'utf-8'
```

### 重建 PDF

```powershell
python -X utf8 _scripts\build_chapter_pdfs.py          # 全部 26 章
python -X utf8 _scripts\build_chapter_pdfs.py --only ch05 ch14   # 指定章
```

以無頭 Chrome 將 `html_v2/chNN.html` 輸出為 `pdf/第NN章_*.pdf`。每章會驗證：第一頁必須出現 `_scripts/five_e_titles.json` 登记的 5e 官方英文章名；頁數與舊版落差超過 0.75–1.6 倍即警告。

### 重新抽取英文原文（需外接硬碟上的 5e PDF，內含 pymupdf）

```powershell
python -X utf8 _scripts\extract_en_chapters.py
```

將 5e 英文 PDF 切為 `raw_en/ch01_en.txt` … `ch26_en.txt`，章界以 `CHAPTER N` 標頭比對，並剔除目錄誤判。

### 校對後結構驗證

```powershell
python -X utf8 _scripts\diff_proofread.py              # 全部章
python -X utf8 _scripts\diff_proofread.py ch03         # 指定章
```

對照 `html_v2_backup_pre_proofread/`：報告每章變更區塊數，並確認 SVG／表格／問答計數不變、`<style>` 區塊逐位元組相同、檔案以 `</html>` 收尾。

## 校對狀態

2026-09：全部 26 章已逐章對照 `raw_en/` 英文原文做事實校對，共修正約 312 處（表格數值、公式、術語、測驗解答），風格與版面未動，PDF 已重建。逐條勘誤（含 5e 原文依據、可疑未改項）存於本機 `errata_all.md`／`errata_wave1.md`，尚未納入 repo。

## 其他環境事實

- 平台：Windows（PowerShell 5.1）；Python 3.11；PDF 輸出依賴本機 Chrome。
- 題目保留英文原文（考試為英文），解析為繁體中文。
- 2025-07-01 新考綱：科學基礎 80 題 90 分鐘、實務應用 110 題 150 分鐘，兩部分皆需 70 分及格。
