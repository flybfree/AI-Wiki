---
title: GUIDE: Guiding Internal Evidence with Language Instructions
url: http://arxiv.org/abs/2608.30712v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_12-50-03Z_GUIDE_GuidingInternalEvidencewithLanguageInstructi.md
generated_at: 2026-08-31 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GUIDE, a framework that steers multimodal models to rely on evidence according to language instructions rather than shortcut cues. It combines parameter-efficient adaptation with instruction-conditioned gating and evaluates evidence pathways using sensitivity analysis. Experiments show improved robustness under targeted perturbations across multiple tasks.

## Key Takeaways
- GUIDE introduces a pathway-level evaluation framework that measures reliance sensitivity, controlled perturbation, pathway modulation, and autoregressive decoding dynamics to characterize how instruction affects evidence usage.
- The approach redistributes evidence reliance in a structured way while preserving task performance across multimodal reasoning, classification, and generation tasks.
- Experiments on datasets such as GQA, TextVQA, MM‑IMDb, CREMA‑D, RAVDESS, and Flickr30K demonstrate that GUIDE enhances robustness to evidence perturbations and enables controllable modulation.

## Context
Multimodal models often follow surface instructions but ignore internal reasoning pathways, leading to brittle behavior when cues shift. This work addresses the need for explicit control over which visual or textual evidence drives predictions, a gap in current instruction-following methods that focus only on output.

## Implications
For practitioners, GUIDE offers a tool to debug and improve model reasoning by isolating evidence pathways, potentially reducing hallucinations. In industry, this could lead to more reliable AI systems where specific data sources are trusted or excluded based on operational rules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30712v1)
