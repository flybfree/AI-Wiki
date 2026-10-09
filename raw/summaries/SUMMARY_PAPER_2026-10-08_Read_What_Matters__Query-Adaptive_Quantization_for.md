---
title: Read What Matters: Query-Adaptive Quantization for KV Caches
url: http://arxiv.org/abs/2610.11245v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_04-47-41Z_ReadWhatMatters_Query_AdaptiveQuantizationforKVCac.md
generated_at: 2026-10-08 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReadKV addresses a fundamental mismatch in KV-cache management: cache entries are stored before future queries are known, yet each decoding query demands precision in different locations. The paper introduces a progressive quantization scheme where keys and values are stored in multi-resolution codes, and each query adaptively allocates read budgets to key channels and value tokens based on its specific attention needs. Across six base models, the method achieves near-lossless quality (≤0.66% C4 perplexity increase) while reading only four bits from an eight-bit cache, using roughly a quarter of the logical reads and half the retained capacity of a 16-bit cache, and demonstrates 39% lower latency than TurboQuant on tested hardware.

## Key Takeaways
- ReadKV uses a two-stage query-adaptive allocation: first, key-channel prefixes are selected using the query vector to reconstruct keys for attention computation; second, value-token prefixes are allocated using the resulting attention weights. Stored cache entries remain unchanged across queries, meaning the progressive code prefixes support multiple reconstruction precisions without re-encoding. Each stage optimizes a calibrated distortion objective under a fixed bit budget, and the authors prove exact allocation under diminishing refinement gains while connecting these objectives to attention-output error bounds.
- The paper provides a theoretical proof that query-dependent access strictly outperforms every query-independent reader at the same read budget, even when competing encoders and decoders are unrestricted. This is demonstrated through a finite-dimensional attention family, establishing that adaptivity is not merely an engineering convenience but a fundamental information-theoretic advantage for KV-cache reading.
- Empirically, reading four bits on average from an eight-bit cache increases C4 perplexity by at most 0.66% across six base models, consistently outperforming a baseline that stores and fully reads four bits at the same payload-read budget. On an NVIDIA A10G with an 8K-token, batch-one, single-layer workload, a restricted eight-bit ReadKV reader with a two-bit mean payload-read budget achieves 39% lower latency than the TurboQuant codec, with additional quality validation on long-context QA and retrieval tasks using two instruction-tuned models.

## Context
KV-cache memory has become the dominant bottleneck in long-context transformer inference, where bytes moved per decoding step overwhelm weight-loading costs. Existing quantization methods like TurboQuant apply uniform compression to cache entries, ignoring the fact that different queries attend to different key channels and value tokens with varying precision needs. ReadKV sits at the intersection of rate-distortion theory, attention mechanism design, and hardware-aware memory management, offering a principled framework that separates storage capacity from per-query read bandwidth. This distinction is critical because long-context serving increasingly depends on cache bandwidth rather than compute throughput, making read-budget optimization as important as compression ratio.

## Implications
For practitioners deploying long-context LLMs at scale, ReadKV demonstrates that adaptive read budgets can slash memory bandwidth requirements by roughly 75% while preserving model quality, directly translating to lower serving costs and higher throughput on commodity hardware like the NVIDIA A10G. The theoretical separation between retained bits and fetched bits opens a new design axis for inference infrastructure: systems can store higher-precision cache entries for long-context reuse while each individual query only fetches the minimal precision it needs, decoupling storage provisioning from per-request latency. For the research community, the proof that query-dependent access strictly dominates query-independent readers under fixed budgets challenges the assumption that uniform quantization is near-optimal and motivates further exploration of adaptive, query-aware memory hierarchies in transformer serving stacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11245v1)
