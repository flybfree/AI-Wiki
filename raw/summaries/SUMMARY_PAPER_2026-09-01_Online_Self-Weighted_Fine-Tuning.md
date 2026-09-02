---
title: Online Self-Weighted Fine-Tuning
url: http://arxiv.org/abs/2609.00734v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_05-12-45Z_OnlineSelf_WeightedFine_Tuning.md
generated_at: 2026-09-01 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Online Self-Weighted Fine-Tuning (OSW-FT), a method that improves standard supervised fine-tuning by adding online trajectory-level weighting based on few inference rollouts. The approach adapts the loss magnitude to reflect the model’s current competence while keeping the optimization direction aligned with expert demonstrations. Experiments across Qwen3 models from 0.6B to 4B show consistent gains over SFT, especially on binary-verifiable reasoning benchmarks such as AIME.

## Key Takeaways
- OSW-FT estimates the model's success rate using a small number of inference-only rollouts and rescales the standard SFT loss accordingly.
- The optimization direction remains anchored to the expert trajectory while the update magnitude adapts online, allowing dynamic response to performance changes.
- The estimator is unbiased for the exact OSW-FT surrogate update with any finite rollout count, and convergence is analyzed relative to this surrogate objective.

## Context
In AI fine-tuning, supervised methods like SFT assign uniform loss weights regardless of model progress, while reinforcement learning approaches often require large numbers of samples and can be unstable. This paper proposes a lightweight alternative that leverages only two online rollouts per query, offering a favorable compute-performance trade-off for small-to-medium language models.

## Implications
Practitioners can apply OSW-FT to improve reasoning capabilities without the heavy sampling burden of traditional RL fine-tuning. The method enables efficient adaptation of binary-verifiable tasks across a range of model sizes, supporting scalable deployment in resource-constrained settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00734v1)
