---
title: UniNav: A Unified World-Action Diffusion Model for Visual Navigation
published: 2026-08-04T07:15:45Z
authors: Changqing Zhou, Yueru Luo, Zeyu Jiang, Changhao Chen
url: http://arxiv.org/abs/2608.03244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniNav: A Unified World-Action Diffusion Model for Visual Navigation

## Abstract
Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visual observations and continuous waypoint trajectories through a single diffusion process. Given history frames and a goal image, UniNav jointly denoises visual and waypoint tokens within a single transformer, unifying future prediction and action generation in a shared framework. To improve spatial grounding, we incorporate geometry-aware camera tokens. We also train on both trajectory-labeled navigation data and video-only data, enabling the model to benefit from diverse videos without waypoint annotations. Based on this unified framework, we introduce two variants: UniNav-Full jointly predicts interpretable future observations and their corresponding trajectories, while UniNav-Fast removes future-image tokens at inference for efficient trajectory prediction. Experiments on navigation benchmarks show that UniNav outperforms the strongest baseline in ATE across all datasets. With one-step inference, UniNav-Fast achieves a latency of 0.1s without a substantial accuracy drop. Code will be released.

## Metadata
- **Published**: 2026-08-04T07:15:45Z
- **Authors**: Changqing Zhou, Yueru Luo, Zeyu Jiang, Changhao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03244v1)