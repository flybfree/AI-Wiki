---
title: A Cross-Domain Evaluation of Prompting Techniques for Large Language Models
published: 2026-10-17T23:18:46Z
authors: Kevin Krazius, Tim Schlippe, Paul Libbrecht
url: http://arxiv.org/abs/2610.24913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Cross-Domain Evaluation of Prompting Techniques for Large Language Models

## Abstract
Prompt engineering has become a central mechanism for guiding the behavior of Large Language Models (LLMs) across a wide range of reasoning and language understanding tasks [1], [2]. However, existing studies frequently evaluate prompting techniques using different LLMs, datasets, or task settings, making direct comparisons across methods and domains difficult [3]. Consequently, in this paper we present a controlled cross-domain evaluation of Zero-Shot prompting, Few-Shot prompting, Retrieval-Augmented Generation (RAG), and automatic prompt optimization based on a PE2-inspired optimization pipeline [4]-[6]. All experiments were conducted with the same LLM and evaluated on six benchmark datasets covering arithmetic reasoning, logical reasoning, commonsense reasoning, and factual verification. The results show that no prompting strategy consistently outperforms the others across all domains, and pairwise statistical comparisons of the highest-performing configurations revealed no significant differences. RAG achieves the highest overall average accuracy of 78.33% when 300 examples are available for retrieval, while Few-Shot Prompting achieves comparatively high accuracies across several structured reasoning tasks. Zero-Shot Prompting remains competitive on tasks with self-contained inputs, whereas the PE2-inspired optimization approach produces stable but not systematically superior results compared to the other evaluated prompting techniques. Furthermore, increasing the number of task-specific examples does not consistently improve performance across prompting techniques, indicating strong domain and task dependency. These findings suggest that prompting techniques should be selected adaptively based on task characteristics rather than treated as universally applicable optimization strategies.

## Metadata
- **Published**: 2026-10-17T23:18:46Z
- **Authors**: Kevin Krazius, Tim Schlippe, Paul Libbrecht
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24913v1)