---
title: Capacity-Dependent Effects of Data Selection for Reasoning
url: http://arxiv.org/abs/2608.13721v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_19-31-46Z_Capacity_DependentEffectsofDataSelectionforReasoni.md
generated_at: 2026-08-16 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper revisits the assumption that high‑likelihood responses are always best for reasoning fine‑tuning and demonstrates that the benefit of such data depends on model capacity and training duration, revealing a “Fast‑Fit / Slow‑Gain” pattern where small models improve quickly with high‑likelihood supervision but larger models eventually need low‑likelihood data to continue learning.

## Key Takeaways
- High‑likelihood data provides faster and more stable early improvements, especially for smaller models.  
- Low‑likelihood data becomes increasingly beneficial as model size grows and training is allowed to continue longer.  
- The value of likelihood‑based selection varies with model capacity and computing budget rather than following a single universal rule.

## Context
Reasoning fine‑tuning often relies on teacher‑student distillation, where the quality of selected supervision samples influences learning outcomes. Understanding how data difficulty interacts with model size is crucial for designing effective training pipelines in large language models.

## Implications
Practitioners must consider both model capacity and available compute when choosing which responses to use as supervision data, avoiding a one‑size‑fits‑all strategy that could limit performance gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13721v1)
