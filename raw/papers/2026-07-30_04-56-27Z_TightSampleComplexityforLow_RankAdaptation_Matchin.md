---
title: Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection
published: 2026-07-30T04:56:27Z
authors: Arunan J
url: http://arxiv.org/abs/2607.27680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection

## Abstract
Low-Rank Adaptation (LoRA) has become the standard mechanism for fine-tuning large pretrained models, yet its statistical properties remain only partially understood. Existing generalization results provide upper bounds of the form O~(sqrt(rd/n)) or O~(rd/n), but a matching lower bound is missing, and the question of how to choose the LoRA rank r has no formal answer. Both gaps are closed here. A local Rademacher argument establishes an upper bound of O~(rd/n) on the excess risk of the empirical risk minimizer over rank-r LoRA, whenever the target adaptation has rank at most r. A matching minimax lower bound of Omega(rd/n) is then proved via a Fano-type packing of the rank-r subspace of R^{d x d}; the bound applies to any estimator whose output lies in the rank-r LoRA class. Combining the two yields a rank-selection dichotomy. For the constrained empirical risk minimizer, the optimal rank equals the intrinsic rank r*, and over-ranking strictly hurts. For adaptive estimators of the nuclear-norm-then-truncate type, over-ranking is harmless and the rate saturates at Theta~(r* d / n) regardless of r. Taken together, the three results characterize the statistical complexity of LoRA fine-tuning within the well-specified locally quadratic regime, and identify the empirically observed over-parameterization penalty as a property of unregularized empirical risk minimization rather than of the LoRA class itself. Predictions of the theory are verified on a synthetic trace-regression benchmark and on real LoRA fine-tuning across three (model, task) configurations covering DistilBERT and RoBERTa on SST-2 and MRPC. All configurations exhibit the predicted U-shape in validation loss, with two showing statistically significant loss inflation at large ranks (paired permutation p = 0.016).

## Metadata
- **Published**: 2026-07-30T04:56:27Z
- **Authors**: Arunan J
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27680v1)