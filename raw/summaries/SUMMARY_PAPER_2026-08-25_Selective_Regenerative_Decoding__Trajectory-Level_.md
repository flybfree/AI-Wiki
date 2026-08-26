---
title: Selective Regenerative Decoding: Trajectory-Level Intervention for Inference-Time Reasoning
url: http://arxiv.org/abs/2608.24338v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_10-01-56Z_SelectiveRegenerativeDecoding_Trajectory_LevelInte.md
generated_at: 2026-08-25 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
Selective Regenerative Decoding (SRD) proposes a method that refines only the degraded parts of low‑quality candidate trajectories while keeping useful prefixes, avoiding discarding entire paths. The approach improves sample efficiency by 1.28‑to‑1.36× over rejection sampling and maintains higher trajectory quality as the pool expands.

## Key Takeaways
- SRD replaces whole‑trajectory keep/discard decisions with segment‑level interventions that retain high‑quality prefixes and regenerate only low‑quality suffixes.
- The method achieves a provable 1.28‑to‑1.36 fold gain in sample efficiency compared to rejection sampling, with gains increasing as the candidate pool grows.
- SRD matches Best‑of‑N accuracy on benchmark reasoning tasks while generating far fewer tokens than speculative rejection.

## Context
Current inference‑time decoding treats each trajectory as an all‑or‑nothing decision, leading to wasted computation. This paper introduces a more nuanced strategy that can adaptively improve low‑quality outputs without expanding the model size.

## Implications
SRD opens a new efficiency frontier for LLM reasoning, allowing practitioners to balance accuracy and compute in regimes where full speculative rejection is too costly. The approach could be integrated into existing decoding pipelines with minimal architectural changes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24338v1)
