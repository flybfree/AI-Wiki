---
title: MobiWave: Dispatch-Oriented Graph Wavelets and Drift-Guided Selective Optimization for Autonomous Fleet Rebalancing
published: 2026-07-27T12:39:04Z
authors: Xiao Han, Pinbo Wang, Yuanshao Zhu, Guojiang Shen, Xiangjie Kong
url: http://arxiv.org/abs/2607.24365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MobiWave: Dispatch-Oriented Graph Wavelets and Drift-Guided Selective Optimization for Autonomous Fleet Rebalancing

## Abstract
Autonomous fleets enable mobility platforms to coordinate idle vehicles directly, making fleet-wide rebalancing possible. However, two obstacles limit reliable deployment: overlapping regional and local traffic patterns can hide roads that remain useful for dispatch, and mobility drift can make a trained policy unreliable. Existing spatial aggregation mixes these patterns, while updating all parameters from limited recent data is costly and can damage stable knowledge. We propose \name, a framework that connects a dispatch-oriented multi-scale graph wavelet module with Drift-Guided Layer-Selective Optimization (DGLS). The first module addresses the representation challenge by separating graph-frequency patterns and weighting each scale according to its value for demand prediction and feasible rebalancing. DGLS addresses the adaptation challenge by measuring Dispatch-weighted Spectral Drift, selecting affected layers within a resource budget, and separating short shocks from persistent changes through a drift-aware fast--slow update. Candidate validation further rejects updates that fail to improve held-out dispatch reward without worsening monitored service or safety constraints. Experiments on both real-world datasets and simluated environments demonstrate the effectiveness of \name\ in comparing with state-of-the-art methods. The source code and datasets are available at https://anonymous.4open.science/r/MobiWave-40F8/.

## Metadata
- **Published**: 2026-07-27T12:39:04Z
- **Authors**: Xiao Han, Pinbo Wang, Yuanshao Zhu, Guojiang Shen, Xiangjie Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24365v1)