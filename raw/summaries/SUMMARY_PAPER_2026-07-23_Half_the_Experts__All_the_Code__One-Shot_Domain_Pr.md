---
title: Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding
url: http://arxiv.org/abs/2607.16721v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-18_09-17-41Z_HalftheExperts_AlltheCode_One_ShotDomainPruningofM.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how many expert subnetworks can be removed from two open‑weight mixture‑of‑experts language models while preserving their ability to generate correct code, using a human‑judged benchmark. It finds that up to half the experts can be pruned with no detectable loss on coding tasks, but the optimal strategy differs between the Qwen3.6 and Gemma-4-26B families. The study also shows that perplexity is an unreliable metric for code quality, that a lightweight fine‑tune recovers much of what aggressive pruning loses, and that pruning can beat quantization only when the latter would require dropping below three bits per weight.

## Key Takeaways
- Half the experts can be removed from either model with no statistically detectable loss on the primary code benchmark.  
- The damage primarily affects abilities outside coding, which is the intended trade‑off for a coding‑focused model.  
- A single‑shot repair turn eliminates the 2‑bit quantization penalty entirely, indicating that aggressive pruning can outperform quantization.

## Context
Mixture‑of‑experts models are widely used to create large open‑weight language systems that fit on consumer hardware by activating only a few experts per token. However, most of their capacity is tied to expertise irrelevant to coding tasks. Recent work has explored pruning these expert pools, yet often relies on generic compression metrics that do not reflect task‑specific performance.

## Implications
This research demonstrates that per‑model validation on the actual serving task is essential for effective pruning decisions. It suggests that industry practitioners should prioritize human evaluation over automated perplexity scores when optimizing MoE models for specialized domains like coding assistance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16721v1)
