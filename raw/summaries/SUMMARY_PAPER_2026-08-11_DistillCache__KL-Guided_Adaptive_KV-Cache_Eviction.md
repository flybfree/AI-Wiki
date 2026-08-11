---
title: DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference
url: http://arxiv.org/abs/2608.08878v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_19-33-43Z_DistillCache_KL_GuidedAdaptiveKV_CacheEvictionforM.md
generated_at: 2026-08-11 12:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DistillCache, a reinforcement learning approach that evicts key-value pairs from the attention cache to reduce memory usage while preserving model output distribution. On Mistral-7B-Instruct-v0.3 it achieves 94.2% of full-cache accuracy with only 25% cache budget, beating heuristic methods like H2O and SnapKV by up to two points on long-context tasks.

## Key Takeaways
- DistillCache treats KV-cache eviction as a sequential decision problem solved with REINFORCE using per-step KL-divergence reward to keep the full-cache output distribution. - The learned policy uses attention statistics, value norms, entropy and position signals for lightweight policy network. - On LongBench at 25% cache budget DistillCache retains 94.2% of full-cache accuracy, outperforming H2O and SnapKV by up to two absolute points.

## Context
Memory constraints limit the context length that large language models can handle in practice. Existing eviction heuristics often ignore future predictive influence, leading to performance drops on long sequences. This work demonstrates that learned policies can adaptively manage cache size without sacrificing much accuracy.

## Implications
For practitioners deploying LLMs at scale, DistillCache offers a practical path to extend context windows while reducing GPU memory demand. The approach may inspire similar RL-based optimizations for other model families and inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08878v1)
