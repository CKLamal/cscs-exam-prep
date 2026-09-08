# Build bank/cram.json + bank/brainscape.json: junk filter, dedupe, balanced selection within caps,
# schema fields, UTF-8 no BOM, then validate by re-parse.
import json, re, unicodedata

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"
CRAM_SRC = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\cram\cram_extracted.json"
BS_SRC = r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape\brainscape_extracted.json"

JUNK = re.compile(r"\bCITB\b|\bscaffold|forklift|\bHSE\b|manual handling|\bNEBOSH\b|\bCPCS\b|construction site|skilled worker|cat and dog|bankman|signaller|site safety", re.I)

def norm(s):
    s = unicodedata.normalize("NFKD", s).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", "", s)).strip()

CH_MULTI = re.compile(r"chapters?\s*(\d{1,2})\s*(?:\+|and|/)\s*(\d{1,2})", re.I)
CH_ONE = re.compile(r"(?:chapter|ch\.?|chpt\.?|section)\s*-?\s*(\d{1,2})", re.I)

def chapter_part(title):
    t = title or ""
    m = CH_MULTI.search(t)
    if m or "+" in t.lower().replace("cscs", ""):
        nums = [int(x) for x in re.findall(r"(?:chapters?|ch\.?|chpt\.?)\s*-?\s*(\d{1,2})", t, re.I)]
        if len(nums) >= 2:
            part = 1 if all(n <= 11 for n in nums) else (2 if all(n >= 12 for n in nums) else None)
            return None, part  # multi-chapter: chapter null
    m = CH_ONE.search(t)
    if m:
        n = int(m.group(1))
        if 1 <= n <= 26:
            return n, (1 if n <= 11 else 2)
    tl = t.lower()
    if any(k in tl for k in ("nutrition", "psychology", "exercise science", "scientific", "bioenergetics",
                             "biomechanic", "structure and function", "endocrine", "adaptation", "normative data")):
        return None, 1
    if any(k in tl for k in ("program design", "practical", "applied", "technique", "implementation",
                             "organization", "organisation", "administration", "periodization", "facility")):
        return None, 2
    return None, None

def domain_of(title):
    tl = (title or "").lower()
    table = [
        ("nutrition", "Nutrition"), ("psycholog", "Sport Psychology"),
        ("exercise technique", "Exercise Technique"),
        ("program design", "Program Design"), ("periodization", "Program Design"),
        ("organization", "Organization & Administration"), ("organisation", "Organization & Administration"),
        ("administration", "Organization & Administration"), ("normative data", "Program Implementation"),
        ("exercise science", "Exercise Sciences"), ("scientific", "Exercise Sciences"),
        ("practical", "Practical/Applied"), ("applied", "Practical/Applied"),
    ]
    for k, v in table:
        if k in tl:
            return v
    return None

# set/deck ids whose title names one chapter but content mixes chapters
MULTI_EXCEPTIONS = {"cscs-test-prep-chapter-1-5124275"}

def build(src_path, prefix, cap, source, source_url, license_note):
    data = json.load(open(src_path, encoding="utf-8"))
    tot = junk = empty_a = dup = 0
    per_set = []
    seen = set()
    queues = []
    for s in data:  # sets sorted by size desc (input order preserved from extraction)
        kept = []
        for c in s["cards"]:
            tot += 1
            if not c["a"].strip():
                empty_a += 1
                continue
            if JUNK.search(c["q"] + " " + c["a"]):
                junk += 1
                continue
            n = norm(c["q"])
            if n in seen:
                dup += 1
                continue
            seen.add(n)
            kept.append(c)
        per_set.append((s.get("title") or s.get("set_id") or s.get("deck_id"), len(s["cards"]), len(kept)))
        queues.append((s, kept))
    # balanced round-robin fill to cap
    chosen = []
    idx = 0
    while len(chosen) < cap:
        advanced = False
        for s, kept in queues:
            if idx < len(kept):
                chosen.append((s, kept[idx]))
                advanced = True
                if len(chosen) >= cap:
                    break
        if not advanced:
            break
        idx += 1
    questions = []
    for i, (s, c) in enumerate(chosen, 1):
        title = s.get("title") or ""
        sid = s.get("set_id") or s.get("deck_id") or ""
        if sid in MULTI_EXCEPTIONS:
            ch, part = None, None
        else:
            ch, part = chapter_part(title)
        questions.append({
            "id": f"{prefix}-{i:03d}",
            "part": part,
            "domain": domain_of(title),
            "textbook_chapter": ch,
            "question": c["q"],
            "options": None,
            "answer": None,
            "answer_text": c["a"],
            "explanation_en": None,
            "item_type": "flashcard",
            "tags": [title],
        })
    doc = {"source": source, "source_url": source_url, "retrieved_utc": "2026-09-08",
           "license_note": license_note, "questions": questions}
    out = rf"{BANK}\{prefix}.json"
    with open(out, "w", encoding="utf-8", newline="") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"== {prefix}: wrote {len(questions)} (raw {tot}, junk {junk}, empty-ans {empty_a}, dup {dup})")
    for t, raw, kept in per_set:
        print(f"   {raw:4d} -> {kept:4d}  {t[:60]!r}")
    return out

build(CRAM_SRC, "cram", 600, "cram-flashcard-sets",
      "https://www.cram.com (15 public CSCS flashcard sets; see tags for set titles)",
      "Public user-generated flashcards; personal study use.")
build(BS_SRC, "brainscape", 800, "brainscape-public-decks",
      "https://www.brainscape.com (18 public CSCS decks from 6 user packs; see tags for deck titles)",
      "Public user-generated flashcards; personal study use.")

# ---- validation ----
print("\n== VALIDATION ==")
for prefix in ("cram", "brainscape"):
    p = rf"{BANK}\{prefix}.json"
    raw = open(p, "rb").read()
    assert raw[:3] != b"\xef\xbb\xbf", "BOM found!"
    doc = json.loads(raw.decode("utf-8"))
    qs = doc["questions"]
    ids = [q["id"] for q in qs]
    assert len(ids) == len(set(ids))
    assert all(q["item_type"] == "flashcard" and q["options"] is None and q["answer"] is None
               and q["question"].strip() and q["answer_text"].strip() for q in qs)
    nq = [norm(q["question"]) for q in qs]
    assert len(nq) == len(set(nq)), "dupes!"
    b = sum(1 for q in qs if q["part"] == 1); b2 = sum(1 for q in qs if q["part"] == 2)
    print(f"{prefix}: OK {len(qs)} questions, part1={b} part2={b2} null-part={len(qs)-b-b2}")
    for q in qs[:2]:
        print("   sample:", q["id"], "|", q["question"][:80], "|", q["answer_text"][:60], "| ch", q["textbook_chapter"])
