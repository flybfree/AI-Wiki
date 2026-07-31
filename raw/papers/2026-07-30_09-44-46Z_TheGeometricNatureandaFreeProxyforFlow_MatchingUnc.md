---
title: The Geometric Nature and a Free Proxy for Flow-Matching Uncertainty
published: 2026-07-30T09:44:46Z
authors: Ziyang Rao, Yiren Zhao, Weiyu Guo, Ben Fei, Yandong Guo, Hui Xiong
url: http://arxiv.org/abs/2607.27933v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Geometric Nature and a Free Proxy for Flow-Matching Uncertainty

## Abstract
Flow matching (FM) has become a popular action head paradigm for modern embodied models. However, as a conditional generative model, it does not explicitly expose its inherent uncertainty, producing faulty action chunks even when it misinterprets the scene or encounters out-of-distribution (OOD) inputs. Therefore, determining when an FM-generated action can be trusted is essential for safe deployment, yet existing uncertainty estimation methods on real-time control suffer from several issues: extra training budget, high computational overhead, and low generalization ability. In this work, we provide a geometric interpretation of FM uncertainty in the velocity field, showing that uncertainty manifests as deviation from an ideal affine-isotropic contraction field. Building on this observation, we introduce denoising acceleration ($\mathrm{accel}$), a highly-generalizable and cost-free uncertainty proxy that measures the bending of the denoising trajectory from a single forward pass, without additional model evaluations, training, or resampling. We theoretically and empirically demonstrate that $\mathrm{accel}$ is a faithful proxy for FM uncertainty and further test its utility in online failure detection. Results show that $\mathrm{accel}$ identifies failing rollouts well before termination, matching or even outperforming costly resampling- and training-based baselines across settings under realistic deployment budget. Code and demos available at: https://github.com/rrrrrrzy/fm-geometry.

## Metadata
- **Published**: 2026-07-30T09:44:46Z
- **Authors**: Ziyang Rao, Yiren Zhao, Weiyu Guo, Ben Fei, Yandong Guo, Hui Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27933v1)