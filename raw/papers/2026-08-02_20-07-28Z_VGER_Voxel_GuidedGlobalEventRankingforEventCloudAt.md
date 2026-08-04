---
title: VGER: Voxel-Guided Global Event Ranking for Event Cloud Attribution
published: 2026-08-02T20:07:28Z
authors: Youxin Jiang, Baoheng Fu, Hongwei Ren, Xiangqian Wu
url: http://arxiv.org/abs/2608.01470v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VGER: Voxel-Guided Global Event Ranking for Event Cloud Attribution

## Abstract
Event cameras produce sparse and asynchronous event streams that provide rich spatio-temporal information for efficient perception. Recent advances in event-based models have demonstrated strong performance by directly modeling asynchronous events without dense frame reconstruction. However, identifying the event-level evidence behind their predictions is crucial for improving model transparency and reliability. Directly adapting point-level saliency methods from point clouds provides fine-grained attribution but overlooks event-specific spatio-temporal structures. To address this limitation, we propose Voxel-Guided Global Event Ranking (VGER), a training-free attribution framework for point-based event cloud networks. VGER combines event-level gradient evidence with task-aware voxel perturbation evidence, transferring regional contribution into event-level attribution scores while preserving fine-grained resolution. Furthermore, VGER introduces a unified event ranking strategy, where high-ranked events are expected to be prediction-critical and low-ranked events are expected to have limited influence on predictions. We evaluate VGER on three event-based benchmarks with PointNet, PointNet++, and EventMamba. Across nine dataset-backbone settings, VGER consistently improves both high-tail and low-tail deletion performance over point-level saliency baselines.

## Metadata
- **Published**: 2026-08-02T20:07:28Z
- **Authors**: Youxin Jiang, Baoheng Fu, Hongwei Ren, Xiangqian Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01470v1)