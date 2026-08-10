---
title: MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents
url: http://arxiv.org/abs/2608.07068v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-18-31Z_MemOPD_On_PolicyDistillationthroughMemoryStateAlig.md
generated_at: 2026-08-09 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
MemOPD addresses the problem of long‑horizon agents where growing contexts degrade performance by introducing memory compression that misaligns teacher supervision with student rollouts. The authors propose Memory‑Aligned On‑Policy Distillation which restores original token positions and causal visibility before packing, ensuring the teacher scores actions under exactly the states they were generated in. Experiments show a 7 % F1 gain over persistent‑history scoring and up to 416 % improvement over PPO while achieving a 1.63× speedup.

## Key Takeaways
- The paper demonstrates that memory compression can break the alignment between teacher supervision and student rollouts, causing actions to be on‑policy by provenance but not by state.
- MemOPD’s reconstruction of token positions and causal visibility restores full‑vocabulary teacher supervision at sampled action positions while preserving PPO’s final task objective.
- The method yields a 7 % F1 increase over persistent‑history teacher scoring, a 416.2 % boost over PPO, and a 1.63× reduction in actor computation time.

## Context
Long‑horizon reinforcement learning suffers from context explosion, prompting research into compact memory mechanisms that trade off performance for efficiency. This work advances the field by linking memory compression directly to on‑policy distillation, showing how teacher‑student alignment can be restored without sacrificing training speed or accuracy.

## Implications
For practitioners building long‑running agents, MemOPD offers a practical way to maintain high reward while reducing computational load, potentially enabling deployment of larger models in resource‑constrained settings. The approach also highlights the importance of preserving interaction structure when compressing memory for any future on‑policy training pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07068v1)
