# Brainscape pipeline phase 1+3: fetch pack pages, harvest deck links+counts, pick top decks,
# fetch deck pages, extract all cards (both SSR formats: preview scf-face cards & thin-card rows).
import json, re, os, time, html as htmlmod
import requests

RAW = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.9"}

PACKS = [
    "https://www.brainscape.com/packs/cscs-prep-1381405",
    "https://www.brainscape.com/packs/nsca-cscs-flashcards-17159362",
    "https://www.brainscape.com/packs/cscs-22071782",
    "https://www.brainscape.com/packs/cscs-exercise-science-section-14689900",
    "https://www.brainscape.com/packs/cscs-practical-applied-pass-prep-15863340",
]
# already-dumped sources: probe_pack_20661425 (Ty Jahnke), probe2_14791808_browser (India Davis sidebar)
EXTRA_HTML = [os.path.join(RAW, "probe_pack_20661425.html"),
              os.path.join(RAW, "probe2_14791808_browser.html")]

TAG_RE = re.compile(r"<[^>]+>")
DECK_LINK_RE = re.compile(r'href="(/flashcards/[a-z0-9-]+-(\d+)(?:/packs/(\d+))?)"[^>]*>(.*?)</a>', re.S)

def clean(t):
    t = htmlmod.unescape(t)
    t = TAG_RE.sub(" ", t)
    t = re.sub(r"\*\*", "", t)
    return re.sub(r"\s+", " ", t).strip()

def harvest(page):
    """deck_id -> (url, title, count)"""
    found = {}
    # sidebar/deck-list pattern: <a ... href="/flashcards/slug-ID/packs/P"> ... <div class="deck-name">T</div><div class="deck-card-count">N</div>
    for m in re.finditer(r'href="(/flashcards/[a-z0-9-]+-(\d+)(?:/packs/(\d+))?)"[^>]*>(.*?)</a>', page, re.S):
        href, did, pack, inner = m.group(1), m.group(2), m.group(3), m.group(4)
        name_m = re.search(r'class="deck-name"[^>]*>(.*?)</div>', inner, re.S)
        cnt_m = re.search(r'class="deck-card-count"[^>]*>(\d+)', inner)
        name = clean(name_m.group(1)) if name_m else ""
        cnt = int(cnt_m.group(1)) if cnt_m else None
        if not name and not cnt:
            continue
        prev = found.get(did)
        if not prev or (prev[2] is None and cnt is not None) or (not prev[1] and name):
            found[did] = (href, name, cnt)
    # pack pages may use different markup; fallback: bare links + preceding count text
    for m in re.finditer(r'href="(/flashcards/([a-z0-9-]+)-(\d+)(?:/packs/(\d+))?)"', page):
        did = m.group(3)
        if did not in found:
            found[did] = (m.group(1), "", None)
    return found

decks = {}  # did -> (url, title, count)
for url in PACKS:
    pid = url.rstrip("/").split("-")[-1]
    try:
        r = requests.get(url, headers=UA, timeout=30)
        page = r.text
    except Exception as e:
        print("PACK FETCH ERR", url, e)
        continue
    open(os.path.join(RAW, f"pack_{pid}.html"), "w", encoding="utf-8", newline="").write(page)
    f = harvest(page)
    print(f"pack {pid}: http={r.status_code} decks={len(f)} with_counts={sum(1 for v in f.values() if v[2])}")
    for k, v in f.items():
        decks.setdefault(k, v)
    time.sleep(0.7)
for path in EXTRA_HTML:
    f = harvest(open(path, encoding="utf-8").read())
    print("extra", os.path.basename(path), "decks=", len(f))
    for k, v in f.items():
        decks.setdefault(k, v)

# selection: decks with known counts, ranked desc, max 5 per pack, cap 18
by_pack = {}
cand = []
for did, (href, name, cnt) in decks.items():
    if cnt is None:
        continue
    pack = href.split("/packs/")[-1] if "/packs/" in href else (href.split("-")[-1])
    cand.append((cnt, did, href, name, pack))
cand.sort(reverse=True)
sel, per_pack = [], {}
for cnt, did, href, name, pack in cand:
    if per_pack.get(pack, 0) >= 5:
        continue
    per_pack[pack] = per_pack.get(pack, 0) + 1
    sel.append((cnt, did, href, name))
    if len(sel) >= 18:
        break
print("SELECTED", len(sel), "total cards:", sum(c for c, *_ in sel))
for c, did, href, name in sel:
    print(f"  {c:4d} {name[:55]!r}")

with open(os.path.join(RAW, "deck_selection.json"), "w", encoding="utf-8", newline="") as f:
    json.dump([{"count": c, "deck_id": d, "href": h, "title": n} for c, d, h, n in sel], f, indent=1)

Q1_RE = re.compile(r'class="flashcard-contents question-contents".*?class="scf-face"[^>]*>(.*?)</div>', re.S)
A1_RE = re.compile(r'class="flashcard-contents answer-contents".*?class="scf-face"[^>]*>(.*?)</div>', re.S)
Q2_RE = re.compile(r'class="question-content"[^>]*>(.*?)</div>', re.S)
A2_RE = re.compile(r'class="answer-content"[^>]*>(.*?)</div>', re.S)

def extract_cards(page):
    cards = []
    chunks = page.split('<div class="flashcard-row')
    for ch in chunks[1:]:
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
    url = "https://www.brainscape.com" + href
    try:
        r = requests.get(url, headers=UA, timeout=30)
        page = r.text
    except Exception as e:
        print("DECK ERR", did, e)
        continue
    open(os.path.join(RAW, f"deck_{did}.html"), "w", encoding="utf-8", newline="").write(page)
    cards = extract_cards(page)
    hdr = re.search(r'\((\d+)\s+cards?\)', page)
    declared = int(hdr.group(1)) if hdr else None
    print(f"deck {did}: http={r.status_code} extracted={len(cards)} declared={declared} title={title[:50]!r}")
    out.append({"deck_id": did, "url": url, "title": title, "declared": declared, "cards": cards})
    time.sleep(0.7)

with open(os.path.join(RAW, "brainscape_extracted.json"), "w", encoding="utf-8", newline="") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOTAL BRAINSCAPE", sum(len(s["cards"]) for s in out))
