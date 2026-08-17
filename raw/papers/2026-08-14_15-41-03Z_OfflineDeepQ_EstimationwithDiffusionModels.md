---
title: Offline Deep Q* Estimation with Diffusion Models
published: 2026-08-14T15:41:03Z
authors: Xiaohong Chen, Yuling Jiao, Lican Kang, Jerry Zhijian Yang, Chen Zhong
url: http://arxiv.org/abs/2608.14401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Offline Deep Q* Estimation with Diffusion Models

## Abstract
In offline RL, estimating the optimal action-value function $Q^*$ can be formulated as solving the optimal Bellman equation based solely on offline observations. A fundamental challenge is that the reward function and transition kernel are unknown, so the optimal Bellman operator is not directly observable from data. To address this issue, we propose a novel framework that decouples operator estimation from value function learning. In this approach, we first formulate conditional diffusion models to estimate the reward law and transition kernel, which induces a data-driven approximation of the optimal Bellman operator. We then plug these estimators into the Bellman equation and obtain a deep estimator of $Q^*$ by minimizing the empirical Bellman residual over a neural network function class. Theoretically, we first establish sharp nonasymptotic convergence rates for learning the optimal Bellman operator through an end-to-end analysis of conditional diffusion estimation in total variation distance. We then establish the oracle value-stage rate $\widetilde{\mathcal O}\bigl(n^{-\frac{2β}{d_x+d_a+2β}}\bigr)$ for the excess Bellman residual risk. Finally, under a concentrability condition, we translate this residual bound into an $L^2$ convergence rate of $\widetilde{\mathcal O}\bigl(n^{-\fracβ{d_x+d_a+2β}}\bigr)$ for the resulting deep estimator of $Q^*$, where $d_x$ and $d_a$ denote the dimensions of the state and action spaces, respectively, and $β$ denotes the Hölder smoothness index of $Q^*$. Importantly, our theoretical analysis does not rely on completeness assumptions commonly used in deep RL theory. Extensive numerical experiments demonstrate the effectiveness of the proposed method and its strong empirical performance.

## Metadata
- **Published**: 2026-08-14T15:41:03Z
- **Authors**: Xiaohong Chen, Yuling Jiao, Lican Kang, Jerry Zhijian Yang, Chen Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14401v1)