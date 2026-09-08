import re
p = open(r'D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape\probe2_14791808_browser.html', encoding='utf-8').read()
i1 = p.find('data-number="1"')
i2 = p.find('data-number="3"')
print(p[i1-200:i2+50])
