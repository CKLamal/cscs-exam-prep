# Probe brainscape: fetch one known deck page + one pack page, dump raw HTML for route inspection.
import re, sys
import requests

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.9"}

for url, fname in [
    ("https://www.brainscape.com/flashcards/scientific-foundations-3-11741227", "probe_deck_11741227.html"),
    ("https://www.brainscape.com/packs/20661425", "probe_pack_20661425.html"),
]:
    r = requests.get(url, headers=UA, timeout=30)
    open(rf"{RAW}\{fname}", "w", encoding="utf-8", newline="").write(r.text)
    print(fname, "http", r.status_code, "len", len(r.text), "final_url", r.url)
    # quick structural signals
    p = r.text
    for sig in ["__NEXT_DATA__", "window.__", "application/json", "QuestionPreview", "card-content",
                "question_body", "answer_body", "<script", "deck", "flashcard"]:
        print("   sig", sig, p.count(sig))
    print("   ---")
