---
title: Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity
published: 2026-07-30T21:21:52Z
authors: Naman Saxena, Mudit Gaur, Vaneet Aggarwal
url: http://arxiv.org/abs/2607.28849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity

## Abstract
Bilevel reinforcement learning (RL) is an important framework within the literature of RL that can be used to formalize various categories of problems, such as meta-learning, hierarchical task decomposition, and reinforcement learning from human feedback (RL-HF). Most of the bilevel RL algorithms are either not scalable because of using hypergradient with Hessian, or they suffer from high sample complexity because of using penalty-based approximation methods. In this work, we propose a hypergradient-based bilevel RL algorithm using the optimality of the Boltzmann policy for the entropy regularized discounted RL objective function. Our proposed algorithm is Hessian-free and obtains an iteration complexity of $O(ε^{-1})$ and state-of-the-art sample complexity of $\tilde{O}(ε^{-2})$ under mild regularity conditions. Further, in our convergence analysis, we are able to remove the assumption of the Polyak-Lojasiewicz (PL) condition on the outer-level objective function present in the prior state-of-the-art sample complexity work.

## Metadata
- **Published**: 2026-07-30T21:21:52Z
- **Authors**: Naman Saxena, Mudit Gaur, Vaneet Aggarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28849v1)