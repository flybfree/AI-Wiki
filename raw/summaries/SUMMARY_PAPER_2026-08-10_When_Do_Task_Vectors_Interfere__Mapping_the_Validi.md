---
title: When Do Task Vectors Interfere? Mapping the Validity Boundaries of Weight-Space Composition
url: http://arxiv.org/abs/2608.09490v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_11-58-04Z_WhenDoTaskVectorsInterfere_MappingtheValidityBound.md
generated_at: 2026-08-10 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when task vectors cause interference by measuring functional non‑additivity of fine‑tuning displacements, showing that code+safety tasks are more non‑additive than matched controls on code and instruction prompts but not math prompts; predictions hold across six tasks and multiple models. It establishes a boundary between raw prompt types preserving contrast versus wrappers collapsing it.

## Key Takeaways
- Code+safety is more non‑additive than the matched code+math control on code and instruction prompts, indicating functional interference.
- The predicted sign of pairwise comparisons holds for all eight high‑vs‑low unseen task pairs in a six‑task expansion.
- Raw public prompts preserve the continuous contrast while an instruction‑style wrapper collapses it.

## Context
This work addresses a gap in understanding how parameter adjustments translate to functional changes, which is crucial for reliable model adaptation and scaling. By separating geometry from function, the study provides a principled metric for evaluating fine‑tuning impact across tasks and architectures.

## Implications
Practitioners can rely on weight‑space composition as an input‑conditioned indicator of performance shifts rather than assume universal merging. This guides design of fine‑tuning pipelines to avoid hidden interference, especially when using wrappers or evaluation tools that may mask true effects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09490v1)
