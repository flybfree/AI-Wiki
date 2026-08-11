---
title: SpikeWorld: Fast-State Adaptation for Frozen Spiking World Models
published: 2026-08-07T18:57:06Z
authors: Ziqiao Yu
url: http://arxiv.org/abs/2608.07712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpikeWorld: Fast-State Adaptation for Frozen Spiking World Models

## Abstract
A predictive model receives a self-supervised signal whenever the consequence of an action is observed. Using that signal after deployment is difficult when dynamics and semantics share parameters: freezing prevents adaptation, whereas weight updates require optimizer state and may alter the learned representation. Here we introduce SpikeWorld, a 1.45M-parameter sparse spiking model jointly trained for heterogeneous sensory prediction, semantics, image-text binding and action-conditioned dynamics. At deployment, all trained parameters are frozen. Delayed next-state residuals update two external paths: cumulative fixed-bank losses select the bounded action correction, while route-specific residual matrices refine next-state prediction. Neither path uses labels, teacher outputs, rewards, success signals or the true shift value. Joint optimization improves action next-state MSE by 17.10\% while also improving multimodal prediction, semantic accuracy and image-text retrieval. On held-out shear and attenuation streams, the combined external state improves aggregate prediction by 5.48\% and 30.01\%; its fixed-bank action path improves tracking by 24.20\% and 3.94\%, respectively. In a six-arm study comprising 450 new Meta-World trajectories (75 per arm), SpikeWorld raises frozen-policy reward by 7.90 (95\% CI [2.48, 14.06]); the 13.33-point success difference is descriptive (CI [0, 40]). For identical sensory inputs, model parameters and inherited semantic outputs remain bitwise unchanged. A 16-byte RLS estimator obtains the highest non-oracle reward on linear attenuation, showing that the contribution is not superior linear identification, but its integration with a frozen multimodal spiking checkpoint. Reference code is publicly available at https://github.com/Oooorca/SpikeWorld.

## Metadata
- **Published**: 2026-08-07T18:57:06Z
- **Authors**: Ziqiao Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07712v1)