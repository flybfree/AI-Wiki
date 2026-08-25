---
title: FreKoo++: Learning Continuous Spectral Dynamics for Temporal Domain Generalization
published: 2026-08-23T05:22:47Z
authors: En Yu, Xiaoyu Yang, Wei Duan, Guangquan Zhang, Jie Lu
url: http://arxiv.org/abs/2608.22224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FreKoo++: Learning Continuous Spectral Dynamics for Temporal Domain Generalization

## Abstract
Temporal Domain Generalization (TDG) aims to learn from historical domains and generalize to unseen future distributions under concept drift. Nevertheless, prevailing TDG methods struggle with complex real-world streaming scenarios involving both multi-scale drift patterns (e.g., long-term periodicity intertwined with short-term incremental changes) and local uncertainties, especially in continuous settings where observations arrive irregularly. To address this limitation, we propose FreKoo++, a novel continuous spectral-dynamical framework that pioneers the unification of continuous Koopman modal dynamics with adaptive spectral disentanglement. Specifically, FreKoo++ maps source-domain parameters into a compact latent space, modeling their evolution as a superposition of learnable continuous modes where complex eigenvalues jointly encode oscillatory frequency and temporal growth or decay. This formulation naturally accommodates irregular timestamps and supports arbitrary horizon extrapolation without rigid discrete stepping. Furthermore, we propose a new adaptive soft spectral weighting mechanism backed by stability and spectral regularization, which automatically isolates persistent dominant dynamics from transient noise without relying on manual frequency thresholds. We derive modal approximation and generalization bounds that characterize how amplitude and eigenvalue estimation errors propagate with the prediction horizon. Extensive experiments on both discrete and continuous TDG benchmarks demonstrate that FreKoo++ achieves state-of-the-art performance under complex multi-scale drifts and irregular sampling.

## Metadata
- **Published**: 2026-08-23T05:22:47Z
- **Authors**: En Yu, Xiaoyu Yang, Wei Duan, Guangquan Zhang, Jie Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22224v1)