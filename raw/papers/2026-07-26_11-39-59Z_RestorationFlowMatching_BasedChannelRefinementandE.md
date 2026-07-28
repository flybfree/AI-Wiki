---
title: Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications
published: 2026-07-26T11:39:59Z
authors: Wenkai Liu, Nan Ma, Jianqiao Chen, Xiaodong Xu, Meixia Tao, Ping Zhang
url: http://arxiv.org/abs/2607.23615v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications

## Abstract
In multiple-input multiple-output (MIMO) semantic communication, imperfect channel state information (CSI) and equalization mismatch can seriously degrade semantic reconstruction quality. To address this issue, we propose a unified restoration flow matching (RFM)-based framework for channel refinement and equalization correction. Specifically, the channel RFM (CRFM) module is developed to refine the coarse channel, thereby improving channel estimation accuracy. Based on the refined channel, the developed semantic RFM (SRFM) module is employed to correct the residual distortions in the post-equalization latent space. The key idea is to formulate the two cascaded inverse problems of channel estimation and equalization as the unified conditional restoration task, in which the learned conditional velocity field guides the perturbed distribution towards the target distribution. To enhance the robustness of these two modules under various distortion conditions, we develop a dual-anchor perturbation training strategy that jointly learns near-manifold refinement and large-error correction, and implement inference through a few-step deterministic ordinary differential equation (ODE) solver. Extensive experiments on MIMO channels and visual semantic transmission tasks demonstrate that the proposed scheme improves key metrics for channel estimation and semantic reconstruction quality. Moreover, compared with representative diffusion-based generative baselines, the proposed method requires fewer sampling steps.

## Metadata
- **Published**: 2026-07-26T11:39:59Z
- **Authors**: Wenkai Liu, Nan Ma, Jianqiao Chen, Xiaodong Xu, Meixia Tao, Ping Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23615v1)