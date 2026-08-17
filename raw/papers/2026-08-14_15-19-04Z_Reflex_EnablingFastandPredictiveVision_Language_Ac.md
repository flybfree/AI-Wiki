---
title: Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation
published: 2026-08-14T15:19:04Z
authors: Yuxuan Chen, Wanruo Zhang, Xiao Li
url: http://arxiv.org/abs/2608.14379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation

## Abstract
Vision-Language-Action (VLA) models have recently achieved promising performance in robotic manipulation. However, existing benchmarks mainly evaluate generalization on static manipulation tasks and largely overlook dynamic interaction scenarios. To address this gap, we present ReflexBench, a benchmark for reaction-critical manipulation. ReflexBench contains six dynamic tasks and introduces an evaluation framework that decouples simulator stepping from robot control while supporting configurable latency under synchronous and asynchronous inference. Building upon ReflexBench, we propose ReflexVLA, an efficient VLA model designed for reaction-critical manipulation without large-scale robot-data pretraining. ReflexVLA enhances temporal reasoning through latent future prediction and multi-frame temporal fusion within the vision backbone, while reducing deployment latency through batched visual encoding and CUDA Graph replay. Experiments show that ReflexVLA consistently improves dynamic manipulation performance while maintaining competitive accuracy on standard static manipulation benchmarks, and real-world experiments further demonstrate its effectiveness under practical deployment conditions. Project website: https://reflexvla.github.io

## Metadata
- **Published**: 2026-08-14T15:19:04Z
- **Authors**: Yuxuan Chen, Wanruo Zhang, Xiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14379v1)