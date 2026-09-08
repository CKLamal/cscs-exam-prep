import re
p = open(r'D:\dgx-spark\cscs-exam-prep\mock-exams\raw_sources\brainscape\probe2_14791808_browser.html', encoding='utf-8').read()
i = p.find('id="card-back-475797521"')
print(p[i-3500:i+1200])
