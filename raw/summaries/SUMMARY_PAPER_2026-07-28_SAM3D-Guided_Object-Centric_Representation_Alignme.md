---
title: SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models
url: http://arxiv.org/abs/2607.25912v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_16-05-32Z_SAM3D_GuidedObject_CentricRepresentationAlignmentf.md
generated_at: 2026-07-28 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SAM3D‑Guided Object-Centric Representation Alignment, a framework that enriches vision‑language‑action (VLA) models with fine‑grained 3D object priors. By leveraging SAM3D as a frozen 3D teacher and aligning its outputs with the intermediate features of $π_0$, the model learns to understand target objects in depth without adding extra components at inference time. The approach yields strong simulation results, reaching 99.1 % on LIBERO and an average action length of 4.11 on CALVIN.

## Key Takeaways
- localizes task‑relevant objects with object recognition models, creates masks, and uses SAM3D to extract dense object‑level 3D representations that are aligned with $π_0$ visual features.  
- the policy internalizes target‑object 3D information while preserving the original RGB‑language‑to‑action pipeline, eliminating the need for depth maps, point clouds, masks, or SAM3D at test time.  
- the method consistently improves performance on benchmark tasks and is especially effective in long‑horizon manipulation where robots must attend to different targets across subtasks.

## Context
Vision‑language‑action systems aim to enable general robot manipulation but typically depend on 2D visual‑language backbones that ignore fine‑grained 3D object details. This limitation hampers performance under occlusion, pose variation, scale changes, and precise spatial interaction. The proposed work addresses this gap by introducing an object‑centric 3D alignment mechanism that enriches the representation with explicit 3D priors.

## Implications
The findings demonstrate that integrating SAM3D as a teacher can boost VLA models without compromising simplicity or hardware requirements at deployment, making high‑quality 3D understanding accessible to practitioners. This advancement supports more reliable long‑horizon manipulation in both simulated and real‑world robotics settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25912v1)
