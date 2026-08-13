---
title: DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation
url: http://arxiv.org/abs/2608.12308v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-54-33Z_DreamFly_CausalMemoryandReceding_HorizonDiffusionP.md
generated_at: 2026-08-12 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DreamFly, a diffusion‑based framework that combines causal memory with receding‑horizon planning for aerial vision‑language navigation. Experiments on OpenFly show that DreamFly achieves 32.04% seen and 29.46% unseen success rates while maintaining the lowest navigation error among all compared methods.

## Key Takeaways
- The model uses a causally aligned historical memory that augments the current visual representation with only observations preceding the decision step, allowing temporal reasoning without leaking future information.
- Navigation is treated as receding‑horizon diffusion planning: the policy predicts a K‑step action chunk but executes only the first action before replanning, using future actions as auxiliary targets while preserving closed‑loop feedback.
- LiteStop estimates stop probability directly from action logits at the initial all‑mask state, decoupling explicit termination from action generation.

## Context
Aerial vision‑language navigation faces persistent challenges such as limited historical context, short planning horizons, and unreliable implicit termination. Existing VLA models are adapted to aerial tasks but struggle with these constraints, leaving a gap that this work aims to fill by integrating memory, future‑aware planning, and explicit stop estimation.

## Implications
For the field of autonomous aerial robots, DreamFly’s approach reduces navigation error and improves reliability in both seen and unseen environments. Practitioners can leverage its causal memory and receding‑horizon diffusion paradigm to develop safer, more robust perception‑to‑action systems that handle partial observability effectively.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12308v1)
