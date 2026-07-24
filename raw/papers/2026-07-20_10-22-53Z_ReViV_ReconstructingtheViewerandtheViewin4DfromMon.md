---
title: ReViV: Reconstructing the Viewer and the View in 4D from Monocular Egocentric Video
published: 2026-07-20T10:22:53Z
authors: Xiaozhong Lyu, Gen Li, Zhiyin Qian, Xucong Zhang, Marc Pollefeys, Siyu Tang
url: http://arxiv.org/abs/2607.17790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReViV: Reconstructing the Viewer and the View in 4D from Monocular Egocentric Video

## Abstract
Egocentric devices, such as wearable front-facing cameras, provide a unique perspective for capturing the continuous interaction between a human viewer and the surrounding environment. A holistic and efficient multimodal model capable of reconstructing this 4D representation is therefore highly desirable. However, existing approaches often rely on auxiliary inputs such as pre-computed camera trajectories, treat scene perception and human ego-motion modeling as separate problems despite their strong interdependency, and suffer from slow inference time. To address these limitations, we present ReViV, the first unified framework for holistic egocentric 4D reconstruction that extracts both viewer and view dynamics from a single monocular RGB video. We formulate the task as learning the full joint probability distribution over multimodal signals, including RGB video, camera trajectory, gaze direction, full-body motion, hand motion, and depth. Powered by a Masked Generative Egocentric Transformer, ReViV operates within a single feed-forward architecture to simultaneously reconstruct the temporally consistent 4D reconstruction across the viewer and the view with fast inference speed. Extensive experiments on diverse benchmarks, including HoloAssist, HOT3D, ARCTIC, Aria Digital Twin, and TACO, demonstrate that ReViV achieves state-of-the-art accuracy and efficiency across holistic ego-body, hand, and gaze reconstruction, camera tracking, while maintaining highly competitive egocentric depth estimation without relying on heavy task-specific priors. Code and models are fully open-sourced: https://reviv4d.github.io/.

## Metadata
- **Published**: 2026-07-20T10:22:53Z
- **Authors**: Xiaozhong Lyu, Gen Li, Zhiyin Qian, Xucong Zhang, Marc Pollefeys, Siyu Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17790v1)