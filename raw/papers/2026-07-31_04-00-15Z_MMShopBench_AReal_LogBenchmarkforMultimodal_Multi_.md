---
title: MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents
published: 2026-07-31T04:00:15Z
authors: Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu
url: http://arxiv.org/abs/2607.29002v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents

## Abstract
Online shoppers increasingly turn to AI shopping assistants, using images and multi-turn dialogue to express and refine product needs that are difficult to articulate in text alone. However, existing benchmarks largely rely on text-only or synthetic requests, underrepresenting complex real-world shopping requirements jointly expressed through images and language. We introduce MMShopBench, the first real-log benchmark for multimodal, multi-turn shopping agents. Built from carefully cleaned and manually annotated shopping logs, MMShopBench provides ground-truth annotations of each request's purchase intent and mandatory product requirements. Agents must infer these requirements jointly from user images and multi-turn dialogue, retrieve candidate products through image and text search, and verify that each candidate satisfies all requirements using its product images and structured attributes. We evaluate representative open-source and proprietary models using an evidence-grounded multimodal protocol and construct a companion training set for fine-tuning an open-source model. To ensure reproducible experimentation, we build an offline shopping sandbox, where fine-tuning substantially narrows the performance gap between our open-source model and leading proprietary models, demonstrating the effectiveness of our training data.

## Metadata
- **Published**: 2026-07-31T04:00:15Z
- **Authors**: Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29002v1)