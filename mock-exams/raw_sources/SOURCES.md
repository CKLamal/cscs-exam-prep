# CSCS Practice Question Sources — verified 2026-09-08 (live-fetch tested)

CSCS = NSCA Certified Strength and Conditioning Specialist.
TRAP WARNING: "CSCS" also = UK construction card (CITB). Exclude cscsmocktest.uk, nvqreviews, chawichr/cscs-quiz, anything mentioning forklifts/scaffold/HSE.

## Output contract
Normalized question JSON: see `mock-exams/bank/schema.json` (UTF-8, no BOM).
Target folder: `mock-exams/bank/`. One file per source: `<sourcekey>.json`.
Question text EN. Chinese explanations: keep if source has them (certprep), field for later enrichment.

## TIER 1 — verified extractable with plain HTTP

### 1. liftaroo.app/cscs  → bank/liftaroo.json  (EXPECTED ~854)
- Single GET of https://liftaroo.app/cscs hub HTML (~824KB) contains the FULL MCQ bank embedded as JSON: objects shaped `{"q": "...", "opts": ["...","...","...","..."], "ci": <correct index 0-3>, "exp": "explanation"}`.
- Extract every such object (script tag content). Reddit pass-reports recommend this site ("feels like real exam"). Highest quality-per-fetch.
- /cscs/chNN-*.html pages are exercise videos, NOT questions. Hub only.

### 2. GitHub The-Pack-Man/CSCS-Streamlit-mobile  → bank/packman.json  (EXPECTED ~426)
- raw.githubusercontent.com/The-Pack-Man/CSCS-Streamlit-mobile/main/content/questions/chapter01_*.json .. chapter24_*.json (~226 Q)
- .../content/PracticeTests/BookPracticeTest1.json (100 Q), ChatPractice1.json (100 Q)
- Schema confirmed: `{"id","question","choices":[4],"answer_index","explanation"}`. Chapter files map 1:1 to Essentials 4th ed chapters → set textbook_chapter.
- Also check backups/*.json (444KB) for extra/updated questions — parse if question-shaped.

### 3. GitHub junzhi1117-web/certprep  → bank/certprep.json  (EXPECTED 100)
- raw.githubusercontent.com/junzhi1117-web/certprep/main/src/data/cscs-program-design.ts (50 Q) and cscs-program-implementation.ts (50 Q)
- TS array objects: `{id, question, options:{A,B,C,D}, correct, explanation (traditional Chinese), examTip (zh), topic, part}` → keep zh text in explanation_zh field. part = 2 (Program Design/Implementation).

### 4. Cram.com flashcard sets  → bank/cram.json  (EXPECTED 500+)
- EVERY set page embeds complete deck in `<script type="application/ld+json">`: `hasPart[]` of `{"@type":"Question","name":...,"acceptedAnswer":{"@type":"Answer","text":...}}`. Verified 90/90 and 39/39 full coverage.
- Discovery: Google/exa `site:cram.com/flashcards cscs` + follow similar-set links in fetched pages. Verified CSCS sets include ...-13166538 (90 cards), -10125265, sizes 126/101/90/76/63/56/35/33/32/16.
- Site's own search page = JS shell; do not use it.

### 5. Brainscape public decks  → bank/brainscape.json  (EXPECTED ~800+)
- Deck pages SSR full card front/back text (verified). Example: brainscape.com/flashcards/scientific-foundations-3-11741227, pack page /packs/20661425.
- Known packs: Ty Jahnke "CSCS" 17 decks (~500+), Zachary Taylor "Cscs Extra" (115+), Joshua Amaral pack (11 decks, one has 134 cards). Crawl pack pages for deck URLs.

### 6. Quizlet sets  → bank/quizlet.json  (EXPECTED 1000+)
- KEY: use UA `Lynx/2.8.9` (or any text-mode UA). Chrome UA gets 160KB JS shell; Lynx UA returns full server-rendered terms (verified 2 sets: 976885133 648 terms = 1.4MB; 411370382 121 terms). API v2 = dead (returns HTML error).
- Parse "Terms in this set (N)" section. Start sets: 976885133 (648), 110569805 (229), 411370382 (121), 519458268 (107), 1049400999 (91, may need retry), 489019025, 340198680, 575050214, 634058736, 655535133 (ch1-24 textbook study questions — crawl its links for more chapter sets).
- Flaky per-set: retry 2-3x, 2-4s delay. Flashcard front/back → question + answer text (no options: synthesize MCQ only if trivial; else store as flashcard-style with null options... NO — keep schema: put full front in question, back in explanation, options null is NOT allowed; for flashcard-style items convert to `options: [correct, "", "", ""]`? DECISION: extraction agent should keep only items that are genuinely MCQ-convertible OR mark `"item_type":"flashcard"` extra field allowed, options may be null for flashcards. Tool renders flashcards as reveal-answer cards.)
- Search additional sets via Google/exa `site:quizlet.com cscs chapter study questions`.

### 7. traineracademy.org/training/cscs-practice-test/  → bank/traineracademy.json  (EXPECTED 100)
- Single GET (1.9MB): 100 questions + "Correct answer" markers all in HTML (verified counts 115/103). Parse carefully, keep rationale text if present.

### 8. practicetestgeeks PDF  → bank/ptgeeks.json
- https://practicetestgeeks.com/pdf/NSCA-CSCS_Practice_Test_Questions_and_Answers.pdf — verified 200 application/pdf 139KB BUT needs browser UA + Referer (403 otherwise). Parse text, extract Q + options + answer + explanation.

### 9. NSCA official handbook sample questions  → bank/nsca-sample.json
- https://www.nsca.com/globalassets/certification/certification-pdfs/nsca-certification-handbook.pdf (200 OK, 2.29MB). CSCS sample questions in the appendix. Small count, official quality.

### 10. NSCA official "Practice Exam Volume One" (LEGACY, 2nd-ed era, 64 Q + answer key)  → bank/nsca-vol1.json (mark tags:["legacy"])
- pdfcoffee.com/cscs-prac-exam-pdf-free.html (interstitial; page text preview contains content) or idoc.pub/documents/cscs-practice-exampdf-546g30okz7n8 (15.7MB scan). If parsing cost high, skip page-text route... try exa/text preview first. Optional priority LOW.

## TIER 2 — optional / low yield
- gxsri/cscs-study-platform GitHub (branch master): lessons/0014,0015 mock exams, 0016, 0017 (zh-CN exam-format questions) — HTML with data-correct attrs, ~40 Q/page. Chinese mocks — parseable, LOW-MED priority. → bank/gxsri.json
- open-exam-prep.com/practice/cscs — only ~10 SSR Qs with explanations. Skip unless quick.
- PT Pioneer 100+310 Qs SSR but answers server-graded (QSM plugin, REST 404). Skip.
- physioplus-jp quiz — Japanese. Skip.
- cptexams / mometrix / achievable / pocketprep / practictetestgeeks web app / cscsquestions.com / test-guide.com / freeflash / studyflash — verified NOT extractable or empty. Skip.
- AnkiWeb shared decks (IDs seen: 1750838600 "NSCA CSCS Review", 1808253012 "CSCS Full") — /shared/get?id= 404'd from this network; info pages exist but JS. Manual/browser only. Skip for now.

## Exam blueprint for the mock tool (CURRENT DCO, effective 2025-07-01 — primary source: NSCA JTA-2025 PDF)
- Section 1 Scientific Foundations: 80 scored + 15 unscored, 90 min.
  Exercise Sciences 48 (60%), Sport Psychology 20 (25%), Nutrition 12 (15%).
- Section 2 Practical/Applied: 110 scored + 15 unscored, 150 min.
  Program Design 44 (40%), Exercise Technique 28 (25%), Program Implementation 22 (20%), Organization & Administration 16 (15%).
- Pass: scaled score >= 70 each section; both required; retake after 30 days; PA section contains 30-40 video/image items (mock tool: optional image placeholder).
- Old 2020 blueprint (55/24/21 + 36/35/11/18) still on many third-party sites — DO NOT use.
- Chapter→domain mapping: textbook chapters 1-26 exist at cscs-exam-prep/raw/chNN.txt (UTF-8 verified, simplified Chinese translation of Essentials 4th ed).
