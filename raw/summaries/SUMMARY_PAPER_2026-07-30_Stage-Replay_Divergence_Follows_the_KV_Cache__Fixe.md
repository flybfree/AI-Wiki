---
title: Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation
url: http://arxiv.org/abs/2607.28495v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-41-40Z_Stage_ReplayDivergenceFollowstheKVCache_Fixed_Pref.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why identical token sequences can diverge when using different precision levels and cache strategies in large language models. By comparing a live KV‑cache with a one‑shot prefill of the same integer tokens, it finds that BF16 produces 20 out of 200 suffix mismatches while FP32 yields none, indicating that numerical precision influences decoding behavior. The authors also show that exact token replay can be reproduced without preserving full live‑state fidelity when only the key/value cache is transplanted.

## Key Takeaways
- BF16 and FP32 produce different continuation outcomes on 20 of 200 suffixes, highlighting a precision‑driven divergence despite identical inputs.  
- The exact replica test confirms that a fixed prefix can hold all token states constant across constructions, yet the cache’s KV values still cause disagreement in BF16.  
- Bidirectional transplantation of all key/value layers ensures each divergent continuation follows its donor cache, proving that the boundary K/V cache is causally sufficient for the observed divergence.

## Context
This work addresses a growing concern about reproducibility and consistency across different model precisions in AI research. As models scale, subtle numerical differences can lead to observable behavioral changes that are hard to trace. Understanding these effects is crucial for reliable benchmarking and deployment of large language systems.

## Implications
For practitioners, the findings suggest that precision must be considered when evaluating model outputs, not just accuracy metrics. It also implies that preserving only the KV cache may suffice for exact replay, reducing computational overhead while maintaining reproducibility. This insight can guide more efficient training pipelines and debugging strategies in high‑stakes AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28495v1)
