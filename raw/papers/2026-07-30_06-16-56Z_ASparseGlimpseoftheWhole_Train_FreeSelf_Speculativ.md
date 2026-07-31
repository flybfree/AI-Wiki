---
title: A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding
published: 2026-07-30T06:16:56Z
authors: Yuesong Liu, Yuan Zeng, Min Lyu, Ruilin Liu, Yu Guo, Yinlong Xu
url: http://arxiv.org/abs/2607.27735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding

## Abstract
Speculative decoding alleviates the memory-bandwidth bottleneck in large language model inference, but its acceleration is jointly constrained by drafting overhead, token acceptance, and speculation length. We present a unified efficiency analysis showing that extending the speculation horizon can reduce rather than improve speedup when the marginal acceptance probability falls below the relative drafting cost. Guided by this analysis, we introduce SparseSpec-L, a training-free self-speculative decoding framework for long-context inference. SparseSpec-L generates lightweight drafts directly from the target model using a dynamically sparsified and recallable KV cache. It recycles per-head attention statistics produced during full-context verification as a no-extra-forward importance signal, allowing critical historical tokens to be recalled without permanently discarding the dense KV cache. An online entropy-based controller further selects the speculation length according to expected step-wise efficiency. Experiments across multiple long-context tasks and model scales show consistent end-to-end acceleration, with up to speedup over autoregressive decoding while preserving the target model's output distribution.

## Metadata
- **Published**: 2026-07-30T06:16:56Z
- **Authors**: Yuesong Liu, Yuan Zeng, Min Lyu, Ruilin Liu, Yu Guo, Yinlong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27735v1)