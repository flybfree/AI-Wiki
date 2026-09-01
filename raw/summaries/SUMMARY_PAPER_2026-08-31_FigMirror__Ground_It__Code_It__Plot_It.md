---
title: FigMirror: Ground It, Code It, Plot It
url: http://arxiv.org/abs/2608.28814v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_19-26-24Z_FigMirror_GroundIt_CodeIt_PlotIt.md
generated_at: 2026-08-31 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FigMirror an agentic framework that converts scientific figure styles into executable plotting code while preserving visual style for new data. It leverages ground coordinates and measurement capabilities of computer‑use models to achieve accurate style transfer. Experiments demonstrate consistent superiority over prior methods on reference‑conditioned style transfer tasks.

## Key Takeaways
- FigMirror uses Grounded Measurement to locate visual elements by pixel coordinates and extract their properties via executable code, enabling precise style replication.
- The framework outperforms existing approaches that rely solely on pixel‑level optimization or manual style mapping, showing higher fidelity in new plot generation.
- A benchmark called PlotTwin‑Bench is introduced with fine‑grained image and code metrics to evaluate both visual similarity and code correctness.

## Context
Modern computer‑use models are being applied to tasks where agents interact with visual content through code. This work extends that trend by focusing on scientific figure generation, a niche but valuable application for researchers and educators. By grounding measurements in coordinates, FigMirror bridges the gap between image understanding and programmatic output, aligning with broader efforts toward multimodal AI.

## Implications
For the field of AI research, FigMirror showcases how agentic reasoning can automate style transfer without sacrificing visual quality, opening pathways for automated report generation. In industry, it could streamline data visualization pipelines, reducing manual design effort while maintaining scientific accuracy and brand consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28814v1)
