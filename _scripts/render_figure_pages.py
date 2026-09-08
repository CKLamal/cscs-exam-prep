"""Render 14 figure-only 5e textbook pages (no text layer) at 200 dpi to figs/,
then append one fig_inventory.txt row per page.

Book page N == PDF page index N (1-based); 1:1 mapping confirmed.
Row format matches the existing TSV: chapter, figure label, page, position,
WxH (pixels), Traditional-Chinese description. CRLF line endings, UTF-8 no BOM.
"""
import os

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = r"F:\BaiduNetdiskDownload\Essentials of Strength Training and Conditioning.pdf"
FIGS = os.path.join(ROOT, "figs")
INVENTORY = os.path.join(ROOT, "fig_inventory.txt")
DPI = 200

# (book page, chapter, chapter CN numeral, chapter topic)
PAGES = [
    (119, 2, "二", "生物力學"),
    (288, 5, "五", "無氧訓練適應"),
    (389, 7, "七", "年齡差異"),
    (769, 14, "十四", "測試管理與評分解釋"),
    (784, 14, "十四", "測試管理與評分解釋"),
    (847, 14, "十四", "測試管理與評分解釋"),
    (991, 16, "十六", "自由重量與器械技巧"),
    (1160, 17, "十七", "替代模式與非傳統器械技巧"),
    (1168, 17, "十七", "替代模式與非傳統器械技巧"),
    (1173, 17, "十七", "替代模式與非傳統器械技巧"),
    (1365, 19, "十九", "增強式訓練"),
    (1383, 19, "十九", "增強式訓練"),
    (1789, 26, "二十六", "設施政策、程序與法律問題"),
    (1820, 26, "二十六", "設施政策、程序與法律問題"),
]


def main() -> None:
    doc = pymupdf.open(PDF)
    if doc.page_count < 1820:
        raise SystemExit(f"PDF has only {doc.page_count} pages, need >= 1820")

    os.makedirs(FIGS, exist_ok=True)
    matrix = pymupdf.Matrix(DPI / 72, DPI / 72)
    rows = []
    for page, chapter, chapter_cn, topic in PAGES:
        out = os.path.join(FIGS, f"fig_p{page}.png")
        if os.path.exists(out):
            raise SystemExit(f"{out} already exists; refusing to overwrite")
        pix = doc[page - 1].get_pixmap(matrix=matrix)
        pix.save(out)
        desc = f"整頁圖（圖內含標示，無文字層），屬第{chapter_cn}章{topic}主題"
        rows.append(f"{chapter}\tfull-page\tp{page}\tfull\t{pix.width}x{pix.height}\t{desc}")
        print(f"{out}\t{pix.width}x{pix.height}\t{os.path.getsize(out)} bytes")

    with open(INVENTORY, "a", encoding="utf-8", newline="") as f:
        f.write("".join(row + "\r\n" for row in rows))
    print(f"appended {len(rows)} rows to {INVENTORY}")


if __name__ == "__main__":
    main()
