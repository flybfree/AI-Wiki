---
title: WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning
url: http://arxiv.org/abs/2607.28418v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-01-03Z_WIDE_BoostingAdaptiveLLMInferenceviaToken_levelDyn.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WIDE, an end‑to‑end differentiable token‑level dynamic width pruning framework for large language models that targets both prefill and decode inference. By allowing each token to choose attention‑head groups and FFN‑channel groups, WIDE achieves fine‑grained computation allocation and delivers up to 4.95× speedup in decoding while maintaining high accuracy at 50% sparsity.

## Key Takeaways
- WIDE extends dynamic pruning from layer‑level decisions to neuron‑block granularity, enabling each token to independently select sparse attention heads and FFN channels.
- The two‑stage training pipeline learns token‑wise sparse execution patterns that retain quality better than prior coarse‑grained methods at high sparsity levels.
- A co‑design framework decomposes dynamic sparsity into mask reordering, block‑level skipping, and intra‑block skipping, making the acceleration hardware‑agnostic yet still efficient.

## Context
Dynamic pruning aims to reduce model size and inference cost without sacrificing performance, a critical need as LLMs scale. Existing approaches either use static masks that limit throughput or coarse dynamic decisions that underperform on real workloads, highlighting a gap in practical deployment solutions.

## Implications
For researchers, WIDE offers a template for integrating fine‑grained sparsity into training pipelines, encouraging research beyond layer‑level pruning. For industry practitioners, the framework translates to tangible performance gains and lower latency, making large language models more viable for real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28418v1)
