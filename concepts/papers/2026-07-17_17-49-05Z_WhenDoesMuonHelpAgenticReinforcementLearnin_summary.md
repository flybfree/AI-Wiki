# Summary: 2026-07-17_17-49-05Z_WhenDoesMuonHelpAgenticReinforcementLearning.md
Saved: 2026-07-19 21:01
Source: 2026-07-17_17-49-05Z_WhenDoesMuonHelpAgenticReinforcementLearning.md
Model: None

---

## Summary  
The paper investigates whether the Muon optimizer can improve performance in agentic reinforcement learning tasks after pre‑training with large language models. It conducts single‑seed experiments comparing vanilla Muon to AdamW on the ALFWorld benchmark using Qwen2.5-0.5B-Instruct under Group-in-Group Policy Optimization (GiGPO). The results show that applying Muon selectively to hidden weight matrices significantly boosts validation success rates, especially with certain advantage estimators and learning rates. These findings suggest that optimizer choice matters for RL post‑training despite its limited impact on pre‑training.

## Key Contributions  
- Finding 1: Vanilla Muon applied only to hidden layers increases final-window validation success from 0.290 to 0.546 (+88%) in GiGPO.  
- Finding 2: The benefit is rate‑dependent; at learning rate 3e‑5 Muon improves GRPO from 0.161 to 0.268, while GraphGPO's late-window gap narrows near saturation.  
- Finding 3: At a lower learning rate (1e‑5) Muon drives GraphGPO success to 0.901, lifts normalized validation AUC from 0.399 to 0.556, and achieves 0.5/0.75 success thresholds earlier in the update schedule.

## Methodology  
The authors employ matched single‑seed comparisons between Muon and AdamW on the ALFWorld environment using Qwen2.5-0.5B-Instruct. They implement Group-in-Group Policy Optimization (GiGPO) to evaluate final‑window performance, varying the application of Muon (only hidden weights), advantage estimator (GRPO vs GraphGPO), and learning rates (3e‑5 and 1e‑5). Experiments are run with a single seed per configuration.

## Results  
The main experimental results are the reported success probabilities and AUC improvements across configurations. Muon yields higher final‑window success, especially for GRPO at moderate LR; at low LR it maximizes GraphGPO performance and improves AUc significantly. It also accelerates reaching predefined thresholds earlier.

## Significance  
This work demonstrates that optimizer selection can affect RL post‑training, opening a research direction to jointly study optimizers, advantage estimators, and learning rates for agentic RL. It challenges the assumption that Muon’s value is limited to pre‑training.

## Related Concepts  
Muon optimizer, AdamW, Group-in-Group Policy Optimization (GiGPO), GRPO, GraphGPO, advantage estimator, learning rate schedule, final-window validation, ALFWorld benchmark, Qwen2.5-0.5B-Instruct
