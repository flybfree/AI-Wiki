---
title: HypEMBER: Hypernetwork-based Ensemble for Robust Policy Learning of Parametrized Dynamical Systems
published: 2026-07-21T23:37:34Z
authors: Nicolò Botteghi, Gabriele Pascali, Urban Fasel, Andrea Manzoni
url: http://arxiv.org/abs/2607.19628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HypEMBER: Hypernetwork-based Ensemble for Robust Policy Learning of Parametrized Dynamical Systems

## Abstract
In this work we investigate reinforcement learning (RL) as a framework for the robust control of parametrized dynamical systems in presence of measurements and model uncertainties. High-dimensional state spaces, expensive numerical solvers, the partial knowledge of the governing equations, and the dependence on physical parameters that may be uncertain or difficult to estimate accurately, make the use of standard RL approaches computationally unfeasible. Indeed, lack of robustness and poor generalization across parameter variations are further amplified in presence of noisy or incomplete measurements, ultimately hampering control performance. To address these challenges, we introduce HypEMBER, a novel RL framework based on the combination of hypernetworks and ensemble learning. In the proposed approach, both the policy and value functions are represented through hypernetworks that generate the weights of the underlying models conditioned on the physical parameters of the system, thereby enabling parametric generalization across different dynamical regimes. In addition, an ensemble of policy and value approximators is employed to quantify epistemic uncertainty, leading to improved exploration strategies and enhanced robustness during and after training. The performance of the proposed framework is assessed on two representative parametrized control problems: (i) the one-dimensional Kuramoto-Sivashinsky equation and (ii) a particle-navigation task in a two-dimensional time-dependent gyre flow, focusing on robustness with respect to measurement noise and parameter misspecification. Numerical results demonstrate that HypEMBER consistently improves training stability and sample efficiency, while achieving superior robustness to uncertainties affecting both the system dynamics and the available observations, in comparison with state-of-the-art RL methods.

## Metadata
- **Published**: 2026-07-21T23:37:34Z
- **Authors**: Nicolò Botteghi, Gabriele Pascali, Urban Fasel, Andrea Manzoni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19628v1)