# Summary: 2026-08-10_11-22-53Z_WDL_OPD_Weak_DrivenOn_PolicyDistillationviaMixture.md
Saved: 2026-08-10 23:46
Source: 2026-08-10_11-22-53Z_WDL_OPD_Weak_DrivenOn_PolicyDistillationviaMixture.md
Model: None

---

## Summary  
The paper proposes WDL‑OPD, a mixture‑constrained co‑training method that stabilizes on‑policy distillation by jointly training an anchor policy and an auxiliary evaluator while matching their token distributions to a frozen teacher via reverse KL. It addresses the instability of standard OPD where each update alters both the policy and the states on which the next update is computed. By freezing the auxiliary in one regime, WDL‑OPD recovers known methods such as anchor‑plus‑contrast proxy targets; joint training introduces branch‑level degrees of freedom that static delta functions cannot express. The method achieves state‑of‑the‑art performance on MATH500 and code generation benchmarks across 1.7B and 4B model sizes.

## Key Contributions  
- [Finding 1] WDL‑OPD introduces a mixture‑constrained co‑training framework with two trainable policies that stabilizes on‑policy distillation.  
- [Finding 2] Freezing the auxiliary recovers anchor‑plus‑contrast proxy targets closely related to OPD² and W2S‑OPD, while joint training provides branch‑level degrees of freedom beyond static delta functions.  
- [Finding 3] Experiments show WDL‑OPD outperforms seven single‑policy OPD configurations on both MATH500 (4B: 0.685 vs 0.630) and code generation (dev scores 0.637 vs 0.375).

## Methodology  
The authors adopt a co‑training setup where an anchor policy generates rollouts, an auxiliary policy evaluates the same visited states, and a geometric mixture of their token distributions is constrained to match a frozen teacher via reverse KL divergence; both policies receive gradient updates from this constraint.

## Results  
In recorded Qwen3 experiments at 1.7B and 4B scale, WDL‑OPD produced the strongest student checkpoint across four scale‑domain settings, raising MATH500 accuracy by 0.055 (from 0.630 to 0.685) and code generation dev scores from 0.375 to 0.637.

## Significance  
This work demonstrates that stabilizing on‑policy distillation through mixture constraints not only improves performance but also introduces a more expressive training regime than static delta functions, offering a scalable path for high‑capacity language models.

## Related Concepts  
- On‑policy distillation (OPD)  
- Contrast proxy target  
- W2S‑OPD  
- Reverse KL matching  
- Mixture‑constrained co‑training
