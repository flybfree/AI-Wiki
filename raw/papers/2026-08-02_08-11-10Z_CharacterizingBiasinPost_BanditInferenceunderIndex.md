---
title: Characterizing Bias in Post-Bandit Inference under Index Algorithms
published: 2026-08-02T08:11:10Z
authors: Lisu Wang, Yilun Chen, Jiaqi Lu
url: http://arxiv.org/abs/2608.01069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Characterizing Bias in Post-Bandit Inference under Index Algorithms

## Abstract
Bandit algorithms generate data for downstream inference, but adaptive sampling biases post-bandit sample means. We analyze this bias for stable index algorithms, including UCB1 and its generalizations, and derive sharp leading-order expressions for the sample-mean bias and expected $Z$-statistic. Our characterization reveals the algorithmic origin of bias through a key index-function-dependent quantity, which we term effective exploration rate. For example, under UCB1, the effective exploration rate is of order $\sqrt{\log T}$, and the standardized bias of any arm (that is not uniquely optimal) decays at the extremely slow rate $1/\sqrt{\log T}$. We also show how the choice of the index function affects both regret and bias, which reveals a regret-bias trade-off: more exploratory algorithm reduces bias but increases regret. Our sharp characterization for bias uses a novel empirical fluid approximation of the algorithm's sampling dynamics, which may be of independent interest.

## Metadata
- **Published**: 2026-08-02T08:11:10Z
- **Authors**: Lisu Wang, Yilun Chen, Jiaqi Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01069v1)