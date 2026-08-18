---
title: Identifying parameter couplings and uncertainties of mixed-noise stochastic systems via full-covariance Gaussian mixture network
published: 2026-08-15T12:30:10Z
authors: Xiaolong Wang, Xiangwen Hao, Jing Feng, Yuanyuan Liu, Yong Xu
url: http://arxiv.org/abs/2608.15198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Identifying parameter couplings and uncertainties of mixed-noise stochastic systems via full-covariance Gaussian mixture network

## Abstract
Parameter identification of stochastic dynamical systems driven by mixed noises is challenging due to intractable likelihood functions. We propose PENN-GMD, a parameter estimation neural network that maps partially observed trajectories to a Gaussian mixture distribution (GMD) over the system parameters. Unlike conventional uncertainty estimates, the GMD employs full covariance matrices to explicitly reveal parameter couplings and multi-modal likelihood structures. The network is trained by minimizing the negative log-likelihood via a surjective parameterization that hard-encodes all GMD constraints, thereby approximating the true likelihood. We validate the method on five numerical examples with increasing complexity, including systems driven by fractional Gaussian and Lévy noises, oscillators with colored noise, coupled neurons under different observability, and an aeroelastic airfoil with unidentifiable stochastic disturbances. Results demonstrate that PENN-GMD accurately recovers likelihood distributions, captures parameter couplings, and naturally diagnoses non-identifiability through variance broadening or mode splitting. These capabilities establish PENN-GMD as a practical tool for uncertainty-aware parameter identification in complex stochastic systems where conventional likelihood-based methods are infeasible.

## Metadata
- **Published**: 2026-08-15T12:30:10Z
- **Authors**: Xiaolong Wang, Xiangwen Hao, Jing Feng, Yuanyuan Liu, Yong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15198v1)