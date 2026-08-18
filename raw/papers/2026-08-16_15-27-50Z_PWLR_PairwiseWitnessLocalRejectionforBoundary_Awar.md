---
title: PWLR: Pairwise Witness Local Rejection for Boundary-Aware Out-of-Distribution Detection
published: 2026-08-16T15:27:50Z
authors: Chengyao Jia, Ruixuan Wang
url: http://arxiv.org/abs/2608.15802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PWLR: Pairwise Witness Local Rejection for Boundary-Aware Out-of-Distribution Detection

## Abstract
Out-of-distribution (OOD) detection remains challenging for image classifiers, especially when near-OOD samples lie close to in-distribution (ID) class boundaries. Recent vision-language detectors improve OOD detection through class semantics, local prompting, or LLM-generated outlier concepts, but seldom use language as explicit boundary evidence between confusing ID classes. We propose Pairwise Witness Local Rejection (PWLR), which uses an MLLM offline to describe visible local cues that favor one ID class over a specific rival class. These cue phrases are then screened with ID-only data under a frozen vision-language backbone, so that only reliable local verifiers are kept. At inference, PWLR first retains a small set of globally plausible classes, then checks whether any of them is locally supported against its most relevant rivals, and finally combines this pairwise local evidence with the global class score through calibration. Experiments on ImageNet-100 far-OOD, cleaner/challenging OOD and near-OOD benchmarks show that PWLR consistently improves strong vision-language baselines across multiple backbones. Source code will be released.

## Metadata
- **Published**: 2026-08-16T15:27:50Z
- **Authors**: Chengyao Jia, Ruixuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15802v1)