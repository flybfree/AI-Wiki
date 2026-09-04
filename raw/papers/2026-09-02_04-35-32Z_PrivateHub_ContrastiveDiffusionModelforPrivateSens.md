---
title: PrivateHub: Contrastive Diffusion Model for Private Sensor-Intensive Environment Data Generation
published: 2026-09-02T04:35:32Z
authors: Jiechao Gao, Yuandong Pan, Jie Wang, Michael Lepech, Bradford Campbell
url: http://arxiv.org/abs/2609.02958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrivateHub: Contrastive Diffusion Model for Private Sensor-Intensive Environment Data Generation

## Abstract
Sensor-intensive environments enable many intelligent services by inferring user applications from heterogeneous data streams. However, not all applications should be exposed: users want some activities to stay private. This creates a tension between inferring applications for useful services and preventing unwanted inference. Existing approaches such as differential privacy and rule-based filtering protect individual streams but cannot address the privacy risk from cross-sensor inference.   We introduce Privatehub, which uses contrastive learning within a diffusion model to generate synthetic multi-sensor streams that keep non-private applications detectable while concealing private ones. Privatehub has two stages: App-Conditioned Pre-training (ACP), which conditions the model on multi-sensor data with application embeddings, and App-Aware Fine-tuning (AAF), which separates private from non-private data via contrastive learning. We also define a threat model for the multi-sensor sharing setting. Experiments on three real-world multi-sensor datasets show Privatehub lowers private-application accuracy by 40 to 50\% without hurting non-private performance, and stays robust when the attacker retrains on the synthetic data.

## Metadata
- **Published**: 2026-09-02T04:35:32Z
- **Authors**: Jiechao Gao, Yuandong Pan, Jie Wang, Michael Lepech, Bradford Campbell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02958v1)