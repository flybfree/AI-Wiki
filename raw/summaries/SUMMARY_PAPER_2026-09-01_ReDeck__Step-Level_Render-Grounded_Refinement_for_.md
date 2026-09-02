---
title: ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation
url: http://arxiv.org/abs/2609.00194v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-12-10Z_ReDeck_Step_LevelRender_GroundedRefinementforDocum.md
generated_at: 2026-09-01 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ReDeck, a step‑level render‑grounded refinement framework for generating document‑to‑slide outputs. By decomposing slide revision into atomic edit actions and providing renderer‑derived observations after each step, ReDeck enables “one edit, one observation” feedback that resolves local layout errors such as overflow or clipping. Experiments on GPT‑5.4, Claude‑4.6, and Gemini‑3.1 show consistent improvements over existing agents, confirming that timely granular feedback is essential for reliable slide generation.

## Key Takeaways
- ReDeck replaces the monolithic “one version, one feedback” loop with step‑level render feedback, allowing immediate detection of spatial errors like overflow or overlap.
- The framework integrates multi‑granular feedback: step‑level render observations, turn‑level adaptive semantic/design guidance, and a submission‑level hard layout gate to balance local repair with global quality.
- Ablations reveal that both feedback timing and granularity are critical; without fine‑grained observation after each edit, refinement performance degrades sharply.

## Context
Slide generation remains a bottleneck in AI‑assisted presentation creation because current models treat the entire deck as a single output, missing the opportunity to correct local layout issues. This limitation hampers scalability and user experience, where precise placement of text and images is crucial for readability and visual appeal.

## Implications
For practitioners developing slide generation tools, ReDeck offers a blueprint for integrating real‑time feedback into iterative design pipelines, reducing manual correction effort. The approach could be adapted to other image‑based content creation tasks that require fine spatial control, potentially lowering the cost of producing high‑quality editable artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00194v1)
