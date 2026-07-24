# Summary: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Saved: 2026-07-24 02:57
Source: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
Model: None

---

## Summary  
The paper investigates why representation‑level class unlearning works or fails in neural networks and shows that gradient concentration, not weight saliency, drives forgetting. By ablating the saliency masking mechanism used by SalUn and comparing it to random masks of equal sparsity and unconstrained updates, the authors find that all three configurations affect the same representational subspace. This suggests that effective unlearning should target latent representations directly rather than relying on intricate weight‑selection strategies.

## Key Contributions  
- Finding 1: Forget gradients are strongly concentrated in the final network layers (≈ 92 % of squared gradient energy on CIFAR‑10) before any mask is applied.  
- Finding 2: Saliency masks exhibit limited class specificity, with a specificity index ranging from 0.09 to 0.11, selecting highly overlapping parameter subsets across different forget classes.  
- Finding 3: Representation‑level recoverability (linear probing, prototype recovery, layer‑wise CKA) is statistically equivalent among saliency masking, random masks, and unconstrained updates.

## Methodology  
The authors employ a matched‑compute experimental design on CIFAR‑10 and CIFAR‑100 using ResNet‑18. They train the model on a single class, then apply three forgetting update regimes: (i) SalUn’s saliency‑based masking, (ii) random masks of equal sparsity, and (iii) unconstrained updates. The unlearning objective, optimization schedule, and computational budget are held constant across all configurations to isolate the effect of mask type.

## Results  
All three configurations exhibit statistically indistinguishable representation‑level recoverability measured by linear probing, prototype recovery, and layer‑wise CKA. Gradient energy analysis confirms that ~92 % of the squared gradient norm resides in the last layers regardless of whether a mask is used. Saliency masks capture only 0.09–0.11 proportion of class‑specific gradients, indicating low specificity.

## Significance  
The study decouples representation forgetting from weight‑selection complexity, implying that effective unlearning should operate on latent space rather than on elaborate saliency heuristics. This aligns with prior work suggesting direct manipulation of representations yields more robust and interpretable forgetting mechanisms.

## Related Concepts  
- Gradient concentration  
- Weight saliency / importance maps  
- Representation‑level class unlearning  
- Linear probing, prototype recovery, CKA (Cross‑Kernel Alignment)  
- Matched‑compute experimental design
