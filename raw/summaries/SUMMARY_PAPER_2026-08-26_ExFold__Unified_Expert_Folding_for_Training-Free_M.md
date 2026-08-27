---
title: ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration
url: http://arxiv.org/abs/2608.24938v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-24_08-53-58Z_ExFold_UnifiedExpertFoldingforTraining_FreeMoEPref.md
generated_at: 2026-08-26 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
ExFold is a training‑free framework that jointly accelerates prefill and decode in MoE models by treating both phases as output‑approximation problems. It folds excluded experts into retained ones using calibrated scalar projectors, achieving speedups while preserving quality. The method casts prefill acceleration to token‑level Top‑K folding and decode acceleration to batch‑level expert‑pool folding.

## Key Takeaways
- ExFold treats prefill acceleration as token‑level Top‑K folding, selecting only a subset of experts per token.
- Decode acceleration is realized through batch‑level expert‑pool folding, reducing memory traffic from the activated pool.
- A shared folding mechanism recovers contributions of budget‑excluded experts via calibrated scalar projectors.

## Context
MoE models are widely used to scale capacity with bounded compute, yet serving latency suffers because prefill and decode have distinct bottlenecks. Existing acceleration methods optimize only one resource proxy or approximate excluded expert contributions, leaving the other phase under‑served.

## Implications
This unified approach reduces hardware complexity by reusing a single kernel across both phases, lowering deployment cost. Practitioners can integrate ExFold into existing MoE pipelines for faster inference without retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24938v1)
