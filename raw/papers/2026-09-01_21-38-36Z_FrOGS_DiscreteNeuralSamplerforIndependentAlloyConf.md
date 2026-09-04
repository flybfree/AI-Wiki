---
title: FrOGS: Discrete Neural Sampler for Independent Alloy Configurations Across Chemical Conditions
published: 2026-09-01T21:38:36Z
authors: Kyucheol Min, Elyssa Hofgard, Tess Smidt
url: http://arxiv.org/abs/2609.02948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FrOGS: Discrete Neural Sampler for Independent Alloy Configurations Across Chemical Conditions

## Abstract
Predicting the thermodynamic properties of an alloy requires sampling its configurations across many chemical conditions and recovering free energies on a common absolute scale. Markov chain Monte Carlo (MCMC) is the standard tool, but it requires separate simulations at different conditions, and auxiliary free-energy methods such as thermodynamic integration are used to place results on a common absolute scale. Modern discrete neural samplers typically use reverse KL divergence as the objective and can be mode-seeking or biased. We present Free energy Offering Generative Sampler (FrOGS), a hybrid discrete neural sampler that couples an autoregressive model to a continuous-time Markov chain (CTMC) to be trained jointly under a single shared loss. FrOGS draws i.i.d. configurations, returns an unbiased estimate of the partition function, and gives consistent estimates of thermodynamic observables. We train a single model across a wide range of chemical conditions to produce estimates on a common absolute free-energy scale. FrOGS matches exact finite-size results on the 2D Ising model and reference phase diagrams for AgPd and CuAu, without mode collapse. We additionally compare to SEGAL, a published autoregressive baseline, and find that only FrOGS recovers the stability range of the CuAu$_3$ phase.

## Metadata
- **Published**: 2026-09-01T21:38:36Z
- **Authors**: Kyucheol Min, Elyssa Hofgard, Tess Smidt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02948v1)