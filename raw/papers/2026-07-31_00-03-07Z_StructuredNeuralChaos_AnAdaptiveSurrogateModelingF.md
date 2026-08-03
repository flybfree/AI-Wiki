---
title: Structured Neural Chaos: An Adaptive Surrogate Modeling Framework for Functional Uncertainty Quantification and Global Sensitivity Analysis
published: 2026-07-31T00:03:07Z
authors: Isabel Corona Guevara, Yeping Hu
url: http://arxiv.org/abs/2607.28903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structured Neural Chaos: An Adaptive Surrogate Modeling Framework for Functional Uncertainty Quantification and Global Sensitivity Analysis

## Abstract
Variance-based global sensitivity analysis (GSA) plays a key role in uncertainty quantification by identifying the contributions of uncertain inputs to the variability of the model response. The repeated model evaluations required for these tasks are often prohibitively expensive; surrogate models provide an efficient alternative by constructing inexpensive approximations of the underlying system response. Constructing surrogate models that combine scalability and interpretability for systems with high-dimensional stochastic inputs and functional responses remains challenging, particularly when sensitivity estimates are required across spatial or temporal domains. Polynomial chaos expansion (PCE) provides an effective framework for uncertainty propagation and sensitivity analysis due to its orthogonal structure and direct relationship with variance-based sensitivity measures. However, PCE suffers from the curse of dimensionality, whose computational burden is amplified for problems with functional responses. In this work, we introduce the Structured Neural Chaos (sNC) expansion as a surrogate modeling framework for variance-based GSA, inspired by the interpretability and orthogonal structure of PCE. The proposed framework retains the interpretability of structured decompositions while leveraging the expressive power of neural networks. The sNC expansion mirrors a truncated functional ANOVA decomposition, where each interaction component admits a separable low-rank approximation whose basis functions and coefficients are parameterized by neural networks. The expansion is constructed sequentially, adaptively identifying the dominant modes within each ANOVA subspace and determining the effective complexity of the representation. The resulting structure enables the extraction of statistical and sensitivity quantities directly from the coefficients of the sNC expansion at negligible cost.

## Metadata
- **Published**: 2026-07-31T00:03:07Z
- **Authors**: Isabel Corona Guevara, Yeping Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28903v1)