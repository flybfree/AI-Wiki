---
title: Suppression Sticks, Locality Is Fragile: A Closed-Loop Target-and-Control Audit of Task-Vector Negation in VLA Policies
url: http://arxiv.org/abs/2608.04692v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-59-53Z_SuppressionSticks_LocalityIsFragile_AClosed_LoopTa.md
generated_at: 2026-08-05 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates task‑vector subtraction in multitask vision‑language‑action (VLA) policies across ten LIBERO‑Goal skills and discovers three distinct regimes: suppression of targets, resistance to editing, or global collapse. It reports that five tasks become fully suppressible while average baseline‑normalized control retention drops to 52%, indicating a noticeable loss of related functionality.

## Key Takeaways
- For five skills subtraction creates target‑control separation but the mean baseline‑normalized control retention is only 52%, showing that editing harms performance on controls that are not directly targeted.  
- Each task‑vector edit materially harms at least one nominally unrelated control, revealing non‑local side effects beyond the intended suppression of the target skill.  
- A matched‑norm control identifies a local sign asymmetry around one Goal anchor and multi‑vector outcomes vary with anchor and scale, proving that mean cosine similarity does not capture this variation.

## Context
Task‑vector arithmetic offers a closed‑form method for editing AI models, yet its reliability in closed‑loop robotics remains uncertain. This study empirically maps the failure modes of subtraction across diverse VLA policies to clarify where local assumptions break down.

## Implications
Practitioners must evaluate task‑vector edits with both target and control metrics to prevent unintended behavior degradation. The findings underscore a need for robust, locally aware evaluation frameworks before deploying model edits in safety‑critical applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04692v1)
