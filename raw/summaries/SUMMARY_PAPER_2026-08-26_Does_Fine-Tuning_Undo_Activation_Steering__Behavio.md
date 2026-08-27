---
title: Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal
url: http://arxiv.org/abs/2608.24988v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_17-59-57Z_DoesFine_TuningUndoActivationSteering_BehaviouralR.md
generated_at: 2026-08-26 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether activation steering embedded in language model weights remains effective after fine‑tuning under instruction tuning protocols. It finds that while behaviour often degrades, the weight edit itself is largely preserved with minimal change to mean vectors and near‑orthogonal updates.

## Key Takeaways
- Steering degrades when optimisation pressure conflicts with targeted behaviour, yet the underlying weight pattern stays intact.
- Fine‑tuning does not reverse or dismantle the steering mechanism; instead it leaves the weight edit unchanged.
- Behavioural recovery is achieved through orthogonal fine‑tuning updates rather than undoing the original editing.

## Context
Activation steering offers a way to embed behavioural constraints directly into model weights, reducing reliance on inference‑time interventions. This study highlights that such embedded interventions can survive training but may not translate into observable behaviour changes after downstream optimisation.

## Implications
Practitioners must validate alignment outcomes post‑fine‑tuning rather than assuming embedding preserves function. The findings suggest a need for robust behavioural testing pipelines to detect when steering is functionally lost despite weight stability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24988v1)
