---
title: CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport
url: http://arxiv.org/abs/2608.13226v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-29-15Z_CoverPrune_Coverage_DrivenTokenPruningfor3DVLMsvia.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
CoverPrune introduces a training‑free token pruning method for 3D Vision‑Language Models that shifts focus from diversity to visual evidence coverage. By modeling inference‑time pruning as an Optimal Transport problem and solving it with the Feature‑Spatial‑Temporal cost function, CoverPrune retains essential geometric structures while drastically reducing computational load.

## Key Takeaways
- The method replaces diversity maximization with a coverage‑driven objective that preserves representative tokens across views.  
- An efficient Spatial‑Guided Greedy Selection algorithm approximates the Optimal Transport formulation without enumerating all subsets, making token pruning tractable at inference time.  
- CoverPrune‑Lite achieves comparable efficiency gains using locally structured matching, offering minimal overhead for aggressive pruning budgets.

## Context
3D Vision‑Language Models excel in spatial reasoning but are limited by their large visual token counts which hinder real‑time deployment. Current pruning strategies often sacrifice representativeness to improve diversity, leading to degraded performance on multi‑view tasks. CoverPrune addresses this gap by aligning token selection with the physical evidence present in the scene.

## Implications
For developers and researchers, CoverPrune provides a practical pathway to deploy 3D VLMs at scale without sacrificing reasoning quality. The framework’s training‑free nature reduces development overhead, while its focus on coverage ensures that essential spatial information is not lost during compression. This approach could become standard in vision systems where inference latency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13226v1)
