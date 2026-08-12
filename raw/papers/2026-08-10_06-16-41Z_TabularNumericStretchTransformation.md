---
title: Tabular Numeric Stretch Transformation
published: 2026-08-10T06:16:41Z
authors: Zihao Ye, Juyong Kim, Johnna Sundberg, Burak Varici, Pradeep Ravikumar
url: http://arxiv.org/abs/2608.09162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tabular Numeric Stretch Transformation

## Abstract
Tabular data presents unique challenges for deep learning due to its heterogeneous nature, where numeric features exhibit diverse distributions, scales, and statistical properties. Although recent advances have improved how models learn from tabular data, how numeric data are transformed into model-friendly representations remains comparatively underexplored. We introduce the stretch transformation framework, which formulates numeric feature preprocessing as an optimization problem to make the target function smoother and thus more learnable. Our framework has two variants: (1) unsupervised stretch, which uniformly redistributes feature density via minimax optimization, and (2) supervised stretch, which optimizes target-aware numeric feature transformations from the perspective of target-function smoothness by minimizing the target function's Dirichlet energy in the transformed space. Our theoretical analysis further connects this framework to several popular transformations: unsupervised stretch is closely related to Piecewise Linear Encoding through a shared piecewise-linear geometry and approaches the empirical CDF transformation as the number of bins grows, while supervised stretch becomes closely related to target encoding in the fine-binning limit. Comprehensive experiments on 38 datasets from the TALENT benchmark demonstrate that supervised stretch consistently outperforms all baselines. These results show that explicitly optimizing for target function smoothness is a powerful and underexplored strategy for tabular deep learning.

## Metadata
- **Published**: 2026-08-10T06:16:41Z
- **Authors**: Zihao Ye, Juyong Kim, Johnna Sundberg, Burak Varici, Pradeep Ravikumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09162v1)