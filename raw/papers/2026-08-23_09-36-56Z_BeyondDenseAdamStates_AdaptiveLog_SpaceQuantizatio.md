---
title: Beyond Dense Adam States: Adaptive Log-Space Quantization for Memory-Efficient Optimizers
published: 2026-08-23T09:36:56Z
authors: Yan Wang
url: http://arxiv.org/abs/2608.22322v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Dense Adam States: Adaptive Log-Space Quantization for Memory-Efficient Optimizers

## Abstract
Low-precision optimizer-state methods are commonly designed for dense Adam-style moments, but memory-efficient optimizers maintain factored, confidence-based, or projected states whose quantization errors propagate differently. We characterize this heterogeneity in optimizer-state traces from language-model pre-training and introduce Adaptive Log-Space (AL) quantization, a block-wise representation for non-negative states that adapts its nonzero range per block while preserving exact zeros. AL8 and AL16 are combined with independent signed-momentum encodings and state-specific precision choices.   Across 96 runs totaling 214.7 GPU-hours, we evaluate AdamW, Adafactor, CAME, and APOLLO paths. On a 20K-step TinyLlama-1.1B benchmark, AdamW with AL8 second moments and 8-bit uniform momentum reaches 72.90 perplexity, versus 72.48 for FP32 and 73.54 for an 8-bit dynamic-quantization baseline, while reducing measured optimizer-state storage from 8392.7 to 2119.2 MiB. CAME requires higher precision for its non-negative states: AL16 reaches 86.16 perplexity versus 86.68 for FP32, while all-AL8 reaches 90.19. In a 100K-step GPT-2 experiment, topology-aware parameter protection reduces the late-loss gap of quantized Adafactor from +0.1185 to +0.0159. These results support state- and topology-aware optimizer quantization. End-to-end comparisons use a single training seed and are reported as empirical measurements.

## Metadata
- **Published**: 2026-08-23T09:36:56Z
- **Authors**: Yan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22322v1)