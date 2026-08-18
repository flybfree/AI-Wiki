---
title: ReRef-3D: A Benchmark for Spatial Referring Expression-Guided 3D Scene Rearrangement
published: 2026-08-17T02:03:28Z
authors: Mary Lynn Martin, Yifei Zhang, Martha Palmer, Maria Leonor Pacheco
url: http://arxiv.org/abs/2608.16011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReRef-3D: A Benchmark for Spatial Referring Expression-Guided 3D Scene Rearrangement

## Abstract
We introduce ReRef-3D, a benchmark for language-guided placement in 3D scenes. It contains 33,826 instructions across 998 CLEVR-derived scenes, spanning 16 placement families and direct, one-hop, and two-hop references. Each instruction must be resolved into a valid new placement position. Given that an instruction defines a region of acceptable placements rather than one coordinate, our evaluation inserts a prediction into the scene, recomputes relations, and tests relation satisfaction and physical validity. Each instruction also includes a verified naturalized rewrite. After fine-tuning, LLaVA-3D, 3D-LLM, and PlaceIt3D produce valid placements for 68.3%, 31.6%, and 22.4% of instructions, respectively. Across models, relation satisfaction surpasses physical validity, relations such as nearest and between are the most difficult, and phrasing has minimal effect on performance.

## Metadata
- **Published**: 2026-08-17T02:03:28Z
- **Authors**: Mary Lynn Martin, Yifei Zhang, Martha Palmer, Maria Leonor Pacheco
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16011v1)