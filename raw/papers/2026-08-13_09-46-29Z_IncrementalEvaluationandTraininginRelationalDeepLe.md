---
title: Incremental Evaluation and Training in Relational Deep Learning
published: 2026-08-13T09:46:29Z
authors: Jakub Peleška, Gustav Šír
url: http://arxiv.org/abs/2608.13023v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Incremental Evaluation and Training in Relational Deep Learning

## Abstract
Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs to enable end-to-end representation learning. However, prevailing RDL evaluation practices rely on static, single-episode dataset snapshots, overlooking the continuous, time-evolving nature of real-world databases. Consequently, current RDL benchmarks fail to capture how model performance changes as new data accumulates over time. To address this limitation, we introduce an incremental, multi-episode evaluation and training paradigm to assess and improve the temporal robustness and adaptability of state-of-the-art RDL models. Using established large-scale datasets, we examine data evolution and model training dynamics, demonstrating that temporal concept drifts occur in the majority of predictive tasks. We present multiple incremental training regimes for fine-tuning the models and demonstrate that transfer learning is both feasible and highly effective in the RDL setting. Alongside a new temporal evaluation metric that prioritizes near-future accuracy, we show that our incrementally fine-tuned models consistently outperform the standard, expensive, from-scratch trained baselines.

## Metadata
- **Published**: 2026-08-13T09:46:29Z
- **Authors**: Jakub Peleška, Gustav Šír
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13023v1)