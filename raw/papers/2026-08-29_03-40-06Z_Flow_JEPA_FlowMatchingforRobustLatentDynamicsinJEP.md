---
title: Flow-JEPA: Flow Matching for Robust Latent Dynamics in JEPA World Models
published: 2026-08-29T03:40:06Z
authors: Yanchen Huo, Ziying Song, Yadan Luo
url: http://arxiv.org/abs/2608.29029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flow-JEPA: Flow Matching for Robust Latent Dynamics in JEPA World Models

## Abstract
Joint-Embedding Predictive Architectures (JEPAs) have shown strong potential for learning compact predictive representations, and LeWorldModel (LeWM) extends this paradigm to reconstruction-free latent world modeling from pixels. However, its deterministic autoregressive predictor generates future states through repeated one-step transitions, which can accumulate errors and remain sensitive to task-irrelevant visual perturbations. In this work, we propose Flow-JEPA (F-JEPA), a conditional flow matching dynamics model that jointly generates a sequence of future latent states conditioned on the current observation and actions. A Gaussian distribution serves as the flow source, exposing the vector field to perturbed latent trajectories as it learns to transport them toward clean future representations. This formulation retains the reconstruction-free JEPA framework while replacing point-wise transition regression with stochastic trajectory-level prediction. F-JEPA raises mean success from $86\%$ to $92\%$ under clean observations and from $67\%$ to $86\%$ under noisy conditions, suggesting that conditional flow matching provides a promising alternative to deterministic autoregressive dynamics in JEPA world models.

## Metadata
- **Published**: 2026-08-29T03:40:06Z
- **Authors**: Yanchen Huo, Ziying Song, Yadan Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29029v1)