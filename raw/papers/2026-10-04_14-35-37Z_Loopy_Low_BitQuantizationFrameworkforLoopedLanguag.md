---
title: Loopy: Low-Bit Quantization Framework for Looped Language Models
published: 2026-10-04T14:35:37Z
authors: Zeyu LI, Yipu ZHANG, Jintao Chen, Xin LI, Wei ZHANG
url: http://arxiv.org/abs/2610.05265v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loopy: Low-Bit Quantization Framework for Looped Language Models

## Abstract
Looped language models provide a parameter-efficient way to scale iterative test-time computation by repeatedly executing a shared recurrent core. Post-training quantization (PTQ) can reduce the memory footprint and inference cost of looped language models, but errors introduced by a quantized shared core affect subsequent cores. Among PTQ methods, channel scaling and orthogonal rotations preserve the floating-point computation while producing representations with different quantization quality. We find that quantization configuration candidate rankings can change with recurrent depth, motivating configuration selection at the target deployment depth. However, evaluating every candidate over the full calibration set at this depth is costly. We therefore propose Loopy, a PTQ framework that formulates shared-core quantization through a recurrent-depth-aware objective, selecting shared low-bit representations by their final prediction loss at the target deployment depth. Channel scaling and orthogonal rotations parameterize the candidate representations. To approximately solve this selection problem efficiently, Loopy progressively allocates calibration windows to promising candidates while preserving complete target-depth execution, using only forward evaluations. Across eight settings, Loopy achieves the state-of-the-art results among different baselines. On Ouro-1.4B under W4A4, Loopy reduces LAMBADA perplexity by 36.5% relative to SpinQuant. Our code is available at https://github.com/Shameless0817/Loopy-review.git.

## Metadata
- **Published**: 2026-10-04T14:35:37Z
- **Authors**: Zeyu LI, Yipu ZHANG, Jintao Chen, Xin LI, Wei ZHANG
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05265v1)