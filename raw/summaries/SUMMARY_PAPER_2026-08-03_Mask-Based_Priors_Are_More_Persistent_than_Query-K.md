---
title: Mask-Based Priors Are More Persistent than Query-Key Initializations
url: http://arxiv.org/abs/2608.00418v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_03-39-57Z_Mask_BasedPriorsAreMorePersistentthanQuery_KeyInit.md
generated_at: 2026-08-03 23:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why Transformers fail on Boolean extrapolation tasks and proposes a simple fix: initializing an additive attention mask that encodes the task’s interaction structure. The authors show that such mask‑based priors remain stable during training, whereas query‑key initializations are overwritten, leading to near‑perfect performance compared with vanilla models.

## Key Takeaways
- Mask‑based initialization directly injects a finite, learnable attention‑logit bias from the task’s interaction structure, separating structural constraints from content‑dependent scores.  
- Unlike QK‑based priors that can be quickly overwritten by optimization, mask biases persist throughout training and prevent the default minimum‑degree interpolation bias.  
- The approach yields near‑perfect extrapolation on Boolean reasoning tasks while also boosting low‑data arithmetic performance and remaining competitive on vision and language benchmarks.

## Context
Understanding Transformer inductive bias is crucial because current models generalize in systematic, undesirable ways that hinder reliable generalization. Prior work has explored structured initialization to steer attention patterns, but most methods rely on query‑key projections that are sensitive to training dynamics. This study introduces a more robust alternative that leverages the model’s own attention mechanism.

## Implications
Practitioners can adopt mask‑based priors as a lightweight way to enforce task‑specific inductive bias without complex architectural changes. The method offers a clear path toward more reliable generalization across diverse domains, potentially improving performance in low‑resource settings and reducing reliance on large training data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00418v1)
