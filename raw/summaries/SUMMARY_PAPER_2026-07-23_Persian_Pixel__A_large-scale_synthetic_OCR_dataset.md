---
title: Persian Pixel: A large-scale synthetic OCR dataset for Persian language
url: http://arxiv.org/abs/2607.20385v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-13-25Z_PersianPixel_Alarge_scalesyntheticOCRdatasetforPer.md
generated_at: 2026-07-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Persian Pixel, a synthetic OCR dataset for the Persian language with over 343,000 image-text pairs generated from a seven‑million‑word corpus using SynthOCR‑Gen. The dataset models cursive connectivity, glyph variants, diacritics and multiple typefaces while adding stochastic degradation to simulate real documents. It provides an open resource for training transformer‑based OCR models such as TrOCR.

## Key Takeaways
- Persian Pixel supplies 343,000 high‑fidelity image text pairs covering sentence paragraph and full‑page layouts generated from a curated seven‑million‑word corpus.
- The synthetic pipeline faithfully reproduces contextual character joining, positional glyph variants, diacritic placement and multiple Persian typefaces.
- Realistic degradation models emulate ink bleed, paper aging, blur, illumination variation, scanner imperfections and compression artifacts.

## Context
Persian OCR remains underdeveloped due to script complexity and scarce annotated data. Synthetic datasets like Persian Pixel offer scalable alternatives that reduce annotation costs and accelerate research in low‑resource scripts.

## Implications
Practitioners can fine‑tune state‑of‑the‑art OCR systems without manual labeling, improving document digitization pipelines for Persian texts. This resource supports broader AI initiatives focused on multilingual and culturally specific language processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20385v1)
