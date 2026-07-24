---
title: Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers
url: http://arxiv.org/abs/2607.15456v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_20-58-16Z_LoopedLatentAttention_Cross_LoopKVCompressionforLo.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Looped Latent Attention (LLA) as a codec for looped Transformers that compresses the recurrent key‑value cache by storing low‑rank latents instead of full vectors. It shows that the cache follows a short trajectory across loops, allowing per‑head compression while preserving attention quality. The method is initialized from teacher activations and refined with distillation, achieving exact cache reduction.

## Key Takeaways
- For each fixed token layer head the K/V vectors follow a low‑rank path across loops so a small set of latents can reconstruct them when needed.
- LLA compresses recurrence by 21.3× on H200 while increasing batch capacity from 32 to 768 sequences at 4k context, demonstrating exact reduction without loss.
- The codec remains near‑lossless (≈32×) on long math rollouts and improves MATH‑500 by 4× after refinement.

## Context
Looped Transformers aim to reuse computation across recurrence steps but suffer from large per‑step caches that limit context length. This work addresses the bottleneck by exploiting structural low‑rankness of the cache, offering a scalable solution for long‑context generation tasks.

## Implications
The exact compression and minimal loss make LLA attractive for deploying massive models on limited hardware. Practitioners can adopt it to extend batch sizes or context depth without retraining, accelerating research in efficient large language model serving.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15456v1)
