---
title: MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning
published: 2026-08-22T07:04:18Z
authors: Suifeng Zhao, Zida Liu, Xinyu Lei, Lei Sun, Jun Gao, Sujian Li
url: http://arxiv.org/abs/2608.21808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning

## Abstract
Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation and the generated answers. To address these limitations, we propose MCite-RL, a citation-enhanced agentic reinforcement learning framework designed for reliable multimodal RAG. MCite-RL introduces an Agentic Refinement module for visual citation that employs iterative retrieval, reasoning, and recursive cropping to progressively narrow the search space, transforming citation into a dynamic, evidence-driven reasoning process rather than a static step. Furthermore, we incorporate a Citation-enhanced Reward mechanism that integrates both process-level and outcome-level feedback within a reinforcement learning paradigm to jointly optimize answer accuracy and source traceability. Extensive experiments on benchmarks such as Wiki-VISA, FinRAGBench-V, and MMLongBench-Doc demonstrate that MCite-RL effectively achieves the joint optimization of citation precision and answer quality.

## Metadata
- **Published**: 2026-08-22T07:04:18Z
- **Authors**: Suifeng Zhao, Zida Liu, Xinyu Lei, Lei Sun, Jun Gao, Sujian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21808v1)