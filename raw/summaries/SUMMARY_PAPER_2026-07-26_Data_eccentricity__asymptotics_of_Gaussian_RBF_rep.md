---
title: Data eccentricity, asymptotics of Gaussian RBF reproducing kernel Hilbert space, and kernel PCA
url: http://arxiv.org/abs/2607.21823v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_21-18-41Z_Dataeccentricity_asymptoticsofGaussianRBFreproduci.md
generated_at: 2026-07-26 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the asymptotic properties of Gaussian RBF reproducing kernel Hilbert space and its relationship to Euclidean space as bandwidth grows large. It demonstrates that kernel PCA with Gaussian RBF converges to classical linear PCA under isotropic scaling. The analysis also introduces a geometric eccentricity measure ρ linking convergence speed to data spread.

## Key Takeaways
- Up to isotropic scaling, the Gaussian RBF RKHS becomes isometric to Euclidean space in the large bandwidth limit.
- Kernel PCA eigenvalues and eigenprojections converge to those of linear PCA as σ approaches infinity with error O((ρσ)^2).
- The ratio ρ of maximum to median pairwise distance predicts dataset-specific convergence behavior.

## Context
This work bridges kernel theory and statistical learning, showing that many kernel-based methods behave like their non‑kernel counterparts when the bandwidth is large. It provides a theoretical justification for using linear PCA as an approximation in high‑bandwidth regimes.

## Implications
For practitioners, this means that increasing bandwidth can be safely replaced by standard linear techniques without loss of performance. The eccentricity measure offers a practical diagnostic to decide when kernel methods are unnecessary, streamlining model selection and computation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21823v1)
