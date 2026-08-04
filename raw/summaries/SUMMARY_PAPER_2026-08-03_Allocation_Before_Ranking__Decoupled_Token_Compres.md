---
title: Allocation Before Ranking: Decoupled Token Compression for OmniLLMs
url: http://arxiv.org/abs/2608.01665v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-56-33Z_AllocationBeforeRanking_DecoupledTokenCompressionf.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Macer, a training-free token compression method for OmniLLMs that decouples allocation and ranking. Instead of applying a single top‑K rule across modalities, it first allocates explicit budgets to audio and video tokens before performing modality‑specific rankings. The approach reduces token cost while maintaining high accuracy.

## Key Takeaways
- Allocation budgets are assigned separately for audio and video tokens, allowing each modality to compete within its own shallow layers.
- Ranking is performed after budget allocation, eliminating the bias that favors audio tokens in shared top‑K strategies.
- At 25 % retention Macer retains 98.7 % of full‑token performance on Qwen2.5‑Omni‑7B and improves over OmniZip at lower FLOPs.

## Context
Token compression is essential for scaling multimodal models, yet existing methods treat audio and video tokens as a single set, leading to unfair capacity distribution. This paper addresses the mis‑specification by separating allocation from ranking, offering a more balanced solution.

## Implications
The decoupled approach can be adopted in any large‑scale multimodal system to improve fairness and efficiency without retraining. Practitioners may achieve higher performance at lower computational cost, encouraging broader adoption of compressed models in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01665v1)
