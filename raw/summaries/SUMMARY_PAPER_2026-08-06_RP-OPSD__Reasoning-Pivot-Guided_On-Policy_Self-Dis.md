---
title: RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer
url: http://arxiv.org/abs/2608.06347v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-52-06Z_RP_OPSD_Reasoning_Pivot_GuidedOn_PolicySelf_Distil.md
generated_at: 2026-08-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RP-OPSD, a method that guides on-policy self-distillation to focus on reasoning pivots in multilingual tasks. Experiments on 17 languages show it beats existing baselines and OPSD variants. The approach uses distributional shift between teacher views with and without an English reference solution as a proxy.

## Key Takeaways
- RP-OPSD prioritizes distillation of tokens that act as reasoning pivots, which advance or redirect the inference process.
- It leverages the difference in teacher outputs when an English reference is present to identify pivot tokens.
- The method downweights surface text tokens and concentrates on control and state-update tokens.

## Context
Multilingual reasoning transfer remains a bottleneck for large language models that operate across languages. Current self-distillation methods treat all token supervision equally, ignoring the structural role of pivots in cross-lingual inference.

## Implications
This work provides a principled way to improve multilingual model alignment by focusing on reasoning control signals. Practitioners can adopt RP-OPSD to fine-tune models for low-resource languages without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06347v1)
