---
title: Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation
url: http://arxiv.org/abs/2608.23138v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_11-43-49Z_Pointing_VLA_TypedSpatialGroundingInterfacesforVis.md
generated_at: 2026-08-24 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
Pointing-VLA introduces typed hidden‑state spatial readouts that replace autoregressive text coordinates with explicit geometry predictions, enabling precise visual grounding for VLA tasks. The approach integrates these reads into Embodied-R1 to produce actionable point targets and object‑functional heatmaps without serializing geometry as text. Evaluation on Bridge/WidowX and physical pick‑place shows a 72.9% average success rate, surpassing prior methods.

## Key Takeaways
- The paper replaces autoregressive text coordinates with typed hidden‑state spatial readouts that output normalized points and object‑functional heatmaps directly from geometry heads.
- Explicit execution contracts map PICK to source‑conditioned OFG and PLACE to Pointing, aligning tasks with stage‑specific targets.
- Performance gains include a 20× reduction in controller recording time and up to 6.9× faster decoding compared to text‑based Embodied‑R1 on external suites.

## Context
The work addresses a longstanding bottleneck where vision‑language reasoning is decoupled from robot execution, limiting the reliability of VLA systems. By providing inspectable, typed interfaces, it opens pathways for modular and composable multimodal pipelines.

## Implications
These results demonstrate that structured spatial readouts can boost autonomous robot success rates by over 28 percentage points across visual contexts. For industry practitioners, the faster decoding and reduced controller load translate into scalable deployment of VLA‑driven manipulation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23138v1)
