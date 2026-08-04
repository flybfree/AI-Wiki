---
title: CAVE: Competence-Aware Visual Boundary Evidence Alignment for Video Temporal Grounding
published: 2026-08-03T11:27:29Z
authors: Wei Jia, Zhicong Lu, Yu Chen, Xiang Wang, Shuai Li, Wenqian Lv, Jiayue Cao, Huaxing liu
url: http://arxiv.org/abs/2608.02078v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAVE: Competence-Aware Visual Boundary Evidence Alignment for Video Temporal Grounding

## Abstract
Large vision-language models (LVLMs) have achieved substantial performance gains in Video Temporal Grounding (VTG) through reinforcement learning (RL). However, existing methods primarily rely on outcome correctness rewards that evaluate only the final predicted intervals, leaving boundary-related visual evidence and its correspondence with timestamp predictions insufficiently constrained. In this paper, we delve into timestamp prediction and its underlying boundary-level visual evidence, showing prevalent misalignment between visual evidence and predicted timestamps across widely used benchmarks. To address this issue, we propose Competence-Aware Visual Boundary Evidence Alignment (CAVE), which augments localization optimization with boundary-specific visual evidence rewards to mitigate evidence-timestamp misalignment. Specifically, to explicitly represent the boundary-specific visual evidence, CAVE introduces boundary-specific evidence tokens and initializes their structured generation and distinct boundary semantics through a lightweight supervised warm-up. During RL, the visual boundary evidence alignment reward reinforces the visual attention of special evidence tokens within the ground-truth boundaries, thereby promoting alignment between visual evidence and temporal boundaries. Moreover, performance-aware gating for evidence supervision is designed to adaptively retain evidence guidance for poorly localized groups while reducing it once localization becomes sufficiently accurate to avoid over-constraining fine-grained boundary refinement. Extensive experiments on several public VTG benchmarks demonstrate the effectiveness of our method.

## Metadata
- **Published**: 2026-08-03T11:27:29Z
- **Authors**: Wei Jia, Zhicong Lu, Yu Chen, Xiang Wang, Shuai Li, Wenqian Lv, Jiayue Cao, Huaxing liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02078v1)