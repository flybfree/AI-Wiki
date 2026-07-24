---
title: HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation
url: http://arxiv.org/abs/2607.20125v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_13-29-35Z_HeadCast_CastingAttentionHeadsforEfficientAutoregr.md
generated_at: 2026-07-23 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HeadCast, a training‑free acceleration framework for autoregressive video diffusion models that tackles the growing cost of attention inference caused by large key‑value caches. By classifying each attention head into one of four archetypes and restructuring the cache accordingly, HeadCast restores high‑quality generation while cutting compute time.

## Key Takeaways
- The classification of heads is performed once at the maximum‑noise step, revealing stable heterogeneous behaviors that guide their routing.
- Global heads are preserved to maintain long‑range temporal consistency, avoiding the flicker caused by coarse eviction heuristics.
- The Spatial pathway’s fixed‑size grid yields scalable savings, delivering up to 1.95× speedup at 1080P without sacrificing VBench quality.

## Context
Autoregressive video diffusion models are promising for long and streaming video synthesis but suffer from high attention costs as resolution increases. Existing solutions either discard cache entries with heuristics that degrade output or require costly model re‑training, limiting practical deployment.

## Implications
Faster inference enables real‑time streaming applications and reduces compute expenses for large language‑video systems. Practitioners can adopt HeadCast immediately on existing models without retraining, accelerating research and industry adoption of high‑resolution AR video generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20125v1)
