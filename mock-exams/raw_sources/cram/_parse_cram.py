# Re-parse dumped cram HTML with corrected extractor: Question uses "text" (or "name"); acceptedAnswer.text.
import json, re, html as htmlmod, glob, os

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\cram"
LD_RE = re.compile(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")

def clean(t):
    t = htmlmod.unescape(t)
    t = TAG_RE.sub(" ", t)
    return re.sub(r"\s+", " ", t).strip()

out = []
for path in glob.glob(os.path.join(RAW, "*.html")):
    sid = os.path.basename(path)[:-5]
    page = open(path, encoding="utf-8").read()
    cards, title = [], None
    for m in LD_RE.finditer(page):
        try:
            data = json.loads(m.group(1).strip())
        except Exception:
            continue
        items = data if isinstance(data, list) else [data]
        for d in items:
            if not isinstance(d, dict):
                continue
            if d.get("@type") == "Quiz" or "hasPart" in d:
                if title is None:
                    title = d.get("name")
                hp = d.get("hasPart") or []
                if isinstance(hp, dict):
                    hp = [hp]
                for q in hp:
                    if isinstance(q, dict) and q.get("@type") == "Question":
                        front = clean(str(q.get("text") or q.get("name") or ""))
                        acc = q.get("acceptedAnswer") or {}
                        back = clean(str(acc.get("text", ""))) if isinstance(acc, dict) else ""
                        if front:
                            cards.append({"q": front, "a": back})
    declared = None
    mm = re.search(r"(\d+)\s+Cards in this Set", page)
    if mm:
        declared = int(mm.group(1))
    print(f"{sid}: extracted={len(cards)} declared={declared} title={str(title)[:55]!r}")
    out.append({"set_id": sid, "url": "https://www.cram.com/flashcards/" + sid,
                "title": title, "declared": declared, "cards": cards})

with open(os.path.join(RAW, "cram_extracted.json"), "w", encoding="utf-8", newline="") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOTAL", sum(len(s["cards"]) for s in out))
