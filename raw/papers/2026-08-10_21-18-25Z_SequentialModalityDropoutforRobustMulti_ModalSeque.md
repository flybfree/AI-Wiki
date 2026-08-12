---
title: Sequential Modality Dropout for Robust Multi-Modal Sequential Recommendation
published: 2026-08-10T21:18:25Z
authors: Guanqun Yang, Wenlong Zhang
url: http://arxiv.org/abs/2608.10240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sequential Modality Dropout for Robust Multi-Modal Sequential Recommendation

## Abstract
Multi-modal sequential recommenders assume every item carries every modality, but real product catalogs often miss images or text, and a model trained on complete data loses much of its recommendation accuracy when a modality is unavailable at serving time. We propose Sequential Modality Dropout (SMD): during training, each modality stream (image and text) is independently erased with probability p for an entire user interaction history, so the model learns to predict the next item without relying on any single modality. We measure robustness by retention, the fraction of a model's full-modality accuracy (HR@10) that survives when a modality is removed at test time. Across four backbones (MM-SASRec, IISAN, MISSRec, and fMRLRec) on four Amazon domains, SMD raises text retention by 1.0 to 3.2x at essentially no cost to full-modality accuracy; under an extreme 95% per-item missing rate, it retains 61% of HR@10 versus 22% without (a 2.8x improvement). An optional cross-modal reconstruction loss further lifts retention from 90% to 98% on a simple additive backbone under severe text missingness. SMD is a four-line, architecture-agnostic change that makes multi-modal sequential recommenders robust to the missing modalities they actually encounter in deployment.

## Metadata
- **Published**: 2026-08-10T21:18:25Z
- **Authors**: Guanqun Yang, Wenlong Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10240v1)