# Summary: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Saved: 2026-07-24 02:46
Source: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Model: None

---

## Summary
[This paper investigates why representation-level class unlearning succeeds or fails, focusing on gradient concentration rather than weight saliency. It introduces an ablation study that compares saliency‑based masking with random and unconstrained updates while controlling for other factors. The goal is to determine whether the observed representational forgetting is driven by gradient energy distribution or by which weights are selected. The contribution is evidence that forgetting is governed by gradient concentration and representation geometry.]

## Key Contributions
- [Finding 1: Gradient concentration accounts for ~92% of squared gradient energy in final layers, indicating that most forgetting occurs there regardless of mask type.]  
- [Finding 2: Saliency masks exhibit low class specificity (0.09–0.11), selecting overlapping parameter subsets across classes.]  
- [Finding 3: All three configurations—saliency, random, and unconstrained updates—yield statistically equivalent representation-level recoverability.]

## Methodology
[The authors conduct a matched‑compute experiment on CIFAR‑10 and CIFAR‑100 using ResNet‑18. They train models with the same objective, schedule, and computational budget, then apply three forgetting update strategies: (i) saliency‑based masking of weights with high gradient magnitude, (ii) random masks preserving sparsity, and (iii) unconstrained updates to all parameters. After each configuration they evaluate representation‑level metrics such as linear probing accuracy, prototype recovery, and layer‑wise CKA.]

## Results
[Across all three configurations the representation‑level recoverability is statistically indistinguishable; linear probing shows similar degradation, prototype recovery recovers at comparable rates, and CKA scores align across layers. Crucially, before any mask is applied gradient energy is concentrated in the last layers (≈92% of total squared gradient), suggesting that forgetting operates within a narrow representational subspace.]

## Significance
[These findings challenge the prevailing belief that saliency‑driven weight selection is essential for effective unlearning. By showing that gradient concentration and representation geometry dominate, the work supports the need for objectives that act directly on latent representations rather than on complex parameter masks.]

## Related Concepts
- Gradient concentration  
- Weight saliency  
- Representation‑level forgetting  
- Class unlearning  
- Latent space manipulation
