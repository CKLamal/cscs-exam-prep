import re, json
p = open(r'D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape\probe2_14791808_browser.html', encoding='utf-8').read()
print("== data attrs ==")
seen = set()
for m in re.finditer(r'data-[a-z_-]+="[^"]{0,120}"', p):
    s = m.group(0)
    if s not in seen:
        seen.add(s)
        print(s)
print("== api/url mentions ==")
for m in re.finditer(r'["\x27][^"\x27]{0,100}(api|study|sandbox)[^"\x27]{0,100}["\x27]', p, re.I):
    print(repr(m.group(0)[:140]))
print("== ids near flashcard divs ==")
for m in list(re.finditer(r'id="(card-front|card-back)-(\d+)"', p))[:6]:
    print(m.group(0))
print("count card-front", len(re.findall(r'id="card-front-\d+"', p)), "card-back", len(re.findall(r'id="card-back-\d+"', p)))
