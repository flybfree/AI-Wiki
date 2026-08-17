---
title: FLARE MCMC: Fidelity-based Layer-Adaptive REcursive proposals for MCMC
published: 2026-08-13T21:02:46Z
authors: Harini Venkatesan, Christian Shelton, Ming-Feng Ho, Simeon Bird, Mengxuan Wu
url: http://arxiv.org/abs/2608.13774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLARE MCMC: Fidelity-based Layer-Adaptive REcursive proposals for MCMC

## Abstract
Markov chain Monte Carlo (MCMC) requires only the ability to evaluate the likelihood, making it a common technique for inference in complex models. However, it can have a slow mixing rate, requiring the generation of many samples to obtain good estimates and an overall high computational cost. FLARE MCMC is a multi-fidelity layered MCMC method that exploits lower-fidelity approximations of the true likelihood calculation to improve mixing and leads to overall faster performance. Such lower-fidelity likelihoods are commonly available in scientific and engineering applications where the model involves a simulation whose resolution or accuracy can be tuned. Our technique uses recursive, layered chains with simple layer tuning; it does not require the likelihood to take any form or have any particular internal mathematical structure. We demonstrate experimentally that FLARE MCMC achieves larger effective sample sizes for the same computational time across different scientific domains including hydrology and cosmology.

## Metadata
- **Published**: 2026-08-13T21:02:46Z
- **Authors**: Harini Venkatesan, Christian Shelton, Ming-Feng Ho, Simeon Bird, Mengxuan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13774v1)