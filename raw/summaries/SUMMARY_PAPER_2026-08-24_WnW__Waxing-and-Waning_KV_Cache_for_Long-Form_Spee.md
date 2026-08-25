---
title: WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs
url: http://arxiv.org/abs/2608.22704v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_01-48-30Z_WnW_Waxing_and_WaningKVCacheforLong_FormSpeechLLMs.md
generated_at: 2026-08-24 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WnW (Waxing-and-Waning KV Cache) to address the memory bottleneck caused by long-form audio inputs in speech large language models. By classifying attention heads into anchor, tidal, and fixed roles through offline calibration, WnW dynamically manages GPU and CPU resources while preserving near‑full cache accuracy on long audio datasets.

## Key Takeaways
- Anchor heads stay on GPU and act as an importance observer, guiding which KV positions are kept active during decoding.  
- Tidal heads reside in a CPU‑resident buffer that is recalled chunk‑by‑chunk based on scores computed from anchor heads, allowing recovery of evicted tokens.  
- Fixed heads keep only a small GPU subset; the remainder is permanently discarded to reduce memory usage.

## Context
Speech LLMs face severe KV cache costs when processing long audio clips, limiting their practical use. Existing compression methods either discard all non‑GPU KV entries or cannot recover them, leading to premature termination on long inputs. This work offers a principled, scalable approach that balances GPU and CPU workloads without sacrificing performance.

## Implications
WnW enables real‑world deployment of large language models on limited hardware by minimizing GPU memory pressure while maintaining high accuracy. Practitioners can adopt this cache strategy to extend model reachability across diverse audio domains with minimal runtime overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22704v1)
