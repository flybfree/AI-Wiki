---
title: ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control
url: http://arxiv.org/abs/2608.23034v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_09-37-51Z_ST__2_U_StatefulTest_TimeUnlearningviaRestrictedKn.md
generated_at: 2026-08-24 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control (ST$^2$U), a method that addresses the problem of knowledge re‑entry during inference in large language models. By treating unlearning as trajectory‑wide boundary control, ST$^2$U achieves stronger retention and lower re‑entry rates compared to previous test‑time baselines across multiple benchmarks.

## Key Takeaways
- The model defines restricted knowledge boundaries in low‑dimensional invertible coordinates while preserving orthogonal components unchanged.  
- During inference it applies minimal boundary corrections anchored in the current context to keep risk within safe limits.  
- Historical correction states are propagated across tokens, preventing later generations from re‑entering restricted regions.

## Context
Large language models often need to forget specific knowledge without costly retraining, yet test‑time methods can cause unintended re‑entry of that knowledge as generation proceeds. This work contributes a trajectory‑aware approach that maintains performance while limiting the impact on inference speed and model behavior.

## Implications
ST$^2$U offers practitioners a practical way to align models with safety constraints during deployment without retraining, reducing both risk exposure and operational overhead in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23034v1)
