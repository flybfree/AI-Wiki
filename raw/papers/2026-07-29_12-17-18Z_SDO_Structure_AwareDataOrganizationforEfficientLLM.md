---
title: SDO: Structure-Aware Data Organization for Efficient LLM Post-Training
published: 2026-07-29T12:17:18Z
authors: Jinliang Gao, Ning Yang, Hai Wang, Baili Xiao, Pin Lyu
url: http://arxiv.org/abs/2607.27273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SDO: Structure-Aware Data Organization for Efficient LLM Post-Training

## Abstract
Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules. However, data organization itself is usually treated as a static preprocessing step: embedding-based grouping methods construct fixed partitions before training and cannot adapt to the evolving sample exposure during optimization. As a result, all samples receive similar exposure despite their different optimization needs, leading to redundant updates for some samples while leaving others under-optimized. To address this problem, we propose SDO (Structure-Aware Data Organization), a plug-and-play data organization framework with an exposure-driven feedback mechanism that organizes mini-batch composition and sample exposure according to representation-space structure. SDO operates epoch by epoch on frozen external embeddings, avoiding model warm-up training overhead: within each epoch, locality-aware batching forms coherent mini-batches via KNN neighborhood traversal; across epochs, exposure-balanced scheduling records per-sample participation and reduces the sampling probability of over-exposed samples to preserve long-term coverage. Across SFT, DPO, and GRPO, SDO accelerates convergence, with the largest gains observed in the early-to-mid phase, producing more coherent gradients and more balanced accuracy across question types without permanently excluding training samples.

## Metadata
- **Published**: 2026-07-29T12:17:18Z
- **Authors**: Jinliang Gao, Ning Yang, Hai Wang, Baili Xiao, Pin Lyu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27273v1)