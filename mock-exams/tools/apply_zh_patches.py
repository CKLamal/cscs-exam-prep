"""Apply bank/zh/patch_*.json (id -> explanation_zh) onto bank/merged.json."""
import json, glob, os, sys

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"

def main():
    d = json.load(open(os.path.join(BANK, "merged.json"), encoding="utf-8"))
    by_id = {q["id"]: q for q in d["questions"]}
    applied = missing = unknown = 0
    for f in sorted(glob.glob(os.path.join(BANK, "zh", "patch_*.json"))):
        patch = json.load(open(f, encoding="utf-8"))
        for qid, zh in patch.items():
            q = by_id.get(qid)
            if q is None:
                unknown += 1
                continue
            if q.get("explanation_zh"):
                missing += 1  # already had zh (certprep) - keep original
                continue
            q["explanation_zh"] = zh
            applied += 1
    json.dump(d, open(os.path.join(BANK, "merged.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    with_zh = sum(1 for q in d["questions"] if q.get("explanation_zh"))
    print(f"applied={applied} kept-existing={missing} unknown-ids={unknown} "
          f"total_with_zh={with_zh}/{len(d['questions'])}")

if __name__ == "__main__":
    main()
