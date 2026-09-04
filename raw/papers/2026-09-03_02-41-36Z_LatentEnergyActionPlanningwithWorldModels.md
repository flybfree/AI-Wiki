---
title: Latent Energy Action Planning with World Models
published: 2026-09-03T02:41:36Z
authors: Phu Pham, Aniket Bera
url: http://arxiv.org/abs/2609.03294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent Energy Action Planning with World Models

## Abstract
Latent world models support efficient model predictive control from high-dimensional observations, yet optimizing a single learned latent objective can favor action sequences whose decoder-predicted terminal descriptor does not match the goal descriptor. We introduce Latent Energy Action Planning (LEAP), which treats the complete action horizon as a differentiable variable and optimizes it through a frozen LeWorldModel (LeWM). LEAP couples terminal latent goal matching with a terminal-window state energy. Low energy requires the predicted terminal latent to agree with the goal latent and the decoder-predicted terminal descriptor to agree with the goal descriptor. A frozen goal-conditioned proposal initializes the search, a quasi-Newton solver refines actions through the autoregressive rollout, and post-optimization projection enforces the admissible action range. Across four control domains using the officially released LeWM checkpoints, the complete LEAP planning system raises mean success from 77.5% for LeWM planned with the cross-entropy method (LeWM+CEM) to 94.8% under a matched protocol, a 17.3-percentage-point improvement, while retaining the frozen LeWM representation and predictor.

## Metadata
- **Published**: 2026-09-03T02:41:36Z
- **Authors**: Phu Pham, Aniket Bera
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03294v1)