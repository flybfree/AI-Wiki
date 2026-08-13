---
title: Foresight Without Seeing: Latent Futures for World Action Models
published: 2026-08-12T03:27:43Z
authors: Jiakai Huang, Zhongbo Wu, Zheng Zhang, Zihan Wang, Shan You, Tao Huang
url: http://arxiv.org/abs/2608.11605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Foresight Without Seeing: Latent Futures for World Action Models

## Abstract
World Action Models (WAMs) couple future visual prediction with robot action generation, enabling policies to model how the physical world evolves during interaction. Existing WAMs differ in how predictive dynamics are exposed to the action pathway. Explicit-future WAMs provide direct access to predicted scene evolution, but incur substantial inference costs from iterative video denoising. In contrast, direct-policy WAMs efficiently predict actions from the current observation but lack an explicit inference-time interface for exposing predictive dynamics to the Action DiT. To bridge this gap, we propose ForeWAM, a dynamics-conditioned direct-policy WAM that provides predictive context for action generation without decoding future videos. At its core, Future-KV performs a single Video DiT prefill over the current visual latent and stochastic future slots, and reuses the resulting layer-wise key-value states throughout action denoising. We further introduce dynamics registers supervised by a frozen latent action teacher, encouraging the implicit future states to capture interaction-induced transitions such as object motion, contact changes, and task progress. Ground-truth future observations and the teacher are used only during training; deployment requires neither and performs no future video generation. Without embodied robot data pretraining, the standard and accelerated variants of ForeWAM achieve average success rates of 96.7% and 96.9% on LIBERO, respectively. The standard variant further achieves 61.6% success on LIBERO-Plus. These results demonstrate that direct-policy WAMs can retain efficient action prediction while exposing predictive dynamics to the action pathway without explicitly generating future observations.

## Metadata
- **Published**: 2026-08-12T03:27:43Z
- **Authors**: Jiakai Huang, Zhongbo Wu, Zheng Zhang, Zihan Wang, Shan You, Tao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11605v1)