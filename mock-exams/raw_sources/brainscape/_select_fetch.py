# Phase 2 redo: harvest deck links/titles/counts from CACHED pack+deck HTML (all formats),
# select top decks (max 5/pack, cap 18), fetch only uncached deck pages, extract cards.
import json, re, os, time, html as htmlmod
import requests

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
TAG_RE = re.compile(r"<[^>]+>")

def clean(t):
    t = htmlmod.unescape(t)
    t = TAG_RE.sub(" ", t)
    return re.sub(r"\s+", " ", t).strip()

decks = {}  # did -> [href, title, count]

def harvest(page):
    n = 0
    # pack page format: deck-list-link + deck-item-title + deck-item-count "491\n cards"
    for m in re.finditer(r'<a class="deck-list-link" href="(/flashcards/[a-z0-9-]+-(\d+)(?:/packs/(\d+))?)"[^>]*>(.*?)</a>', page, re.S):
        href, did, inner = m.group(1), m.group(2), m.group(4)
        t = re.search(r'class="deck-item-title"[^>]*>(.*?)</div>', inner, re.S)
        c = re.search(r'class="deck-item-count"[^>]*>\s*(\d+)', inner)
        if did not in decks or decks[did][2] is None:
            decks[did] = [href, clean(t.group(1)) if t else decks.get(did, ["", "", None])[1],
                          int(c.group(1)) if c else decks.get(did, ["", "", None])[2]]
            n += 1
    # deck page sidebar format: deck-link + deck-name + deck-card-count
    for m in re.finditer(r'<a class="deck-link[^"]*" href="(/flashcards/[a-z0-9-]+-(\d+)(?:/packs/(\d+))?)">(?:(?!</a>).)*?</a>', page, re.S):
        href, did, inner = m.group(1), m.group(2), m.group(0)
        t = re.search(r'class="deck-name"[^>]*>(.*?)</div>', inner, re.S)
        c = re.search(r'class="deck-card-count"[^>]*>(\d+)', inner)
        if did not in decks or decks[did][2] is None:
            decks[did] = [href, clean(t.group(1)) if t else decks.get(did, ["", "", None])[1],
                          int(c.group(1)) if c else decks.get(did, ["", "", None])[2]]
            n += 1
    return n

for fn in sorted(os.listdir(RAW)):
    if fn.endswith(".html"):
        harvest(open(os.path.join(RAW, fn), encoding="utf-8").read())

cand = [(v[2], d, v[0], v[1]) for d, v in decks.items() if v[2]]
cand.sort(reverse=True)
print("decks known:", len(decks), "with counts:", len(cand))
sel, per_pack = [], {}
for cnt, did, href, name in cand:
    pack = href.rsplit("/packs/", 1)[-1] if "/packs/" in href else "solo-" + did
    if per_pack.get(pack, 0) >= 5:
        continue
    per_pack[pack] = per_pack.get(pack, 0) + 1
    sel.append((cnt, did, href, name))
    if len(sel) >= 18:
        break
print("SELECTED", len(sel), "raw cards:", sum(c for c, *_ in sel))
for c, d, h, n in sel:
    print(f"  {c:4d} {d} {n[:58]!r}")

Q1_RE = re.compile(r'class="flashcard-contents question-contents".*?class="scf-face"[^>]*>(.*?)</div>', re.S)
A1_RE = re.compile(r'class="flashcard-contents answer-contents".*?class="scf-face"[^>]*>(.*?)</div>', re.S)
Q2_RE = re.compile(r'class="question-content"[^>]*>(.*?)</div>', re.S)
A2_RE = re.compile(r'class="answer-content"[^>]*>(.*?)</div>', re.S)

def extract_cards(page):
    cards = []
    for ch in page.split('<div class="flashcard-row')[1:]:
        q = a = None
        m = Q1_RE.search(ch) or Q2_RE.search(ch)
        n = A1_RE.search(ch) or A2_RE.search(ch)
        if m: q = clean(m.group(1))
        if n: a = clean(n.group(1))
        if q:
            cards.append({"q": q, "a": a or ""})
    return cards

out = []
for cnt, did, href, title in sel:
    path = os.path.join(RAW, f"deck_{did}.html")
    url = "https://www.brainscape.com" + href
    if os.path.exists(path):
        page = open(path, encoding="utf-8").read()
        src = "cached"
    else:
        r = requests.get(url, headers=UA, timeout=30)
        page = r.text
        open(path, "w", encoding="utf-8", newline="").write(page)
        src = f"fetched {r.status_code}"
        time.sleep(0.7)
    cards = extract_cards(page)
    hdr = re.search(r'\((\d+)\s+cards?\)', page)
    declared = int(hdr.group(1)) if hdr else None
    print(f"deck {did}: {src} extracted={len(cards)} declared={declared} {title[:50]!r}")
    out.append({"deck_id": did, "url": url, "title": title, "declared": declared, "cards": cards})

with open(os.path.join(RAW, "brainscape_extracted.json"), "w", encoding="utf-8", newline="") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOTAL BRAINSCAPE", sum(len(s["cards"]) for s in out))
