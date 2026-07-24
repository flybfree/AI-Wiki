---
title: Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos
published: 2026-07-22T07:45:50Z
authors: Penglei Sun, Yehua Huang, Zhuoli Tao, Xiang Li, Runwei Guan, Yaoxian Song, Kaiyong Zhao, Henghui Ding, Bo Han, Yang Yang, Xiaowen Chu
url: http://arxiv.org/abs/2607.19857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos

## Abstract
Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes. In real UAV deployment, the UAV must respond while it flies, so such perception runs in an online streaming manner, where frames arrive sequentially and the model responds to each one without access to future frames. However, applying current Multimodal Large Language Models (MLLMs) to this setting raises two challenges. First, targets viewed from the air are often tiny, yet the visual compression in existing MLLMs treats all regions equally and discards their fine-grained details. Second, understanding a continuous stream requires past-frame context, yet retaining the entire history is infeasible on resource-constrained onboard hardware, whereas discarding it causes the target to drift or disappear. We address the tiny object and streaming challenges from both data and method perspectives. From the data perspective, we present \textbf{DroneEyes}, the \textbf{first} pixel-level and open-vocabulary referring-segmentation dataset for tiny aerial targets, comprising $2,140$ high-definition videos and $176,623$ pairs across Object Description and Referring Expression tasks, with dense per-frame masks. From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams.

## Metadata
- **Published**: 2026-07-22T07:45:50Z
- **Authors**: Penglei Sun, Yehua Huang, Zhuoli Tao, Xiang Li, Runwei Guan, Yaoxian Song, Kaiyong Zhao, Henghui Ding, Bo Han, Yang Yang, Xiaowen Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19857v1)