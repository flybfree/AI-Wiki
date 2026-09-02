---
title: TempCloze: Can Video-LLMs Identify the Missing Middle?
published: 2026-09-01T16:45:02Z
authors: Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu, Jiahao Meng, Han Chen, Ziyu Wang, Hongyang Du
url: http://arxiv.org/abs/2609.01515v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TempCloze: Can Video-LLMs Identify the Missing Middle?

## Abstract
Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly long-take and egocentric videos. We construct same-source distractors along three dimensions: Semantic asks what event should happen, Alignment probes when it should occur, and Progression tests how it should unfold, while shared scenes and objects reduce appearance cues. Our evaluation of 10 proprietary and 21 open-source Video-LLMs reveals Alignment as the primary bottleneck: models often recognize plausible semantic content and local event progression but struggle with temporal alignment. We further conduct error pattern and behavioral sensitivity analyses on TempCloze-Mixed and TempCloze-Hard with four representative models to examine where errors arise and how candidate order, context direction, visible span, frame density, and test-time scaling influence model choices.

## Metadata
- **Published**: 2026-09-01T16:45:02Z
- **Authors**: Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu, Jiahao Meng, Han Chen, Ziyu Wang, Hongyang Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01515v1)