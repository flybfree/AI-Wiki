---
title: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance
url: http://arxiv.org/abs/2608.09853v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_17-09-37Z_RynnValue_ScalingRoboticValueFoundationModelswithT.md
generated_at: 2026-08-11 12:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RynnValue, an open-source value foundation model for robotic manipulation that uses temporal distance as supervision instead of task‑specific anchors like preferences or progress. By leveraging timestamps to compute cost‑to‑goal distances across a large dataset of over 7 000 hours and 3 million instruction‑conditioned clips, RynnValue learns robust value representations without preference labels. The model achieves high agreement with human judgments on OOD evaluation and improves real‑world policy success rates significantly.

## Key Takeaways
- Temporal distance replaces preference or progress anchors, allowing scaling to massive unannotated corpora.
- Random temporal sampling, shuffling, and value‑isolation attention prevent shortcuts that degrade generalization.
- The model reaches Kendall’s tau_a of 0.675 on RBM‑EVAL‑OOD, outperforming state‑of‑the‑art preference models.

## Context
Current robot learning systems rely heavily on human‑provided preferences or progress metrics, which are limited in quantity and often do not transfer across different robotic bodies or viewpoints. This scarcity hampers the development of generalist policies that can operate reliably in unseen environments. RynnValue addresses this gap by providing a scalable, label‑light supervision signal derived from raw timestamps.

## Implications
For industry practitioners, RynnValue offers a practical path to train value models without costly preference data collection, accelerating deployment of multi‑task robotics. The approach could enable continuous improvement of policies through online learning and zero‑shot transfer across new tasks or hardware, fostering more adaptable AI agents in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09853v1)
