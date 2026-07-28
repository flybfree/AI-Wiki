---
title: Perturbative-NeuSA: A Structured Spectral Framework for Time-Dependent PDEs
published: 2026-07-27T12:25:32Z
authors: Xianli Zhu, Jia Yin
url: http://arxiv.org/abs/2607.24345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Perturbative-NeuSA: A Structured Spectral Framework for Time-Dependent PDEs

## Abstract
Neural spectral PDE solvers often learn an entire unresolved vector field even when an inexpensive approximate model can already capture most of the trajectory. Here we introduce Perturbative-NeuSA, a residual formulation that decomposes the target solution into a low-fidelity background and a high-resolution perturbation, so that only the unresolved dynamics is learned. Starting from the exact perturbation equation, the method combines a fixed spectral operator, a background-dependent correction, the background defect in the target PDE, and an optional neural closure. This construction makes the roles of physical structure and neural closure separately measurable. Across 2D Burgers, Klein-Gordon, and heterogeneous 2D wave equations, the deterministic structured solver outperforms the trained NeuSA baseline while requiring no neural-network training. The largest gains occur on Burgers, where the deterministic correction reduces training and extrapolation errors by factors of 24 and 44, respectively. In addition, a Klein-Gordon sweep over seven background resolutions shows that the effect of the closure is conditional: it improves a poor background by 3.6 times, becomes neutral at intermediate resolutions, and degrades a well-resolved background. For the wave equation, however, the closure provides an additional 18% reduction when the remaining residual is interface-localized. Multi-initial-condition diagnostics further show that the useful closure regime depends on the initial-condition spectrum and can disappear in extrapolation when structured correction already captures the dominant Burgers dynamics. Perturbative-NeuSA therefore reframes neural closure as a conditional, diagnosable correction governed by background fidelity, residual organization, and compatibility with the closure model.

## Metadata
- **Published**: 2026-07-27T12:25:32Z
- **Authors**: Xianli Zhu, Jia Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24345v1)