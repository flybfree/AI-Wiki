---
title: A Scaled-Up Empirical Study of Syntactic Language Models
published: 2026-10-12T14:16:58Z
authors: Pengcheng Wang, Zhexuan Zhang, Chao Lou, Kewei Tu
url: http://arxiv.org/abs/2610.16837v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Scaled-Up Empirical Study of Syntactic Language Models

## Abstract
Syntactic language models (SLMs) that generate sentences along with their syntactic tree structures have shown promise in both syntactic generalization and downstream tasks. Prior studies, however, have mostly evaluated smaller models trained on less pretraining data and tested on narrower task suites. In addition, the design space of tree linearization and attention masks remains underexplored. We conduct a large-scale empirical study of 12 controlled configurations---one terminal baseline and 11 SLM variants spanning different linearizations and masks---at scales up to 1B parameters and 100B training tokens, evaluated across 11 downstream tasks and two syntactic benchmarks. The experimental results show that SLMs with standard causal attention match or exceed structural-mask variants across downstream and syntactic benchmarks. They require no architectural modifications and remain compatible with FlashAttention. We also observe that when scaling up to the 1B-parameter scale, the top-performing SLM variant no longer shows a clear advantage over a compute-matched non-structural baseline, suggesting that SLMs may become less competitive with scale. Our code is available at https://github.com/qlwpc/TG-Interpolation.

## Metadata
- **Published**: 2026-10-12T14:16:58Z
- **Authors**: Pengcheng Wang, Zhexuan Zhang, Chao Lou, Kewei Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16837v1)