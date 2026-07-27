---
title: Scaling Laws for Classical Machine Learning on Tabular Data: A Benchmark Study
url: http://arxiv.org/abs/2607.21866v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_23-45-09Z_ScalingLawsforClassicalMachineLearningonTabularDat.md
generated_at: 2026-07-26 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper studies how classical machine learning models on tabular data scale with dataset size and replicates the work across many students and datasets to fit power-law error curves. It finds that tree ensembles dominate at full data while linear models underperform classification, that exponents are roughly shared across model families, and that implementation variance is high due to unconstrained protocol steps.

## Key Takeaways
- Power laws fit with R^2 > 0.8 on 77.7% of cells, showing tree ensembles dominate at full data while linear models underperform classification.
- Approximate shared exponents within a model family: five out of six families have a single exponent that predicts cross-dataset curves as well as per-dataset exponents (R^2 gap <0.011), though AIC prefers unconstrained fit and curve collapse is partial with 32‑58% points within ±0.5 dex.
- Replicator-implementation variance: independent re-implementations differ by mean CV(b)=0.144 on the fitted exponent, indicating spread from preprocessing, encoding, missing-value handling.

## Context
Classical ML learning curves have been studied mainly in small labs with limited data and a single model per experiment, limiting insights into how models generalize across diverse datasets. This study expands that view by scaling up to classroom‑level replication, revealing systematic patterns that were previously invisible at the small scale.

## Implications
For practitioners, the findings suggest that tree ensembles are more reliable for large tabular problems while linear methods need careful tuning or alternative approaches. The observed exponent sharing hints that model families may share underlying scaling behavior, which could inform hyperparameter design and data‑requirement tables. High implementation variance underscores the importance of standardizing preprocessing pipelines to ensure reproducible results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21866v1)
