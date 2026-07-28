---
title: Transfer Learning Architectures for Scalable Multi-Fidelity Bayesian Optimization
published: 2026-07-26T01:23:06Z
authors: Jaewook Lee, Ethan Errington, Christian D. Lorenz, Miao Guo
url: http://arxiv.org/abs/2607.23404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transfer Learning Architectures for Scalable Multi-Fidelity Bayesian Optimization

## Abstract
Self-driving laboratories increasingly rely on multi-fidelity Bayesian optimization (MFBO) to balance cheap, approximate evaluations against scarce, expensive ones, with a predictive surrogate at its core. Gaussian processes (GPs) are the default choice, but they scale poorly as data accumulate and assume a smooth landscape that molecular and materials search spaces routinely violate. Transfer learning offers an alternative suited to this regime: it learns a representation from abundant cheap data and adapts it to sparse expensive data. Despite its use in property prediction, transfer learning has not been tested as the engine of a closed-loop optimization. Here we benchmark eleven transfer-learning surrogates against four GP methods under an identical selection rule, fidelity budget, and model size, across nine tasks spanning synthetic functions to real chemistry and materials problems. GPs win on smooth, low-dimensional functions but perform worst on molecular and materials problems, where transfer-learning surrogates reach substantially better solutions using far less computation. Because acquisition policy is held fixed across surrogates, this advantage is attributable to the surrogate itself. Uncertainty-driven exploration is not reliably beneficial, and calibration does not predict optimization performance, so greedy exploitation of the transfer-learned mean is the more robust default. Transfer learning is therefore the surrogate of choice for molecular and materials MFBO.

## Metadata
- **Published**: 2026-07-26T01:23:06Z
- **Authors**: Jaewook Lee, Ethan Errington, Christian D. Lorenz, Miao Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23404v1)