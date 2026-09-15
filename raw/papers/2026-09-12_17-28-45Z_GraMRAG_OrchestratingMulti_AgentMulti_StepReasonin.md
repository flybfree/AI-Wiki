---
title: GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning
published: 2026-09-12T17:28:45Z
authors: Zhongyu Wang
url: http://arxiv.org/abs/2609.14066v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning

## Abstract
Although existing multi-agent Retrieval-Augmented Generation (RAG) systems have demonstrated promise on complex multimodal reasoning tasks, they remain fundamentally limited in reasoning depth and memory structure, suffering from inadequate retrieval and state blindness when answering knowledge-intensive questions. To address these limitations, we propose GraMRAG, a graph memory-guided multi-agent RAG framework that integrates a dynamic multimodal memory graph to enable stable, multi-step multimodal reasoning. We introduce a vision-text bridged reasoning paradigm that unifies multi-scale entity cropping with a ReAct-style visual toolchain, enhancing the long-horizon cross-modal reasoning capability. We further construct a multimodal memory graph that formalizes agent reasoning as a dynamic directed acyclic graph (DAG), explicitly modeling action-observation dependencies to mitigate state blindness and suppress redundant retrieval. Moreover, we propose Topology-Aware Policy Optimization (TAPO) that leverages graph topology for critical path identification and targeted node pruning, enabling fine-grained credit assignment across multi-step reasoning trajectories. Extensive experiments on challenging multimodal benchmarks demonstrate that our approach consistently outperforms existing baselines and achieves state-of-the-art performance on complex long-horizon reasoning tasks.

## Metadata
- **Published**: 2026-09-12T17:28:45Z
- **Authors**: Zhongyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14066v1)