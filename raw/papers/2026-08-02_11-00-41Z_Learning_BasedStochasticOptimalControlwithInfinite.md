---
title: Learning-Based Stochastic Optimal Control with Infinite-Horizon Probabilistic Constraints
published: 2026-08-02T11:00:41Z
authors: Francesco Cordiano, Kanghui He, Bart De Schutter
url: http://arxiv.org/abs/2608.01151v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning-Based Stochastic Optimal Control with Infinite-Horizon Probabilistic Constraints

## Abstract
In this paper, we consider stochastic optimal control problems with infinite-horizon joint chance constraints. By means of an appropriate state augmentation, we reformulate the original problem as a constrained Markov decision process, in which both the cost and the constraint function exhibit an additive structure. We then prove that this formulation enjoys strong duality, thereby enabling us to reformulate the problem as an equivalent unconstrained one in the Lagrange dual framework. We propose a dual-ascent algorithm to solve the resulting problem and show that it converges to a deterministic Markov policy defined over the augmented state space that is both optimal and feasible. To accommodate continuous state-input spaces, we propose a dedicated learning algorithm to approximate the value function in an offline training setting, thereby significantly reducing the computational complexity of the online control phase. We then test our approach on a numerical example and demonstrate its effectiveness compared to online predictive control methods in terms of performance and computational complexity.

## Metadata
- **Published**: 2026-08-02T11:00:41Z
- **Authors**: Francesco Cordiano, Kanghui He, Bart De Schutter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01151v1)