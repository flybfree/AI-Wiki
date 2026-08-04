---
title: AttnLink: Turning Attention into Schema Links for Text-to-SQL
published: 2026-08-01T14:44:25Z
authors: Jinwang Song, Tao Liu, Haowen Zheng, Xiangheng Li, Yifan Li, Hongying Zan
url: http://arxiv.org/abs/2608.00693v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AttnLink: Turning Attention into Schema Links for Text-to-SQL

## Abstract
Schema linking is a critical component of Text-to-SQL systems, but existing approaches often trade off contextual modeling capacity, score-based controllability, and inference efficiency. We introduce AttnLink, an attention-based framework that converts LLMs' internal attention into continuous relevance scores for schema items. AttnLink extracts the attention from the generation-start position to candidate schema spans, enabling all candidates to be ranked in a single prefill pass without autoregressive decoding. We develop two variants: AttnLink-U, which directly probes pretrained attention without parameter updates, and AttnLink-S, which aligns the attention distribution with gold schema items through direct supervision. To improve coverage of multiple relevant schema items, AttnLink-S combines a set-mass objective with an adaptive probability-floor regularizer. The resulting scores support post-hoc precision-recall control through temperature scaling and cumulative-mass selection. Experiments on Spider, BIRD, and Spider2-SQLite show that AttnLink-S achieves mAP scores of 99.22%, 95.95%, and 83.29%, respectively, with millisecond-scale schema-linking latency. It also yields the best or tied-best execution accuracy for downstream SQL generation in seven of nine generator-dataset settings.

## Metadata
- **Published**: 2026-08-01T14:44:25Z
- **Authors**: Jinwang Song, Tao Liu, Haowen Zheng, Xiangheng Li, Yifan Li, Hongying Zan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00693v1)