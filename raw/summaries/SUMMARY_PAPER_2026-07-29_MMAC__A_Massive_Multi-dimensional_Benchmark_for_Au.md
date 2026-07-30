---
title: MMAC: A Massive Multi-dimensional Benchmark for Audio Captioning
url: http://arxiv.org/abs/2607.27109v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_16-38-08Z_MMAC_AMassiveMulti_dimensionalBenchmarkforAudioCap.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MMAC, a massive multi-dimensional benchmark for audio captioning that evaluates both information coverage and description reliability across many dimensions. The benchmark includes 5,638 clips from diverse sources covering six capability categories and fifteen evaluation dimensions. Evaluations of open-source and proprietary AudioLLMs show clear differences in performance.

## Key Takeaways
- MMAC provides a comprehensive set of audio clips that span multiple data sources to test how well captions capture relevant information across many dimensions.
- The benchmark evaluates both the presence of relevant content (information coverage) and whether the described content matches the reference label (description reliability).
- Results demonstrate significant variations in model performance depending on which evaluation dimension is targeted.

## Context
Audio captioning has progressed with large language models that generate free-form descriptions, yet existing benchmarks often focus only on generation quality or task accuracy. This limits understanding of how well models handle nuanced aspects like factual consistency and coverage across diverse audio content.

## Implications
MMAC offers practitioners a standardized way to assess AudioLLMs beyond simple metrics, enabling more informed model selection and development. The released benchmark and evaluation code will facilitate reproducible research and industry adoption of robust audio captioning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27109v1)
