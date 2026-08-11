---
title: Linearized 2-Simplicial Attention
url: http://arxiv.org/abs/2608.09307v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
generated_at: 2026-08-11 13:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a linearized version of 2-simplicial attention that rewrites the trilinear score as an inner product between a composite query and key, enabling the sum over one axis to resemble ordinary softmax attention while retaining global reach via a fixed‑size state. It stores the entire past in this state and processes only recent tokens explicitly over a short window, achieving linear cost per token. The model attains the highest mean downstream accuracy at 16k context, improving LAMBADA perplexity from 715.6 to 602.6.

## Key Takeaways
- The trilinear score is transformed into an inner product between a composite query and key, allowing the sum over one axis to resemble ordinary softmax attention.
- Positive random features approximate the sum, storing past in fixed‑size state while recent tokens are processed explicitly over a short window, yielding linear cost per token.
- Under matched compute, this model outperforms KDA hybrid at 16k context, reducing LAMBADA perplexity from 715.6 to 602.6.

## Context
This work addresses the quadratic complexity of standard attention in long sequences, a persistent bottleneck for large language models. By enabling global reach with linear cost, it aligns with trends toward efficient, scalable transformer variants that can handle longer contexts without sacrificing performance or memory usage.

## Implications
Practitioners can adopt this architecture to build models that scale to 16k contexts without sacrificing performance or memory, potentially lowering inference latency and hardware demands in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09307v1)
