# Audit extracted data: UK-junk keyword hits, empty answers, dup rates, samples.
import json, re, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKD", s).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", "", s)).strip()

JUNK = re.compile(r"\bCITB\b|\bscaffold|forklift|\bHSE\b|manual handling|\bNEBOSH\b|\bCPCS\b|construction site|skilled worker|cat and dog|bankman|signaller|site safety|ladder .*construction", re.I)

for tag, path, key in [("CRAM", r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\cram\cram_extracted.json", "set_id"),
                       ("BRAINSCAPE", r"D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape\brainscape_extracted.json", "deck_id")]:
    data = json.load(open(path, encoding="utf-8"))
    tot = junk = empty_a = 0
    seen = set(); dup = 0
    for s in data:
        for c in s["cards"]:
            tot += 1
            both = c["q"] + " " + c["a"]
            if JUNK.search(both): junk += 1
            if not c["a"].strip(): empty_a += 1
            n = norm(c["q"])
            if n in seen: dup += 1
            else: seen.add(n)
    print(tag, "total", tot, "junk-hits", junk, "empty-answers", empty_a, "dup", dup, f"uniq {len(seen)}")
    print("  sample q/a from first set:")
    for c in data[0]["cards"][:3]:
        print("   Q:", c["q"][:110])
        print("   A:", c["a"][:110])
