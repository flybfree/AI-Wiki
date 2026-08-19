---
title: Feature Priming in Online Linear Regression: Sparse-Regret Lower Bounds and a Tight Univariate Rate
url: http://arxiv.org/abs/2608.17573v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_09-32-03Z_FeaturePriminginOnlineLinearRegression_Sparse_Regr.md
generated_at: 2026-08-18 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates feature priming in online linear regression, showing that the best predictor often relies on a few features and thus regret should depend on sparsity rather than dimension. The authors prove negative results for three common priming rules against a zero‑loss one‑sparse comparator and identify cheap nuisance interpolation as the obstacle.

## Key Takeaways
- Cheap nuisance interpolation causes refits to underweight truly predictive coordinates, leading to clipped prediction loss.
- Hadamard constructions force Ω(min{T,√d}) regret for all three rules against a zero‑loss one‑sparse comparator, even with fixed prime powers and selectors.
- Regret is controlled by data rank; Euclidean‑normalized triangular constructions match this dependence under powered univariate priming.

## Context
Feature priming seeks to improve online learning efficiency in high‑dimensional settings where only a few features matter. Understanding the trade‑off between sparsity and regret helps design algorithms that adapt quickly without overfitting noise, a key concern for scalable AI systems.

## Implications
For practitioners, this work clarifies when feature priming can be effective and warns against relying on cheap interpolation tricks that degrade performance. It guides algorithm designers to prioritize data rank and use constructions that respect sparsity, ensuring robust online learning in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17573v1)
