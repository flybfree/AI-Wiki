---
title: The Zero Pattern of a Design Matrix Drives Multiple Descent in Over-parameterized Regression
url: http://arxiv.org/abs/2607.24041v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_06-30-49Z_TheZeroPatternofaDesignMatrixDrivesMultipleDescent.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the risk of multiple descent in over‑parameterized linear regression when covariance matrices are degenerate or dependent, which previous studies ignore. It derives deterministic equivalents for prediction risk in a vanishing‑ridge regime and shows that such degeneracy can cause multiple minima. The analysis uses a graph representation of variance profiles to locate singular configurations.

## Key Takeaways
- Degenerate covariance matrices create variance spikes that correspond to multiple descent paths, allowing the optimizer to converge to several local minima simultaneously.
- Dependence among covariates amplifies these spikes, making the risk surface non‑convex and unpredictable.
- Maximum matchings in a bipartite graph derived from the variance profile identify exactly where singularities occur.

## Context
Over‑parameterized models are common in modern machine learning, but standard analyses assume independent features with full covariance matrices. When those assumptions break down, existing risk bounds fail to capture the true behavior of the loss surface, limiting reliable model selection and generalization guarantees.

## Implications
Practitioners must monitor feature correlations and matrix rank as they increase model capacity, because hidden singularities can cause training instability and poor performance. This insight guides regularization strategies that explicitly address covariance degeneracy in high‑dimensional settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24041v1)
