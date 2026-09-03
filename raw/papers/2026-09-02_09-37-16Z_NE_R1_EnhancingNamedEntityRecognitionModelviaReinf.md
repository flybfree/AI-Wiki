---
title: NE-R1: Enhancing Named Entity Recognition Model via Reinforcement Learning
published: 2026-09-02T09:37:16Z
authors: Meixuan Chen, Hehan Li, Ruizhi Zhao, Xin Lu, peizhi xu, Liwei Qian, LI Meifang, shuanglong li, Hanmeng Liu, Xin Pei, Yanbiao Ma
url: http://arxiv.org/abs/2609.02366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NE-R1: Enhancing Named Entity Recognition Model via Reinforcement Learning

## Abstract
Named Entity Recognition (NER) has achieved substantial progress since the advent of large language models (LLMs). Nevertheless, the recognition of long-tail and domain-specific entities remains challenging due to the deficiency in parametric knowledge. Retrieval-augmented generation (RAG) offers a promising remedy by injecting external knowledge, but it also introduces noise and unnecessary cost when dealing with familiar cases. In this paper, we propose NE-R1, a novel framework for adaptive retrieval-augmented NER. We design a "retrieval-on-demand" mechanism for NER. Then we integrate it into models by a two-stage training method: (1) multi-task instruction tuning initialization; (2) end-to-end RL optimization with CoT. To achieve reasonable selection between parameterized and external knowledge, we design a multi-dimensional reward considering both accuracy and retrieval benefit. NE-R1 achieves state-of-the-art performance on various benchmarks, with an average F1 score gain of 2.52% in in-domain evaluation and 1.18% in zero-shot cross-domain evaluation.

## Metadata
- **Published**: 2026-09-02T09:37:16Z
- **Authors**: Meixuan Chen, Hehan Li, Ruizhi Zhao, Xin Lu, peizhi xu, Liwei Qian, LI Meifang, shuanglong li, Hanmeng Liu, Xin Pei, Yanbiao Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02366v1)