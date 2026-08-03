---
title: Feature Interaction Modeling for Physics-Informed Neural Networks and Neural Operators
published: 2026-07-30T18:28:50Z
authors: Quan Gu, Hongxia Liu
url: http://arxiv.org/abs/2607.28762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feature Interaction Modeling for Physics-Informed Neural Networks and Neural Operators

## Abstract
This work embeds feature interaction modules derived from factorization machines (FMs) into physics-informed neural networks (PINNs) and neural operator learning, to enhance model expressiveness for solution manifolds of parameterized partial differential equations (PDEs). Motivated by the second-order Taylor expansion of multivariate functions to characterize variable couplings, we first propose FM-PINN. It explicitly captures spatio-temporal variable interactions and improves the approximation accuracy for smooth high-order PDEs. We further group spatial coordinates, time, physical parameters, and initial and boundary conditions into independent feature sets and model their cross-group interactions. Based on this strategy, we develop FM-Operator and FM-DeepONet, which are particularly effective for nonlinear conservation laws and problems with sharp gradients or discontinuities, while offering no consistent advantage on smooth operator learning benchmarks. Numerical tests demonstrate that the proposed mechanism delivers substantial accuracy gains on challenging shock-dominated equations, indicating a promising direction for physics-consistent modeling of parameterized PDEs with strong cross-field dependencies.

## Metadata
- **Published**: 2026-07-30T18:28:50Z
- **Authors**: Quan Gu, Hongxia Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28762v1)