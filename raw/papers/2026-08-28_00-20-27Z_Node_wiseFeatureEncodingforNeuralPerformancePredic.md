---
title: Node-wise Feature Encoding for Neural Performance Prediction
published: 2026-08-28T00:20:27Z
authors: Matthew Grenier, William Hammer, Andrew Heuer, Nikhil Krishna, Yi Wang, Ramtin Zand
url: http://arxiv.org/abs/2608.27794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Node-wise Feature Encoding for Neural Performance Prediction

## Abstract
As neural networks are increasingly deployed on resource constrained edge devices, accurate prediction of latency and energy is critical for efficient neural architecture search. Existing GNN and transformer based predictors achieve strong results but largely ignore node-level computational cost, limiting their ability to model performance critical operations. To address this, we introduce FeatureFormer, a neural performance predictor that incorporates explicit node-wise encodings of FLOPs, parameter counts, and memory proxies within a gated graph attention architecture. We also present NNEQ, a new large-scale energy consumption dataset that enables unified evaluation of latency and energy prediction. Extensive experiments demonstrate that FeatureFormer achieves state-of-the-art performance across both metrics, including challenging out-of-domain settings. Finally, we show that the proposed encoding is broadly applicable and consistently improves existing predictors with negligible overhead.

## Metadata
- **Published**: 2026-08-28T00:20:27Z
- **Authors**: Matthew Grenier, William Hammer, Andrew Heuer, Nikhil Krishna, Yi Wang, Ramtin Zand
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27794v1)