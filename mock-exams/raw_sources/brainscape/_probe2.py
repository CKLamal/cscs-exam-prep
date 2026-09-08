# Probe brainscape deck pages with browser UA vs bot UA; find where card text lives.
import re
import requests

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape"
UAS = {
    "browser": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"},
    "googlebot": {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"},
    "lynx": {"User-Agent": "Lynx/2.8.9rel.1 libwww-FM/2.14"},
}

urls = [
    "https://www.brainscape.com/flashcards/nsca-cscs-chapter-1-14791808/packs/21791126",
    "https://www.brainscape.com/flashcards/cscs-ch-1-structure-function-of-body-sys-11139994/packs/19776051",
]
for tag, h in UAS.items():
    for url in urls:
        r = requests.get(url, headers=h, timeout=30, allow_redirects=True)
        p = r.text
        did = re.search(r"flashcards/([a-z0-9-]+)-(\d+)", url)
        fname = f"probe2_{did.group(2)}_{tag}.html"
        open(rf"{RAW}\{fname}", "w", encoding="utf-8", newline="").write(p)
        marks = {
            "len": len(p), "http": r.status_code, "final": r.url[:70],
            "A-Band": p.count("A-Band"), "sarcomere": p.lower().count("sarcomere"),
            "json-ld": p.count("application/ld+json"), "NEXT_DATA": p.count("__NEXT_DATA__"),
            "questions": p.count('"question"'), "answer_body": p.count("answer"),
        }
        print(tag, did.group(2), marks)
