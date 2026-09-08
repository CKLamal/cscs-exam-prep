"""Merge bank/*.json sources into bank/merged.json with cross-source dedupe.

Dedupe policy:
- MCQ: key = normalized(question + '|' + answer_text). First source wins by
  quality priority (has explanation_en > source priority order).
- Flashcard: key = normalized(question). A flashcard whose front matches an
  MCQ question is dropped (MCQ is studyable in exam form).
Garbage filter: non-printable ratio > 5% or too-short fields are dropped.
"""
import json, glob, os, re, unicodedata, sys

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"
SRC_PRIORITY = ["liftaroo", "packman", "traineracademy", "certprep",
                "nsca-sample", "nsca-vol1", "ptgeeks", "quizlet",
                "cram", "brainscape"]

def norm(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def printable_ratio(s):
    if not s:
        return 1.0
    bad = sum(1 for c in s if unicodedata.category(c) in ("Cc", "Co", "Cn") and c != "\n")
    return 1 - bad / len(s)

def load_sources():
    files = {os.path.basename(f)[:-5]: f for f in glob.glob(os.path.join(BANK, "*.json"))}
    out = []
    for key in SRC_PRIORITY:
        if key in files:
            out.append((key, json.load(open(files[key], encoding="utf-8"))))
    for k, f in files.items():  # any file not in priority list
        if k not in SRC_PRIORITY and k != "schema" and k != "merged":
            out.append((k, json.load(open(f, encoding="utf-8"))))
    return out

def main():
    dropped = {"garbled": 0, "dup": 0, "dup_vs_mcq": 0, "incomplete": 0}
    per_src = {}
    mcq_keys, flash_keys, kept = {}, {}, []

    # pass 1: MCQs (priority order), pass 2: flashcards
    sources = load_sources()
    for want_mcq in (True, False):
        for key, doc in sources:
            src = doc.get("source", key)
            for q in doc.get("questions", []):
                is_mcq = q.get("item_type", "mcq") == "mcq"
                if is_mcq != want_mcq:
                    continue
                question = (q.get("question") or "").strip()
                per_src[key] = per_src.get(key, 0) + 1
                min_len = 15 if is_mcq else 2  # flashcard fronts may be short terms
                if len(question) < min_len or printable_ratio(question) < 0.95:
                    dropped["garbled"] += 1
                    continue
                if is_mcq:
                    if not q.get("options") or q.get("answer") is None:
                        dropped["incomplete"] += 1
                        continue
                    if q["answer"] >= len(q["options"]):
                        dropped["incomplete"] += 1
                        continue
                    k = norm(question) + "|" + norm(q.get("answer_text") or
                                                    q["options"][q["answer"]])
                    if k in mcq_keys:
                        # keep the copy that has an explanation
                        if not q.get("explanation_en") and not q.get("explanation_zh"):
                            dropped["dup"] += 1
                            continue
                        for i, prev in enumerate(kept):
                            if prev["_k"] == k:
                                if not (prev.get("explanation_en") or prev.get("explanation_zh")):
                                    kept[i] = {**q, "_k": k, "_src": key}
                                break
                        dropped["dup"] += 1
                        continue
                    mcq_keys[k] = True
                    kept.append({**q, "_k": k, "_src": key})
                else:
                    k = norm(question)
                    if k in mcq_keys:
                        dropped["dup_vs_mcq"] += 1
                        continue
                    if k in flash_keys:
                        dropped["dup"] += 1
                        continue
                    flash_keys[k] = True
                    kept.append({**q, "_k": k, "_src": key})

    merged = []
    for i, q in enumerate(kept, 1):
        q.pop("_k", None)
        src = q.pop("_src")
        q["id"] = f"q{i:04d}"
        q["source"] = src
        merged.append(q)

    out = {
        "generated_utc": "2026-09-08",
        "note": "Merged+deduped from bank source files. See SOURCES.md for provenance.",
        "counts": {
            "total": len(merged),
            "mcq": sum(1 for q in merged if q.get("item_type", "mcq") == "mcq"),
            "flashcard": sum(1 for q in merged if q.get("item_type") == "flashcard"),
        },
        "questions": merged,
    }
    json.dump(out, open(os.path.join(BANK, "merged.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("per-source read:", per_src)
    print("dropped:", dropped)
    print("kept:", out["counts"])

if __name__ == "__main__":
    main()
