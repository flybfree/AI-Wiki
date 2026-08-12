---
title: Efficient Weak-Entropy PINN for Solving Hyperbolic Conservation Laws
published: 2026-08-11T02:34:15Z
authors: Qi Gao, Kuang Huang, Xuan Di
url: http://arxiv.org/abs/2608.10389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Weak-Entropy PINN for Solving Hyperbolic Conservation Laws

## Abstract
In recent years, neural networks have significantly advanced numerical solutions of partial differential equations (PDEs). However, solving PDEs with discontinuous solutions, such as hyperbolic conservation laws, remains challenging for neural network-based methods such as physics-informed neural networks (PINNs). Existing methods often rely on strong prior assumptions such as knowledge of discontinuity locations, or they introduce artificial smoothing terms that degrade accuracy. However, accurately solving these conservation laws and predicting the formation and propagation of discontinuities in solutions is crucial in many practical applications, including gas dynamics and traffic flow modeling. In this paper, we introduce a novel Weak-Entropy PINN (WEPINN) framework for hyperbolic conservation laws with discontinuous solutions. The method enforces the governing equations in their weak (integral) formulation and incorporates the entropy condition to select the physically admissible solution, while employing the discrete fast Fourier transform (DFFT) for efficient numerical integration. Our method is tested through extensive numerical experiments on a variety of scalar conservation laws and systems of conservation laws in one and two dimensional spaces. These experiments demonstrate that our method can accurately resolve sharp discontinuities while effectively capturing interactions between multiple shock and rarefaction waves.

## Metadata
- **Published**: 2026-08-11T02:34:15Z
- **Authors**: Qi Gao, Kuang Huang, Xuan Di
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10389v1)