# Summary: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Saved: 2026-07-24 03:02
Source: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Model: None

---

## Summary  
This paper investigates why representation‑level class unlearning works, focusing on gradient concentration rather than weight saliency. It conducts controlled experiments to show that forgetting is driven by the distribution of squared gradient energy across layers and the geometry of representations, not by which specific weights are masked. The authors demonstrate that all masking strategies produce equivalent results because they operate within the same representational subspace.

## Key Contributions  
- Finding 1: Forget gradients concentrate in final network layers (≈92 % of squared gradient energy), indicating that representation‑level forgetting is governed by gradient concentration.  
- Finding 2: Saliency masks have limited class specificity (0.09–0.11) and select overlapping parameter subsets across forget classes, showing low discriminative power.  
- Finding 3: All three configurations—saliency‑based masking, random masks of equal sparsity, and unconstrained updates—yield statistically equivalent representation‑level recoverability.

## Methodology  
The authors used a matched‑compute experimental design on CIFAR‑10 and CIFAR‑100 with ResNet‑18. They trained models to forget specific classes while keeping the same optimization schedule, computational budget, and unlearning objective. The three configurations compared were: (i) SalUn’s saliency‑based mask, (ii) a random mask of identical sparsity, and (iii) an unrestricted update that applies the full gradient. They evaluated representation‑level performance via linear probing, prototype recovery, and layer‑wise CKA.

## Results  
Across all three configurations, the models exhibited comparable representational recoverability: linear probing accuracy was within 2 % of each other, prototype recovery error differed by less than 1 %, and CKA scores were statistically indistinguishable (p > 0.05). The key observation is that before any mask, ~92 % of the squared gradient energy resides in the last layers, so masking does not change which representational subspace is altered.

## Significance  
These results challenge the prevailing belief that saliency‑based weight selection is essential for representation‑level unlearning. By showing that forgetting can be achieved through any mask that respects sparsity, the study suggests that future methods should focus on directly acting on latent representations rather than on complex weight‑selection heuristics.

## Related Concepts  
- Gradient concentration: distribution of gradient magnitude across layers.  
- Representation‑level class unlearning: removal of a class’s influence without degrading overall performance.  
- Saliency masking: selecting weights with high absolute gradients to forget them.  
- Latent representation: the subspace of features that encode class information.
