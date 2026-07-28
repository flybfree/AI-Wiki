---
title: Spatial-IQ: Deconstructing Spatial Intelligence via Hierarchical Capability Tests
url: http://arxiv.org/abs/2607.22864v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_19-09-25Z_Spatial_IQ_DeconstructingSpatialIntelligenceviaHie.md
generated_at: 2026-07-27 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Spatial-IQ a hierarchical diagnostic framework that breaks down object counting in stacked 3D structures into nine perceptual and cognitive sub‑tasks aligned with human developmental stages plus mental rotation as a probe. Experiments on 80,000 procedurally generated scenes show top models often succeed at the final task while failing lower‑level tasks revealing shortcut behavior. Training with chain‑of‑thought supervision over these sub‑tasks combined with verifiable rewards improves consistency and accuracy.

## Key Takeaways
- The framework isolates whether model failures stem from perception or cognition by testing nine sub‑tasks that map to human spatial development.
- Models can achieve high target‑task scores without preserving the full chain of lower‑level abilities indicating reliance on shortcuts.
- Chain‑of‑thought supervision over hierarchical tasks together with reinforcement learning yields better performance across all sub‑tasks and the final counting task.

## Context
Spatial reasoning remains a bottleneck for multimodal large language models despite their visual strengths. Existing benchmarks treat spatial tasks as opaque, preventing researchers from understanding failure modes or designing effective training signals. This work addresses that gap by providing a transparent diagnostic pipeline.

## Implications
For AI developers, Spatial‑IQ offers a practical method to diagnose and improve spatial reasoning in models without retraining entire architectures. Practitioners can use the decomposition to target specific weaknesses and apply chain‑of‑thought supervision as an efficient training strategy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22864v1)
