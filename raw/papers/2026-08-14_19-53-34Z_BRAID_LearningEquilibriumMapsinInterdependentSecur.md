---
title: BRAID: Learning Equilibrium Maps in Interdependent Security Games via Weight-Tied Iterative Graph Neural Networks
published: 2026-08-14T19:53:34Z
authors: Elnaz Nowrouzi, Zhiqun Zuo, Xueru Zhang, Mohammad Mahdi Khalili
url: http://arxiv.org/abs/2608.14856v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BRAID: Learning Equilibrium Maps in Interdependent Security Games via Weight-Tied Iterative Graph Neural Networks

## Abstract
Computing Nash equilibria in interdependent security (IDS) games on networks is computationally expensive: best-response dynamics may need hundreds of iterations per instance, and downstream tasks such as auditing, stress-testing, and incentive design often require repeatedly re-solving the game under parameter perturbations. We propose BRAID, a Best-Response Amortized Iterative Dynamics model that uses a weight-tied iterative graph neural network to learn a direct map from game parameters to Nash equilibrium effort profiles, replacing iterative best response computation with a single forward pass that is up to 43X faster per instance. BRAID is derived from the best-response fixed-point structure of IDS games: its SUM aggregation reflects additive neighbor coupling, and a weight-tied gated recurrent unit (GRU) mirrors a damped best-response update. The same architecture applies across IDS specifications that vary investment-cost curvature and neighborhood aggregation, including log-linear, quadratic-cost, and log constant-elasticity-of-substitution (CES) utilities. Beyond equilibrium prediction, BRAID also recovers how equilibrium efforts change under perturbations to game parameters, including costs and network edge weights. We make this sensitivity recovery an explicit evaluation target and introduce two training strategies, interior-equilibrium training and input-noise regularization, that improve the local behavior of the learned equilibrium map without using sensitivity labels. Experiments show that BRAID effectively predicts Nash equilibria and recovers equilibrium sensitivities across utility specifications and network sizes.

## Metadata
- **Published**: 2026-08-14T19:53:34Z
- **Authors**: Elnaz Nowrouzi, Zhiqun Zuo, Xueru Zhang, Mohammad Mahdi Khalili
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14856v1)