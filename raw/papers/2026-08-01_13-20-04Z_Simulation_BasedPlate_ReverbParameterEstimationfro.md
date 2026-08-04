---
title: Simulation-Based Plate-Reverb Parameter Estimation from a Single Impulse Response
published: 2026-08-01T13:20:04Z
authors: Minhui Lu, Joshua D. Reiss
url: http://arxiv.org/abs/2608.00656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simulation-Based Plate-Reverb Parameter Estimation from a Single Impulse Response

## Abstract
We present a simulation-trained, non-iterative estimator for Task A of the 1st DAFx Parameter Estimation Challenge. Each unnormalized plate-reverb impulse response is summarized by amplitude, spectral, and decay descriptors, and an ensemble of tree regressors estimates the six target parameters in one pass. Across two independent synthetic validation sets, the normalized models outperform the training-set mean and an earlier raw-regression baseline. On a shared set, the final ensemble also outperforms a single run of the official default PSO at substantially lower inference cost. Since the official labels are hidden, parameter accuracy is measured on simulator-matched data, and the released responses support only audio-side consistency checks. The estimator returns point estimates without uncertainty.

## Metadata
- **Published**: 2026-08-01T13:20:04Z
- **Authors**: Minhui Lu, Joshua D. Reiss
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00656v1)