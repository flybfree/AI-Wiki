---
title: Unsupervised Continual Learning with Growing Self-Organizing Maps and Synthetic Replay
published: 2026-08-27T19:48:44Z
authors: Pujan Thapa, Alexander Ororbia, Travis Desell
url: http://arxiv.org/abs/2608.27662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unsupervised Continual Learning with Growing Self-Organizing Maps and Synthetic Replay

## Abstract
This work presents a generative continual learning framework based on growing self-organizing maps (GSOMs) that are augmented with learned distributional statistics as well as encoder-decoder models for class-incremental learning. The proposed approach enables exemplar-free replay using distributional statistical memory, which eliminates the need to store raw data. Each GSOM unit maintains its own mean, variance, and covariance estimates, which are subsequently used to generate synthetic samples for replay; in encoder-decoder configurations, these samples are then decoded back into the input space (via ancestral sampling) for subsequent training. Our method is fully unsupervised, as it does not rely on explicit task boundaries or class labels during training. Results across multiple benchmarks show that the proposed approach achieves performance competitive even with supervised state-of-the-art memory-based methods while consistently outperforming memory-free approaches. In several settings, our framework matches or exceeds existing baselines, particularly in challenging single-class incremental scenarios. We also provide baseline results for single-class incremental TinyImageNet and MiniImageNet, offering a useful reference for future work. This work highlights the effectiveness of an unsupervised, adaptive, topology-driven neural form of statistical replay as a scalable, flexible approach to continual learning.

## Metadata
- **Published**: 2026-08-27T19:48:44Z
- **Authors**: Pujan Thapa, Alexander Ororbia, Travis Desell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27662v1)