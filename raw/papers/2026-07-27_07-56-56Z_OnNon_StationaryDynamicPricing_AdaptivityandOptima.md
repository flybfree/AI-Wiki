---
title: On Non-Stationary Dynamic Pricing: Adaptivity and Optimality
published: 2026-07-27T07:56:56Z
authors: Feiyu Jiang, Zifeng Zhao
url: http://arxiv.org/abs/2607.24115v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Non-Stationary Dynamic Pricing: Adaptivity and Optimality

## Abstract
We study the contextual dynamic pricing problem under non-stationarity, where a firm sells products to $T$ sequentially arriving consumers that behave according to an unknown demand model that can change over time. The demand model is assumed to be a generalized linear model (GLM), allowing for a feature vector in $\mathbb{R}^d$ that encodes products and consumer information. To achieve optimal revenue (i.e., least regret), the firm needs to learn and exploit the unknown GLMs while monitoring for potential changes. We propose a multiscale change-point detection based algorithm that achieves a regret of order $\widetilde{O}(\sqrt{s_TdT}\wedge\{V_T^{1/3}d^{1/3}T^{2/3}+\sqrt{dT}\})$, where $s_T$ is the number of piecewise stationary segments and $V_T$ is a newly defined notion of design-adjusted variation budget of model parameters. Our algorithm is adaptive and does not require knowing $s_T$ or $V_T$. Moreover, to our knowledge, this is the first dynamic pricing algorithm that is adaptive to the nature of changes and achieves the best-of-both-worlds rate, thus closing a long-standing gap in the literature. We remark that, due to the varying contexts, existing works in the adaptive non-stationary bandit literature cannot be applied to achieve optimality for contextual dynamic pricing. The regret is further accompanied with a newly constructed minimax lower bound, confirming the optimality of our algorithm (up to logarithmic factors). Extensive numerical experiments are conducted to illustrate the efficiency and robustness of the proposed algorithm in non-stationary dynamic pricing.

## Metadata
- **Published**: 2026-07-27T07:56:56Z
- **Authors**: Feiyu Jiang, Zifeng Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24115v1)