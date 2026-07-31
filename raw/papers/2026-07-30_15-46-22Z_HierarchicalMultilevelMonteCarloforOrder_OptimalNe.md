---
title: Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs
published: 2026-07-30T15:46:22Z
authors: Ankur Naskar, Vaneet Aggarwal
url: http://arxiv.org/abs/2607.28390v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs

## Abstract
Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, extending order-optimal convergence guarantees to neural critics in average-reward CMDPs has remained open. The main challenge is a fundamental bias-cost trade-off in neural critic estimation: under Neural Tangent Kernel (NTK) analysis, reducing critic bias substantially increases critic optimization cost, preventing order-optimal convergence in the primal-dual framework. We resolve this bottleneck by introducing a hierarchical Multilevel Monte Carlo (MLMC) neural critic that performs debiasing simultaneously across trajectory sampling and critic optimization. The resulting estimator attains the bias of a long critic optimization run with only logarithmic expected sample cost. Building on this estimator, we develop a primal-dual Natural Actor-Critic algorithm that achieves both an optimality gap and a constraint violation of order $\tilde{O}(T^{-1/2})$. This establishes the first order-optimal convergence guarantees for infinite-horizon average-reward CMDPs with general policy parameterization and neural critics, while eliminating the need to know the underlying mixing time. Our results are novel even in the unconstrained setting.

## Metadata
- **Published**: 2026-07-30T15:46:22Z
- **Authors**: Ankur Naskar, Vaneet Aggarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28390v1)