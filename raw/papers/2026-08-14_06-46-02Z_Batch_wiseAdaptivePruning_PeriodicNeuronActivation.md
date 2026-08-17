---
title: Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning for Language Reasoning Model
published: 2026-08-14T06:46:02Z
authors: Yongmin Kim, Shota Takashiro, Yusuke Iwasawa, Takeshi Kojima, Yutaka Matsuo
url: http://arxiv.org/abs/2608.14003v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning for Language Reasoning Model

## Abstract
Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chain-of-thought generation, but incur substantial computational costs during inference. In production settings, batched inference is essential for high throughput, yet the existing training-free adaptive pruning methods we evaluate severely degrade in this regime. Because a batch must share a single pruning mask, these methods aggregate activations across samples and then apply threshold-based selection; the threshold, calibrated offline on unaggregated activations, no longer matches the aggregated distribution, so the realized sparsity ratio drifts and accuracy on reasoning tasks collapses under batched inference.   In this work, we propose a training-free adaptive pruning method designed specifically for batched inference in LRMs, built on two components. First, we replace threshold-based selection with periodic top-k selection over the aggregated importance scores, which is unaffected by the shift that aggregation induces in the activation distribution, and which runs selection once per update period rather than at every token, preserving the speedup. Second, based on the observation that important neurons re-fire periodically during long reasoning generation, we introduce an activation memory that accumulates importance across update phases so that recurring neurons are retained.   Experiments on diverse reasoning benchmarks demonstrate that our method outperforms the previous state-of-the-art adaptive pruning method by 39.7 percentage points in average accuracy at batch size 4 with 50% target sparsity on DeepSeek-R1-Distill-Qwen-7B, and reaches 1.40x speedup over dense inference at 50% actual sparsity.

## Metadata
- **Published**: 2026-08-14T06:46:02Z
- **Authors**: Yongmin Kim, Shota Takashiro, Yusuke Iwasawa, Takeshi Kojima, Yutaka Matsuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14003v1)