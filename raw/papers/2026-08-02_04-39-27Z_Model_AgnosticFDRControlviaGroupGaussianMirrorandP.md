---
title: Model-Agnostic FDR Control via Group Gaussian Mirror and Permutation SHAP
published: 2026-08-02T04:39:27Z
authors: Jiaan Han, Junxiao Chen, Yanzhe Fu
url: http://arxiv.org/abs/2608.00989v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Model-Agnostic FDR Control via Group Gaussian Mirror and Permutation SHAP

## Abstract
Most FDR-controlled feature selection methods are designed for coordinate-wise hypotheses, where each feature has a single weight or importance score. This abstraction fails in sequential and grouped models, where one original feature is represented by a block of sub-features, such as lags, recurrent states, or attention-based interactions. We propose a grouped-feature FDR control framework for such settings. For grouped linear models, we construct null-symmetric block-level mirror statistics with matrix-valued perturbations. For neural sequential models, we combine Permutation SHAP derivatives as model-agnostic block-level importance scores with kernel-based dependence measure. The framework is model-agnostic across network architectures, does not require specifying the covariate distribution, and reduces to Gaussian Mirror or Neural Gaussian Mirror when the block size is one. We prove FDR control for low- and high-dimensional grouped linear models and asymptotic symmetry of smoothed Permutation SHAP derivatives under fixed fitted nonlinear models. Experiments on simulated and real-world datasets show reliable FDR control and improved power under correlated grouped-feature signals.

## Metadata
- **Published**: 2026-08-02T04:39:27Z
- **Authors**: Jiaan Han, Junxiao Chen, Yanzhe Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00989v1)