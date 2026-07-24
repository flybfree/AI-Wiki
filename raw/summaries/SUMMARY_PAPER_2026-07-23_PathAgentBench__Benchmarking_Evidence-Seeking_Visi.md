---
title: PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image
url: http://arxiv.org/abs/2607.19261v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_16-33-44Z_PathAgentBench_BenchmarkingEvidence_SeekingVision_.md
generated_at: 2026-07-23 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PathAgentBench, a benchmark for evidence-seeking vision-language models on whole-slide pathology images. It tests four capabilities: image-to-text matching, text-to-image retrieval, diagnostic region localization, and multi-scale reasoning. The best models achieve high accuracy in reasoning but struggle with localization.

## Key Takeaways
- The benchmark contains 1,822 TCGA WSIs and 17,135 diagnostic paths annotated by ten board-certified pathologists, enabling rigorous testing of evidence-seeking tasks across magnifications.
- Leading open-weight models achieve over 93% accuracy in multi-scale reasoning but only about 50% accuracy in cross-modal matching tasks, showing strong reasoning but limited retrieval performance.
- Diagnostic region localization remains challenging with mean intersection-over-union below 0.09, outperforming a simple center-based heuristic.

## Context
Pathology diagnosis relies on extracting evidence from gigapixel whole-slide images at multiple magnifications, yet most benchmarks evaluate models on pre-cropped patches or extracted features, ignoring direct evidence acquisition. This paper addresses that gap by providing a unified framework for measuring evidence-seeking capabilities in real diagnostic workflows.

## Implications
For AI practitioners, PathAgentBench highlights the need to balance reasoning with practical evidence gathering, guiding model design toward better localization and retrieval. Industry adoption could improve diagnostic tool accuracy but requires addressing the current limitations in autonomous exploration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19261v1)
