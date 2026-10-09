---
title: Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute
url: http://arxiv.org/abs/2610.10845v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_19-50-53Z_RealLong_TermMemoryforAI_A50_Million_TokenWindowTh.md
generated_at: 2026-10-08 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces galahad-kv, a memory layer that persists the internal key-value (KV) state of large language model attention blocks to encrypted local NVMe storage, allowing a model to resume processing at arbitrary depths in a 50-million-token stream without recomputing prior context. Tested on real public text served through vLLM on a single NVIDIA H100 GPU using Gemma 4 12B and Gemma 4 31B, the system achieved 100% successful byte-exact KV state retrieval across all probed depths, delivering 2.8x to 4.3x faster block loading than recomputation while consuming 8.8x to 12.3x less GPU energy.

## Key Takeaways
- The galahad-kv package stores KV state for blocks of approximately 16,000 tokens to encrypted local NVMe disk and reloads them byte-exact, eliminating recomputation entirely. Across 100 probes spanning depths from 0 to 50 million tokens on both Gemma 4 12B and Gemma 4 31B, every single retrieval succeeded without any recomputation, demonstrating reliable persistence of model internal state at extreme context depths.
- Performance and efficiency gains are substantial: loading a stored block was 2.8x to 4.3x faster than recomputing it from scratch, and GPU energy consumption dropped by a factor of 8.8x to 12.3x. Critically, GPU memory usage remained flat across the entire 50-million-token stream, meaning the approach does not scale memory requirements with context length the way naive long-context handling does.
- Factual recall over very long contexts was tested by planting facts millions of tokens earlier and querying the model. The 12B model answered correctly 82 out of 100 times, while the 31B model achieved 98 out of 100, with neither model hallucinating fabricated answers. However, the authors explicitly note this is reuse of stored state rather than a wider attention window, and answer quality depends on the underlying model's capability.

## Context
Long-context handling in large language models has become a central bottleneck as applications demand reasoning over documents, codebases, and conversation histories spanning millions of tokens. Current approaches either truncate context, use sliding windows that discard older information, or attempt to extend attention windows at enormous compute and memory cost. This paper addresses the problem from a systems-engineering angle rather than an architectural one, treating the model's KV cache as a persistable artifact that can be offloaded to commodity storage and restored on demand. The test protocol is explicitly designed to resist common benchmark-gaming strategies, and the entire reproduction uses public software under a free licence, making it accessible for independent verification.

## Implications
For practitioners deploying LLMs in production, this approach offers a path to handling very long documents or multi-session interactions on a single GPU without the prohibitive memory and energy costs of extended attention windows. The flat GPU memory profile and dramatic energy savings make it particularly relevant for cost-constrained inference services and edge deployments. For the research community, the work shifts attention from purely architectural solutions toward systems-level caching strategies, suggesting that practical long-term memory for AI may be achievable through careful engineering around existing model architectures rather than requiring fundamentally new attention mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10845v1)
