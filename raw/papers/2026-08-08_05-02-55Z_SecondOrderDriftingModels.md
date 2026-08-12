---
title: Second Order Drifting Models
published: 2026-08-08T05:02:55Z
authors: Drake Brown, Yuhao Huang, Shih-Hsin Wang, Bao Wang
url: http://arxiv.org/abs/2608.07924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Second Order Drifting Models

## Abstract
Drifting models are a recent class of one-step generative models that evolve the model distribution during training using a predefined sample-based drift field. Although they avoid iterative inference, their kernel-based drift fields induce frequency-dependent training dynamics: In the linearized regime, each Fourier mode of the density residual decays at a rate determined by the kernel spectrum, leading to slow recovery of fine-scale structure. We propose Second-Order Drifting Models, which lift drifting dynamics into phase space by augmenting generated samples with artificial velocity variables. We show that the resulting density perturbations obey accelerated second-order dynamics in Fourier space, connecting drifting models to the celebrated Nesterov acceleration from optimization theory. This provides a principled mechanism for mitigating the spectral stiffness of first-order drifting while preserving one-step inference. We derive a practical semi-implicit training algorithm and evaluate it on synthetic distribution matching, sequential data generation, and robotic control. Across these settings, the second-order drifting model improves convergence behavior and achieves competitive or superior performance over first-order drifting baselines.

## Metadata
- **Published**: 2026-08-08T05:02:55Z
- **Authors**: Drake Brown, Yuhao Huang, Shih-Hsin Wang, Bao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07924v1)