---
title: Quantum-Classical Physics-Informed Kolmogorov-Arnold Networks for Solving Fuzzy Differential Equations
published: 2026-08-09T16:01:03Z
authors: Xiang Rao, Yuxuan Shen
url: http://arxiv.org/abs/2608.08782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantum-Classical Physics-Informed Kolmogorov-Arnold Networks for Solving Fuzzy Differential Equations

## Abstract
In this study, we propose a quantum-classical physics-informed Kolmogorov-Arnold network (QCPIKAN) dedicated to the solution of fuzzy differential equations. The network takes the spatiotemporal coordinates and membership level as joint inputs and employs ChebyKAN modules and a parameterized quantum circuit to construct a hybrid function approximator. It simultaneously approximates the lower and upper endpoint functions associated with the α-cuts and incorporates the governing equations, initial-boundary conditions, and fuzzy-structural constraints into the training objective. Theoretically, a unified error-analysis framework is established for QCPIKAN and PIKAN, in which the endpoint-solution error is decomposed into approximation, sampling, optimization, and fuzzy-structure constraint errors. Under the assumptions of well-posedness and residual stability, it is proved that QCPIKAN has a smaller a priori error bound when the representational gain introduced by quantum entanglement features exceeds the additional computational error. Numerical experiments are conducted for elliptic, parabolic, and hyperbolic equations in an ideal quantum-simulation environment. The results show that QCPIKAN captures the overall contraction of the solution interval as increases. At most tested membership levels, the mean relative L2 error of PIKAN is approximately 1.1-2.7 times that of QCPIKAN. In the fuzzy convection example, the mean wavefront-position error of PIKAN is approximately 1.77 times that of QCPIKAN. Nevertheless, both models still exhibit local fuzzy-structure violations near boundaries, in high-gradient regions, and around the wavefront. These results indicate that QCPIKAN provides a quantum-classical hybrid physics-informed computational framework with comparatively high predictive accuracy for solving fuzzy partial differential equations represented by α-cuts.

## Metadata
- **Published**: 2026-08-09T16:01:03Z
- **Authors**: Xiang Rao, Yuxuan Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08782v1)