---
title: SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference
url: http://arxiv.org/abs/2608.28911v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_22-19-47Z_SemKV_SemanticMixed_PrecisionKVCacheQuantizationGu.md
generated_at: 2026-08-31 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SemKV, a method for quantizing the key‑value cache in long‑context LLMs using mixed precision guided by a statistical “quality cliff.” Experiments show that uniform quantization collapses at 2.0 bits per value while a fractional‑bit affine quantizer remains indistinguishable from FP16 down to 2.322 code bits, after which a quality cliff appears. SemKV leverages model‑internal importance scores to assign two adjacent precisions above the cliff, achieving a 6× storage reduction without detectable loss.

## Key Takeaways
- Uniform KV quantization degrades sharply between 2.0 and 2.322 code bits per value, forming a quality cliff that repeats across generation time and multi‑turn dialogue.
- SemKV’s importance‑aware mixed precision interpolates above the cliff, preserving every token while delivering up to six times less storage than FP16 KV cache.
- Optimizing the affine base with TurboQuant‑MSE lowers the cliff to 7.9×, expanding the range of lossless quantization.

## Context
Long‑context LLMs suffer from memory bottlenecks as the KV cache scales linearly with context length, limiting practical inference. Traditional solutions like token pruning or uniform quantization often sacrifice quality at sharp thresholds, making long‑range reasoning unreliable. This work addresses those limits by quantizing only the cache and using statistical profiling to avoid abrupt quality drops.

## Implications
The findings enable developers to deploy high‑quality KV caches with dramatically reduced memory footprints, supporting larger context windows on edge devices or low‑power hardware. By providing a systematic way to locate and exploit the cliff, SemKV offers a practical path toward efficient long‑context inference without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28911v1)
