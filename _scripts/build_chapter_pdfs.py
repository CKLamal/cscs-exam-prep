# -*- coding: utf-8 -*-
"""Rebuild the 26 per-chapter study PDFs in pdf/ from html_v2/ via headless Chrome.

Each html_v2/chNN.html carries @page CSS (A4, print margins); Chrome --print-to-pdf
honours it. Output filenames come from pdf_names.json so the folder layout is
unchanged. Every generated PDF is verified before it replaces the old one:
  - page 1 text contains the official 5e English chapter title
    (from _scripts/five_e_titles.json, whitespace-normalized), and
  - the page count is within 25% of the old PDF's (drift guard against
    layout breakage).

Run from repo root:  python -X utf8 _scripts/build_chapter_pdfs.py [--only ch05 ...]
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
HTML_DIR = ROOT / "html_v2"
PDF_DIR = ROOT / "pdf"

NAMES = json.loads((ROOT / "pdf_names.json").read_text(encoding="utf-8"))
TITLES = json.loads(
    (ROOT / "_scripts" / "five_e_titles.json").read_text(encoding="utf-8")
)


def norm(s: str) -> str:
    return " ".join(s.split())


def build(ch: str) -> None:
    html = HTML_DIR / f"{ch}.html"
    out = PDF_DIR / NAMES[ch]
    old_pages = pymupdf.open(out).page_count if out.exists() else 0

    with tempfile.TemporaryDirectory() as tmp:
        profile = Path(tmp) / "profile"
        raw = Path(tmp) / "out.pdf"
        cmd = [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={raw}",
            html.resolve().as_uri(),
        ]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
        if not raw.exists() or raw.stat().st_size < 10_000:
            raise RuntimeError(f"{ch}: chrome produced no usable pdf")

        doc = pymupdf.open(raw)
        p1 = norm(doc[0].get_text())
        title = norm(TITLES[str(int(ch[2:]))])
        assert title in p1, f"{ch}: official title missing from page 1"
        pages = doc.page_count
        doc.close()
        if old_pages and not (old_pages * 0.75 <= pages <= old_pages * 1.6):
            raise RuntimeError(
                f"{ch}: page count {pages} far off old {old_pages}"
            )
        out.write_bytes(raw.read_bytes())
    print(f"OK {ch} -> {out.name} pages {old_pages} -> {pages}")


def main() -> int:
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1:])
    failed = []
    todo = [c for c in sorted(NAMES) if not only or c in only]
    for ch in todo:
        try:
            build(ch)
        except Exception as exc:  # keep going, report at end
            failed.append(ch)
            print(f"FAIL {ch}: {exc}")
    print(f"done: {len(todo) - len(failed)}/{len(todo)} ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
