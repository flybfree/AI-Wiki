---
title: DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models
url: http://arxiv.org/abs/2608.06243v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_16-29-24Z_DASH_Divergence_AdaptiveSupervisionHorizonsforOn_P.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Divergence-Adaptive Supervision Horizons (DASH), a method that refines on‑policy self‑distillation by making token‑level supervision weights responsive to the temporal evolution of local divergences. Experiments across three mathematical reasoning benchmarks and model scales show that DASH consistently outperforms vanilla OPSD reruns, demonstrating that adaptive propagation gates improve learning efficiency without extra forward passes.

## Key Takeaways
- The standard OPSD approach treats every local divergence with a uniform coefficient, ignoring how its magnitude changes over the generation sequence.  
- DASH maps each local divergence to an adaptive gate that reflects its distance from the sequence‑level mean, enabling variable backward aggregation based on the divergence history.  
- These gates are computed solely from teacher and student distributions already produced by OPSD, so no additional forward passes are required.

## Context
The field of reinforcement learning with verifiable rewards (RLVR) seeks dense supervision to boost language model reasoning, yet sparse sequence‑level signals limit progress. On‑policy self‑distillation addresses this by providing token‑level feedback, but its static weighting fails to capture the nuanced dynamics of divergence evolution during autoregressive generation.

## Implications
DASH offers a scalable way to enhance self‑supervised training pipelines without extra compute, encouraging more efficient model refinement in industry settings. Practitioners can adopt DASH to improve reasoning performance on complex tasks while maintaining cost‑effective training resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06243v1)
