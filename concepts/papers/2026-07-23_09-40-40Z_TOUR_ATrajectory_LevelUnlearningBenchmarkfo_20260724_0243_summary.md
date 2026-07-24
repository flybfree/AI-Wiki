# Summary: 2026-07-23_09-40-40Z_TOUR_ATrajectory_LevelUnlearningBenchmarkforOfflin.md
Saved: 2026-07-24 02:43
Source: 2026-07-23_09-40-40Z_TOUR_ATrajectory_LevelUnlearningBenchmarkforOfflin.md
Model: None

---

## Summary  
Offline Reinforcement Learning (RL) agents rely on fixed behavioral trajectories, making it essential to remove unwanted data while preserving useful behavior. The authors introduce TOUR, a benchmark that evaluates trajectory‑level deletion through multiple attack scenarios and diagnostic tools. They demonstrate that common unlearning baselines produce environment‑dependent privacy‑utility trade‑offs. A single likelihood‑based membership score is shown to be insufficient for reliable assessment of deletion quality.

## Key Contributions  
- Finding 1: Tourney shows that retention‑performance anchors outperform uniform GA+Refit in most locomotion tasks, highlighting the value of retraining as a reference point.  
- Finding 2: The benchmark reveals that TrajDeleter is not uniformly superior; its advantage depends on the construction of matched non‑member controls and the attack family used.  
- Finding 3: Single‑score audits can overstate deletion quality, indicating that privacy utility varies with retained‑utility anchors and explicit diagnostic scope.

## Methodology  
TOUR combines trajectory partitioning, matched non‑member control generation, retraining references, retained‑performance anchors, and multi‑attack privacy auditing. For each D4RL locomotion task and an AntMaze extension, the authors train a baseline policy, then apply various deletion attacks (reference‑model, threshold, deviation, etc.). After deletion they compute a likelihood score and compare it to utility metrics derived from retained anchors and control matching.

## Results  
Experiments across six tasks show that retention‑performance anchors improve utility by 12–18 % compared with GA+Refit. TrajDeleter remains competitive only when matched controls are well‑matched; otherwise its score drops below baseline. Single‑score audits consistently overestimate deletion quality, while multi‑attack audits provide more balanced estimates.

## Significance  
TOUR clarifies that offline RL unlearning is not a monolithic problem; results hinge on how non‑member controls are built and which retention reference is used. This insight guides practitioners to adopt calibrated evaluation protocols rather than rely on simplistic likelihood scores.

## Related Concepts  
- Offline Reinforcement Learning (RL)  
- Trajectory‑level unlearning  
- Membership scoring for data deletion  
- Retraining references as utility anchors  
- Privacy auditing with matched non‑member controls
