title: "Summary: 2026-06-25_17-59-36Z_ReinforcementLearningwithoutGround_TruthSolutionsc.md"
# Summary: 2026-06-25_17-59-36Z_ReinforcementLearningwithoutGround_TruthSolutionsc.md
Saved: 2026-06-25 22:01
Source: 2026-06-25_17-59-36Z_ReinforcementLearningwithoutGround_TruthSolutionsc.md
Model: None

---


## Summary  
The paper proposes a reinforcement‑learning framework called RiVER that enables training large language models on coding tasks without relying on ground‑truth solutions, using only score‑based feedback from deterministic execution. It addresses two major challenges in score‑based RL—scale dominance and frequency dominance—and demonstrates that such calibration can improve both relative ranking and exact‑solution performance across multiple benchmarks.

## Key Contributions  
- [Finding 1] Introduces the RiVER framework that replaces ground‑truth rewards with continuous, instance‑wise comparative feedback.  
- [Finding 2] Identifies scale dominance (unbalanced score magnitudes) and frequency dominance (repeated suboptimal solutions) as obstacles to stable policy updates in group‑relative RL.  
- [Finding 3] Shows empirical gains of up to 9.4 % ranking improvement for Qwen3‑8B on ALE‑Bench, plus absolute improvements of 2.4 % on LiveCodeBench and 3.5 % on USACO.

## Methodology  
The authors train LLMs using reinforcement learning with verifiable rewards (RLVR) where the reward is a deterministic execution score derived from ranking solvers rather than true correctness. They employ calibrated reward shaping that emphasizes top‑ranked solutions while bounding feedback for other valid ones, mitigating scale and frequency dominance through instance‑wise comparisons.

## Results  
On 12 AtCoder Heuristic Contest tasks, RiVER improves ALE rating rank by 8.9 % (Qwen3‑8B) and 9.4 % (GLM‑Z1‑9B‑0414). Across exact‑solution benchmarks, the same models gain an average absolute improvement of 2.4 % on LiveCodeBench and 3.5 % on USACO. Baseline methods using raw scores improve ALE ranking but show no transfer to exact solutions.

## Significance  
By decoupling training from ground‑truth answers, RiVER opens a scalable path for improving coding LLMs in environments where correct solutions are unavailable, such as large‑scale benchmarking or limited data settings.

## Related Concepts  
- Reinforcement Learning with Verifiable Rewards (RLVR)  
- Score‑based optimization  
- Group‑relative RL  
- Calibrated reward shaping  
- Scale dominance and frequency dominance
