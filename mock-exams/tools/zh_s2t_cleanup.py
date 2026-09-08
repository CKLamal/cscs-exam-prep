"""One-off cleanup: convert Simplified-Chinese explanation_zh entries to Traditional (s2twp).

Detection: entry contains chars from a list of common simplified-only characters.
Entries already Traditional pass untouched (not converted at all -> no 里/裡 risk).
"""
import json
from opencc import OpenCC

P = r"D:\dgx-spark\cscs-exam-prep\mock-exams\bank\merged.json"

SIMP = set(
    "这为练关运强时单钟对论测发层们让认识经济环标准举组间歇负周期度数别缓冲击"
    "肉关节软韧骨骼纤维募集姿态平衡协调灵活素摄碳水化合蛋白质激泌代谢糖酵解"
    "磷阈增递减超级辅卧蹲硬拉挺抓清洁翻站抛药箱躯干骨盆脊椎肩胛肘腕指踝膝趾"
    "臂腿胸腹腰颈间盘髓膜束收缩伤发炎肿疼痛康复恢复监控量耗压血氧通气乳酸稳"
    "态欠债基温调节汗液流失钠热习服冻赔训练锻炼测验确定应该见长期兴奋收缩"
    "兴奋补充剂咖啡因酸氢钠盐氨丁羟甲甲基站蹲跳落地摆臂牵张反射传神经递质"
    "兴奋收缩耦联肌浆网钙离子横桥滑行丝带状构触动电位的极膜静息动作导速髓鞘"
    "灰白质大脑皮质小脑髓桥延脊髓神经冲动运动单位募集频率编码大小原则性强直"
    "融合抽搐疲劳恢复超量补偿间期负荷递增线性波动周期化准备过渡赛季比赛季节"
    "进度假休整微调减量 taper 峰值巅峰高峰表现状态特征评估测试筛选模拟预测"
    "最大重复百分比预计算调整体成分脂肪瘦体重质量指数围度皮褶厚度生物电阻抗"
    "双能射线吸收仪水下称重法置换法精确可靠准确客观简便易行标准化程序仪器"
    "校准误差变异系数系数者被试验对象受试样本群体选择随机分层整群抽样调查"
    "问卷访谈观察记录档案统计描述推断显著性差异相关回归预测模型变量控制混杂"
    "因素实验设计前测后测对照组安慰剂效应盲法单双随机分配分组干预措施方案"
    "实施 adherence 顺从性脱落流失样本量功效检验假设错误类型第一第二类"
)

def main():
    d = json.load(open(P, encoding="utf-8"))
    cc = OpenCC("s2twp")
    conv = tot = 0
    for q in d["questions"]:
        z = q.get("explanation_zh")
        if not z:
            continue
        tot += 1
        if any(c in SIMP for c in z):
            nz = cc.convert(z)
            if nz != z:
                q["explanation_zh"] = nz
                conv += 1
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"zh entries={tot}, converted-from-simplified={conv}")

if __name__ == "__main__":
    main()
