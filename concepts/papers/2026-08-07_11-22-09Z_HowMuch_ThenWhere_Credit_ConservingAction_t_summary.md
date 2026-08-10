# Summary: 2026-08-07_11-22-09Z_HowMuch_ThenWhere_Credit_ConservingAction_to_Token.md
Saved: 2026-08-09 22:55
Source: 2026-08-07_11-22-09Z_HowMuch_ThenWhere_Credit_ConservingAction_to_Token.md
Model: None

---

## Summary  
The paper addresses credit assignment in multi‑turn reinforcement learning, proposing a method that separates trajectory‑level credit from token‑level distribution. It uses checkpoint‑calibrated TD residuals to assign per‑action credits that telescope to the trajectory advantage and feedback‑conditioned teacher‑student likelihood gaps to allocate each credit across realized action tokens. Per‑action normalization preserves the action‑average coefficient and prevents sign flips at the token level. This construction is paired with an action‑mean reduction that removes the implicit dependence of an action’s scalar surrogate weight on its token length.

## Key Contributions  
- [Finding 1] FACTOR separates trajectory‑level credit assignment from token‑level allocation, enabling precise telescoping of credits to the overall advantage.  
- [Finding 2] The method employs checkpoint‑calibrated TD residuals for per‑action credit and feedback‑conditioned teacher‑student likelihood gaps for token allocation.  
- [Finding 3] Ablations show that per‑action TD credit is the dominant driver of improvement, with hindsight token allocation providing complementary gains.

## Methodology  
The authors approach by constructing a credit assignment pipeline that first computes per‑action credit via checkpoint‑calibrated TD residuals, then allocates each credit across tokens using feedback‑conditioned teacher‑student likelihood gaps while normalizing to keep the action‑average coefficient constant. They also implement an action‑mean reduction that decouples the scalar surrogate weight from token length, ensuring the inner action‑mean equals the trajectory advantage.

## Results  
Experiments on ALFWorld, WebShop, and ScienceWorld demonstrate that FACTOR consistently outperforms competitive baselines across all seeds and environments, with the largest gains observed in the longest‑horizon tasks. Hyperparameters remain stable when transferred to larger backbones or different model families without retuning. Ablation studies confirm that per‑action TD credit is the dominant driver of improvement, while hindsight token allocation contributes complementary gains.

## Significance  
This work advances RL by providing a principled way to allocate credit that respects both trajectory advantage and token‑level impact, potentially improving stability and learning efficiency in long interactions. By decoupling credit assignment from token length, FACTOR may enable more robust training of multi‑turn agents across diverse environments.

## Related Concepts  
- Credit assignment  
- Trajectory advantage  
- Teacher‑student likelihood gap  
- Per‑action normalization  
- Action‑mean reduction  
- Multi‑turn reinforcement learning  
- ALFWorld benchmark
