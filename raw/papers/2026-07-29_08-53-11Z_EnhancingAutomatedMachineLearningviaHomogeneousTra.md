---
title: Enhancing Automated Machine Learning via Homogeneous Train-Test Splitting Methods
published: 2026-07-29T08:53:11Z
authors: Yearn Tan Yin Tze, Charles Grellois
url: http://arxiv.org/abs/2607.26625v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Automated Machine Learning via Homogeneous Train-Test Splitting Methods

## Abstract
Accurate model evaluation in machine learning depends critically on how datasets are split into training and testing subsets. Standard random splitting assumes that both partitions share the same underlying distribution, an assumption often violated in datasets with class imbalance, natural clustering, or spatial autocorrelation. This paper investigates the role of statistical similarity in train-test splitting and its consequences for AutoML model evaluation. Five established strategies are compared across fifteen UCI benchmark datasets: random splitting, stratified sampling, Kennard-Stone, Duplex, and SPXY. Similarity is assessed using chi-square, Kolmogorov-Smirnov, and Maximum Mean Discrepancy (MMD) tests. Geometry-based methods consistently produce near-zero MMD scores, introducing instability into downstream performance estimates. The proposed Optimised-Distribution method treats similarity as an explicit optimisation objective and achieves the highest mean MMD similarity, 89.0%, across all strategies evaluated.

## Metadata
- **Published**: 2026-07-29T08:53:11Z
- **Authors**: Yearn Tan Yin Tze, Charles Grellois
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26625v1)