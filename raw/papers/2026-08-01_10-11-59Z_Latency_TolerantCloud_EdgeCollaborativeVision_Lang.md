---
title: Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization
published: 2026-08-01T10:11:59Z
authors: Daojie Peng, Fulong Ma, Bingtao Wang, Sheng Wang, Jun Ma
url: http://arxiv.org/abs/2608.00569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization

## Abstract
Deploying billion-parameter Vision-Language-Action (VLA) policies on mobile robots creates a systems conflict: semantic reasoning benefits from cloud GPUs, whereas closed-loop control must respond locally despite network delay and jitter. Existing hierarchical and asynchronous policies improve throughput, but their slow-path representations can still arrive stale or require explicit scheduling and delay cues. We introduce CloudEdgeVLA, a cloud-edge policy that treats temporal misalignment as a representation-learning problem. A cloud VLA encodes delayed observations into slowly varying task features, while a lightweight edge head combines the latest available cloud feature with current local vision. During training, current and randomly delayed frames are paired with the same current action target in fresh and stale paths. This objective encourages the cloud representation to preserve task-level information while the edge path supplies state-sensitive corrections. Across four LIBERO suites, CloudEdgeVLA retains 63.8--78.0% success with a 40-step uniform-delay window, whereas VLASH reaches at most 6.4% and the evaluated single-path baselines at most 3.0%. By removing blocking synchronization from the control loop, the design offers a practical route to scalable VLA deployment in which cloud models can grow while edge computation remains lightweight and responsive.

## Metadata
- **Published**: 2026-08-01T10:11:59Z
- **Authors**: Daojie Peng, Fulong Ma, Bingtao Wang, Sheng Wang, Jun Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00569v1)