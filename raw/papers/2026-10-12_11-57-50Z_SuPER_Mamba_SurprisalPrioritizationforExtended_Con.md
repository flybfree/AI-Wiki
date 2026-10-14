---
title: SuPER-Mamba: Surprisal Prioritization for Extended-Context Routing in Mamba
published: 2026-10-12T11:57:50Z
authors: Zhetong Zhang, Gayan K Kulatilleke
url: http://arxiv.org/abs/2610.16636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SuPER-Mamba: Surprisal Prioritization for Extended-Context Routing in Mamba

## Abstract
State space models provide efficient linear-complexity processing for long sequences, but their performance frequently degrades as context length grows. We propose SuPER-Mamba, a training-free framework that uses Surprisal as a model-intrinsic signal for long-range state routing in pretrained Mamba models. SuPER-Mamba computes position-wise Surprisal from next-token predictions, aggregates neighboring responses through Local Pooling, and uses the resulting scores to prioritize Global-Channel updates without query-dependent scoring or additional training. We evaluate SuPER-Mamba on three state-space models across the LongBench-E benchmark. The results show that SuPER-Mamba improves the average score from 8.06 to 15.69, corresponding to a 94.7% relative gain over the Base Models and a 13.1% improvement over the state-of-the-art prior baseline. Ablation and length-wise analyses further support the effectiveness of the proposed routing framework.

## Metadata
- **Published**: 2026-10-12T11:57:50Z
- **Authors**: Zhetong Zhang, Gayan K Kulatilleke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16636v1)