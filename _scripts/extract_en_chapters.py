# -*- coding: utf-8 -*-
"""Split the 5e English textbook PDF into per-chapter text files.

Chapter start pages are found by scanning for pages whose first non-empty
line is exactly "CHAPTER N" (front-matter TOC pages start with CONTENTS, so
they cannot false-match). Each chapter's text runs from its start page to
the page before the next chapter starts. Output: raw_en/chNN_en.txt plus a
printed page-range map for auditing.

Run from repo root:  python -X utf8 _scripts/extract_en_chapters.py
"""
import json
import re
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r"F:\BaiduNetdiskDownload\Essentials of Strength Training and Conditioning.pdf")
OUT_DIR = ROOT / "raw_en"
TITLES = json.loads((ROOT / "_scripts" / "five_e_titles.json").read_text(encoding="utf-8"))
HEAD_RE = re.compile(r"^CHAPTER\s+(\d{1,2})\b")


def main() -> int:
    doc = pymupdf.open(SRC)
    candidates: dict[int, list[int]] = {c: [] for c in range(1, 27)}
    for i, page in enumerate(doc):
        lines = [ln.strip() for ln in page.get_text().splitlines() if ln.strip()]
        if not lines:
            continue
        m = HEAD_RE.match(lines[0])
        if m and 1 <= int(m.group(1)) <= 26:
            candidates[int(m.group(1))].append(i)

    # Contents/front-matter pages can repeat "CHAPTER N" lines: for each
    # chapter take the earliest candidate that follows the previous chapter's
    # chosen start, so TOC false hits (early pages) are skipped.
    starts: dict[int, int] = {}
    prev = -1
    for ch in range(1, 27):
        nxt = next((p for p in candidates[ch] if p > prev), None)
        if nxt is None:
            print(f"WARN: no chapter head found for ch{ch}")
            continue
        starts[ch] = nxt
        prev = nxt

    OUT_DIR.mkdir(exist_ok=True)
    ordered = sorted(starts.items())
    print(f"{'ch':>4} {'pdf_pages':>12} {'chars':>9}  title_ok")
    for idx, (ch, start) in enumerate(ordered):
        end = ordered[idx + 1][1] - 1 if idx + 1 < len(ordered) else doc.page_count - 1
        if ch == 26:  # drop index/appendix pages that follow the last chapter
            for p in range(start, end + 1):
                lines = [ln.strip() for ln in doc[p].get_text().splitlines()]
                if any(ln == "INDEX" for ln in lines):
                    end = p - 1
                    break
        text = "\n".join(doc[p].get_text() for p in range(start, end + 1))
        (OUT_DIR / f"ch{ch:02d}_en.txt").write_text(text, encoding="utf-8")
        ok = TITLES[str(ch)].split()[0].lower() in text[:4000].lower()
        print(f"{ch:>4} {start + 1:>5}-{end + 1:<6} {len(text):>9}  {ok}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
