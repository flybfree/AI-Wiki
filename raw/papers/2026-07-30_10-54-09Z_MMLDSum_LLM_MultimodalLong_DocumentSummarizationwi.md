---
title: MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware
published: 2026-07-30T10:54:09Z
authors: Xianpeng Zhang, Jiahua Yang, Dongyu Chen, Lei zhang, Jian Ma, Xu guohuan, Haonan Lu, Tianhuang Su, Chuangchuang Wang, Kai Tang
url: http://arxiv.org/abs/2607.28006v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware

## Abstract
Multimodal long documents are core carriers of professional knowledge, where critical evidence is sparsely distributed across paragraphs and modalities. This easily causes key information omission and cross-modal hallucinations in summarization by multimodal LLMs. These issues stem from attention drift in long-range dependency modeling and gaps in inter-modal alignment. To address this, we introduce MMLDSum-Bench, a high-quality benchmark for multimodal long-document summarization, covering multiple domains, context-length scales, and visual-textual modality distributions. We further propose MMLDSum-LLM, a reproducible two-stage training framework that combines supervised fine-tuning with visual-alignment weighted loss and keyword-aware weighted loss, followed by GRPO with a multi-objective reward (keyword coverage, image-text alignment, ROUGE, and length control). Extensive experiments on MMLDSum-Bench, comparing against leading closed-source and open-source multimodal models under a unified evaluation protocol - including LLM-as-a-judge scoring, atomic-claim precision/recall, image-text alignment (ITA), and ROUGE - demonstrate that our approach significantly improves key-information coverage and cross-modal consistency.

## Metadata
- **Published**: 2026-07-30T10:54:09Z
- **Authors**: Xianpeng Zhang, Jiahua Yang, Dongyu Chen, Lei zhang, Jian Ma, Xu guohuan, Haonan Lu, Tianhuang Su, Chuangchuang Wang, Kai Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28006v1)