---
title: Asymptotically Optimal Regret for Reinforcement Learning without Horizon Dependence
published: 2026-07-22T07:42:19Z
authors: Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du
url: http://arxiv.org/abs/2607.19854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asymptotically Optimal Regret for Reinforcement Learning without Horizon Dependence

## Abstract
We study horizon-free regret minimization for finite-horizon time-homogeneous tabular Markov decision processes with $S$ states, $A$ actions, horizon $H$, and per-trajectory total reward bounded by $1$.   We propose a new algorithm and prove a regret upper bound \[\tilde O(\sqrt{SAK}+S^8A^3)\] with failure probability $δ$, where $K$ is the number of episodes and $\tilde O(\cdot)$ hides $\mathsf{poly}\log(S,A,K,1/δ)$.   Thus, the regret is $H$-free and asymptotically optimal, matching the contextual-bandit lower bound $Ω(\sqrt{SAK})$ up to logarithmic factors. This completely removes the $\log H$ dependence from the previous $\tilde O(\sqrt{SAK\log H}+S^2A\log H)$ guarantee of Zhang et al. (2021), and drastically improves the prior best horizon-free regret $\tilde O(\sqrt{S^9A^3K})$ of Zhang et al. (2022) asymptotically.   The main technical difficulty is that the optimal value functions $\{V_h^*\}_{h=1}^H$ are time-inhomogeneous even though the transition kernel is time-homogeneous. A direct union bound over all value functions typically incurs an additional $\min\{\log H,S\}$ factor. We avoid this factor by (i) exploiting the monotonicity of $V_h^*$ in $h$ and (ii) non-trivially projecting the value functions onto an $S$-dimensional grid.   Our analysis relies on three additional ingredients. First, we introduce a horizon-truncation argument that enables reward-based exploration and removes the cost of a separate reward-free exploration phase. Second, we design a cutting bonus that preserves both optimism and the monotonicity needed for planning. Third, we prove a new bound on total deviation for time-homogeneous MDPs, which controls the clipped variance terms in the cutting bonus with adjustable polynomial dependence on $S$ and without any dependence on $H$. Together, these tools yield an asymptotically optimal horizon-free regret guarantee.

## Metadata
- **Published**: 2026-07-22T07:42:19Z
- **Authors**: Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19854v1)