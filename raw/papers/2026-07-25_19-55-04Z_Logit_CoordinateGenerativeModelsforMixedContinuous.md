---
title: Logit-Coordinate Generative Models for Mixed Continuous-Categorical Tabular Data
published: 2026-07-25T19:55:04Z
authors: Yuefei Shen, Xiaotong Shen
url: http://arxiv.org/abs/2607.23348v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Logit-Coordinate Generative Models for Mixed Continuous-Categorical Tabular Data

## Abstract
Mixed continuous--categorical data pose a representation problem for continuous generative models. Flow Matching and Gaussian diffusion operate in Euclidean spaces, whereas categorical laws lie on probability simplices and may be highly imbalanced. We study a logit-coordinate framework that encodes categorical variables as smoothed natural parameters and combines them with transformed numerical variables. This yields common formulations of Logit Flow Matching and Logit Diffusion. We introduce a mixed-distribution discrepancy separating categorical marginal error from conditional continuous Wasserstein error, and derive stability bounds and imbalance-aware nonparametric rates linking vector-field or drift error to decoded mixed-distribution error. Controlled simulations show that scaled-logit coordinates improve or match one-hot coordinates, especially under severe rare-cell imbalance. Across four real-data benchmarks and ten splits per dataset, Logit FM improves the primary distributional metrics on three datasets and is comparable on Churn2; Block-Conditional Logit FM consistently improves the flat model; and Logit Diffusion generally improves over or matches One-Hot Diffusion.

## Metadata
- **Published**: 2026-07-25T19:55:04Z
- **Authors**: Yuefei Shen, Xiaotong Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23348v1)