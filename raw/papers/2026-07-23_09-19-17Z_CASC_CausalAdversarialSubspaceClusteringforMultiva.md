---
title: CASC: Causal Adversarial Subspace Clustering for Multivariate Spatiotemporal Data
published: 2026-07-23T09:19:17Z
authors: Francis Ndikum Nji, Vandana Janeja, Jianwu Wang
url: http://arxiv.org/abs/2607.21088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CASC: Causal Adversarial Subspace Clustering for Multivariate Spatiotemporal Data

## Abstract
Deep subspace clustering plays a critical role in applications involving multivariate spatiotemporal data, such as sea ice monitoring, disease spread analysis, and tracking neuro-degeneration over time. Despite recent advances, existing methods primarily rely on geometric self-expressiveness, assume static subspace structures, and often fail to capture causal dependencies, local spatial interactions, and long-range temporal dynamics inherent in complex spatiotemporal systems. To address these limitations, we propose a novel Causal Adversarial Subspace Clustering (CASC) framework for discovering evolving latent regimes in high-dimensional spatiotemporal data. CASC integrates a U-Net-inspired deep adversarial clustering architecture with stacked FAConvLSTM layers to preserve spatial and temporal structure while learning robust latent representations. A graph attention transformer-based self-expressive network is introduced to jointly model local spatial relationships, global dependencies, and long-range temporal interactions. Furthermore, we propose two new learning objectives: (1) a Causal Subspace Preservation Loss that aligns self-expression coefficients with latent causal relationships, encouraging clusters to reflect underlying causal processes rather than simple feature similarity, and (2) a Dynamic Temporal Subspace Evolution Loss that captures evolving subspace structures and temporal regime transitions in nonstationary environments. Together, these components transform deep subspace clustering from a correlation-driven paradigm into a causal-temporal regime discovery framework.

## Metadata
- **Published**: 2026-07-23T09:19:17Z
- **Authors**: Francis Ndikum Nji, Vandana Janeja, Jianwu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21088v1)