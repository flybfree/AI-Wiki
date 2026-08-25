---
title: PatchGate: Narrowing the Verbalization Gap with Intrinsic Object Inventories in Frozen Vision-Language Models
url: http://arxiv.org/abs/2608.21819v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_07-37-40Z_PatchGate_NarrowingtheVerbalizationGapwithIntrinsi.md
generated_at: 2026-08-24 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PatchGate, a training-free method that narrows the verbalization gap in frozen vision‑language models by extracting intrinsic object evidence and using it to calibrate decoding. On AMBER it raises visible‑object coverage from 49.4% to 56.0% while lowering hallucination scores from 7.5 to 6.6, achieved with only one extra forward pass.

## Key Takeaways
- PatchGate extracts visual evidence from decoder layers without any task prompt, creating an object set that the model can use during generation.
- The framework calibrates decoding logits to favor under‑verbalized but evidence‑supported objects and suppress over‑verbalized weak support.
- Results show improved coverage (+13.4%) and reduced hallucination (-12.0%) on AMBER without fine‑tuning or external detectors.

## Context
Vision‑language models often generate captions that miss visible objects or include irrelevant ones, limiting their reliability for downstream tasks such as image retrieval or robotics. Training‑free approaches are attractive because they avoid costly fine‑tuning while still boosting performance.

## Implications
This work demonstrates that simple post‑hoc calibration can significantly improve model outputs without retraining, offering a low‑cost solution for practitioners needing reliable captions in production systems. It also highlights the potential of intrinsic evidence extraction as a general technique across frozen models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21819v1)
