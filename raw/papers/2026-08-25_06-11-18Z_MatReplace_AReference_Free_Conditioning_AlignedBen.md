---
title: MatReplace: A Reference-Free, Conditioning-Aligned Benchmark for Material Replacement in Interior Scenes
published: 2026-08-25T06:11:18Z
authors: Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy, See-Kiong Ng, Luu Anh Tuan
url: http://arxiv.org/abs/2608.24107v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MatReplace: A Reference-Free, Conditioning-Aligned Benchmark for Material Replacement in Interior Scenes

## Abstract
Material replacement is a common interior-design operation: changing the material of a selected surface while preserving its geometry, surroundings, and illumination. Despite its commercial relevance, no public benchmark isolates this task, and evaluating it is challenging. Reference-based metrics penalize valid outputs in this inherently one-to-many setting, favor the style of the reference generator, and cannot fairly compare editors that receive different forms of guidance. We introduce MatReplace, a reference-free benchmark that evaluates edits along four verifiable dimensions: local material correctness, global lighting harmony, outside preservation, and inside structure. It defines three tracks that vary one conditioning signal at a time: (A) instruction only, (B) instruction plus region mask, and (C) material reference image instead of instruction. Our results reveal a clear divide between naming and visually grounding materials. In Track A, leading closed-source editors achieve exemplar-level material rendering and surpass the exemplar anchor under our primary aggregate. In Track B, masks help only mask-compatible models with weak scene preservation, with task-paired, single-seed effects ranging from +0.137 to -0.090 across aligned model families. In Track C, reference-image conditioning degrades every family under both aggregates, by -0.031 to -0.508; in the worst cases, models repaint the reference image itself and perform worse than returning the input unchanged. Thus, named-material rendering is largely solved by the strongest closed editors on this distribution, but grounding materials from pixels remains an open challenge. Expert ratings validate our ranking (Kendall's tau = 0.68) and align with our aggregates more closely than GT-referenced or CLIP-based baselines.

## Metadata
- **Published**: 2026-08-25T06:11:18Z
- **Authors**: Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy, See-Kiong Ng, Luu Anh Tuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24107v1)