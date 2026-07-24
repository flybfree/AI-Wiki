---
title: RF-Agent: A Practical Framework for Building Language Agents for RFIC Design
published: 2026-07-21T06:53:09Z
authors: Yueqi Xing, Houbo He, Jolie Wang, Erin Ni, Shikai Wang, Qiufeng Li, Weidong Cao, Taiyun Chi
url: http://arxiv.org/abs/2607.18772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RF-Agent: A Practical Framework for Building Language Agents for RFIC Design

## Abstract
Large language models (LLMs) have driven rapid progress in electronic design automation (EDA), yet their application to radio-frequency (RF) circuit design remains limited by the scarcity of domain-specific datasets and standardized benchmarks. We present RF-Agent, which addresses this gap through textbook-driven knowledge distillation. A multi-agent Question-Thinking-Solution-Answer (QTSA) pipeline converts a subsection-level corpus from seven canonical RF textbooks into the first-of-its-kind RF-domain reasoning dataset (over 11,000 samples) with a dedicated multiple-choice benchmark. On this benchmark we study two adaptation strategies: supervised fine-tuning (SFT) and three retrieval-augmented generation (RAG) configurations (semantic, keyword, hybrid). Across multiple LLM families, domain-specific SFT significantly improves RF reasoning, especially for small and medium-sized models; among RAG configurations, semantic retrieval performs best, indicating embedding-based context alignment suits RF reasoning better than naive fusion. The dataset and benchmark provide a reusable foundation for future work on LLM-aided RF circuit design.

## Metadata
- **Published**: 2026-07-21T06:53:09Z
- **Authors**: Yueqi Xing, Houbo He, Jolie Wang, Erin Ni, Shikai Wang, Qiufeng Li, Weidong Cao, Taiyun Chi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18772v1)