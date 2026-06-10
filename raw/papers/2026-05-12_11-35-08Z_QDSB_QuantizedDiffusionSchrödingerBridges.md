---
title: 'QDSB: Quantized Diffusion Schrödinger Bridges'
published: 2026-05-12T11:35:08Z
authors: Tobias Fuchs, Florian Kalinke, Nadja Klein
url: http://arxiv.org/abs/2605.11983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QDSB: Quantized Diffusion Schrödinger Bridges

## Abstract
Learning generative models in settings where the source and target distributions are only specified through unpaired samples is gaining in importance. Here, one frequently-used model are Schrödinger bridges (SB), which represent the most likely evolution between both endpoint distributions. To accelerate training, simulation-free SBs avoid the path simulation of the original SB models. However, learning simulation-free SBs requires paired data; a coupling of the source and target samples is obtained as the solution of the entropic optimal transport (OT) problem. As obtaining the optimal global coupling is infeasible in many practical cases, the entropic OT problem is iteratively solved on minibatches instead. Still, the repeated cost remains substantial and the locality can distort the global transport geometry. We propose quantized diffusion Schrödinger bridges (QDSB), which compute the endpoint coupling on anchor-quantized endpoint distributions and lift the resulting plan back to original data points through cell-wise sampling. We show that the regularized optimal coupling is stable w.r.t. anchor quantization, with an error controlled by the quality of the anchor approximation. In real-world experiments, QDSB matches the sample quality of existing baselines, requiring substantially less time. Code and data are available at github.com/mathefuchs/qdsb.

## Metadata
- **Published**: 2026-05-12T11:35:08Z
- **Authors**: Tobias Fuchs, Florian Kalinke, Nadja Klein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11983v1)