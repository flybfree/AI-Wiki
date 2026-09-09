---
title: One MLLM, One Call: Efficient Zero-Shot Vision-and-Language Navigation via Spatial-Aware Waypoints
published: 2026-09-06T08:49:10Z
authors: Shiqi Pan, Qi Zheng, Hanqin Sun, Youjian Zhang, Daquan Feng, Xu Wang
url: http://arxiv.org/abs/2609.06476v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One MLLM, One Call: Efficient Zero-Shot Vision-and-Language Navigation via Spatial-Aware Waypoints

## Abstract
Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to navigate unseen environments by following natural language instructions. Current zero-shot VLN-CE methods either rely on pre-trained waypoint predictors or require multiple queries to large models per step. To address prohibitive inference latency and computational overhead, we propose O2C-Nav, an efficient zero-shot navigation framework that calls only a single large model once per decision step. Our approach introduces a training-free structured waypoint generator and a novel abstract representation that projects sparse, history-aware candidate waypoints directly onto RGB images as visual markers. The MLLM selects a waypoint or generates a fallback target bounding box at each step, while a low-level Fast Marching Method (FMM) planner converts the selected target into an executable collision-free path. This paradigm provides the model with concrete spatial perception and explicit memory while significantly reducing the visual processing load. Extensive evaluations on the R2R-CE and RxR-CE benchmarks demonstrate that O2C-Nav outperforms current state-of-the-art zero-shot methods, highlighting its great potential for real-time robotic deployment. Code is available at https://github.com/kkpsq/O2C-Nav-Code.

## Metadata
- **Published**: 2026-09-06T08:49:10Z
- **Authors**: Shiqi Pan, Qi Zheng, Hanqin Sun, Youjian Zhang, Daquan Feng, Xu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06476v1)