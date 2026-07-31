---
title: A Query-Efficient Stochastic Volume Rendering Framework for Time-Varying Implicit Neural Volumes
published: 2026-07-30T11:27:06Z
authors: Alper Sahistan, Haichao Miao, Zhimin Li, Peer-Timo Bremer, Joshua A Levine, Valerio Pascucci
url: http://arxiv.org/abs/2607.28047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Query-Efficient Stochastic Volume Rendering Framework for Time-Varying Implicit Neural Volumes

## Abstract
Time-varying implicit neural representations (INRs) provide a compact representation of scientific volumes and, for modalities such as dynamic X-ray computed tomography (CT), are often the only practical way to represent the data. However, interactive volume rendering of INRs is challenging, as cheap memory lookups are replaced by expensive neural inferences, hindering the performance. Therefore, conventional volume rendering methods such as ray marching with dense sampling are often impractical. While resampling, caching, and retraining can mitigate this cost, they compromise convenience and accuracy and become impractical for time-varying data. We tackle these challenges using a query-efficient stochastic volume rendering framework based on delta tracking. Our system employs a four-stage pipeline that exploits heterogeneous parallelism, using ray tracing cores for traversal and tensor cores for batched neural evaluation. Furthermore, we present strategies to reduce INR queries via ray budgeting and query pruning, thereby increasing per-frame performance. Using our renderer, many time-varying INRs can be rendered directly from their original representation. The system achieves ~30-40 FPS at 1024x1024 resolution on an RTX 4090 GPU and converges to high-fidelity images. Moreover, the system enables interactive temporal exploration of the continuous domain, with timestep updates taking approximately 1-2 ms.

## Metadata
- **Published**: 2026-07-30T11:27:06Z
- **Authors**: Alper Sahistan, Haichao Miao, Zhimin Li, Peer-Timo Bremer, Joshua A Levine, Valerio Pascucci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28047v1)