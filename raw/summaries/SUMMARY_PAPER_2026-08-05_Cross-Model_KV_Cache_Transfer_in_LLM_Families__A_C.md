---
title: Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse
url: http://arxiv.org/abs/2608.03893v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-26-47Z_Cross_ModelKVCacheTransferinLLMFamilies_AClosed_Fo.md
generated_at: 2026-08-05 01:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes cross-model KV cache transfer to avoid re-prefilling when swapping models in a family. It discovers that the relationship between source and target layers is linear, allowing a closed-form ridge mapper to reuse keys and values. The mapper runs 2.7‑25x faster than re-prefill and remains stable across multi-turn handoff.

## Key Takeaways
- One source layer accounts for 56% of variance in the target’s keys and 32% in its values when moving from Qwen3 14B to 32B.  
- With multiple source layers, this contribution rises to 79% in keys and 65% in values, showing strong linear structure across matched-KV pairs.  
- A ridge regression mapper calibrated on 500 FineWeb-Edu sequences retains 73–98% of standalone‑prefill accuracy for four model pairs while a nonlinear MLP recovers up to +37 pp HellaSwag on the failures.

## Context
This work addresses a bottleneck in dynamic model routing where each handshake incurs costly re-prefilling, limiting efficiency

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03893v1)
