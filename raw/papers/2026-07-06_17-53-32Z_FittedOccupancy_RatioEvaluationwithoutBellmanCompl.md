---
title: Fitted Occupancy-Ratio Evaluation without Bellman Completeness
published: 2026-07-06T17:53:32Z
authors: Lars van der Laan, Nathan Kallus
url: http://arxiv.org/abs/2607.05375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fitted Occupancy-Ratio Evaluation without Bellman Completeness

## Abstract
Occupancy ratios correct distribution shift in offline reinforcement learning and are central to off-policy evaluation. Existing primal-dual and minimax methods typically estimate these ratios by enforcing occupancy-balance moments over a critic class. We propose fitted occupancy-ratio evaluation (FORE), a fitted fixed-point method that characterizes the discounted occupancy ratio through an adjoint Bellman recursion. At each iteration, FORE solves a single-level density-ratio objective on one-step-transition data, thereby projecting the adjoint Bellman image onto a log-ratio class in Kullback--Leibler (KL) divergence. Unlike analyses of fitted Q-evaluation, which typically require value-function realizability together with Bellman completeness or projected-operator stability, our central approximation condition is just realizability of the discounted occupancy ratio itself. Under this condition, the population KL-projected recursion contracts in relative entropy toward the true ratio by virtue of the adjoint Bellman operator being a KL-contraction. For the empirical recursion, we establish finite-sample regret bounds that yield convergence in KL up to log-ratio approximation error and a statistical error governed by the complexity of the ratio hypothesis class. The fitted ratio supports direct value estimation by reward reweighting, occupancy-weighted fitted Q-evaluation, and doubly robust estimation that combines the fitted ratio with a fitted Q-function. Together, these results identify discounted occupancy-ratio realizability as a sufficient condition for offline policy evaluation without any completeness assumptions.

## Metadata
- **Published**: 2026-07-06T17:53:32Z
- **Authors**: Lars van der Laan, Nathan Kallus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.05375v1)