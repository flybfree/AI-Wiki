---
title: Vector-Bench: Can Models Surgically Edit SVG Code?
url: http://arxiv.org/abs/2607.19056v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_12-44-39Z_Vector_Bench_CanModelsSurgicallyEditSVGCode.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Vector‑Bench, a benchmark that tests whether AI models can edit SVG code precisely according to visual instructions while preserving all other elements. The evaluation across 34 model endpoints shows that even the best performers achieve only about 15 % full specification success despite higher reported repair progress.

## Key Takeaways
- apparent repair progress and specification‑faithful editing remain substantially different, as models can fix visible defects without meeting the exact attribute‑aware requirements.  
- the strongest endpoint reaches only 15.0 % full specification success even though it shows 43.7 % mean repair progress, highlighting a gap between surface fixes and correct output.  
- validity‑gated repair progress and valid‑output unintended change rate (UCR) explain only partial outcomes, indicating that many repairs are syntactically valid but still introduce unwanted changes.

## Context
Vector editing is essential for precise graphic design where exact control over shapes, colors, and paths matters. Current AI models often generate raster approximations or produce syntactically correct but semantically incorrect SVG, limiting their practical utility in creative and technical workflows.

## Implications
For the field of computer vision and generative AI, this work underscores that visual‑only metrics are insufficient for assessing vector editing fidelity. Practitioners must adopt stricter specification‑based evaluation to ensure models produce usable, error‑free SVG code.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19056v1)
