---
title: SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation
url: http://arxiv.org/abs/2608.10775v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_10-28-59Z_SkillLens_VisualSkillCardsforRetrieval_AugmentedGU.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Visual Skill Cards (VSCs) to capture reusable visual procedures in interaction traces, enabling retrieval‑augmented GUI action prediction and on‑policy distillation. Experiments show that integrating VSCs improves a frozen GPT‑5.4‑mini executor by 11.6 points in Step SR and 2.9 points overall on Multimodal‑Mind2Web, while CardDistill further boosts student‑only Qwen3‑VL‑2B metrics by 12.0 and 3.2 points.

## Key Takeaways
- VSCs bind reusable procedures with visual evidence and verification signals, turning long noisy traces into concise state‑conditioned memory entries.
- At inference, SkillLens retrieves only the most relevant cards, letting a fixed visual‑language model executor expand just the needed evidence for grounded GUI prediction.
- CardDistill leverages VSC evidence as privileged teacher context to train a student that can act without runtime card retrieval.

## Context
Visual skill representation bridges the gap between raw interaction traces and text‑only skills by preserving visual state information. This work advances multimodal AI agents that understand software interfaces, supporting more reliable and efficient human‑computer collaboration.

## Implications
For developers building assistive or autonomous UI tools, VSCs provide a memory of proven workflows that can be recalled on demand. Practitioners gain a framework to train models that act intelligently without constant online lookup, reducing latency and improving user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10775v1)
