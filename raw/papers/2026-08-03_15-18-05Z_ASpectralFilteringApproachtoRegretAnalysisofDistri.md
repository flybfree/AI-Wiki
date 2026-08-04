---
title: A Spectral Filtering Approach to Regret Analysis of Distributed Online Control for Linear Dynamical Systems
published: 2026-08-03T15:18:05Z
authors: Ting-Jui Chang
url: http://arxiv.org/abs/2608.02375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Spectral Filtering Approach to Regret Analysis of Distributed Online Control for Linear Dynamical Systems

## Abstract
This paper studies the distributed online control problem over a network of linear time-invariant (LTI) systems in the presence of adversarial disturbances and time-varying convex costs. The network cost is characterized by the summation of local cost functions, where each local function is sequentially revealed only to the corresponding agent. The goal of each agent is to generate a control sequence, using only local observations and neighbor communication, that competes with the best {\it centralized} linear policy in hindsight. We extend the recently proposed Online Spectral Control framework from the centralized setting to the distributed setting. In particular, each agent applies a spectral controller obtained by convolving past disturbances with the leading eigenvectors of a Hankel matrix, while the controller parameters are updated through a distributed online gradient descent step over the local surrogate costs. We formulate this problem this problem as a {\it regret} minimization problem based on the spectral parameterization, and under standard assumptions, we establish a sublinear regret bound of $O(\frac{\sqrt{T}\text{poly}(\log T)}{γ^3})$, where $T$ is the time horizon and $γ$ denotes the stability margin. The resulting bound also captures the dependence on the network size and connectivity.

## Metadata
- **Published**: 2026-08-03T15:18:05Z
- **Authors**: Ting-Jui Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02375v1)