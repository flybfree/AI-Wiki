---
title: Personalized Federated Sparse Adaptation of Time-Series Foundation Models
published: 2026-08-05T11:01:47Z
authors: Priyanka Nihalchandani, Naman Srivastava, Varun Ojha, Pandarasamy Arjunan
url: http://arxiv.org/abs/2608.04695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personalized Federated Sparse Adaptation of Time-Series Foundation Models

## Abstract
Federated adaptation of time-series foundation models (TSFMs) is attractive for building energy forecasting because meter data are private, distributed, and highly non-IID. However, a single parameter-sharing strategy is unlikely to serve all pretrained TSFMs or building clients: fully shared adapters can suppress building-specific temporal behavior, while fully local adaptation discards cross-building transfer. We propose a personalized federated sparse adaptation framework with a heterogeneous temporal mixture-of-experts (MoE) adapter placed after the pretrained TSFM representation. A sequence-level router maps each 168-hour context window to a top-$k$ subset of experts specialized for periodicity, long-range interactions, local variation, trend-residual structure, and multi-resolution behavior. We compare global FL, local training, and personalized FL variants with globally shared or client-private expert banks. Across 50 buildings and three TSFM backbones, personalization consistently outperforms Global FL-MoE and Local MoE, while the best sparse-adaptation strategy varies by backbone and metric. Routing behavior further reveals client-level expert specialization, expert concentration, and near-uniform routing across backbones, showing that federated TSFM adaptation should be both client-aware and backbone-aware.

## Metadata
- **Published**: 2026-08-05T11:01:47Z
- **Authors**: Priyanka Nihalchandani, Naman Srivastava, Varun Ojha, Pandarasamy Arjunan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04695v1)