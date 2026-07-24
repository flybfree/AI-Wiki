# Summary: 2026-07-23_09-40-40Z_TOUR_ATrajectory_LevelUnlearningBenchmarkforOfflin.md
Saved: 2026-07-24 02:36
Source: 2026-07-23_09-40-40Z_TOUR_ATrajectory_LevelUnlearningBenchmarkforOfflin.md
Model: None

---

## Summary  
The paper introduces TOUR, a benchmark for trajectory‑level unlearning in offline reinforcement learning (RL), which evaluates how well data can be removed after training while preserving useful behavior and privacy. It demonstrates that common deletion baselines exhibit environment‑dependent trade‑offs between privacy and utility, and that a single likelihood‑based membership score often misrepresents the true quality of deletions. The authors also show that retraining or fine‑tuning provides stronger retained‑utility references than uniform GA+Refit, while TrajDeleter is not uniformly superior under identical audit conditions. These findings highlight the instability of conclusions drawn from single‑score audits and underscore the need for careful construction of non‑member controls and retention strategies.

## Key Contributions  
- [Finding 1] TOUR reveals that deletion baselines have environment‑dependent privacy‑utility behavior, meaning that removing trajectories can either degrade utility or violate privacy depending on the task.  
- [Finding 2] Retraining or fine‑tuning yields stronger retained‑utility references than uniform GA+Refit, and TrajDeleter is not consistently superior across audit protocols.  
- [Finding 3] A single likelihood‑based membership score can overstate deletion quality because it does not account for matched non‑member construction, attack families, or retained performance.

## Methodology  
TOUR combines several components: (1) trajectory‑level partitioning to isolate the set of trajectories to be deleted; (2) construction of matched non‑member controls that reflect the distribution of actions in the original dataset; (3) retraining references that capture the utility of preserved behavior after deletion; (4) retained‑performance anchors that serve as benchmarks for evaluating utility loss; and (5) multi‑attack privacy auditing that tests various attack families against a likelihood score. The benchmark runs on D4RL locomotion tasks and an exploratory AntMaze extension, measuring both privacy leakage and utility preservation.

## Results  
Experiments show that baseline deletion methods such as GA+Refit often produce high privacy scores but low retained performance, while TRAJDeleter sometimes outperforms them in privacy but still suffers from utility loss. Retraining‑based approaches consistently retain higher performance with comparable or better privacy. Crucially, the likelihood score alone fails to capture these nuances; attacks that rely on reference models, thresholds, deviations, action errors, representation mismatches, or limited queries can inflate deletion quality metrics. The results demonstrate that offline RL unlearning conclusions are not stable under single‑score audits and depend heavily on construction choices.

## Significance  
TOUR provides a rigorous framework for evaluating trajectory‑level unlearning in offline RL, moving beyond ad‑hoc score comparisons to consider matched controls, retention strategies, and attack dynamics. It clarifies that privacy‑utility trade‑offs are task‑specific and that single‑score metrics can be misleading, guiding researchers toward more holistic assessment protocols.

## Related Concepts  
- Trajectory‑level deletion  
- Membership scoring in offline RL  
- Privacy‑utility trade‑off  
- Retraining references / fine‑tuning  
- GA+Refit baseline  
- TRAJDeleter  
- Likelihood‑based attack families (reference model, threshold, deviation, action error, representation‑based, query‑limited)
