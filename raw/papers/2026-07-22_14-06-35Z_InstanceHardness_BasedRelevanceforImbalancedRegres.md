---
title: Instance Hardness-Based Relevance for Imbalanced Regression
published: 2026-07-22T14:06:35Z
authors: Vitor M. Leitao, Juscimara G. Avelino, George D. C. Cavalcanti, Rafael M. O. Cruz
url: http://arxiv.org/abs/2607.20173v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instance Hardness-Based Relevance for Imbalanced Regression

## Abstract
Imbalanced regression problems arise when the target variable has an asymmetric distribution, resulting in underrepresented value ranges in the dataset. Traditional approaches for identifying rare instances rely on a relevance function that assigns higher importance to specific regions of the target distribution. However, the effectiveness of imbalance-aware learning methods depends strongly on how relevance is defined. In more complex scenarios, such as bimodal distributions, traditional relevance functions struggle to capture rarity, as they assign fixed relevance values based solely on target values, thereby compromising the distinction between truly rare and normal instances. To address these limitations, this study proposes an Instance Hardness-based relevance function (InHaR) for identifying rare instances in regression problems. Unlike traditional relevance functions, the proposed approach incorporates learning difficulty, allowing rarity to be inferred not only from the target distribution but also from the difficulty of instances for the learning algorithm. This property is particularly important in bimodal scenarios, where rarity cannot be accurately inferred from target values alone. Experimental results demonstrate that the InHaR correctly identifies rare regions under bimodal distributions and, when used to guide resampling strategies such as Random Oversampling (RO) and Gaussian Noise (GN), leads to significant improvements in predictive performance compared to traditional relevance-based approaches. The code, dataset, and further details about the proposed method are publicly available at https://github.com/VitorLeitao/instance-hardness-Imbalanced-regression.

## Metadata
- **Published**: 2026-07-22T14:06:35Z
- **Authors**: Vitor M. Leitao, Juscimara G. Avelino, George D. C. Cavalcanti, Rafael M. O. Cruz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20173v2)