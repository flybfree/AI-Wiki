---
title: GLOBE: Trajectory-Aligned Gradient Matching with Structured SparseOptimization for Coreset Selection
url: http://arxiv.org/abs/2608.02690v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_09-01-29Z_GLOBE_Trajectory_AlignedGradientMatchingwithStruct.md
generated_at: 2026-08-05 01:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GLOBE, a coreset selection method that aligns gradient trajectories across training checkpoints to improve on‑device deep learning. By jointly matching first‑order and second‑order moments of these trajectories, GLOBE selects a compact subset while preserving the full dataset’s optimization behavior.

## Key Takeaways
- GLOBE treats coreset selection as a globally optimized sparse weighting problem using gradient trajectories rather than single‑snapshot gradients.  
- The multi‑order matching objective aligns both mean and projected uncentered second‑order moments, capturing evolving dynamics and reducing correlation bias.  
- Structured sparsity is enforced through Group LASSO, Elastic Net regularization, and nonnegative budget constraints to stabilize weights of correlated samples.

## Context
On‑device AI training faces severe computational limits, making efficient coreset selection essential for practical deep learning. Existing approaches often ignore the temporal evolution of gradients, leading to suboptimal sampling that degrades model performance.

## Implications
GLOBE’s trajectory‑aligned framework enables higher test accuracy with far fewer samples, supporting scalable AI deployment in resource‑constrained environments. Practitioners can adopt this method to achieve data‑efficient training without sacrificing quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02690v1)
