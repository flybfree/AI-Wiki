---
title: Rethinking Normalization Placement for LLMs: Post-Norm under Curriculum Depth Growing
url: http://arxiv.org/abs/2608.13156v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_12-24-30Z_RethinkingNormalizationPlacementforLLMs_Post_Normu.md
generated_at: 2026-08-13 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how normalization placement affects model performance when depth is added through a curriculum, using a Qwen3-8B teacher and a nine‑layer student. The results show that while pre‑norm and post‑norm are nearly identical under joint training (validation CE differs by 0.0004), post‑norm yields a larger gain of 0.0328 during curriculum growth, an order of magnitude improvement. Moreover, the ranking of placement strategies crosses over as blocks are appended, indicating that the interaction between normalization and curriculum depth matters.

## Key Takeaways
- Pre-norm and post-norm produce almost identical validation CE under joint training, differing by only 0.0004.
- Post-norm improves validation CE by 0.0328 when using curriculum growth, a gain that is an order of magnitude larger than the pre‑norm advantage.
- The ranking of placement strategies changes during curriculum: post-norm takes the lead once new blocks are appended.

## Context
Normalization placement has long been treated as a fixed architectural choice in Transformers because it simplifies joint optimization across full depths. Recent work on curriculum learning, where depth is introduced incrementally via boundary representations, reveals that this simplification may no longer hold when training proceeds through staged block appending. Understanding how normalization interacts with curriculum growth is essential for designing efficient and scalable models.

## Implications
Treating normalization placement and training curriculum as coupled design choices can lead to better performance without sacrificing compute efficiency. Practitioners should consider the interaction between these factors, especially in distillation or incremental model expansion scenarios where depth is added gradually.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13156v1)
