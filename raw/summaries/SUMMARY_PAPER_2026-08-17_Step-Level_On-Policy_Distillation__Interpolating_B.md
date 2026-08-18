---
title: Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning
url: http://arxiv.org/abs/2608.16333v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-37-39Z_Step_LevelOn_PolicyDistillation_InterpolatingBetwe.md
generated_at: 2026-08-17 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Step-Level On-Policy Distillation (SOPD), a method that merges the long‑horizon correction of supervised fine‑tuning with the on‑policy advantage of traditional distillation. By providing step‑level supervision over complete student trajectories, SOPD yields more coherent repairs than token‑level OPD while still leveraging teacher guidance. Experiments show that SOPD outperforms both vanilla SFT and OPD across reasoning and agent tasks.

## Key Takeaways
- SOPD replaces fragmented token corrections with full trajectory‑level steps, enabling a complete repair path instead of isolated fixes.  
- The method reduces to supervised fine‑tuning when step length is set to the entire sequence, preserving its strong alignment benefits.  
- Compared to OPD, SOPD delivers longer‑horizon guidance that improves performance on complex tasks such as ALFWorld.

## Context
On‑policy distillation has become a popular technique for aligning student models with teacher logits using limited data, yet it often suffers from short‑range corrections that do not propagate across the whole trajectory. Supervised fine‑tuning offers long‑range alignment but requires large labeled datasets and does not exploit on‑policy advantages. SOPD bridges this gap by combining both approaches within a single framework.

## Implications
Practitioners can adopt SOPD to obtain higher accuracy with less data, especially in settings where teacher responses are costly to generate. The method’s flexibility—switching between SFT and OPD behavior—offers a practical tool for fine‑tuning agents and reasoning models without sacrificing efficiency or quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16333v1)
