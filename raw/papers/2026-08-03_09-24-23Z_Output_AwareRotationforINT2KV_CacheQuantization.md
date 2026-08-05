---
title: Output-Aware Rotation for INT2 KV-Cache Quantization
published: 2026-08-03T09:24:23Z
authors: Vincent-Daniel Yun, Woosang Lim, Minsoo Cheong, Sunwoo Lee, Murali Annavaram, Sai Praneeth Karimireddy, Sungjoo Yoo
url: http://arxiv.org/abs/2608.02691v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Output-Aware Rotation for INT2 KV-Cache Quantization

## Abstract
The key-value (KV) cache has become a major memory and bandwidth bottleneck in long-context large language model inference, making ultra-low-bit quantization increasingly important. However, existing rotation-based INT2 methods optimize cache statistics or proxy errors before the complete attention readout, even though the model is ultimately affected by the error propagated through attention and the output projection $W_O$. To address this mismatch, we propose \textit{OptR}, an output-aware rotation method that minimizes post-$W_O$ attention-output error. OptR decomposes the post-$W_O$ attention-output error into key- and value-induced terms and learns per-head orthogonal corrections through the full INT2 quantization and attention path. OptR further applies an attention-equivalent key reparameterization to reduce large channel-wise offsets without changing the softmax distribution. Across three models and five reasoning and coding benchmarks, OptR consistently improves both QuaRot and OSCAR and strengthens long-context retrieval, while preserving the paged KV-cache format with negligible inference overhead.

## Metadata
- **Published**: 2026-08-03T09:24:23Z
- **Authors**: Vincent-Daniel Yun, Woosang Lim, Minsoo Cheong, Sunwoo Lee, Murali Annavaram, Sai Praneeth Karimireddy, Sungjoo Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02691v1)