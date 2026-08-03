---
title: Dynamics-aware identification of governing equations from sparse and noisy data
published: 2026-07-31T05:21:43Z
authors: Pongpisit Thanasutives, Yoshinobu Kawahara
url: http://arxiv.org/abs/2607.29036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamics-aware identification of governing equations from sparse and noisy data

## Abstract
Sparse identification of nonlinear dynamics (SINDy) and PDE functional identification (PDE-FIND) recover parsimonious ordinary and partial differential equations (ODEs and PDEs) from data. However, sparse and noisy temporal measurements can make derivative estimates unreliable. To address this problem, we evaluate Koopman-based upsampling techniques implemented with dynamic mode decomposition (DMD), extended DMD (EDMD), and optimized DMD. These methods learn finite-dimensional approximations of Koopman evolution on selected observables and are used to interpolate and denoise snapshots inside the observed time window before derivative estimation and sparse regression. The empirical benchmark comprises two ODE systems, Lorenz-63 and Van der Pol, and three periodic PDE systems, Burgers, Fisher-Kolmogorov-Petrovskii-Piskunov (Fisher-KPP), and linear advection-diffusion, over sparse and noisy sampling regimes. Polynomial EDMD gives the strongest ODE results, especially in coefficient accuracy. The PDE results are system-dependent: low-rank DMD-assisted reconstructions improve Burgers and advection-diffusion discovery, while the raw baseline (without upsampling) remains competitive for the Fisher-KPP data. A comparison against linear and smoothing-spline interpolation techniques shows that the selected Koopman-based preprocessors provide overall performance gains over these non-dynamical alternatives. We also demonstrate that DMD-assisted upsampling can stabilize Pareto-based non-oracle support-size selection. Overall, Koopman-based upsampling is best viewed as a dynamics-aware preprocessing step that can reduce derivative-estimation error when its observable representation and low-rank structure are appropriate for the data.

## Metadata
- **Published**: 2026-07-31T05:21:43Z
- **Authors**: Pongpisit Thanasutives, Yoshinobu Kawahara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29036v1)