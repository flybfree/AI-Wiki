---
title: Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection
published: 2026-09-16T12:51:51Z
authors: Ziyi Zhou, Xiaoming Zhang, Hui Pang, Yuting Zhang, Tiesunlong Shen, Bingyu Yan, Erik Cambria, Litian Zhang
url: http://arxiv.org/abs/2609.18597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection

## Abstract
Propagation structures provide crucial evidence for fake news detection, yet existing approaches primarily rely on supervised GNN-based models, which require substantial labeled data and exhibit limited generalization. Although large language models (LLMs) exhibit strong reasoning capabilities, directly feeding them raw propagation graphs creates a significant modality mismatch and severe information overload, making structure-aware reasoning unreliable in zero-shot and few-shot settings. To bridge this gap, we propose MAGER, a multi-agent genetic evolution framework that automatically discovers meta-paths optimized for LLM reasoning. By compressing complex propagation graphs into informative subgraphs, the evolved meta-paths alleviate both information overload and modality mismatch, enabling frozen LLMs to perform structure-aware veracity reasoning. We further introduce a graph in-context learning strategy that retrieves semantically and structurally similar demonstrations to strengthen classification and reasoning. Extensive experiments show that MAGER substantially improves frozen LLMs as standalone fake news detectors in data-efficient settings. Our code is available at https://github.com/SenticNet/MAGER.

## Metadata
- **Published**: 2026-09-16T12:51:51Z
- **Authors**: Ziyi Zhou, Xiaoming Zhang, Hui Pang, Yuting Zhang, Tiesunlong Shen, Bingyu Yan, Erik Cambria, Litian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18597v1)