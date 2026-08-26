---
title: qshap: Fast Shapley Decomposition of $R^2$ for Gradient-Boosted Trees
published: 2026-08-25T06:06:16Z
authors: Zhongli Jiang, Min Zhang, Dabao Zhang
url: http://arxiv.org/abs/2608.24104v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# qshap: Fast Shapley Decomposition of $R^2$ for Gradient-Boosted Trees

## Abstract
Numerous methods have been developed to quantify feature attributions in individual predictions for tree ensembles. However, many applications require global measures of feature contributions to overall model performance. Although local attribution scores can be aggregated to characterize feature importance, such summaries do not directly decompose measures of predictive performance, such as $R^2$. This article introduces qshap, available in both R and Python, which provides Shapley decomposition of $R^2$ values for gradient-boosted decision trees (GBDTs) to quantify feature-specific contributions to model performance. By decomposing the quadratic loss of individual observations, qshap provides flexible tools to explore the importance of individual features and observations. qshap currently supports widely used GBDT implementations, including xgboost, lightgbm, and catboost, through a unified tree representation and efficient C++ backends. Its modular design can accommodate other GBDT implementations built from binary decision trees. In addition, we introduce a specialized backend for oblivious trees that exploits their symmetric structure to substantially accelerate computation.

## Metadata
- **Published**: 2026-08-25T06:06:16Z
- **Authors**: Zhongli Jiang, Min Zhang, Dabao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24104v1)