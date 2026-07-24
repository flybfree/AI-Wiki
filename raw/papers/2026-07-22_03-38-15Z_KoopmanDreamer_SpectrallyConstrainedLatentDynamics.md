---
title: Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination
published: 2026-07-22T03:38:15Z
authors: Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan, Xin Xu
url: http://arxiv.org/abs/2607.19719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination

## Abstract
Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. Its Koopman-inspired backbone uses two-dimensional rotation--scaling blocks with bounded radii to represent damping, rotation, and near-periodic modes. Linear and low-rank bilinear action terms capture global and state-dependent control effects, while stochastic-state modulation supplies local correction information. To reduce the mismatch between posterior-conditioned training and prior-only imagination, the model combines posterior-conditioned EMA teacher targets with one-step consistency, multi-step rollout, and open-loop observation-prediction objectives. We further derive a multi-step rollout-error bound that separates amplification by the spectral backbone and bilinear interaction from the additive effects of stochastic-state mismatch and modeling residuals, clarifying the trade-off between error attenuation and long-term information retention. Experimental results on proprioceptive continuous-control tasks from the DeepMind Control Suite and UAV-LiDAR autonomous navigation demonstrate that Koopman Dreamer improves the stability of long-horizon latent rollouts and achieves stronger closed-loop control performance on tasks that rely on high-quality multi-step imagination.

## Metadata
- **Published**: 2026-07-22T03:38:15Z
- **Authors**: Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan, Xin Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19719v1)