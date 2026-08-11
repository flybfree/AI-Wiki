# Summary: 2026-08-10_11-22-53Z_WDL_OPD_Weak_DrivenOn_PolicyDistillationviaMixture.md
Saved: 2026-08-11 00:06
Source: 2026-08-10_11-22-53Z_WDL_OPD_Weak_DrivenOn_PolicyDistillationviaMixture.md
Model: None

---

## Summary  
On‑policy distillation (OPD) aims to align a student model with its own trajectories to eliminate the train‑test mismatch of offline methods. The authors propose **WDL‑OPD**, a mixture‑constrained co‑training framework that introduces two trainable policies: an anchor policy that generates rollouts and an auxiliary policy that evaluates visited states, while matching their token distributions to a frozen teacher via reverse KL. By jointly optimizing both policies under this constraint, WDL‑OPD stabilizes the feedback loop that typically causes OPD to degrade or explode. Experiments on Qwen3 models at 1.7B and 4B scales demonstrate that co‑training outperforms single‑policy OPD configurations.

## Key Contributions  
- [Finding 1] Freezing the auxiliary policy recovers an anchor‑plus‑contrast proxy target closely related to OPD² and W2S‑OPD, showing a stable baseline.  
- [Finding 2] Joint training of both policies introduces branch‑level degrees of freedom that a static delta cannot express, enabling richer alignment.  
- [Finding 3] In recorded Qwen3 experiments, WDL‑OPD produces the strongest student checkpoints across four scale‑domain settings and lifts MATH500 accuracy from 0.630 to 0.685 at 4B and from 0.521 to 0.585 at 1.7B, while seven single‑policy OPD setups suffer entropy growth or trajectory degradation.

## Methodology  
WDL‑OPD employs a mixture‑constrained co‑training scheme: the anchor policy produces a rollout of states and actions; the auxiliary policy receives the same visited state sequence as input and outputs token probabilities. A geometric mixture of these two token distributions is constrained to match the frozen teacher’s distribution using reverse KL divergence, and gradients are back‑propagated through both policies simultaneously. This dual‑policy optimization stabilizes the on‑policy feedback loop by preventing abrupt changes in the student’s trajectory representation.

## Results  
The best checkpoint obtained from WDL‑OPD is stronger than any single‑policy OPD configuration across all four scale domains, achieving MATH500 scores of 0.685 (4B) and 0.585 (1.7B). In contrast, seven single‑policy OPD setups exhibit entropy growth or trajectory degradation, with the best observed development scores being 0.637 and 0.375. These results indicate that co‑training yields a more robust alignment than static delta methods.

## Significance  
WDL‑OPD addresses a longstanding instability in on‑policy distillation by providing a principled, gradient‑driven mechanism that jointly updates both the policy generator and evaluator under a mixture constraint. This enables stronger student models without additional compute, offering a scalable path to higher reasoning performance in large language systems.

## Related Concepts  
- On‑Policy Distillation (OPD)  
- Mixture‑constrained co‑training  
- Reverse KL matching  
- Anchor and auxiliary policies  
- Delta regularization  
- Entropy growth / trajectory degradation
