---
title: Point2Radio: A Foundation Model for Cross-Scene Radio Fields from Material-Aware Point Clouds
published: 2026-07-31T03:45:29Z
authors: Chaozheng Wen, Chenghong Bian, Hongze Chen, Jun Zhang
url: http://arxiv.org/abs/2607.28994v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Point2Radio: A Foundation Model for Cross-Scene Radio Fields from Material-Aware Point Clouds

## Abstract
High-fidelity radio fields are typically simulated for every scene--transmitter configuration or fitted separately to each scene, failing to exploit propagation structures shared across environments. We present Point2Radio, a foundation model that learns a transferable propagation prior from multiple environments. Given a material-aware point cloud and a transmitter (TX) setting, a common encoder produces a TX-conditioned scene representation that can be queried at arbitrary receiver (RX) locations. Task-specific query decoders map this representation to different radio quantities, e.g., three-dimensional (3D) path-gain (PG) fields and power angular spectra (PAS). At inference for a new scene, the model uses only a material-aware point cloud and transceiver queries, running in milliseconds on a single GPU without meshes or explicit path tracing. We evaluate PG prediction on a scene-disjoint split of a 337-scene corpus containing 86,272 TX-conditioned fields. Point2Radio achieves 0.871 dB mean absolute error (MAE), reducing error by 76.7% relative to a same-split UNet-style baseline. The same encoder also supports PAS prediction via a task-specific decoder. Experiments further show that light target-scene fine-tuning improves adaptation to a specific environment.

## Metadata
- **Published**: 2026-07-31T03:45:29Z
- **Authors**: Chaozheng Wen, Chenghong Bian, Hongze Chen, Jun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28994v1)