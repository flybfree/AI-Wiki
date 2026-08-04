---
title: SeDeM: Selective Decompression of Hidden-State Memories for Long-Context Question Answering
url: http://arxiv.org/abs/2608.00311v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_21-44-03Z_SeDeM_SelectiveDecompressionofHidden_StateMemories.md
generated_at: 2026-08-03 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SeDeM, a selective decompression framework that reduces long-context inference cost by storing hidden states in compact memory blocks and expanding only relevant ones during decoding. On four QA benchmarks SeDeM outperforms compression baselines both with 1B and 3B models, achieving higher scores and faster throughput than full-context fine-tuning.

## Key Takeaways
- SeDeM decouples storage of compressed hidden states from decoder conditioning, allowing the decoder to use only selected blocks.  
- The learned selector operates at block level using evidence supervision, improving relevance of retrieved memories.  
- Results show lower online time-to-first-token and higher autoregressive decoding throughput compared with ICAE.

## Context
Long-context processing is a bottleneck for large language models because self‑attention scales quadratically and KV caches grow linearly. Traditional compression methods either require full context or sacrifice accuracy, limiting practical deployment.

## Implications
SeDeM enables cost‑effective generation at very long sequences without sacrificing performance, encouraging adoption of memory‑efficient architectures in industry pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00311v1)
