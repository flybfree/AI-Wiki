---
title: Inferring Missing Trajectory Data with Temporal Convolutional Networks
published: 2026-07-27T23:46:15Z
authors: Ilinca Tiriblecea, Gabriel Turinici
url: http://arxiv.org/abs/2607.25147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inferring Missing Trajectory Data with Temporal Convolutional Networks

## Abstract
Trajectory data collected in real-world settings is frequently incomplete due to sensor failure, communication loss, or occlusion. We address the task of \emph{trajectory inpainting}: reconstructing contiguous missing segments from observed context. We propose a Temporal Convolutional Network (TCN) with symmetric dilation that relaxes the standard causality constraint, allowing each time step to draw on both past and future observations, a property that is essential for inpainting, but absent from forecasting-oriented architectures. The model is trained with a composite loss that combines weighted mean squared error, boundary--continuity penalties, and a smoothness regularizer. Trained on a synthetic dataset of $1,000$ (train), $200$ (validation), and $300$ (test) two-dimensional trajectories with randomly placed 20% masked segments, the model achieves good R$^{2}$, MSE and MAE metrics.

## Metadata
- **Published**: 2026-07-27T23:46:15Z
- **Authors**: Ilinca Tiriblecea, Gabriel Turinici
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25147v1)