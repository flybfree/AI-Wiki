---
title: Minimax Lower Bounds of Kernel Discrepancy Estimation: MMD, HSIC, KSD
url: http://arxiv.org/abs/2607.24235v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_10-13-26Z_MinimaxLowerBoundsofKernelDiscrepancyEstimation_MM.md
generated_at: 2026-07-27 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the minimax lower bound for estimating kernel discrepancies such as MMD, HSIC and KSD on general topological spaces with mild assumptions. It shows that these estimators cannot achieve a faster than n^{-1/2} rate, matching known optimal rates in finite dimensions. The results also extend to mean embedding and centered cross-covariance operator.

## Key Takeaways
- The minimax lower bound for MMD, HSIC and KSD estimation is n^{-1/2} on any topological space under mild kernel conditions.
- This rate is optimal even when kernels are unbounded, extending optimality beyond Euclidean spaces with bounded kernels.
- The same lower bound applies to mean embedding and centered cross-covariance operator as corollaries.

## Context
Kernel discrepancy estimation remains a cornerstone of statistical inference in machine learning and data science. Understanding its fundamental limits guides algorithm design and interpretation of results.

## Implications
For practitioners, these bounds inform expectations about sample complexity for fairness testing and model comparison. Researchers can focus on achieving the optimal n^{-1/2} rate rather than pursuing suboptimal faster methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24235v1)
