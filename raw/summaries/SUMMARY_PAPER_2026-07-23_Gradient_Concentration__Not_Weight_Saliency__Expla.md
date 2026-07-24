---
title: Gradient Concentration, Not Weight Saliency, Explains Representation-Level Class Unlearning
url: http://arxiv.org/abs/2607.21353v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_14-17-51Z_GradientConcentration_NotWeightSaliency_ExplainsRe.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the saliency‑based weight selection used in SalUn is essential for representation‑level unlearning or if gradient concentration alone drives forgetting. By conducting a controlled ablation on CIFAR‑10 and CIFAR‑100 with ResNet‑18, the authors compare saliency masks to random masks of equal sparsity and to unrestricted updates while keeping all other conditions constant.

## Key Takeaways
- Forget gradients are highly concentrated in the final network layers, accounting for about 92 % of squared gradient energy on CIFAR‑10 before any mask is applied.  
- Saliency masks exhibit limited class specificity (specificity index 0.09–0.11), selecting overlapping parameter subsets across different forget classes.  
- All three configurations—saliency masking, random masking, and unconstrained updates—produce statistically equivalent representation‑level recoverability in linear probing, prototype recovery, and layer‑wise CKA.

## Context
Machine unlearning aims to erase the influence of specific training data while preserving model performance. Traditional approaches rely on saliency‑based weight selection, yet it is unclear whether this mechanism contributes meaningfully beyond simple gradient concentration.

## Implications
The results suggest that representation‑level forgetting can be achieved with simpler objectives acting directly on latent representations rather than complex weight‑selection strategies. Practitioners may focus on designing unlearning tasks that target representation geometry instead of optimizing saliency masks, potentially reducing computational overhead and improving robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21353v1)
