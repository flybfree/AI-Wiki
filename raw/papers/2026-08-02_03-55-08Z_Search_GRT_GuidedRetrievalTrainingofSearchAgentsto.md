---
title: Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering
published: 2026-08-02T03:55:08Z
authors: Aounon Kumar, Sudipta Paul, Vivek Kulkarni, Vijay Srinivasan, Srinivas Chappidi
url: http://arxiv.org/abs/2608.00974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering

## Abstract
The effective use of search engines by large language models (LLMs) remains a significant challenge, particularly in complex, multi-hop question-answering (MHQA) tasks. These tasks require the model to decompose questions into subqueries, retrieve relevant information, and synthesize answers from multiple sources, often leading to cascading errors due to poor retrieval in early stages. Reinforcement learning (RL) has shown promise in improving LLMs' search capabilities, but it often suffers from sparse rewards during training, hindering the model's ability to learn effectively. To address these challenges, we introduce Guided Retrieval Training (GRT), a novel method that improves the performance of a search agent by restricting the retrieval process during RL training using ground truth information. By focusing on a curated set of relevant documents, GRT provides the model with a stronger learning signal, mitigating the problem of sparse rewards and improving its ability to generate accurate subqueries and synthesize correct answers. Our experimental results demonstrate that GRT achieves consistent performance improvements over existing methods, such as Search-R1, across a wide range of question-answering (QA) tasks. Notably, GRT excels in MHQA tasks, achieving over 40% improvements in performance. Additionally, GRT enhances training efficiency by achieving better QA performance with fewer training steps.

## Metadata
- **Published**: 2026-08-02T03:55:08Z
- **Authors**: Aounon Kumar, Sudipta Paul, Vivek Kulkarni, Vijay Srinivasan, Srinivas Chappidi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00974v1)