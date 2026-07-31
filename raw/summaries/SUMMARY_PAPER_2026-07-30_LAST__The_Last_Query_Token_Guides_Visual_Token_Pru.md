---
title: LAST: The Last Query Token Guides Visual Token Pruning for Edge-Cloud Collaborative MLLM Inference
url: http://arxiv.org/abs/2607.27952v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-59-25Z_LAST_TheLastQueryTokenGuidesVisualTokenPruningforE.md
generated_at: 2026-07-30 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LAST, a training-free framework that enables edge devices to prune visual tokens based on the last query token’s attention in an edge‑cloud collaborative multimodal language model. The method retains only 12.5% of the original visual tokens while preserving 95.4% of full‑token accuracy across 11 benchmarks, demonstrating strong performance with minimal computational overhead.

## Key Takeaways
- LAST leverages a compact edge‑side VLM as a guidance proxy to derive an importance signal from the last query token’s attention to visual tokens without requiring cloud‑model access.  
- The approach uses causal attention so that the final query token can attend to the entire visual sequence and query context, allowing query‑aware pruning in a single step.  
- Experimental results show LAST consistently achieves the highest accuracy while reducing token budget to 12.5%, with low edge‑side selection overhead.

## Context
The surge of multimodal foundation models has shifted visual intelligence from feature pipelines to token‑based interfaces, increasing cloud inference costs due to dense visual‑token sequences. Existing pruning techniques either ignore query relevance or rely on costly attention aggregation across multiple tokens, limiting their applicability in collaborative edge‑cloud setups.

## Implications
For practitioners, LAST offers a practical solution that reduces bandwidth and cloud compute while maintaining high accuracy, supporting scalable deployment of vision‑enhanced LLMs at the edge. The method’s training‑free nature and lightweight design make it suitable for real‑time applications where resource constraints are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27952v1)
