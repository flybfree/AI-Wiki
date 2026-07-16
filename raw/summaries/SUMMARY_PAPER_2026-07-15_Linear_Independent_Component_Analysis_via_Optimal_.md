---
title: Linear Independent Component Analysis via Optimal Transport
url: http://arxiv.org/abs/2607.14081v1
type: paper-summary
date: 2026-07-15
source_paper: 2026-07-15_17-56-11Z_LinearIndependentComponentAnalysisviaOptimalTransp.md
generated_at: 2026-07-15 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OT-ICA, a method for linear independent component analysis that uses the squared Wasserstein distance to standard Gaussian as a non‑Gaussianity measure. It proves that maximizing this distance corresponds to recovering an independent source component and proposes gradient‑based optimization to find it. Experiments on simulated data show OT-ICA outperforms traditional proxy‑based ICA across various latent variable distributions, with successful applications in EEG artifact removal and econometric price discovery.

## Key Takeaways
- The squared Wasserstein distance between a standard normal distribution and linear projections of the data is maximized when the projection recovers an independent component. - OT-ICA replaces intractable negentropy optimization with this tractable metric, enabling gradient‑based search. - Empirical results demonstrate that OT-ICA outperforms proxy methods such as fourth‑order cumulants for diverse source distributions.

## Context
Linear ICA has long been a cornerstone of blind source separation, yet its reliance on non‑Gaussianity measures limits applicability to non‑Gaussian data. The shift toward Wasserstein distance reflects broader trends in AI toward robust, distribution‑agnostic metrics that align with optimal transport theory.

## Implications
This approach offers practitioners a flexible ICA tool that does not require Gaussian assumptions, improving performance across real‑world signals such as EEG and financial time series. By leveraging optimal transport, OT-ICA could become standard in data‑driven signal processing pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14081v1)
