---
title: SmartRAG: Native Graph-Based RAG for Mobile Device
published: 2026-07-16T07:28:31Z
authors: Zhihan Jiang, Meng Li, Shenghao Liu, Keran Li, Ruiben Zhou, Wei Wang, Xianjun Deng, Shuai Wang, Haipeng Dai
url: http://arxiv.org/abs/2607.14661v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# SmartRAG: Native Graph-Based RAG for Mobile Device

## Abstract
Deploying large language models (LLMs) as personal assistants on mobile devices demands privacy, low latency, and offline availability, yet the computational cost of giant models clashes with strict edge-hardware budgets. We argue that this tension cannot be resolved by model compression alone; it requires decomposing on-device intelligence into complementary functional roles. We present SmartRAG, a fully on-device framework that organizes an intelligent assistant around four coordinated modules -- Perception, Memory, Focus, and Thinking. At the core of SmartRAG is EvoNER, a continually learnable named-entity recognizer that incrementally expands its label inventory through teacher-distilled updates, enabling the system to absorb previously unseen entity types without retraining the backbone LLM. Extracted knowledge is stored in MRGraph, a three-layer provenance-preserving knowledge graph, and retrieved at query time through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search. The on-device LLM is invoked only for high-value semantic operations -- labeling, planning, and answer synthesis -- keeping inference costs bounded. Experiments on four QA benchmarks (TriviaQA, Natural Questions, HotpotQA, MultiHopQA) show that SmartRAG with a quantized 1.7B-parameter backbone achieves multi-hop reasoning performance competitive with models up to 18$\times$ larger, while running entirely on commodity smartphones within practical memory and latency envelopes.

## Metadata
- **Published**: 2026-07-16T07:28:31Z
- **Authors**: Zhihan Jiang, Meng Li, Shenghao Liu, Keran Li, Ruiben Zhou, Wei Wang, Xianjun Deng, Shuai Wang, Haipeng Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14661v2)