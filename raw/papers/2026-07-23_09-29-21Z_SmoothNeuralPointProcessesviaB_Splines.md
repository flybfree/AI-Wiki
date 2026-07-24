---
title: Smooth Neural Point Processes via B-Splines
published: 2026-07-23T09:29:21Z
authors: Michele Bellomo, Riccardo Ramaschi, Alberto Dolara, Tomaso Aste
url: http://arxiv.org/abs/2607.21098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Smooth Neural Point Processes via B-Splines

## Abstract
Temporal point processes (TPPs) provide a general and flexible framework for modeling sequences of events in continuous time. Neural networks have been successfully employed to model TPPs in a highly expressive and data-driven way. Neural TPPs are typically trained via Maximum Likelihood Estimation (MLE) by minimizing the negative log-likelihood (NLL), which depends on both the conditional intensity function (CIF) and its integral over time, the compensator. Recent neural TPP approaches enable exact evaluation of the NLL without numerical integration. However, these methods typically model the compensator rather than the CIF directly, impose constraints on the neural network architecture, and are computationally expensive during training, as event contributions to the NLL are evaluated sequentially rather than in parallel. In this work, we propose a novel neural TPP model that directly parametrizes the CIF as a non-negative combination of B-spline basis functions, whose coefficients are predicted by a neural network. This formulation enables exact evaluation of the NLL, preserves full flexibility in the neural architecture, allows efficient parallelization during training, and naturally supports CIF smoothness regularization through the integrated squared second derivative. Experiments on both synthetic and real-world datasets show improved computational efficiency and predictive accuracy compared to the reference neural TPP baseline.

## Metadata
- **Published**: 2026-07-23T09:29:21Z
- **Authors**: Michele Bellomo, Riccardo Ramaschi, Alberto Dolara, Tomaso Aste
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21098v1)