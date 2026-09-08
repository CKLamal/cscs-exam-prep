"""Regenerate tools/bank-data.js from bank/merged.json (run after zh patch apply)."""
import json, os

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"
TOOLS = r"D:\dgx-spark\cscs-exam-prep\mock-exams\tools"

d = json.load(open(os.path.join(BANK, "merged.json"), encoding="utf-8"))
zh = sum(1 for q in d["questions"] if q.get("explanation_zh"))
js = ("// Generated from bank/merged.json by tools/make_bank_data.py "
      f"({len(d['questions'])} questions, {zh} with explanation_zh)\n"
      "window.CSCS_BANK="
      + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";")
out = os.path.join(TOOLS, "bank-data.js")
open(out, "w", encoding="utf-8").write(js)
print(f"written {os.path.getsize(out)//1024} KB, questions={len(d['questions'])}, zh={zh}")
