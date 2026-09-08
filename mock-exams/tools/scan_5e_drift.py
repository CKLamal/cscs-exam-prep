"""Scan bank/merged.json for possible drift from the 5th edition (read-only).

The question bank comes from pre-5e web sources. This script lists pattern
GROUP HITS (qid | source | part | pattern | snippet) so a later step can
adjudicate each candidate against the 5e text. It changes nothing.

Run:  python -X utf8 tools/scan_5e_drift.py          # full hit report + stats
      python -X utf8 tools/scan_5e_drift.py --rows   # one row per flagged qid
The script asserts merged.json sha256 is identical before and after the scan.
"""
import argparse, hashlib, json, os, re, sys

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"
MERGED = os.path.join(BANK, "merged.json")
FIELDS = ("question", "explanation_en", "explanation_zh", "answer_text")

GROUP_DESC = {
    "G1": "triad-only framing, no RED-s in same field (5e uses RED-s)",
    "G2": "RED-s mention (check wording consistency)",
    "G3": "vaping / e-cigarette (5e NEW in ch6; informational)",
    "G4": "injury psychology / mental-health terms near injury context",
    "G5": "overtraining / overreaching terms (review definitions vs 5e ch24)",
    "G6": "stale chapter title quoted in question text (informational)",
    "G7": "guideline-number traps: rest/recovery/intensity/HR claims",
    "G8": "amenorrhea / estrogen framing (5e broadened to RED-s, both sexes)",
}

# (group, pattern_name, primary regex, context regex, exclude regex, fields)
PATTERNS = [
    ("G1", "G1-triad-only",
     r"female athlete triad|\btriads?\b|女athlete|運動期?三联|女運動員?三联|三联[征症]",
     None, r"RED-?s|relative energy deficiency|energy availability|相對能量不足",
     FIELDS),
    ("G2", "G2-red-s",
     r"\bRED-?s\b|relative energy deficiency|相對能量不足|能量可得性",
     None, None, FIELDS),
    ("G3", "G3-vaping",
     r"\bvaping\b|\bvapes?\b|e-?cigarette|電子煙|电子烟",
     None, None, FIELDS),
    ("G4", "G4-injury-psych",
     r"athletic identity|fear of re-?injury|重新?受傷|運動身份|stress and injury|心理",
     r"injur|rehab|recover", None, FIELDS),
    ("G5", "G5-overtraining",
     r"over-?training|over-?reaching|過度訓練|過度運動",
     None, None, FIELDS),
    ("G6", "G6-stale-chapter-title",
     r"neuromuscular adaptations? to resistance training and detraining"
     r"|aerobic exercise adaptations",
     None, None, ("question",)),
    ("G7", "G7a-rest-interval-units",
     r"rest interval[^.\n]{0,60}(?:seconds?|minutes?|secs?\b|mins?\b)|休息間隔|休息间隔",
     None, None, FIELDS),
    ("G7", "G7b-48-72h-recovery",
     r"48\s*hours|72\s*hours|48[–-]\s*72|48 to 72",
     None, None, FIELDS),
    ("G7", "G7c-1-3-days",
     r"1[ –-]to[ –-]3 days|1-3 days|1–3 days",
     None, None, FIELDS),
    ("G7", "G7d-2-5-minutes",
     r"2[ –-]to[ –-]5 minutes|2-5 minutes|2–5 minutes",
     None, None, FIELDS),
    ("G7", "G7e-30s-circuit-split",
     r"30 seconds", r"circuit|split", None, FIELDS),
    ("G7", "G7f-80-85pct-1RM",
     r"(?:80%|85%)[^.\n]{0,40}1\s*RM", r"strength|resistance|load|intensity",
     None, FIELDS),
    ("G7", "G7g-220-age-hrmax",
     r"220\s*-\s*age|220-age|最大心率",
     None, None, FIELDS),
    ("G8", "G8-amenorrhea-estrogen",
     r"amenorrh|停經|停经|o?estrogen|雌激素",
     None, None, FIELDS),
]
COMPILED = [(g, n, re.compile(p, re.I), re.compile(c, re.I) if c else None,
             re.compile(x, re.I) if x else None, fs)
            for (g, n, p, c, x, fs) in PATTERNS]


def sha256_of(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def group_of(pattern_name):
    """'G7g-220-age-hrmax' -> 'G7'."""
    return re.match(r"G\d", pattern_name).group()


def snippet(text, m):
    lo, hi = max(0, m.start() - 80), min(len(text), m.end() + 80)
    s = re.sub(r"\s+", " ", text[lo:hi]).strip()
    return ("…" if lo > 0 else "") + s + ("…" if hi < len(text) else "")


def scan(questions):
    """Return (hit_rows, flagged: qid -> sorted pattern names)."""
    rows, flagged = [], {}
    for q in questions:
        for group, name, rx, ctx, excl, fields in COMPILED:
            for f in fields:
                text = q.get(f) or ""
                m = rx.search(text)
                if not m or (ctx and not ctx.search(text)) or (excl and excl.search(text)):
                    continue
                rows.append((q["id"], q.get("source"), q.get("part"),
                             f"{name} @{f}", snippet(text, m)))
                flagged.setdefault(q["id"], set()).add(name)
    rows.sort(key=lambda r: (group_of(r[3]), r[0]))  # keep G-sections contiguous
    return rows, flagged


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rows", action="store_true",
                    help="print one tab-separated row per flagged qid "
                         "(qid<TAB>patterns<TAB>source<TAB>part)")
    args = ap.parse_args()

    before = sha256_of(MERGED)
    with open(MERGED, encoding="utf-8") as f:
        data = json.load(f)
    questions = data["questions"]
    by_id = {q["id"]: q for q in questions}
    rows, flagged = scan(questions)
    after = sha256_of(MERGED)

    per_group = {g: set() for g in GROUP_DESC}
    for qid, pats in flagged.items():
        for p in pats:
            per_group[group_of(p)].add(qid)

    def print_stats(stream):
        print("\n===== statistics (unique questions) =====", file=stream)
        for g in sorted(GROUP_DESC):
            print(f"{g}: {len(per_group[g])} qids | {GROUP_DESC[g]}", file=stream)
        print(f"TOTAL flagged questions: {len(flagged)} (bank total {len(questions)})",
              file=stream)
        print(f"merged.json sha256 before: {before}", file=stream)
        print(f"merged.json sha256 after:  {after}", file=stream)
        assert before == after, "scan mutated merged.json — should be impossible (read-only)"
        print("sha256 unchanged: OK", file=stream)

    if args.rows:
        # rows on stdout; stats/guard on stderr so stdout stays machine-parseable
        for qid in sorted(flagged):
            q = by_id[qid]
            print(f"{qid}\t{','.join(sorted(flagged[qid]))}\t{q.get('source')}\t{q.get('part')}")
        print_stats(sys.stderr)
    else:
        current = None
        for qid, src, part, pat, snip in rows:
            grp = group_of(pat)
            if grp != current:
                current = grp
                print(f"\n===== {grp}: {GROUP_DESC[grp]} =====")
            print(f"{qid} | {src} | {part} | {pat} | {snip}")
        print_stats(sys.stdout)


if __name__ == "__main__":
    main()
