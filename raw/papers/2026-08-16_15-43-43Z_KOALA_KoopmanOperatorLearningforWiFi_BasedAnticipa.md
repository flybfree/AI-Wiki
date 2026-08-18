---
title: KOALA: Koopman Operator Learning for WiFi-Based Anticipatory Hum
published: 2026-08-16T15:43:43Z
authors: Quang-Anh N. D., Duc Pham Minh, Thao Phuong Pham, Minh Anh Nguyen, Huan X. Nguyen, Tuan Dang
url: http://arxiv.org/abs/2608.15815v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KOALA: Koopman Operator Learning for WiFi-Based Anticipatory Hum

## Abstract
WiFi Channel State Information (CSI) has emerged as a privacy-preserving alternative to cameras for human pose estimation. However, existing approaches treat pose inference as an instantaneous regression problem and do not model temporal dynamics, making future motion prediction infeasible. Naively applying vision-based prediction methods compounds the estimation noise already present in CSI-derived poses, as autoregressive rollouts amplify errors at every step. We propose KOALA, the framework for human motion prediction directly from WiFi CSI, by lifting noisy CSI-derived pose sequences into a learned Koopman latent space where nonlinear dynamics become linear, enabling multi-horizon prediction via simple matrix-vector products without autoregressive iteration or error accumulation. A residual CSI-conditioned operator resolves the identity attractor problem inherent from Koopman formulations, and an anchor-delta prediction head eliminates the degenerate shortcut of copying the current pose across all horizons. To regularise the lifting and operator jointly, we introduce a Koopman Anchored Latent (KAL) loss that operates in the temporal-encoder feature space, enforcing dynamical consistency across prediction horizons without requiring contrastive, spectral, or auxiliary losses. Experiments on MM-Fi and WiPose show that KOALA achieves robust, consistent performance across both short- and long-term prediction horizons, outperforming all baselines by a substantial margin.

## Metadata
- **Published**: 2026-08-16T15:43:43Z
- **Authors**: Quang-Anh N. D., Duc Pham Minh, Thao Phuong Pham, Minh Anh Nguyen, Huan X. Nguyen, Tuan Dang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15815v1)