---
title: Upper-Expectile Multi-Step Q-Learning for Off-Policy Reinforcement Learning
published: 2026-08-03T10:30:56Z
authors: Abdelghani Ghanem, Mounir Ghogho
url: http://arxiv.org/abs/2608.02034v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Upper-Expectile Multi-Step Q-Learning for Off-Policy Reinforcement Learning

## Abstract
Multi-step returns accelerate reward propagation in off-policy reinforcement learning, but couple the evaluation of each decision to the suboptimal logged actions that follow it, inducing a pessimistic bias that grows with the horizon. We propose Expectile $n$-step Q-learning (ENQ), which replaces the symmetric $n$-step temporal-difference (TD) loss with an asymmetric expectile loss on the action-value error, with expectile level $τ$ as the only method-specific hyperparameter added beyond $n$-step TD. We prove that the ENQ operator is a $γ^{n}$-contraction. Under deterministic dynamics, at $τ=1$, its bias vanishes at the optimal action-value function $Q^*$ on covered in-support pairs, and the corresponding fixed point satisfies the separation-$n$ instance and its multiples of the lower-bound inequality used by Long-Horizon Q-learning (LQL). Under stochastic dynamics, the operator bias admits two-sided bounds with horizon-independent noise constants. Using a single expectile level $τ=0.8$ and a fixed backup horizon across 27 manipulation and navigation task instances, ENQ is competitive with LQL on aggregate, achieves higher measured training-step throughput in our profiling study, and benefits more from a ten-critic ensemble in a controlled scaling experiment.

## Metadata
- **Published**: 2026-08-03T10:30:56Z
- **Authors**: Abdelghani Ghanem, Mounir Ghogho
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02034v1)