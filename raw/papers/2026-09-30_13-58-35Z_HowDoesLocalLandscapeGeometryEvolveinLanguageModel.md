---
title: How Does Local Landscape Geometry Evolve in Language Model Pre-Training?
published: 2026-09-30T13:58:35Z
authors: Zhanpeng Zhou, Yuhan Sun, Bingrui Li, Jinbo Wang, Huaijin Wu, Lei Wu, Junchi Yan
url: http://arxiv.org/abs/2609.39767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Does Local Landscape Geometry Evolve in Language Model Pre-Training?

## Abstract
The scale and expense of pre-training language models make efficient hyperparameter tuning essential, yet a principled guidance is still missing. In this work, we analyze language model pre-training dynamics from a local landscape geometry perspective. Our study reveals two distinct phases. In Phase I, sharpness of the local landscape is initially high, leading to instability and loss plateaus under large learning rates (LRs). The landscape shifts from sharp to flatter regions early in training. This dynamic explains the necessity of LR warmup and further suggests that larger peak LRs require proportionally longer warmup periods. In Phase II, the local landscape is governed by the gradient noise scale. Our theory identifies a depth flatness trade-off: high noise from smaller batches widens the loss basin, whereas reduced noise from larger batches deepens it. This theory motivates a dynamic batch-size (BS) scheduler that begins with a small BS and increases it late in training. Together, we provide a unified view of loss landscape evolution, which translates into actionable tuning strategies for large-scale pre-training.

## Metadata
- **Published**: 2026-09-30T13:58:35Z
- **Authors**: Zhanpeng Zhou, Yuhan Sun, Bingrui Li, Jinbo Wang, Huaijin Wu, Lei Wu, Junchi Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39767v1)