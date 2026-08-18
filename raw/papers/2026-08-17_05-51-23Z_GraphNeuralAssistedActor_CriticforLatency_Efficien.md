---
title: Graph Neural Assisted Actor-Critic for Latency-Efficient Edge Vision System
published: 2026-08-17T05:51:23Z
authors: Alam Noor, Luis Almeida, Kai Li, Jiyan Wu, Miguel Gutiérrez Gaitán, Eduardo Tovar
url: http://arxiv.org/abs/2608.16142v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph Neural Assisted Actor-Critic for Latency-Efficient Edge Vision System

## Abstract
UAV on-board vision systems are widely used for different activities, including monitoring in no-fly zones. In this case, the vision-equipped UAV streams a video to a ground server where an operator assists its activities. The latency of video transmission has a profound impact on the effectiveness of the operator assistance. However, most techniques available for video transmission still incur significant latency costs. In this paper, we propose a graph convolutional neural network-assisted (GCN-Assisted A2C) deep reinforcement learning (DRL) system model to find the optimal pixel-correlated area of a suspicious object. We combine the Lagrangian dual form with gradient descent to prevent lack of convergence and over- and under-penalization constraint violation during latency optimization. The proposed system model sends a sub-group pixel-correlated area of the frame from the UAV to the server rather than the transmission of the whole video frame. The proposed framework utilizes the GCN model to explore hidden representations of feature-correlated groups of pixels. Moreover, the GCN supervises the A2C model, which selects a subgroup to enhance transmission latency, thus supervising the training of UAV actions in A2C. Experimental results show that GCN-assisted A2C reduces video frame transmission latency together with false detection rate in UAV vision systems over other DRL and state-of-the-art models.

## Metadata
- **Published**: 2026-08-17T05:51:23Z
- **Authors**: Alam Noor, Luis Almeida, Kai Li, Jiyan Wu, Miguel Gutiérrez Gaitán, Eduardo Tovar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16142v1)