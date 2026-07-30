---
title: Lilith: Backdoor Generalization under Training-Inference Trigger Shift
url: http://arxiv.org/abs/2607.26099v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_06-23-48Z_Lilith_BackdoorGeneralizationunderTraining_Inferen.md
generated_at: 2026-07-29 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles the blind spot in backdoor research where attacks learned from a single training trigger can generalize to unseen inference triggers, introducing Lilith as a framework that creates such generalization with minimal utility loss. Experiments demonstrate high attack success across diverse datasets and defenses while keeping performance degradation low.

## Key Takeaways
- Backdoors can persist under training‑inference trigger shift, meaning a vulnerability induced by one anchor may activate on new trigger families not present during training.
- Lilith first creates a compact target‑side vulnerability with a single training anchor then builds a bounded inference‑only family that preserves the anchor‑induced representation geometry.
- The activation of the family depends on alignment of representations rather than the specific proposal mechanism used to generate triggers.

## Context
Machine‑learning services increasingly depend on public data, third‑party providers, and outsourced training, which opens opportunities for persistent poisoning attacks that maintain benign utility. Existing backdoor studies focus only on exact trigger reuse or predefined transformation axes, leaving a gap in understanding generalization across trigger families.

## Implications
Practitioners must design defenses that consider trigger shift and representation alignment, not just the original trigger. Ignoring this broader threat can lead to undetected attacks that persist even when training triggers are removed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26099v1)
