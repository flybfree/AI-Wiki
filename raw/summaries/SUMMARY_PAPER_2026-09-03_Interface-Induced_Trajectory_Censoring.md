---
title: Interface-Induced Trajectory Censoring
url: http://arxiv.org/abs/2609.03966v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_15-00-31Z_Interface_InducedTrajectoryCensoring.md
generated_at: 2026-09-03 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how serving interfaces silence model‑generated tool calls, showing that a zero call rate stems from interface censoring rather than a defect in the model itself. Swapping components restores calls but yields only modest gains, and the effect is measurable across a wide range of model sizes.

- On BFCL v4 data with fixed weights, changing only the serving adapter changes scores from 0.00 to 0.96/0.19, indicating that the censoring is caused by the interface rather than the model.
- The interaction between chat template and parser is responsible; fixing one side yields no effect, highlighting a contract problem where neither component alone is defective.
- Across scales, the silent fraction stays low (0‑2) while well‑formed calls rise up to ~72% at 32B, showing that the interface can suppress or amplify model outputs and this effect is measurable across various sizes.

## Context
This work reveals that tool‑call rates are not intrinsic model properties but artifacts of the serving stack. It challenges assumptions about model capability independence and underscores the need for robust interfaces in AI deployment.

## Implications
Practitioners must treat interface design as a critical factor in evaluation; fixing the interface can improve performance without retraining models, guiding cost‑effective deployment strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03966v1)
