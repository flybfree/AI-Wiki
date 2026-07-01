---
title: Intrinsic decomposition and editing of 3D Gaussian splats
url: http://arxiv.org/abs/2606.31637v1
type: paper-summary
date: 2026-06-30
source_paper: 2026-06-30_13-20-44Z_Intrinsicdecompositionandeditingof3DGaussiansplats.md
generated_at: 2026-06-30 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a method to decompose and edit 3D Gaussian splat radiance fields using intrinsic decomposition. It models the decomposition as independent sets of Gaussian primitives, learns them from multi-view images, and allows texture editing without affecting lighting. The workflow enables users to modify planar surface colors directly.

## Key Takeaways
- The intrinsic decomposition is represented by separate Gaussian primitive sets that adapt to each layer's characteristics.
- A data-driven optimization separates multi-view photographs into these intrinsic sets.
- Editing a texture in one image updates the albedo of the corresponding Gaussian set, producing plausible lighting when re-rendered.

## Context
Intrinsic decomposition has been used for 2D image editing to change colors and textures while preserving illumination. Extending this concept to volumetric data like radiance fields is a natural step toward realistic scene manipulation.

## Implications
This approach could enable real-time texture updates in virtual environments, reducing the need for complex lighting recalculations. Practitioners may integrate it into graphics pipelines for interactive content creation and AR applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.31637v1)
