---
title: CreaMem: A Scene-Aware Memory Architecture for Personalized Agents
published: 2026-09-08T10:33:05Z
authors: Qixuan Sun, Yue Que, Bowei He, Jin Guo, Dihang Yang, Wenchang Situ, Chen Ma
url: http://arxiv.org/abs/2609.08550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CreaMem: A Scene-Aware Memory Architecture for Personalized Agents

## Abstract
Long-term memory is a core capability for personalized LLM agents. To support it, existing memory systems organize information using various criteria such as topic segments or summary hierarchies. However, we identify two major limitations in these designs. First, they lack scene awareness: memories from unrelated life scenes share the same retrieval space, which inflates the search space and introduces cross-scene interference. Second, they encode each memory from a single perspective, making it difficult to retrieve complementary views of the same event. In this paper, we propose the CreaMem architecture, which enables scene-aware memory organization by partitioning memory into several Life Scene Memories to reduce cross-scene interference at retrieval. To go beyond the single perspective and achieve cross-memory synergy, entries are dual-coded from both episodic and trait-based perspectives within each memory. We further devise a permemory balanced sampling strategy at retrieval time. Extensive experiments on two long-term memory benchmarks show that CreaMem improves QA accuracy across all evaluation metrics, with particularly large gains on multi-hop reasoning performance, validating scene-aware partitioning and cross-memory synergy. To enhance reproducibility, we release our code in a public GitHub repository.

## Metadata
- **Published**: 2026-09-08T10:33:05Z
- **Authors**: Qixuan Sun, Yue Que, Bowei He, Jin Guo, Dihang Yang, Wenchang Situ, Chen Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08550v1)