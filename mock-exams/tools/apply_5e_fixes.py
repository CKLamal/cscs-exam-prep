"""Apply adjudicated 5e fixes to bank/merged.json (see mock-exams/AUDIT_5e.md).

Each entry in FIXES is {question_id: {field: new_value}}. Only fields whose
current value differs are replaced, so re-running after the fixes are in the
bank is a no-op (applied=0, file untouched). merged.json is rewritten with
the same json.dump parameters as merge_bank.py (ensure_ascii=False, indent=1,
text-mode write), keeping the file byte-format identical outside edited fields.

generated_utc / note / counts are never touched. Question count must stay 3205.

Run:  python -X utf8 tools/apply_5e_fixes.py
"""
import json
import os

BANK = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank"
MERGED = os.path.join(BANK, "merged.json")

# Adjudicated fixes (AUDIT_5e.md 判定=修正). Page citations refer to the 5e
# PDF (PDF page = book page).
FIXES = {
    # q1542 — 4e-era 1:3 recovery key contradicts 5e interval guidance
    # (3-5 min work intervals use 1:1 rest; 2-3 min reps at >=90% VO2max use
    # <=2 min recovery; longer rests blunt the glycolytic stimulus; p1540-1541).
    "q1542": {
        "answer": 1,
        "answer_text": "2 minutes",
        "explanation_zh": "5e 第21章（p1540–1541）：3–5 分鐘的工作間隔，休息時間應等於工作時間（W:R 1:1）；長間歇 HIIT 的例子是 ≥90% VO2max 下跑 2–3 分鐘、搭配 ≤2 分鐘的被動或低強度恢復；休息過長會削弱糖解系統的訓練效果。因此 2 分鐘跑完的 800 公尺間歇，組間休息以約 2 分鐘為宜。（舊答案 6 分鐘採 4e 時代無氧間歇 1:3+ 說法，與 5e 的間歇建議不符。）",
    },
    # q1676 — flashcard teaches the obsolete 4e female-athlete-triad frame;
    # 5e uses RED-S ("formerly known as the female athlete triad", p1693;
    # RED-s content p650).
    "q1676": {
        "answer_text": "A legacy concept (replaced by RED-S in the 5th edition) of three interrelated disorders: low energy availability with disordered eating (including excessive exercising), menstrual dysfunction (amenorrhea) and decreased bone density. RED-S broadens this: low energy availability also affects metabolic rate, immunity, protein synthesis and cardiovascular function, and occurs in males as well as females",
        "explanation_zh": "女運動員三聯症（female athlete triad）：能量可用性不足（飲食失調、含過度運動）、月經功能失調（停經）與骨密度下降三種互相關聯的失調。5e 已改以「運動相對能量不足」（RED-S）取代此舊稱（第24章 p1693）：低能量可用性（攝取低於消耗）除月經與骨健康外，還影響代謝率、免疫、蛋白質合成與心血管功能，男性選手也可能發生（第11章 p650）。",
    },
    # q2442 — "training adaptation syndrome (TAS)" appears nowhere in 5e;
    # 5e frames this as GAS (p1681) plus involution/detraining (p1191, p1584).
    "q2442": {
        "question": "Describe general adaptation syndrome (GAS) in relation to homeostasis.",
        "explanation_zh": "一般適應症候群（GAS，5e 第24章 p1681）：新訓練刺激使身體偏離恆定 (homeostasis) 而出現疲倦（警戒期）；身體能抗住壓力時，適應／恢復期出現超量恢復 (supercompensation)、高於恆定、變得更強；若壓力持續、超過退化 (involution，5e 第18章 p1191；第21章 p1584) 點，身體無法再適應、表現持續下滑，最終導致過度訓練。（5e 通篇以 GAS 與 involution/detraining 表述，已不再使用 training adaptation syndrome〔TAS〕一詞。）",
    },
    # q2453 — hypertrophy rest "30 s-1.5 min" is the 4e row; 5e table 18.15
    # (p1253-1254): hypertrophy 2-3 min multijoint / 60-90 s single-joint.
    "q2453": {
        "answer_text": "Strength 2-5 minutes of rest Power - Single and Multi event 2-5 minutes of rest Hypertrophy 2-3 minutes for multijoint exercises, 60-90 seconds for single-joint exercises Muscular Endurance less than 30 seconds of rest",
        "explanation_zh": "組間休息依訓練目標（5e 第18章表18.15，p1253–1254）：肌力 2–5 分鐘；功率（單次與多次用力專案）2–5 分鐘；肥大：多關節動作 2–3 分鐘、單關節動作 60–90 秒；局部肌耐力 <30 秒。休息長短對應所用能量系統的還原需求。（舊版「肥大 30 秒–1.5 分鐘」在 5e 已改。）",
    },
    # q1444 — question/answer match 5e (table 18.11); zh exam tip still
    # quotes 4e ranges (Power 75-90%/1-5, Hypertrophy 67-85%/6-12).
    "q1444": {
        "explanation_zh": "NSCA 指南：最大肌力（maximal strength）訓練使用 ≥85% 1RM，≤6 次反覆。此強度範圍主要透過神經適應（neural adaptation）提升力量，包括增加運動單元徵召（motor unit recruitment）和發射頻率（rate coding）。\n【考試提示】5e 表18.11（p1237–1238）四大訓練目標的 %1RM 與目標次數：Strength ≥85%（≤6 次，核心動作）、Power 多次用力 75-85%（3-5 次；單次用力 80-90%×1-2 次，p1240）、Hypertrophy 67-80%（8-12 次）、Endurance ≤67%（≥12 次）。必背！",
    },
    # q1447 — correct option stays valid under 5e; zh tip quotes 4e
    # hypertrophy range (5e table 18.11, p1237: 67-80% 1RM, 8-12 reps).
    "q1447": {
        "explanation_zh": "NSCA 肌肥大指南（5e 表18.11，p1237）：67-80% 1RM，8-12 次反覆。75% 1RM（約 10RM）× 10 reps 完全符合此範圍。95%×2 屬於 strength；60%×20 和 50%×30 屬於 endurance。\n【考試提示】Hypertrophy zone = 67-80% 1RM, 8-12 reps（5e 第18章；舊版 67-85%、6-12 次已更新）。考題常給一組數字讓你判斷屬於哪個訓練目標，直接對照範圍即可。",
    },
    # q1456 — correct option remains a valid intermediate hypertrophy dose;
    # zh tip quotes 4e load range/sets (5e tables 18.11 p1237, 18.13 p1248).
    "q1456": {
        "explanation_zh": "NSCA 肌肥大訓練指南（5e 第18章）：核心動作強度 67-80% 1RM（表18.11，p1237）；目標次數初階 8-12、中階 6-12、高階 3-12，組數初階 1-3、中階以上 ≥3（表18.13，p1248）。此範圍產生充足的機械張力（mechanical tension）和代謝壓力（metabolic stress），是肌肥大的兩大刺激因素。\n【考試提示】肌肥大負荷 67-80% 1RM；次數依訓練程度 8-12／6-12／3-12，組數初階 1-3、中階以上 ≥3。Strength = ≥85% 1RM × ≤6 次；Endurance = <67% 1RM × ≥12 次。",
    },
    # q1955 — flashcard answer quotes 4e load/volume tables (hypertrophy
    # 67-85%/6-12/3-6 sets, strength 2-6 sets); 5e tables 18.11/18.13 differ.
    "q1955": {
        "answer_text": "Strength ≥85% of 1RM, ≤6 reps. Power single event 80-90% of 1RM, 1-2 reps. Power multi event 75-85% of 1RM, 3-5 reps. Hypertrophy 67-80% of 1RM, 8-12 reps (novice goal; 6-12 intermediate, 3-12 advanced). Muscular Endurance <67% of 1RM, 12+ reps. Sets: 1-3 for novices, ≥3 for intermediate and advanced",
        "explanation_zh": "負荷與訓練量須與目標對應（5e 第18章表18.11，p1237–1238；表18.13，p1248）：肌力 ≥85% 1RM×≤6 次；功率單次 80–90%×1–2 次（p1240）、多次 75–85%×3–5 次；肥大 67–80%×8–12 次（初階目標；中階 6–12、高階 3–12）；肌耐力 <67%×≥12 次；組數初階 1–3 組、中階以上 ≥3 組。",
    },
}

EDITABLE = ("question", "options", "answer", "answer_text",
            "explanation_en", "explanation_zh")


def brief(v):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    s = " ".join(str(s).split())
    return s[:60]


def main():
    with open(MERGED, encoding="utf-8") as f:
        data = json.load(f)
    questions = data["questions"]
    assert len(questions) == 3205, f"expected 3205 questions, found {len(questions)}"
    by_id = {q["id"]: q for q in questions}
    assert len(by_id) == len(questions), "duplicate question ids"

    applied = 0
    for qid, fields in FIXES.items():
        q = by_id.get(qid)
        if q is None:
            raise KeyError(f"qid {qid} not in bank")
        for field, new in fields.items():
            assert field in EDITABLE, f"{qid}: unexpected field {field}"
            old = q.get(field)
            if old == new:
                continue
            print(f"APPLY {qid} [{field}]: {brief(old)!r} -> {brief(new)!r}")
            q[field] = new
            applied += 1

    if applied:
        # Same dump parameters as merge_bank.py (text-mode write keeps the
        # file's CRLF line endings on Windows).
        json.dump(data, open(MERGED, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        with open(MERGED, encoding="utf-8") as f:
            check = json.load(f)
        assert len(check["questions"]) == 3205
    print(f"applied={applied} (fix groups: {len(FIXES)}), questions=3205")


if __name__ == "__main__":
    main()
