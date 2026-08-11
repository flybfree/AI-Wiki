---
title: VeinCast: Physics-Guided Dynamic Field Graphs with Graph-Conditioned Fusion for Global Medium-Range Weather Forecasting
published: 2026-08-10T08:39:52Z
authors: Zhisheng Chen, Jinhan Li, Yuxuan Li, Yuan Gao, Hao Wu, Zheng Lu, Jinlong Du, Kun Wang, Bo An
url: http://arxiv.org/abs/2608.09286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VeinCast: Physics-Guided Dynamic Field Graphs with Graph-Conditioned Fusion for Global Medium-Range Weather Forecasting

## Abstract
Global medium-range weather forecasting requires modeling structured yet state-dependent interactions among heterogeneous atmospheric fields. Existing data-driven models largely learn these interactions implicitly, whereas equation-level physical constraints may inherit approximation and model-form biases. We present VeinCast, a physics-guided dynamic field graph and graph-conditioned fusion framework that jointly forecasts 69 surface and upper-air fields. Within each local window, its Physics-Guided Dynamic Field Graph combines predefined atmospheric relations with state-dependent Top-K residual edges and adapts Earth-window attention using the resulting graph context. Graph-Conditioned Latent Fusion further employs graph context and source-node centrality to guide field-to-latent aggregation, while bounded feedback preserves field-specific information. On the $1.5^\circ$ ERA5 benchmark, VeinCast demonstrates competitive forecasting performance across all 69 meteorological fields at lead times of up to 14 days, compared with representative global weather forecasting models including FuXi, Pangu-Weather, GraphCast, FengWu, and ARROW. Ablations confirm that the two modules provide complementary gains, demonstrating the effectiveness of relational-level physical guidance for data-driven weather forecasting.

## Metadata
- **Published**: 2026-08-10T08:39:52Z
- **Authors**: Zhisheng Chen, Jinhan Li, Yuxuan Li, Yuan Gao, Hao Wu, Zheng Lu, Jinlong Du, Kun Wang, Bo An
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09286v1)