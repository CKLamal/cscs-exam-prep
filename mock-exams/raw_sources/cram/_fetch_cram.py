# Fetch cram.com CSCS set pages, dump raw HTML, extract full decks from ld+json hasPart.
import json, re, sys, time, html as htmlmod
import requests

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\cram"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.9"}

URLS = [
    "https://www.cram.com/flashcards/cscs-test-prep-chapter-1-5124275",
    "https://www.cram.com/flashcards/cscs-12316743",
    "https://www.cram.com/flashcards/cscs-exercise-science-questions-13166538",
    "https://www.cram.com/flashcards/cscs-9077371",
    "https://www.cram.com/flashcards/nsca-cscs-10125265",
    "https://www.cram.com/flashcards/cscs-8955929",
    "https://www.cram.com/flashcards/cscs-exercise-science-7421655",
    "https://www.cram.com/flashcards/cscs-exercise-technique-13174075",
    "https://www.cram.com/flashcards/cscs-program-design-13174206",
    "https://www.cram.com/flashcards/cscs-nutrition-questions-13168177",
    "https://www.cram.com/flashcards/cscs-organziation-administration-questions-13178055",
    "https://www.cram.com/flashcards/cscs-program-design-exam-prep-2682820",
    "https://www.cram.com/flashcards/cscs-chapter-15-3771255",
    "https://www.cram.com/flashcards/cscs-9559333",
    "https://www.cram.com/flashcards/cscs-ch17-program-design-for-resistance-training--10034101",
]

TAG_RE = re.compile(r"<[^>]+>")
LD_RE = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)

def clean(t):
    t = htmlmod.unescape(t)
    t = TAG_RE.sub(" ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def extract(page):
    cards = []
    title = None
    for m in LD_RE.finditer(page):
        try:
            data = json.loads(m.group(1).strip())
        except Exception:
            continue
        items = data if isinstance(data, list) else [data]
        for d in items:
            if not isinstance(d, dict):
                continue
            hp = d.get("hasPart")
            if isinstance(hp, dict):
                hp = [hp]
            if isinstance(hp, list):
                for q in hp:
                    if isinstance(q, dict) and q.get("@type") == "Question":
                        front = clean(str(q.get("name", "")))
                        acc = q.get("acceptedAnswer") or {}
                        back = clean(str(acc.get("text", ""))) if isinstance(acc, dict) else ""
                        if front:
                            cards.append({"q": front, "a": back})
                if title is None:
                    title = d.get("name")
    return title, cards

out = []
for url in URLS:
    sid = url.rstrip("/").split("/")[-1]
    try:
        r = requests.get(url, headers=UA, timeout=30)
        status = r.status_code
        page = r.text
    except Exception as e:
        print(f"{sid}: FETCH-ERROR {e}")
        continue
    with open(rf"{RAW}\{sid}.html", "w", encoding="utf-8", newline="") as f:
        f.write(page)
    title, cards = extract(page)
    declared = None
    m = re.search(r"(\d+)\s+Cards in this Set", page)
    if m:
        declared = int(m.group(1))
    print(f"{sid}: http={status} extracted={len(cards)} declared={declared} title={str(title)[:60]!r}")
    out.append({"set_id": sid, "url": url, "title": title, "declared": declared, "cards": cards})
    time.sleep(0.7)

with open(rf"{RAW}\cram_extracted.json", "w", encoding="utf-8", newline="") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOTAL CARDS", sum(len(s["cards"]) for s in out))
