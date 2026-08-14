---
title: Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization
published: 2026-08-13T16:44:08Z
authors: Jiayi Dan, Bo Li, Lu Deng, Yong Wang
url: http://arxiv.org/abs/2608.13461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization

## Abstract
Post-click conversion rate (CVR) is a key metric in various scenarios including e-commerce and advertising, reflecting the efficiency and user experience in the second stage of the conversion process. Estimating the causal effect on CVR is therefore of great practical importance. However, directly applying existing causal inference methods to clicked samples introduces sample selection bias and increased variance due to the exclusion of non-click data. Recent studies on CVR prediction introduce "ideal loss", which optimizes model parameters using an unbiased estimate of the loss over the full sample. Nevertheless, there is no guarantee that unbiasedness of the loss implies unbiasedness of the final estimator.   We revisit this challenge from the perspective of semiparametric theory. Specifically, we develop a new doubly robust causal effect estimator for chain-structured outcomes such as CVR, and derive its theoretical properties in detail. It achieves a faster convergence rate compared to nuisance parameters estimation and is therefore more robust when using flexible nonparametric estimators, including neural networks. Based on these theoretical findings, we further design a framework based on targeted regularization to improve numerical stability and practical applicability.   Extensive experiments on synthetic and real-world data demonstrate the effectiveness and robustness of our method. In addition, we find that naively combining loss debiasing with standard causal estimators underperforms our method, highlighting the necessity of developing the new estimator tailored to this CVR-style objective with solid theoretical guarantees.

## Metadata
- **Published**: 2026-08-13T16:44:08Z
- **Authors**: Jiayi Dan, Bo Li, Lu Deng, Yong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13461v1)