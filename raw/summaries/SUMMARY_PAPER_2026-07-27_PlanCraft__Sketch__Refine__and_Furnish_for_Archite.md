---
title: PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation
url: http://arxiv.org/abs/2607.23491v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_06-35-14Z_PlanCraft_Sketch_Refine_andFurnishforArchitect_Ins.md
generated_at: 2026-07-27 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents PlanCraft, a three-stage pipeline that generates progressive floor plans and furnishings for 3D residential scenes. By learning from real architect sketches, it supplies partial sketches at every completion level, refines them into precise vectorized layouts, and then furnishes the final scene within defined room boundaries. Experiments show a 61.1% lower FID than the best existing 2D method and surpasses current 3D systems by 15 points in expert-rated spatial rationality.

## Key Takeaways
- Design is inherently progressive; the model supplies partial sketches at every completeness level to mimic an architect’s iterative process.
- The 2D floor plan functions as an irreplaceable spatial contract that must be respected, preventing overlapping rooms or geometrically invalid proportions.
- Even a sketch at only 25% completion outperforms all fully specified baselines in FID and expert-rated spatial rationality.

## Context
This work advances AI-driven architectural design by aligning generative models with the iterative workflow of human architects. It demonstrates that progressive generation can improve realism beyond static conditioning, offering a more faithful representation of how designs evolve.

## Implications
The approach offers a template for other domain-specific progressive generation tasks, encouraging integration of sketch-like feedback loops into AI pipelines. Practitioners can leverage such methods to produce more plausible and efficient design outputs across various architectural domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23491v1)
