---
title: SAFE-G: Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering
published: 2026-08-22T06:34:53Z
authors: Long Shu, Shuochen Liu, Wei Chen, Junda Lin, Zhi Zheng, Huijun Hou, Tong Xu
url: http://arxiv.org/abs/2608.21796v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAFE-G: Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering

## Abstract
Knowledge-based Visual Question Answering (KB-VQA) aims to answer queries that necessitate reasoning over external knowledge sources beyond the visual content. Typically, current methods fuse multimodal features to retrieve external information, subsequently leveraging Multimodal Large Language Models (MLLMs) to derive answers from the retrieved evidence. However, these methods often struggle to capture structural associations within complex contexts to effectively filter noise. Furthermore, they frequently fail to ensure that the reasoning process remains strictly faithful to the retrieved evidence. To address these challenges, we propose SAFE-G, a Structure-Aware Faithful Evidence-guided Generation framework, which enables precise evidence localization and trustworthy reasoning. Specifically, we first employ a coarse-grained hybrid search fusing visual and textual modalities to recall candidate documents, and subsequently implement a structure-aware fine-grained graph retrieval that captures structural dependencies to filter noise and pinpoint precise evidence. Moreover, we introduce a reinforcement learning (RL) strategy with an evidence-grounded reward that assigns credit to correct answers only when the selected evidence is correct. This strict alignment constraint compels the model to anchor its response in the retrieved context, effectively enhancing its capability to locate evidence via multimodal features and perform faithful reasoning. Extensive experiments on the Encyclopedic-VQA and InfoSeek benchmarks demonstrate that SAFE-G outperforms prior methods by a margin of 8.9% and 3.5%, substantially enhancing the overall reasoning accuracy. Our source code is publicly available at: https://github.com/MINE-USTC/SAFE-G.

## Metadata
- **Published**: 2026-08-22T06:34:53Z
- **Authors**: Long Shu, Shuochen Liu, Wei Chen, Junda Lin, Zhi Zheng, Huijun Hou, Tong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21796v1)