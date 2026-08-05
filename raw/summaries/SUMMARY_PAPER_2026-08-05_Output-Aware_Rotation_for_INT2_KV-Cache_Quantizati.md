---
title: Output-Aware Rotation for INT2 KV-Cache Quantization
url: http://arxiv.org/abs/2608.02691v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_09-24-23Z_Output_AwareRotationforINT2KV_CacheQuantization.md
generated_at: 2026-08-05 01:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OptR, an output-aware rotation method that reduces post‑W_O attention-output error in INT2 KV-cache quantization. By decomposing the error into key and value contributions, OptR learns orthogonal corrections through the full quantization path and applies a reparameterization that keeps softmax unchanged. Experiments on three models and five benchmarks show consistent gains in QuaRot and OSCAR while maintaining cache format.

## Key Takeaways
- OptR minimizes post‑W_O attention-output error by separating key and value induced components, learning per‑head orthogonal corrections during full INT2 quantization.
- The method uses an attention‑equivalent key reparameterization to reduce large channel offsets without altering the softmax distribution.
- Results improve both QuaRot and OSCAR scores across reasoning and coding tasks while preserving paged KV-cache format with negligible overhead.

## Context
Long‑context LLMs face severe memory and bandwidth constraints, driving interest in ultra‑low‑bit quantization. Traditional rotation techniques often target cache statistics early, ignoring how errors propagate through attention and output projection, which limits performance gains for long sequences.

## Implications
OptR demonstrates that output‑aware optimization can yield higher accuracy without sacrificing inference efficiency, encouraging more holistic design of quantization pipelines. Practitioners may adopt similar error decomposition strategies to balance precision and latency in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02691v1)
