# Summary: 2026-06-21_17-20-21Z_OnthePositionBiasofOn_PolicyDistillation.md
Saved: 2026-06-22 22:01
Source: 2026-06-21_17-20-21Z_OnthePositionBiasofOn_PolicyDistillation.md
Model: None

---


## Summary  
The paper investigates why on‑policy distillation (OPD) suffers from position bias, where later tokens provide poorer supervision and thus degrade learning efficiency. It proposes Importance‑Weighted On‑Policy Distillation (IW‑OPD), a principled weighting scheme that upweights early tokens with high discrepancy and downweights later ones. The contribution is both theoretical analysis via constrained optimization and an empirical improvement in convergence speed, performance, and final scores on benchmark tasks.  

## Key Contributions  
- Finding 1: Token‑level losses are not uniformly effective; teacher supervision quality declines as rollout length increases.  
- Finding 2: Using only the first 30% of tokens yields performance comparable to full token use, while using only the last 30% is ineffective.  
- Finding 3: A constrained‑optimization framework reveals that token importance follows accumulated distribution discrepancy, justifying upweighting early tokens.  

## Methodology  
The authors model OPD as a constrained optimization problem where the loss vector must satisfy KL divergence constraints. They introduce weights wᵢ proportional to the cumulative Kullback‑Leibler distance between student and teacher distributions up to position i, forming IW‑OPD. This weighting is computed online during rollout, ensuring that tokens with larger deviations receive higher influence.  

## Results  
Experiments on AIME‑2025 and cross‑scale settings show that IW‑OPD converges 1.8× faster than standard OPD, achieves up to 6.9 additional points on AIME‑2025, and outperforms both same‑size and larger teacher models. The improvement persists across diverse rollout lengths.  

## Significance  
By exposing the hidden position bias in OPD, the work provides a theoretical justification for adaptive token weighting, enabling more efficient RL training without sacrificing performance. This insight can be applied to any dense supervision setting where later observations degrade quality.  

## Related Concepts  
- On‑Policy Distillation (OPD)  
- KL divergence regularization  
- Constrained optimization in reinforcement learning  
- Importance‑weighted sampling  
- Token‑level loss aggregation
