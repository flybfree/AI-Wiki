---
title: HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning
published: 2026-09-26T07:43:30Z
authors: Zicheng Zhao, Linhao Luo, Junnan Dong, Haoran Luo, Xiaoli Li, Shirui Pan, Chen Gong
url: http://arxiv.org/abs/2609.32327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning

## Abstract
Large language models (LLMs) have shown strong capabilities, with retrieval-augmented generation (RAG) supporting complex multi-hop reasoning by retrieving evidence distributed across documents. Graph-based approaches exploit connections among evidence, and hypergraph-based retrieval further preserves higher-order entity associations within documents and connects documents through shared entities. However, existing hypergraph retrievers often rely on predefined structural expansion or diffusion, which may miss query-dependent interactions needed to identify relevant evidence. They also leave connections among retrieved evidence implicit, requiring LLMs to reconstruct these connections before reasoning. Therefore, we propose HyperReCo, a framework for retrieving and connecting evidence with a hypergraph neural network (HyperGNN). We represent each document as a hyperedge over its extracted entities, with shared entities connecting the hyperedges. Through hypergraph message passing with joint supervision over documents and entities, the HyperGNN learns query-dependent interactions to retrieve complementary evidence. We further introduce Gradient-Guided Hyper-Path Decoding (GGHD), which uses gradient attribution to interpret the learned interactions and translate them into explicit hyper-paths that help LLMs combine complementary facts for multi-hop reasoning. Experiments on six benchmarks show that HyperReCo achieves the best retrieval performance among the compared methods on all three multi-hop QA datasets, together with strong downstream QA performance. Case studies and further analyses demonstrate the utility of decoded hyper-paths for connecting retrieved evidence.

## Metadata
- **Published**: 2026-09-26T07:43:30Z
- **Authors**: Zicheng Zhao, Linhao Luo, Junnan Dong, Haoran Luo, Xiaoli Li, Shirui Pan, Chen Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32327v1)