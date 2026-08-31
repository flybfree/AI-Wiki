---
title: Blog: Survey of Optimizers
published: 2026-08-28T17:35:11Z
authors: Ruoran Xu
url: http://arxiv.org/abs/2608.28557v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Blog: Survey of Optimizers

## Abstract
Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinates to matrices and layers, from fixed training horizons to policies over time, and from mathematical update rules to state representations that must survive sharding and low-precision computation. This survey organizes recent optimizers and training optimization methods along four largely independent axes: temporal estimation, update geometry, horizon management, and representation and systems. It connects the spectral normalization of Muon, the historical matrix statistics of Shampoo and SOAP, adaptive and hybrid matrix methods, memory-efficient optimizers, schedule-free training, small-batch corrections, and quantized optimizer states. The central empirical conclusion is deliberately non-triumphal: matrix-aware methods represent a genuine advance, but there is no context-independent replacement for AdamW. Rankings change with model scale, data-to-parameter ratio, batch size, schedule, parameter partition, tuning budget, and whether the target metric is tokens, FLOPs, wall-clock time, or memory. The practical consequence is a compositional view of optimizer design and a stricter protocol for evaluating optimizer claims.

## Metadata
- **Published**: 2026-08-28T17:35:11Z
- **Authors**: Ruoran Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28557v1)