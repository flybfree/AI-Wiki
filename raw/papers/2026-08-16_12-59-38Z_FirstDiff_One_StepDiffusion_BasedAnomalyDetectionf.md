---
title: FirstDiff: One-Step Diffusion-Based Anomaly Detection for Multivariate Time Series via Initial Noise Prediction
published: 2026-08-16T12:59:38Z
authors: Ali Boudaghi, Alireza Nemati, Hadi Zare
url: http://arxiv.org/abs/2608.15727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FirstDiff: One-Step Diffusion-Based Anomaly Detection for Multivariate Time Series via Initial Noise Prediction

## Abstract
Diffusion models have recently shown strong potential for multivariate time-series anomaly detection by learning the distribution of normal data through iterative denoising. Existing diffusion-based approaches, however, typically perform anomaly detection after completing the reverse diffusion process, relying primarily on the final reconstructed signal and overlooking informative representations produced during denoising. This design incurs substantial computational cost and limits the use of intermediate diffusion information for anomaly detection.   In this paper, we propose FirstDiff, a diffusion-based anomaly detection framework based on the observation that the predicted diffusion noise at the initial reverse-diffusion evaluation already contains sufficient information for accurate anomaly detection. FirstDiff models the statistical distribution of predicted diffusion noise under normal behavior using validation data, enabling anomaly inference from a single denoising-network evaluation rather than completing the reverse diffusion trajectory.   To model complex temporal and inter-sensor dependencies, FirstDiff employs a Diffusion Transformer as the denoising backbone. Extensive experiments on five public benchmark datasets demonstrate that FirstDiff achieves state-of-the-art performance while reducing diffusion inference from the full reverse trajectory to a single denoising-network evaluation.

## Metadata
- **Published**: 2026-08-16T12:59:38Z
- **Authors**: Ali Boudaghi, Alireza Nemati, Hadi Zare
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15727v1)