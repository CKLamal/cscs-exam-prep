import type { Question } from './types';

export const cscsProgramDesignQuestions: Question[] = [
  // ==================== Periodization (id 1-8) ====================
  {
    id: 1,
    question: "In a traditional (linear) periodization model, how do training volume and intensity change across mesocycles?",
    options: {
      A: "Volume decreases while intensity increases",
      B: "Volume and intensity both increase",
      C: "Volume increases while intensity decreases",
      D: "Volume and intensity both decrease"
    },
    correct: 'A',
    explanation: "傳統線性週期化（classic/linear periodization）的核心特徵是：隨著訓練階段推進，訓練量（volume）逐漸減少，而強度（intensity）逐漸增加。這源自 Matveyev 的經典模型，從高量低強度的一般準備期（General Preparation）過渡到低量高強度的比賽期（Competition）。",
    examTip: "CSCS 考試中「traditional/classic periodization」= volume ↓ intensity ↑，這是最基本的週期化定義，務必牢記。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 2,
    question: "Which periodization model varies training intensity and volume WITHIN a single week?",
    options: {
      A: "Linear periodization",
      B: "Block periodization",
      C: "Daily undulating periodization (DUP)",
      D: "Conjugate sequencing"
    },
    correct: 'C',
    explanation: "每日波動週期化（Daily Undulating Periodization, DUP）在同一週內變化訓練強度和量。例如：週一 hypertrophy（10RM），週三 strength（5RM），週五 power（3RM）。這與線性模型（跨數週才改變）不同。",
    examTip: "DUP = 「within a week」變化；Weekly Undulating = 每週變化；Linear = 跨 mesocycle 漸進變化。考題常考三者區分。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 3,
    question: "Block periodization uses concentrated training blocks. Which of the following correctly describes the typical sequence of blocks?",
    options: {
      A: "Transmutation → Accumulation → Realization",
      B: "Accumulation → Transmutation → Realization",
      C: "Realization → Accumulation → Transmutation",
      D: "Accumulation → Realization → Transmutation"
    },
    correct: 'B',
    explanation: "區塊週期化（Block Periodization）由 Issurin 提出，使用 2-4 週的高度專注訓練區塊（blocks），三個階段依序為：Accumulation（累積，高訓練量建立基礎體能）→ Transmutation（轉化，提升專項肌力與爆發力）→ Realization（實現，減量以達比賽巔峰表現）。",
    examTip: "Block periodization 口訣：A-T-R（Accumulation → Transmutation → Realization）。每塊通常 2-4 週。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 4,
    question: "During the preparatory period of an annual training plan, which sub-phase focuses on building a general fitness base with higher training volume?",
    options: {
      A: "Competition phase",
      B: "Specific preparation phase",
      C: "Transition phase",
      D: "General preparation phase"
    },
    correct: 'D',
    explanation: "年度訓練計畫的準備期（Preparatory Period）分為：一般準備階段（General Preparation）和專項準備階段（Specific Preparation）。一般準備階段以高訓練量、低強度為特徵，目的是建立全面的體能基礎（general fitness base）。",
    examTip: "NSCA 年度計畫架構：Preparatory Period（General Prep → Specific Prep）→ Competition Period（First Transition → Competition）→ Transition Period（Active Rest）。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 5,
    question: "The transition (active rest) phase in an annual training plan typically lasts:",
    options: {
      A: "1-4 weeks",
      B: "8-12 weeks",
      C: "16-20 weeks",
      D: "6-12 months"
    },
    correct: 'A',
    explanation: "過渡期（Transition Phase / Active Rest）通常持續 1-4 週，目的是讓運動員從訓練和比賽的身心壓力中恢復。此階段進行低強度、非結構化的交叉訓練或休閒活動，避免完全不活動以防 detraining。",
    examTip: "Transition phase = 1-4 週 active rest，不是完全休息。若完全停止訓練超過 2 週，會出現明顯的 detraining 效應。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 6,
    question: "The conjugate (concurrent) method of periodization is BEST characterized by:",
    options: {
      A: "Training only one fitness quality per mesocycle",
      B: "Progressively increasing volume throughout the entire macrocycle",
      C: "Exclusively using linear progression for all exercises",
      D: "Using maximal effort, dynamic effort, and repeated effort methods within the same training week"
    },
    correct: 'D',
    explanation: "共軛方法（Conjugate Method）的特徵是在同一訓練週內同時使用多種訓練方法：最大努力法（Maximal Effort, ≥90% 1RM）、動態努力法（Dynamic Effort, 50-80% 1RM with max velocity）、反覆努力法（Repeated Effort）。由 Westside Barbell 推廣，目的是同時發展多種運動能力。",
    examTip: "Conjugate = 同週訓練多種能力；Block = 每塊專注一種能力。兩者是相反的策略，考試常用來互相做干擾選項。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 7,
    question: "A macrocycle in a periodized training program typically refers to:",
    options: {
      A: "A single training session",
      B: "An entire training year or season",
      C: "One week of training",
      D: "A 2-6 week training block"
    },
    correct: 'B',
    explanation: "大週期（Macrocycle）指的是整個訓練年度或賽季（通常 6-12 個月，最長可達 4 年如奧運週期）。週期化層級：Macrocycle（大週期，數月-1年）> Mesocycle（中週期，2-6 週）> Microcycle（小週期，通常 1 週）。",
    examTip: "週期化層級：Macrocycle > Mesocycle > Microcycle（大 > 中 > 小）。考題常考各層級的時間長度定義。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },
  {
    id: 8,
    question: "Weekly undulating periodization differs from daily undulating periodization (DUP) in that training variables are altered:",
    options: {
      A: "Within each training session",
      B: "Every training day within a week",
      C: "Only once per macrocycle",
      D: "On a week-to-week basis across microcycles"
    },
    correct: 'D',
    explanation: "每週波動週期化（Weekly Undulating Periodization, WUP）是在每週（microcycle）之間改變訓練變項，例如第 1 週以肌肥大為主、第 2 週以力量為主、第 3 週以爆發力為主。DUP 則是在同一週內的不同訓練日改變變項。",
    examTip: "DUP = 每天變；WUP = 每週變；Linear = 跨 mesocycle 漸變。三種模型的「改變頻率」是區分關鍵。",
    topic: 'cscs-program-design',
    part: 'Periodization'
  },

  // ==================== 1RM Percentages & Rep Ranges (id 9-16) ====================
  {
    id: 9,
    question: "According to the NSCA, which percentage of 1RM and repetition range is MOST appropriate for developing maximal strength?",
    options: {
      A: "50-65% 1RM, 15-25 reps",
      B: "67-85% 1RM, 6-12 reps",
      C: "≥85% 1RM, ≤6 reps",
      D: "30-50% 1RM, 20-30 reps"
    },
    correct: 'C',
    explanation: "NSCA 指南：最大肌力（maximal strength）訓練使用 ≥85% 1RM，≤6 次反覆。此強度範圍主要透過神經適應（neural adaptation）提升力量，包括增加運動單元徵召（motor unit recruitment）和發射頻率（rate coding）。",
    examTip: "NSCA 四大訓練目標的 %1RM：Strength ≥85%（≤6 reps）、Power 75-90%（1-5 reps）、Hypertrophy 67-85%（6-12 reps）、Endurance ≤67%（≥12 reps）。必背！",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 10,
    question: "A strength and conditioning coach prescribes an exercise at 80% 1RM. According to the NSCA repetition-percentage relationship, approximately how many repetitions can be performed?",
    options: {
      A: "8 reps",
      B: "2 reps",
      C: "15 reps",
      D: "20 reps"
    },
    correct: 'A',
    explanation: "根據 NSCA 的 %1RM-反覆次數對照表：80% 1RM 大約對應 8RM（可做 8 次）。常見對應：100%=1RM、95%≈2RM、93%≈3RM、90%≈4RM、87%≈5RM、85%≈6RM、83%≈7RM、80%≈8RM、77%≈9RM、75%≈10RM。",
    examTip: "背熟 %1RM 對照表是 CSCS 考試必備。快速記法：每降 2-3%，反覆次數約增加 1 次。80% ≈ 8RM 是常考數字。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 11,
    question: "For training muscular power with single-effort events (e.g., shot put), the NSCA recommends which load range?",
    options: {
      A: "80-90% 1RM",
      B: "50-67% 1RM",
      C: "30-50% 1RM",
      D: "≤30% 1RM"
    },
    correct: 'A',
    explanation: "NSCA 區分兩種爆發力訓練負荷：單次爆發動作（single-effort，如鉛球）建議 80-90% 1RM；多次爆發動作（multiple-effort，如多次跳躍）建議 75-85% 1RM。整體爆發力訓練範圍為 75-90% 1RM，1-5 次反覆。",
    examTip: "Power 訓練的負荷取決於動作類型：single-effort = 較重（80-90%）；multiple-effort = 稍輕（75-85%）。兩者都在 75-90% 的大範圍內。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 12,
    question: "Which of the following load and repetition combinations is MOST consistent with NSCA guidelines for muscular hypertrophy?",
    options: {
      A: "95% 1RM for 2 reps",
      B: "60% 1RM for 20 reps",
      C: "75% 1RM for 10 reps",
      D: "50% 1RM for 30 reps"
    },
    correct: 'C',
    explanation: "NSCA 肌肥大指南：67-85% 1RM，6-12 次反覆。75% 1RM（約 10RM）× 10 reps 完全符合此範圍。95%×2 屬於 strength；60%×20 和 50%×30 屬於 endurance。",
    examTip: "Hypertrophy zone = 67-85% 1RM, 6-12 reps。考題常給一組數字讓你判斷屬於哪個訓練目標，直接對照範圍即可。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 13,
    question: "An athlete can perform a maximum of 12 repetitions with 150 lb on the bench press. Using the NSCA %1RM table (12 reps ≈ 67%), the estimated 1RM is CLOSEST to:",
    options: {
      A: "175 lb",
      B: "224 lb",
      C: "195 lb",
      D: "250 lb"
    },
    correct: 'B',
    explanation: "12RM 大約對應 67% 1RM。計算：150 lb ÷ 0.67 ≈ 224 lb。此為 NSCA 考試常見的 1RM 估算計算題。",
    examTip: "1RM 估算公式：1RM = 負重 ÷ %1RM。12RM ≈ 67%，所以 1RM ≈ 150 ÷ 0.67 ≈ 224。考試常見此類計算題。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 14,
    question: "For muscular endurance training, the NSCA recommends a load intensity of:",
    options: {
      A: "≥85% 1RM",
      B: "75-85% 1RM",
      C: "67-85% 1RM",
      D: "≤67% 1RM"
    },
    correct: 'D',
    explanation: "NSCA 肌耐力（muscular endurance）訓練指南：≤67% 1RM，≥12 次反覆。此強度範圍促進慢縮肌纖維（Type I）的適應、提高毛細血管密度和粒線體功能。",
    examTip: "≤67% 1RM + ≥12 reps = Endurance。注意「≤」和「≥」的方向，考題常在這裡設陷阱。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 15,
    question: "When training for muscular power using Olympic lifts (e.g., power clean), the recommended repetition range according to the NSCA is:",
    options: {
      A: "1-5 reps per set",
      B: "8-12 reps per set",
      C: "15-20 reps per set",
      D: "20-25 reps per set"
    },
    correct: 'A',
    explanation: "NSCA 爆發力訓練（包括奧林匹克舉重動作如 power clean、snatch）建議 1-5 次反覆。這是因為爆發力動作需要最大速度和技術品質，高反覆次數會導致疲勞，降低動作速度和技術精確度。",
    examTip: "Power 訓練 = 1-5 reps。奧舉動作絕不超過 5-6 reps，因為疲勞會嚴重影響技術和受傷風險。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },
  {
    id: 16,
    question: "Which of the following 1RM percentage and repetition pairings is INCORRECT according to the NSCA guidelines?",
    options: {
      A: "95% 1RM ≈ 2 repetitions",
      B: "90% 1RM ≈ 4 repetitions",
      C: "80% 1RM ≈ 8 repetitions",
      D: "70% 1RM ≈ 15 repetitions"
    },
    correct: 'D',
    explanation: "根據 NSCA 指南：95% ≈ 2 reps、90% ≈ 4 reps、80% ≈ 8 reps 均正確。但 70% 1RM 大約對應 12 次反覆，而非 15 次。15 reps 大約對應 65% 1RM。因此選項 D 的配對不正確。",
    examTip: "70% 1RM ≈ 12 reps（非 15 reps）。常見陷阱題：注意每個百分比的精確對應次數。",
    topic: 'cscs-program-design',
    part: '1RM & Rep Ranges'
  },

  // ==================== Volume Load (id 17-22) ====================
  {
    id: 17,
    question: "Volume load is calculated as:",
    options: {
      A: "Sets × reps",
      B: "Weight × rest period",
      C: "Reps × weight ÷ time",
      D: "Sets × reps × weight"
    },
    correct: 'D',
    explanation: "訓練量負荷（Volume Load）= 組數（sets）× 反覆次數（reps）× 重量（weight）。例如：3 sets × 10 reps × 100 kg = 3,000 kg volume load。這是量化和追蹤訓練壓力最常用的指標之一。",
    examTip: "Volume Load = Sets × Reps × Weight。注意區分：Training Volume = Sets × Reps（不含重量）；Volume Load 才包含重量。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },
  {
    id: 18,
    question: "An athlete performs 4 sets of 8 reps of the back squat at 120 kg. What is the volume load for this exercise?",
    options: {
      A: "960 kg",
      B: "3,840 kg",
      C: "2,880 kg",
      D: "4,800 kg"
    },
    correct: 'B',
    explanation: "Volume Load = 4 sets × 8 reps × 120 kg = 3,840 kg。這類計算題在 CSCS 考試中非常常見，務必確認乘法正確。",
    examTip: "計算題必拿分。4 × 8 × 120 = 3,840。考試時仔細計算，不要因為粗心失分。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },
  {
    id: 19,
    question: "According to the volume-intensity relationship, as training intensity increases, training volume should generally:",
    options: {
      A: "Decrease",
      B: "Remain unchanged",
      C: "Increase proportionally",
      D: "Increase exponentially"
    },
    correct: 'A',
    explanation: "訓練量與強度呈反比關係（inverse relationship）：當強度增加時，訓練量應相應減少。這是因為高強度訓練對神經肌肉系統的壓力更大，需要更長恢復時間。若同時增加量和強度，將導致過度訓練。",
    examTip: "Volume-Intensity inverse relationship 是週期化的核心原則。考題常問「intensity ↑ 時 volume 應如何？」答案永遠是 ↓。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },
  {
    id: 20,
    question: "A coach compares two bench press protocols:\nProtocol A: 3 sets × 10 reps × 80 kg\nProtocol B: 5 sets × 5 reps × 100 kg\nWhich has the GREATER volume load?",
    options: {
      A: "Protocol A (2,400 kg)",
      B: "Protocol B (2,500 kg)",
      C: "They are equal",
      D: "Cannot be determined without rest period data"
    },
    correct: 'B',
    explanation: "Protocol A：3 × 10 × 80 = 2,400 kg。Protocol B：5 × 5 × 100 = 2,500 kg。Protocol B 的 volume load 較大（2,500 > 2,400）。注意：雖然 Protocol A 的總反覆次數較多（30 vs 25），但因重量較輕，volume load 反而較低。",
    examTip: "Volume load 考量的是「總做功量」，不是單純的反覆次數。高強度低次數的 volume load 可能高於低強度高次數。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },
  {
    id: 21,
    question: "During a hypertrophy phase, an appropriate volume prescription for a core exercise (e.g., squat) according to NSCA guidelines is:",
    options: {
      A: "1-2 sets of 1-3 reps",
      B: "1 set of 15-20 reps",
      C: "10 sets of 1 rep",
      D: "3-6 sets of 6-12 reps"
    },
    correct: 'D',
    explanation: "NSCA 肌肥大訓練指南：核心動作（core exercises）建議 3-6 組、6-12 次反覆（67-85% 1RM）。此範圍產生充足的機械張力（mechanical tension）和代謝壓力（metabolic stress），是肌肥大的兩大刺激因素。",
    examTip: "Hypertrophy 的 volume 處方：3-6 sets × 6-12 reps。Strength = 2-6 sets × ≤6 reps；Endurance = 2-3 sets × ≥12 reps。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },
  {
    id: 22,
    question: "Which of the following is a limitation of using volume load (sets × reps × weight) as a measure of training stress?",
    options: {
      A: "It does not account for biomechanical or metabolic differences between exercises",
      B: "It cannot be calculated for free weight exercises",
      C: "It overestimates the contribution of single-joint exercises",
      D: "It is only valid for exercises performed above 85% 1RM"
    },
    correct: 'A',
    explanation: "訓練量負荷（volume load）的主要限制是無法反映不同動作之間的生物力學和代謝差異。例如，100 kg 的深蹲與 100 kg 的二頭肌彎舉雖然可以計算出相同的 volume load，但對身體造成的實際壓力完全不同。Volume load 也無法反映動作的難度、穩定性需求或代謝成本。",
    examTip: "Volume load 的限制：無法區分動作差異。例如 squat 100 kg vs. curl 100 kg 的生理壓力完全不同，但 volume load 數值可能相同。",
    topic: 'cscs-program-design',
    part: 'Volume Load'
  },

  // ==================== Training Variables (id 23-32) ====================
  {
    id: 23,
    question: "According to the NSCA, the recommended rest period between sets for maximal strength training is:",
    options: {
      A: "30-60 seconds",
      B: "60-90 seconds",
      C: "2-5 minutes",
      D: "5-8 minutes"
    },
    correct: 'C',
    explanation: "NSCA 最大肌力訓練的組間休息建議為 2-5 分鐘。較長休息時間允許 ATP-PCr 系統充分恢復（3-5 分鐘可恢復約 95-100%），確保下一組能維持高強度和良好的動作品質。",
    examTip: "Rest periods by goal：Strength = 2-5 min、Power = 2-5 min、Hypertrophy = 30-90 sec、Endurance = ≤30 sec。這是必背表格！",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 24,
    question: "For hypertrophy training, the recommended rest period between sets is:",
    options: {
      A: "≤30 seconds",
      B: "30-90 seconds",
      C: "2-5 minutes",
      D: "5-8 minutes"
    },
    correct: 'B',
    explanation: "NSCA 肌肥大訓練的組間休息建議為 30-90 秒。較短的休息時間有助於維持較高的代謝壓力（metabolic stress），促進生長激素（GH）和其他合成代謝激素的釋放，這些都是肌肥大的重要驅動因素。",
    examTip: "Hypertrophy = 30-90 sec rest。短休息 → 代謝壓力 ↑ → GH 釋放 ↑ → 肌肥大刺激。考題常問「哪個休息時間最能促進 GH 釋放？」",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 25,
    question: "Which rest period is MOST appropriate for muscular endurance training?",
    options: {
      A: "≤30 seconds",
      B: "1-2 minutes",
      C: "3-4 minutes",
      D: "5-6 minutes"
    },
    correct: 'A',
    explanation: "NSCA 肌耐力訓練的組間休息建議為 ≤30 秒。極短的休息時間迫使身體在不完全恢復的狀態下繼續運動，刺激肌耐力適應（如提升乳酸緩衝能力、增加毛細血管密度）。",
    examTip: "Endurance rest = ≤30 sec，是四個訓練目標中最短的。記住遞減順序：Strength/Power（2-5 min）> Hypertrophy（30-90 sec）> Endurance（≤30 sec）。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 26,
    question: "An athlete trains 4 days per week with an upper/lower body split. What is the training frequency per muscle group per week?",
    options: {
      A: "1 time per week",
      B: "4 times per week",
      C: "6 times per week",
      D: "2 times per week"
    },
    correct: 'D',
    explanation: "上下肢分化（Upper/Lower Split）每週訓練 4 天，通常安排為：週一上肢、週二下肢、週四上肢、週五下肢。因此每個肌群每週被訓練 2 次。這是 NSCA 建議的中階至進階訓練者的理想頻率。",
    examTip: "頻率計算：Upper/Lower 4天 = 每肌群 2次/週；Push/Pull/Legs 6天 = 每肌群 2次/週；Full body 3天 = 每肌群 3次/週。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 27,
    question: "For a novice (untrained) individual, the NSCA recommends a training frequency of:",
    options: {
      A: "2-3 days per week",
      B: "1 day per week",
      C: "5-6 days per week",
      D: "7 days per week"
    },
    correct: 'A',
    explanation: "NSCA 對初學者（novice/untrained）的訓練頻率建議為每週 2-3 天。初學者的恢復能力較低，需要較多的休息天數。隨著訓練經驗增加，可逐漸增加至每週 4-6 天（使用分化訓練）。",
    examTip: "Training frequency by level：Beginner = 2-3 days/week（full body）；Intermediate = 3-4 days/week；Advanced = 4-6 days/week（split routines）。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 28,
    question: "For power training (e.g., hang cleans), the recommended rest period between sets is:",
    options: {
      A: "≤30 seconds",
      B: "30-60 seconds",
      C: "2-5 minutes",
      D: "No rest needed"
    },
    correct: 'C',
    explanation: "NSCA 爆發力訓練的組間休息建議為 2-5 分鐘，與最大肌力訓練相同。爆發力動作需要最大神經肌肉徵召和 ATP-PCr 系統的充分恢復，短休息會降低動作速度和增加受傷風險。",
    examTip: "Power 和 Strength 的 rest period 相同 = 2-5 min。原因都是需要 ATP-PCr 完全恢復。考題可能問「power clean 的休息時間」。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 29,
    question: "Which of the following BEST represents the recommended number of sets for strength training of a core exercise according to the NSCA?",
    options: {
      A: "1-2 sets",
      B: "8-10 sets",
      C: "2-6 sets",
      D: "12-15 sets"
    },
    correct: 'C',
    explanation: "NSCA 核心動作（core exercises，如 squat、bench press、deadlift）的力量訓練建議為 2-6 組。輔助動作（assistance exercises）則建議 1-3 組。組數取決於訓練經驗、訓練階段和具體目標。",
    examTip: "Strength sets：Core exercises = 2-6 sets；Assistance exercises = 1-3 sets。注意這裡的「core exercise」指的是多關節大肌群動作，不是核心肌群訓練。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 30,
    question: "Which of the following rest interval lengths is MOST likely to elicit the greatest acute growth hormone response during resistance training?",
    options: {
      A: "30-60 seconds",
      B: "≤30 seconds",
      C: "3-5 minutes",
      D: "5 minutes or longer"
    },
    correct: 'A',
    explanation: "30-60 秒的短暫休息時間會產生最大的急性生長激素（GH）反應。這是因為較短的休息時間導致更大的代謝壓力（如乳酸堆積、氫離子濃度升高），而這些代謝副產物是刺激 GH 分泌的重要因素。這也是肌肥大訓練建議使用 30-90 秒休息的原因之一。",
    examTip: "短休息（30-60 sec）= 最大 GH 反應 = 代謝壓力最大。這解釋了為何肌肥大訓練用短休息。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 31,
    question: "When designing a resistance training program for a competitive powerlifter in the off-season, which of the following training approaches is MOST appropriate?",
    options: {
      A: "2 days/week, 12-15 reps at 65% 1RM",
      B: "6 days/week, 1-3 reps at 93-100% 1RM",
      C: "1 day/week, 20+ reps at 50% 1RM",
      D: "3-4 days/week, 6-12 reps at 67-85% 1RM with some heavier sets"
    },
    correct: 'D',
    explanation: "力量舉選手在非賽季應建立肌肉量和一般體能基礎。每週 3-4 天訓練，使用 6-12 次反覆（肌肥大範圍）搭配部分較重組（肌力維持）是最合適的。非賽季不應過度使用極高強度（>90%），以避免累積疲勞和受傷風險。",
    examTip: "Off-season = 建立基礎 = 中等強度、中等反覆次數為主。不要在非賽季一直練極大重量。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },
  {
    id: 32,
    question: "When training frequency is increased from 3 to 5 days per week, which program modification is MOST important to prevent overtraining?",
    options: {
      A: "Increase the load by 10% on all exercises",
      B: "Implement a split routine to allow muscle group recovery",
      C: "Reduce rest periods to 15 seconds between sets",
      D: "Add more exercises per session"
    },
    correct: 'B',
    explanation: "當訓練頻率增加時，最重要的調整是採用分化訓練（split routine），讓每個肌群在兩次訓練之間有 48-72 小時的恢復時間。例如從全身訓練改為上下肢分化或推拉分化。增加負荷、減少休息或增加動作都會加重過度訓練風險。",
    examTip: "頻率 ↑ → 必須 split training。NSCA 強調每個肌群需要至少 48 小時恢復。5天全身訓練 = overtraining risk；5天分化訓練 = 適當。",
    topic: 'cscs-program-design',
    part: 'Training Variables'
  },

  // ==================== Program Design Principles (id 33-42) ====================
  {
    id: 33,
    question: "The principle of specificity (SAID principle) states that:",
    options: {
      A: "All exercises should be performed at maximal intensity",
      B: "Training volume should always exceed competition demands",
      C: "Training adaptations are specific to the demands imposed on the body",
      D: "All athletes should follow the same training program"
    },
    correct: 'C',
    explanation: "特異性原則（SAID = Specific Adaptation to Imposed Demands）指出身體的適應是針對施加的特定刺激。訓練計畫必須模擬運動的特定需求（動作模式、肌肉群、能量系統、速度）才能有效轉移到運動表現。",
    examTip: "SAID principle = 訓練適應具有特異性。考題常問「改善垂直跳」該選什麼動作 → 選動作模式最接近的（如 jump squat > leg curl）。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 34,
    question: "According to NSCA exercise order guidelines, which exercise should be performed FIRST in a training session?",
    options: {
      A: "Bicep curl",
      B: "Power clean",
      C: "Lateral raise",
      D: "Tricep pushdown"
    },
    correct: 'B',
    explanation: "NSCA 動作順序原則：(1) 爆發力動作（power/Olympic lifts）最先 → (2) 多關節大肌群動作（core exercises）→ (3) 單關節小肌群動作（assistance exercises）。Power clean 是爆發力動作，應排在最前面，因為它對技術和神經系統要求最高。",
    examTip: "Exercise order：Power exercises → Core (multi-joint) → Assistance (single-joint)。另一原則：Large muscle → Small muscle、Compound → Isolation。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 35,
    question: "Which of the following exercise sequences is MOST consistent with NSCA guidelines for exercise order?",
    options: {
      A: "Bicep curl → bench press → power snatch → squat",
      B: "Power snatch → squat → bench press → bicep curl",
      C: "Bicep curl → tricep extension → squat → power snatch",
      D: "Leg extension → squat → power snatch → bench press"
    },
    correct: 'B',
    explanation: "正確順序：Power snatch（爆發力動作）→ Squat（多關節下肢）→ Bench press（多關節上肢）→ Bicep curl（單關節輔助）。遵循 NSCA 原則：power → core multi-joint → assistance single-joint。",
    examTip: "排列題是 CSCS 高頻題型。記住三層級：Power first → Multi-joint compound → Single-joint isolation。違反此順序的選項直接排除。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 36,
    question: "The principle of progressive overload requires that:",
    options: {
      A: "Training intensity must increase every session",
      B: "Athletes should always train to muscular failure",
      C: "Only training volume should be manipulated",
      D: "Training stress must be gradually increased over time to continue adaptation"
    },
    correct: 'D',
    explanation: "漸進式超負荷原則（Progressive Overload）要求訓練壓力必須隨時間逐漸增加，才能持續產生適應。可以透過增加負荷、反覆次數、組數、訓練頻率或減少休息時間來實現。不需要每次訓練都增加，也不需要練到力竭。",
    examTip: "Progressive overload 的「progressive」= 漸進式，不是每次都加。NSCA 建議初學者每次增加 2.5-10 lb（上肢較少、下肢較多）。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 37,
    question: "An athlete alternates between a bench press set and a bent-over row set with rest between each. This technique is known as:",
    options: {
      A: "Agonist-antagonist paired set (superset)",
      B: "Drop set",
      C: "Forced repetition",
      D: "Pyramid set"
    },
    correct: 'A',
    explanation: "拮抗肌配對組（Agonist-Antagonist Paired Set / Superset）是交替訓練拮抗肌群的動作。Bench press（胸/推）和 Bent-over row（背/拉）是經典的推拉配對。此方法可提高訓練效率、可能增加力量表現（透過交互抑制 reciprocal inhibition）。",
    examTip: "Agonist-antagonist superset 的好處：節省時間、可能提升力量（reciprocal inhibition）、維持肌力平衡。常見配對：bench press/row、bicep curl/tricep extension。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 38,
    question: "When two exercises that stress the same muscle group are performed consecutively (e.g., squat followed by leg press), this is an example of a:",
    options: {
      A: "Agonist-antagonist superset",
      B: "Compound set",
      C: "Circuit training",
      D: "Split set"
    },
    correct: 'B',
    explanation: "複合組（Compound Set）是連續進行兩個訓練相同肌群的動作（如 squat → leg press，都訓練股四頭肌）。與 agonist-antagonist superset（訓練對立肌群）不同。Compound set 會對目標肌群產生更大的疲勞和代謝壓力。",
    examTip: "Compound set = 同肌群連續兩動作（如 squat + leg press）；Agonist-antagonist superset = 對立肌群（如 bench + row）。考題常考兩者的區分。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 39,
    question: "The principle of variation in program design is BEST implemented by:",
    options: {
      A: "Randomly changing exercises every session without a plan",
      B: "Keeping the program exactly the same for 12 months",
      C: "Systematically varying training variables across planned phases",
      D: "Training the same muscle group every day"
    },
    correct: 'C',
    explanation: "變異原則（Principle of Variation）要求有系統地改變訓練變項（強度、量、動作選擇、休息等），通常透過週期化實現。這不是隨機改變（那是 muscle confusion myth），而是有計劃的變化，以避免適應停滯（plateau）和過度訓練。",
    examTip: "Variation ≠ random change。NSCA 強調「planned/systematic variation」。考題選項中若出現「randomly」通常是錯誤的。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 40,
    question: "Circuit training is characterized by:",
    options: {
      A: "Performing one set of each exercise in sequence with minimal rest between stations",
      B: "Performing multiple sets of the same exercise before moving to the next",
      C: "Training only the upper body in a single session",
      D: "Using only maximal loads for all exercises"
    },
    correct: 'A',
    explanation: "循環訓練（Circuit Training）的特徵是：連續進行多個不同動作（stations），每個動作做 1 組後立即移至下一個動作，中間休息極短（通常 15-30 秒）。完成所有動作為一個循環（circuit），可重複 2-3 個循環。適合同時發展肌耐力和心肺耐力。",
    examTip: "Circuit training = 一個動作一組 → 換下一個動作 → 最少休息。與 traditional set training（同一動作做完所有組）不同。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 41,
    question: "The exercise order principle may be intentionally violated when using which of the following training techniques?",
    options: {
      A: "Pyramid training",
      B: "Periodization",
      C: "Progressive overload",
      D: "Pre-exhaustion"
    },
    correct: 'D',
    explanation: "預先疲勞法（Pre-exhaustion）刻意先進行單關節動作以預先疲勞目標肌群，再進行多關節動作。例如：先做 leg extension（股四頭肌預先疲勞）→ 再做 back squat。這違反了一般的「multi-joint before single-joint」原則，但是一種有意為之的訓練技巧。",
    examTip: "Pre-exhaustion 是動作順序原則的合理例外：先單關節疲勞目標肌 → 再多關節複合動作。考試可能問「何時可以違反 exercise order」。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },
  {
    id: 42,
    question: "According to NSCA guidelines, when an athlete cannot maintain proper exercise technique during a set, the strength and conditioning coach should:",
    options: {
      A: "Encourage the athlete to push through the discomfort",
      B: "Terminate the set or reduce the load",
      C: "Increase the rest period to 10 minutes",
      D: "Switch to a ballistic exercise instead"
    },
    correct: 'B',
    explanation: "NSCA 明確指出：當運動員無法維持正確動作技術時，應立即終止該組或降低負荷。繼續在不良技術下訓練會增加受傷風險，且不會產生理想的訓練適應。安全永遠是第一優先。",
    examTip: "NSCA 安全原則：technique breakdown → stop the set 或 reduce load。考題中任何「push through」或「ignore form」的選項都是錯誤的。",
    topic: 'cscs-program-design',
    part: 'Program Design Principles'
  },

  // ==================== Taper & Peaking (id 43-47) ====================
  {
    id: 43,
    question: "During a taper phase leading up to competition, which training variable should be reduced the MOST?",
    options: {
      A: "Training volume",
      B: "Training intensity",
      C: "Exercise selection variety",
      D: "Training frequency (by more than 50%)"
    },
    correct: 'A',
    explanation: "賽前減量期（Taper）最應大幅減少的是訓練量（volume），通常減少 60-90%。訓練強度應維持或僅略微降低，以維持神經肌肉適應。訓練頻率不應減少超過 20-50%，以避免 detraining。",
    examTip: "Taper 的「黃金法則」：Volume ↓↓↓（最多減）、Intensity maintain or ↓ slightly、Frequency ↓ slightly（不超過 50%）。考題最常問「哪個變項減最多？」= Volume。",
    topic: 'cscs-program-design',
    part: 'Taper & Peaking'
  },
  {
    id: 44,
    question: "A taper period typically lasts:",
    options: {
      A: "1-2 days",
      B: "6-8 weeks",
      C: "3-6 months",
      D: "8-14 days"
    },
    correct: 'D',
    explanation: "賽前減量期（Taper）通常持續 8-14 天（約 1-2 週），最長可達 4 週。太短（<1 週）無法充分恢復；太長（>4 週）可能導致 detraining 效應。具體長度取決於前期訓練量和運動員的恢復能力。",
    examTip: "Taper duration = 8-14 days（最常見答案）。研究顯示 2 週 taper 能產生約 2-3% 的表現提升。超過 4 週則開始 detraining。",
    topic: 'cscs-program-design',
    part: 'Taper & Peaking'
  },
  {
    id: 45,
    question: "During a taper, maintaining training intensity is important because it helps preserve:",
    options: {
      A: "Flexibility gains",
      B: "Maximum heart rate",
      C: "Neuromuscular adaptations and strength",
      D: "Body fat percentage"
    },
    correct: 'C',
    explanation: "在減量期維持訓練強度對保留神經肌肉適應（motor unit recruitment、rate coding、intermuscular coordination）和肌力至關重要。如果強度大幅降低，這些神經適應會在 1-2 週內開始減退，導致力量和爆發力下降。",
    examTip: "Taper 維持 intensity 的原因 = 保留 neuromuscular adaptations。肌力的流失速度比有氧能力慢，但神經適應比肌肉適應更快消退。",
    topic: 'cscs-program-design',
    part: 'Taper & Peaking'
  },
  {
    id: 46,
    question: "A deload week is BEST described as:",
    options: {
      A: "A week of complete inactivity",
      B: "A planned reduction in training stress (typically 50-70% of normal volume/intensity) to facilitate recovery",
      C: "A week focused exclusively on cardiovascular training",
      D: "A week where only new exercises are introduced"
    },
    correct: 'B',
    explanation: "Deload week 是有計劃地減少訓練壓力的一週，通常將 volume 和/或 intensity 降低至正常的 50-70%。目的是促進身體恢復、減少累積疲勞、預防過度訓練，同時維持訓練習慣和動作模式。一般每 3-4 週安排一次。",
    examTip: "Deload ≠ complete rest（那是 transition phase）。Deload 仍然訓練，只是降低壓力。常見安排：3 週漸進負荷 + 1 週 deload（3:1 pattern）。",
    topic: 'cscs-program-design',
    part: 'Taper & Peaking'
  },
  {
    id: 47,
    question: "Which type of taper has been shown by research to produce the BEST performance outcomes?",
    options: {
      A: "Step taper (sudden, uniform reduction)",
      B: "Linear taper (gradual, even reduction)",
      C: "Exponential taper with fast decay",
      D: "No-taper approach (maintain all variables)"
    },
    correct: 'C',
    explanation: "研究顯示快速衰減的指數型減量（exponential taper with fast decay）通常產生最佳的競賽表現。在此模式中，訓練量在減量初期快速大幅降低，之後趨於平緩。與線性減量（均勻減少）或階梯式減量（突然減少）相比，快速指數型減量在消除疲勞的同時更好地保持體能水準。",
    examTip: "最佳 taper 類型 = Exponential with fast decay。三種 taper：Step（一次性降）、Linear（均勻漸降）、Exponential（先快後慢，效果最佳）。",
    topic: 'cscs-program-design',
    part: 'Taper & Peaking'
  },

  // ==================== Exercise Selection (id 48-50) ====================
  {
    id: 48,
    question: "The FIRST step in designing a resistance training program, according to the NSCA, is to:",
    options: {
      A: "Select the exercises to be performed",
      B: "Determine the training frequency",
      C: "Conduct a needs analysis",
      D: "Establish the training volume and intensity"
    },
    correct: 'C',
    explanation: "根據 NSCA，設計阻力訓練計畫的第一步是進行需求分析（needs analysis）。需求分析包括兩個面向：(1) 評估運動項目的需求（動作分析、生理需求、常見傷害），(2) 評估運動員的個人狀況（訓練經驗、傷病史、體能水準、可用時間）。只有完成需求分析後，才能適當地選擇動作和設定訓練變項。",
    examTip: "Program design 第一步永遠是 Needs Analysis。先了解運動和運動員，再設計課表。NSCA 流程：Needs analysis → Exercise selection → Exercise order → Volume/Intensity → Rest → Frequency。",
    topic: 'cscs-program-design',
    part: 'Exercise Selection'
  },
  {
    id: 49,
    question: "When selecting exercises for a volleyball player, which of the following combinations BEST applies the principle of specificity?",
    options: {
      A: "Long-distance running and seated machine exercises",
      B: "Wrist curls, seated calf raises, and recumbent bike",
      C: "Bench press only at high reps with short rest",
      D: "Power clean, jump squat, and standing overhead press"
    },
    correct: 'D',
    explanation: "排球的主要動作需求包括：垂直跳躍（jumping）、爆發性高舉過頭動作（overhead hitting/blocking）和快速下肢發力。Power clean 和 jump squat 訓練下肢爆發力，standing overhead press 訓練殺球和攔網所需的肩部力量。這最符合特異性原則（SAID principle）。",
    examTip: "Exercise selection 題型：先分析運動的動作模式和能量系統，再選擇最匹配的訓練動作。排球 = 跳躍（下肢爆發）+ 擊球（上肢 overhead power）→ 選爆發力 + overhead 動作。",
    topic: 'cscs-program-design',
    part: 'Exercise Selection'
  },
  {
    id: 50,
    question: "Which of the following exercises is classified as a power exercise (a subcategory of structural exercises)?",
    options: {
      A: "Barbell back squat",
      B: "Seated bicep curl",
      C: "Power snatch",
      D: "Seated shoulder press machine"
    },
    correct: 'C',
    explanation: "Power exercise 是結構性動作的子類別，需要以快速、爆發性的動作速度完成。Power snatch（抓舉）是典型的 power exercise，因為它需要爆發性地將槓鈴從地面舉至頭頂。Back squat 是結構性動作但通常不歸類為 power exercise（除非以爆發性速度如 jump squat）。Seated curl 和 seated machine press 都不是結構性動作。",
    examTip: "分類層級：All exercises → Structural exercises（脊柱承重）→ Power exercises（結構性 + 快速/爆發性）。典型 power exercises：clean、snatch、push press、jump squat。",
    topic: 'cscs-program-design',
    part: 'Exercise Selection'
  }
];
