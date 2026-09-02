---
title: Figures as Programs: Recursive Generation of Editable Scientific Figures
url: http://arxiv.org/abs/2609.01006v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-53-47Z_FiguresasPrograms_RecursiveGenerationofEditableSci.md
generated_at: 2026-09-01 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FigTree, a multi‑agent system that converts scientific papers into structured SVG programs and then assembles them into high‑quality editable figures. It uses a recursive generation approach where each figure region is treated as an independent program fragment, and a render‑critic loop refines the output by linking visual defects to specific code statements.

## Key Takeaways
- FigTree treats scientific figure creation as a recursive SVG program construction, breaking the figure into hierarchical local regions that are generated independently.  
- The system employs a render‑critic refinement loop that maps visual problems directly to the underlying program statements for precise repairs.  
- Evaluations demonstrate that FigTree produces high‑quality vector figures and enables more effective editing than raster‑based alternatives.

## Context
Current AI image generators can produce visually appealing raster figures but struggle with single‑step human satisfaction and precise edits. This work addresses those limitations by moving figure generation into the realm of program synthesis, where logical structure ensures editability and reproducibility.

## Implications
For researchers, FigTree offers a reproducible pipeline that reduces manual drawing effort and supports iterative refinement. In industry, it can accelerate scientific communication tools and integrate with existing vector editing workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01006v1)
