"""Derive the official CSCS 5th-edition English chapter titles.

Sources, in authority order:
1. Chapter-head lines as printed on the 5e PDF chapter pages.
2. The CONTENTS pages (toc) -- verbatim wording and case win.
3. A prior manual audit list -- cross-check only, never authoritative.

Logic: join chapter-head lines up to (excluding) the author line, derive
Title Case only when the head is not already in exact (mixed) case, then
locate the title verbatim (case-insensitive, whitespace-normalized,
soft-hyphen/figure-space tolerant) in the CONTENTS text. The CONTENTS
spelling is the final title. Any title not found in the CONTENTs stops the
script (exit 3) instead of guessing. Writes five_e_titles.json on success.
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "five_e_titles.json")

# Extraction data: {"toc": CONTENTS pages 11-19 verbatim,
#                   "heads": {chapter: first lines of chapter head page}}
DATA = json.loads(r"""{"heads": {"1": ["CHAPTER 1", "STRUCTURE AND FUNCTION", "OF BODY SYSTEMS", "Michael D. Roberts, PhD", "The author would like to acknowledge the significant contributions of N. Travis Triplett,", "Duncan French, Ann Swank, Carwyn P.M. Sharp, Robert T. Harris, and Gary R. Hunter to"], "10": ["CHAPTER 10", "BASIC NUTRITIONAL", "FACTORS AFFECTING HEALTH", "Cassandra Forsythe, PhD, RD", "The author would like to acknowledge the significant contribution of Marie Spano to this", "chapter."], "11": ["CHAPTER 11", "NUTRITION STRATEGIES FOR", "MAXIMIZING PERFORMANCE", "Shawn M. Arent, PhD, and Abbie E. Smith-Ryan, PhD", "The authors would like to acknowledge the significant contribution of Marie Spano to this chapter.", "After completing this chapter, you will be able to"], "12": ["CHAPTER 12", "PERFORMANCE-ENHANCING", "SUBSTANCES AND METHODS", "Bill I. Campbell, PhD, and Nathaniel D.M.", "Jenkins, PhD", "The authors would like to acknowledge the significant contributions of Jay R. Hoffman"], "13": ["CHAPTER 13\u2005\u2005Principles of Test Selection", "and Administration", "Claire Brady, PhD, and John McMahon, PhD", "Reasons for Testing \u2022 Testing Terminology \u2022 Evaluation", "of Test Quality \u2022 Test Selection \u2022 Test Administration \u2022", "Conclusion"], "14": ["CHAPTER 14", "ADMINISTRATION, SCORING, AND", "INTERPRETATION OF SELECTED TESTS", "David J. Heikkinen, PhD, Jo Clubb, MS, and John McMahon, PhD", "The authors would like to acknowledge the significant contributions of Michael McGuigan, Everett Harman, and John Garhammer", "to this chapter."], "15": ["CHAPTER 15", "PERFORMANCE", "PREPARATION, MOBILITY,", "AND FLEXIBILITY", "Ian Jeffreys, PhD", "After completing this chapter, you will be able to"], "16": ["CHAPTER 16", "EXERCISE TECHNIQUE FOR", "FREE WEIGHT AND MACHINE", "TRAINING", "Scott Caulfield, MA, Guy Hornsby, PhD, and G.", "Gregory Haff, PhD"], "17": ["CHAPTER 17\u2005\u2005Exercise Technique for", "Alternative Modes and", "Nontraditional", "Implement Training", "Justin Keogh, PhD, and G. Gregory Haff,", "PhD"], "18": ["CHAPTER 18", "PROGRAM DESIGN FOR", "RESISTANCE TRAINING", "Timothy J. Suchomel, PhD, and Paul Comfort, PhD", "The authors would like to acknowledge the significant contributions of Jeremy M. Sheppard, N. Travis", "Triplett, Thomas R. Baechle, Roger W. Earle, and Dan Wathen to this chapter."], "19": ["CHAPTER 19", "PROGRAM DESIGN AND", "TECHNIQUE FOR", "PLYOMETRIC TRAINING", "Chris A. Bailey, PhD, and Clive Brewer, MSc", "The authors would like to acknowledge the significant contributions of David H. Potach"], "2": ["CHAPTER 2", "BIOMECHANICS OF", "RESISTANCE EXERCISE", "William R. Johnson, PhD, and Jason Lake, PhD", "The authors would like to acknowledge the significant contributions of Jeffrey M.", "McBride and Everett Harman to this chapter."], "20": ["CHAPTER 20\u2005\u2005Program Design and", "Technique for Speed and", "Agility Training", "Thomas Dos\u2019Santos, PhD, and Paul A.", "Jones, PhD", "Speed and Agility Mechanics \u2022 Neurophysiological Basis"], "21": ["CHAPTER 21", "PROGRAM DESIGN AND", "TECHNIQUE FOR AEROBIC", "ENDURANCE AND METABOLIC", "TRAINING", "Glen B. Deakin, PhD, and Carwyn P.M. Sharp,"], "22": ["CHAPTER 22", "PERIODIZATION", "G. Gregory Haff, PhD", "The author would like to acknowledge the significant contributions of Dan Wathen, Thomas R. Baechle,", "and Roger W. Earle to this chapter.", "After completing this chapter, you will be able to"], "23": ["CHAPTER 23\u2005\u2005Rehabilitation,", "Reconditioning, and", "Medical Issues", "Morey J. Kolber, PhD, PT, and William J.", "Hanney, DPT, PhD", "Allied Health Team \u2022 Types of Injury \u2022 Tissue Healing \u2022"], "24": ["CHAPTER 24", "OVERREACHING,", "OVERTRAINING, AND", "RECOVERY", "Andrew C. Fry, PhD, and Bradley C. Nindl, PhD", "After completing this chapter, you will be able to"], "25": ["CHAPTER 25", "FACILITY DESIGN, LAYOUT,", "AND ORGANIZATION", "Ryan Metzger, MS, Ryan Fowler, MS, and Eric L.", "McMahon, MEd", "The authors would like to acknowledge the significant contributions of Andrea Hudy,"], "26": ["CHAPTER 26", "FACILITY POLICIES,", "PROCEDURES, AND LEGAL", "ISSUES", "Brijesh Patel, MA, and Reed Wainwright, JD", "The authors would like to acknowledge the significant contributions of Traci Statler,"], "3": ["CHAPTER 3", "BIOENERGETICS OF", "EXERCISE AND TRAINING", "Dale W. Chapman, PhD", "The author would like to acknowledge the significant contributions of Trent J. Herda and", "Joel T. Cramer to this chapter."], "4": ["CHAPTER 4", "ENDOCRINE RESPONSES TO", "RESISTANCE EXERCISE AND", "TRAINING", "William J. Kraemer, PhD, Jakob L. Vingren, PhD,", "and Disa L. Hatfield, PhD"], "5": ["CHAPTER 5", "ADAPTATIONS TO", "ANAEROBIC TRAINING", "Brandon Roberts, PhD, and Sean Collins, PhD", "The authors would like to acknowledge the significant contributions of Duncan French", "and Nicholas A. Ratamess to this chapter."], "6": ["CHAPTER 6", "ADAPTATIONS TO AEROBIC", "TRAINING", "Kate Baldwin, PhD, and Glen B. Deakin, PhD", "The authors would like to acknowledge the significant contributions of Ann Swank and", "Carwyn P.M. Sharp to this chapter."], "7": ["CHAPTER 7", "AGE-RELATED DIFFERENCES", "AND THEIR IMPLICATIONS", "FOR RESISTANCE TRAINING", "Rhodri S. Lloyd, PhD, Sylvia Moeskops, PhD, and", "Avery D. Faigenbaum, EdD"], "8": ["CHAPTER 8", "SEX-RELATED DIFFERENCES", "AND THEIR IMPLICATIONS", "FOR RESISTANCE TRAINING", "N. Travis Triplett, PhD, and Nicole Dabbs, PhD", "After completing this chapter, you will be able to"], "9": ["CHAPTER 9", "PSYCHOLOGICAL", "FOUNDATIONS OF", "PERFORMANCE", "Daniel B. Hollander, EdD, and Adam Feit, PhD", "The authors would like to acknowledge the significant contributions of Traci A. Statler,"]}, "toc": "=== pdf page 11 ===\nCONTENTS\nPreface\nAccessing the Lab Activities\nAcknowledgments\nCHAPTER 1\u2005\u2005\u2005\u2005\u2005\u2005Structure and Function of\nBody Systems\nMichael D. Roberts, PhD\nMusculoskeletal System \u2022 Neuromuscular System \u2022\nCardiovascular System \u2022 Respiratory System \u2022 Acute\nResponses to Aerobic Exercise \u2022 Cardiovascular and\nRespiratory Responses to Anaerobic Exercise \u2022\nConclusion\nCHAPTER 2\u2005\u2005\u2005\u2005\u2005\u2005Biomechanics of\nResistance Exercise\nWilliam R. Johnson, PhD, and Jason Lake,\nPhD\nSkeletal Musculature \u2022 Anatomical Planes and Major\nBody Movements \u2022 Human Strength and Power \u2022\nSources of Resistance to Muscle Contraction \u2022 Joint\nBiomechanics: Concerns in Resistance Training \u2022\nConclusion\nCHAPTER 3\u2005\u2005\u2005\u2005\u2005\u2005Bioenergetics of Exercise\nand Training\nDale W. Chapman, PhD\n11\n\n=== pdf page 12 ===\nEssential Terminology \u2022 Biological Energy Systems \u2022\nSubstrate Depletion and Repletion \u2022 Bioenergetic\nLimiting Factors in Exercise Performance \u2022 Oxygen\nUptake and the Aerobic and Anaerobic Contributions to\nExercise \u2022 Metabolic Specificity of Training \u2022 Conclusion\nCHAPTER 4\u2005\u2005\u2005\u2005\u2005\u2005Endocrine Responses to\nResistance Exercise and\nTraining\nWilliam J. Kraemer, PhD, Jakob L. Vingren,\nPhD, and Disa L. Hatfield, PhD\nHistorical Perspective on Interest in the Endocrine\nSystem \u2022 Endocrine Terminology, Functions, and\nMechanisms \u2022 Understanding Signaling Concepts \u2022\nFunctions of the Endocrine System in Resistance\nExercise and Training \u2022 Importance of Recruitment of\nMuscle Tissue \u2022 Muscle as the Target for Hormone\nInteractions \u2022 Role of Receptors in Mediating Hormonal\nChanges \u2022 Categories of Hormones \u2022 Amine Hormone\nInteractions \u2022 Training-Mediated Hormonal Responses\nand Mechanisms \u2022 Interpreting Hormonal Changes in\nPeripheral Blood \u2022 Adaptations in the Endocrine System\nFrom Resistance Training \u2022 Primary Anabolic Hormones\nin Muscle Development \u2022 Growth Hormone \u2022 Insulin-\nLike Growth Factors and Binding Proteins \u2022 IGF\nResponses to Exercise \u2022 Training Adaptations and IGF\nand Binding Proteins \u2022 Adrenal Gland, Cortisol, and Its\nRole in Resistance Exercise \u2022 Catecholamines and Their\nRole in Resistance Exercise and Training \u2022 Other\nHormonal Considerations in Resistance Training \u2022\nConclusion\nCHAPTER 5\u2005\u2005\u2005\u2005\u2005\u2005Adaptations to Anaerobic\nTraining\nBrandon Roberts, PhD, and Sean Collins,\nPhD\nNeural Adaptations \u2022 Muscular Adaptations \u2022\nConnective Tissue Adaptations \u2022 Endocrine Responses\n12\n\n=== pdf page 13 ===\nand Adaptations to Anaerobic Training \u2022 Cardiovascular\nAdaptations to Anaerobic Training \u2022 Compatibility of\nAerobic and Anaerobic Modes of Training \u2022 Detraining \u2022\nConclusion\nCHAPTER 6\u2005\u2005\u2005\u2005\u2005\u2005Adaptations to Aerobic\nTraining\nKate Baldwin, PhD, and Glen B. Deakin,\nPhD\nChronic Adaptations to Aerobic Exercise \u2022 Adaptations\nto Aerobic Endurance Training \u2022 External and Individual\nFactors Influencing Adaptations to Aerobic Endurance\nTraining \u2022 Detraining \u2022 Conclusion\nCHAPTER 7\u2005\u2005\u2005\u2005\u2005\u2005Age-Related Differences\nand Their Implications\nfor Resistance Training\nRhodri S. Lloyd, PhD, Sylvia Moeskops, PhD,\nand Avery D. Faigenbaum, EdD\nYouth Populations \u2022 Older Adults \u2022 Conclusion\nCHAPTER 8\u2005\u2005\u2005\u2005\u2005\u2005Sex-Related Differences\nand Their Implications\nfor Resistance Training\nN. Travis Triplett, PhD, and Nicole Dabbs,\nPhD\nImplications of Resistance Training for Females \u2022\nTraining Responses and Adaptations \u2022 Resistance\nTraining Considerations \u2022 Conclusion\nCHAPTER 9\u2005\u2005\u2005\u2005\u2005\u2005Psychological Foundations\nof Performance\n13\n\n=== pdf page 14 ===\nDaniel B. Hollander, EdD, and Adam Feit,\nPhD\nRole of Sport Psychology \u2022 Ideal Performance State \u2022\nEnergy Management: Arousal, Anxiety, and Stress \u2022\nTheoretical Tenets of Arousal, Anxiety, and Motivation\non Performance \u2022 Motivation \u2022 Attention and Focus \u2022\nPsychological Techniques for Improved Performance \u2022\nMental Health and Strength and Conditioning \u2022\nPsychological Impact of Injury in Sport \u2022 Enhancing\nMotor Skill Acquisition and Learning \u2022 Conclusion\nCHAPTER 10\u2005\u2005Basic Nutritional Factors\nAffecting Health\nCassandra Forsythe, PhD, RD\nRole of Sports Nutrition Professionals \u2022 Standard\nNutrition Guidelines \u2022 Macronutrients \u2022 Vitamins \u2022\nMinerals \u2022 Fluid and Electrolytes \u2022 Conclusion\nCHAPTER 11\u2005\u2005Nutrition Strategies for\nMaximizing Performance\nShawn M. Arent, PhD, and Abbie E. Smith-\nRyan, PhD\nPrecompetition, During-Event, and Postcompetition\nNutrition \u2022 Nutrition Strategies for Altering Body\nComposition \u2022 Relative Energy Deficiency in Sport\n(RED-S) \u2022 Feeding and Eating Disorders \u2022 Conclusion\nCHAPTER 12\u2005\u2005Performance-Enhancing\nSubstances and Methods\nBill I. Campbell, PhD, and Nathaniel D.M.\nJenkins, PhD\nTypes of Performance-Enhancing Substances \u2022\nHormones \u2022 Dietary Supplements \u2022 Conclusion\n14\n\n=== pdf page 15 ===\nCHAPTER 13\u2005\u2005Principles of Test Selection\nand Administration\nClaire Brady, PhD, and John McMahon, PhD\nReasons for Testing \u2022 Testing Terminology \u2022 Evaluation\nof Test Quality \u2022 Test Selection \u2022 Test Administration \u2022\nConclusion\nCHAPTER 14\u2005\u2005Administration, Scoring,\nand Interpretation of\nSelected Tests\nDavid J. Heikkinen, PhD, Jo Clubb, MS, and\nJohn McMahon, PhD\nMeasuring Parameters of Athletic Performance \u2022\nMonitoring Protocols, Procedures, and Equipment \u2022\nStatistical Evaluation of Test Data \u2022 Conclusion\nCHAPTER 15\u2005\u2005Performance Preparation,\nMobility, and Flexibility\nIan Jeffreys, PhD\nPerformance Preparation\u2014The Warm-Up \u2022 Flexibility \u2022\nTypes of Stretching \u2022 Programming Considerations for\nStretching \u2022 Conclusion\nCHAPTER 16\u2005\u2005Exercise Technique for Free\nWeight and Machine\nTraining\nScott Caulfield, MA, Guy Hornsby, PhD, and\nG. Gregory Haff, PhD\nFundamentals of Exercise Technique \u2022 Spotting Free\nWeight Exercises \u2022 Conclusion\n15\n\n=== pdf page 16 ===\nCHAPTER 17\u2005\u2005Exercise Technique for\nAlternative Modes and\nNontraditional\nImplement Training\nJustin Keogh, PhD, and G. Gregory Haff,\nPhD\nGeneral Guidelines \u2022 Bodyweight Training Methods \u2022\nCore Stability and Balance Training Methods \u2022 Variable-\nResistance Training Methods \u2022 Nontraditional\nImplement Training Methods \u2022 Unilateral Training \u2022\nConclusion\nCHAPTER 18\u2005\u2005Program Design for\nResistance Training\nTimothy J. Suchomel, PhD, and Paul\nComfort, PhD\nPrinciples of Anaerobic Exercise Prescription \u2022 Step 1:\nNeeds Analysis \u2022 Step 2: Exercise Selection \u2022 Step 3:\nTraining Frequency \u2022 Step 4: Exercise Order \u2022 Step 5:\nTraining Load and Repetitions \u2022 Step 6: Volume \u2022 Step\n7: Rest Periods \u2022 Conclusion\nCHAPTER 19\u2005\u2005Program Design and\nTechnique for Plyometric\nTraining\nChris A. Bailey, PhD, and Clive Brewer, MSc\nPlyometric Mechanics and Physiology \u2022 Program Design\n\u2022 Program Length \u2022 Warm-Up \u2022 Age Considerations \u2022\nPlyometrics and Other Forms of Exercise \u2022 Safety\nConsiderations \u2022 Conclusion\n16\n\n=== pdf page 17 ===\nCHAPTER 20\u2005\u2005Program Design and\nTechnique for Speed and\nAgility Training\nThomas Dos\u2019Santos, PhD, and Paul A.\nJones, PhD\nSpeed and Agility Mechanics \u2022 Neurophysiological Basis\nfor Speed \u2022 Running Speed \u2022 Methods of Developing\nSpeed \u2022 Agility Performance and Change-of-Direction\nAbility \u2022 Methods of Developing Agility \u2022 Program\nDesign \u2022 Speed Development Strategies \u2022 Agility\nDevelopment Strategies \u2022 Conclusion\nCHAPTER 21\u2005\u2005Program Design and\nTechnique for Aerobic\nEndurance and Metabolic\nTraining\nGlen B. Deakin, PhD, and Carwyn P.M.\nSharp, PhD\nFactors Related to Aerobic Endurance Performance \u2022\nDesigning an Aerobic Endurance Program \u2022 Types of\nAerobic Endurance Training Programs \u2022 Application of\nProgram Design to Training Seasons \u2022 Special Issues\nRelated to Aerobic Endurance Training \u2022 Conclusion\nCHAPTER 22\u2005\u2005Periodization\nG. Gregory Haff, PhD\nCentral Concepts Related to Periodization \u2022\nPeriodization and Planning the Training Process \u2022\nModels of Periodization \u2022 Periodization Hierarchy \u2022\nPeriodization Periods \u2022 Applying Sport Seasons to the\nPeriodization Periods \u2022 Undulating Versus Linear\nPeriodization Models \u2022 Example of an Annual Training\nPlan \u2022 Conclusion\n17\n\n=== pdf page 18 ===\nCHAPTER 23\u2005\u2005Rehabilitation,\nReconditioning, and\nMedical Issues\nMorey J. Kolber, PhD, PT, and William J.\nHanney, DPT, PhD\nAllied Health Team \u2022 Types of Injury \u2022 Tissue Healing \u2022\nGoals of Rehabilitation and Reconditioning \u2022 Program\nDesign \u2022 Reducing Risk of Injury and Reinjury \u2022\nMedical Conditions \u2022 Conclusion\nCHAPTER 24\u2005\u2005Overreaching,\nOvertraining, and\nRecovery\nAndrew C. Fry, PhD, and Bradley C. Nindl,\nPhD\nPeriodization and the General Adaptation Syndrome \u2022\nOvertraining and Overreaching \u2022 Overtraining\nContinuum \u2022 Factors Contributing to Overreaching and\nOvertraining \u2022 Underperformance and Its Relation to\nOvertraining and Overreaching \u2022 Performance-Related\nVariables Affected by Overtraining and Overreaching \u2022\nPhysiological Mechanisms Associated With\nOverreaching and Overtraining \u2022 Assessment of\nOverreaching and Overtraining \u2022 Recovery Methods\nand Strategies \u2022 Conclusion\nCHAPTER 25\u2005\u2005Facility Design, Layout, and\nOrganization\nRyan Metzger, MS, Ryan Fowler, MS, and\nEric L. McMahon, MEd\nGeneral Aspects of New Facility Design \u2022 Existing\nStrength and Conditioning Facilities \u2022 Satellite Training\nFacilities \u2022 Outdoor Training Spaces \u2022 Assessing Athletic\nProgram Needs \u2022 Designing the Strength and\n18\n\n=== pdf page 19 ===\nConditioning Facility \u2022 Arranging Equipment in the\nStrength and Conditioning Facility \u2022 Maintaining and\nCleaning Surfaces and Equipment \u2022 Conclusion\nCHAPTER 26\u2005\u2005Facility Policies,\nProcedures, and Legal\nIssues\nBrijesh Patel, MA, and Reed Wainwright, JD\nMission Statement and Program Goals \u2022 Program\nObjectives \u2022 Strength and Conditioning Performance\nTeam \u2022 Legal and Ethical Issues \u2022 Staff Policies and\nActivities \u2022 Facility Administration \u2022 Emergency\nPlanning and Response \u2022 Conclusion\nAnswers to Study Questions\nIndex\nAbout the Editors\nContributors\nContributors to Previous Editions\n19\n"}""")

# Cross-check list from a prior manual audit (not authoritative).
EXPECTED = {
    1: "Structure and Function of Body Systems",
    2: "Biomechanics of Resistance Exercise",
    3: "Bioenergetics of Exercise and Training",
    4: "Endocrine Responses to Resistance Exercise and Training",
    5: "Adaptations to Anaerobic Training",
    6: "Adaptations to Aerobic Training",
    7: "Age-Related Differences and Their Implications for Resistance Training",
    8: "Sex-Related Differences and Their Implications for Resistance Training",
    9: "Psychological Foundations of Performance",
    10: "Basic Nutritional Factors Affecting Health",
    11: "Nutrition Strategies for Maximizing Performance",
    12: "Performance-Enhancing Substances and Methods",
    13: "Principles of Test Selection and Administration",
    14: "Administration, Scoring, and Interpretation of Selected Tests",
    15: "Performance Preparation, Mobility, and Flexibility",
    16: "Exercise Technique for Free Weight and Machine Training",
    17: "Exercise Technique for Alternative Modes and Nontraditional Implement Training",
    18: "Program Design for Resistance Training",
    19: "Program Design and Technique for Plyometric Training",
    20: "Program Design and Technique for Speed and Agility Training",
    21: "Program Design and Technique for Aerobic Endurance and Metabolic Training",
    22: "Periodization",
    23: "Rehabilitation, Reconditioning, and Medical Issues",
    24: "Overreaching, Overtraining, and Recovery",
    25: "Facility Design, Layout, and Organization",
    26: "Facility Policies, Procedures, and Legal Issues",
}

CHAPTERS = list(range(1, 27))
CHAPTER_MARKER = re.compile(r"\A\s*CHAPTER\s+\d+\b[\s\u00ad\u2000-\u200b]*",
                            re.IGNORECASE)
# An author line carries a degree credential as a standalone word.
AUTHOR_LINE = re.compile(r"\b(?:PhD|EdD|MEd|MSc|MS|MA|RD|DPT|PT|JD)\b")
MINOR_WORDS = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of",
               "on", "or", "the", "to", "via", "with", "yet"}
WS_RUN = re.compile(r"[\s\u00a0\u2000-\u200b]+")


def norm_ws(text):
    """Drop soft hyphens, collapse every whitespace run to one space."""
    return WS_RUN.sub(" ", text.replace("\u00ad", "")).strip()


def head_title(ch):
    """Join chapter-head title lines up to (excluding) the author line."""
    parts = []
    for raw in DATA["heads"][str(ch)]:
        m = CHAPTER_MARKER.match(raw)
        text = norm_ws(raw[m.end():] if m else raw)
        if not text:
            continue
        if AUTHOR_LINE.search(text):
            break
        parts.append(text)
    return " ".join(parts)


def cap_segment(seg):
    return seg[:1].upper() + seg[1:].lower() if seg else seg


def title_case(text):
    words = []
    for i, word in enumerate(text.split()):
        if i and word.lower() in MINOR_WORDS:
            words.append(word.lower())
        else:
            words.append("-".join(cap_segment(s) for s in word.split("-")))
    return " ".join(words)


def toc_find(title):
    """Return the CONTENTS-verbatim spelling, or None when absent."""
    pattern = " ".join(re.escape(t) for t in norm_ws(title).split(" "))
    pattern = pattern.replace("-", "- ?")  # tolerate hyphen line wraps
    m = re.search(pattern, norm_ws(DATA["toc"]), re.IGNORECASE)
    return m.group(0) if m else None


def main():
    titles = {}
    misses = []
    print("ch | derived                    | expected                   | status")
    for ch in CHAPTERS:
        joined = head_title(ch)
        exact_case = any(c.islower() for c in joined)
        derived = joined if exact_case else title_case(joined)
        verbatim = toc_find(derived)
        if verbatim is None:
            misses.append((ch, derived))
            final = derived
        else:
            final = verbatim
        titles[ch] = final
        status = "MATCH" if final == EXPECTED[ch] else "DIFF"
        print("%2d | %-28s | %-28s | %s" % (ch, derived[:28], EXPECTED[ch][:28], status))
        if status == "DIFF":
            print("   DIFF ch%d resolved by CONTENTS verbatim:" % ch)
            print("     toc      : %s" % final)
            print("     expected : %s" % EXPECTED[ch])
    if misses:
        print("\nSTOP: titles not found verbatim in CONTENTS pages (no guessing):")
        for ch, derived in misses:
            print("  ch%d: %s" % (ch, derived))
        sys.exit(3)
    with io.open(OUT_JSON, "w", encoding="utf-8", newline="") as f:
        json.dump({str(ch): titles[ch] for ch in CHAPTERS}, f,
                  ensure_ascii=False, indent=2)
        f.write("\n")
    print("\nWrote %s (26 titles from CONTENTS verbatim)." % OUT_JSON)


if __name__ == "__main__":
    main()
