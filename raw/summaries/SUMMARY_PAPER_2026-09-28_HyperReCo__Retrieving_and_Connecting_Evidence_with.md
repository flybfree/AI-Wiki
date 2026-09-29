---
title: HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning
url: http://arxiv.org/abs/2609.32327v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_07-43-30Z_HyperReCo_RetrievingandConnectingEvidencewithHyper.md
generated_at: 2026-09-28 20:58
model: qwen3.6-35b-a3b
---

## Summary
HyperReCo is a framework designed to enhance retrieval-augmented generation for large language models by utilizing hypergraph neural networks to retrieve and explicitly connect evidence for multi-hop reasoning. The approach addresses limitations in existing methods where query-dependent interactions are overlooked and evidence connections remain implicit, leading to superior retrieval performance and downstream question-answering accuracy across multiple benchmarks. By introducing Gradient-Guided Hyper-Path Decoding, the model translates learned interactions into explicit hyper-paths that facilitate more effective fact combination by the LLM.

## Key Takeaways
- The framework represents documents as hyperedges composed of extracted entities, where shared entities link these hyperedges; through message passing with joint supervision over documents and entities, the HyperGNN captures query-dependent interactions to retrieve complementary evidence that predefined structural expansions often miss.
- Gradient-Guided Hyper-Path Decoding (GGHD) leverages gradient attribution to interpret the learned hypergraph interactions and converts them into explicit hyper-paths, providing LLMs with clear structural guidance on how to connect retrieved evidence rather than requiring the model to reconstruct these relationships implicitly.
- Experimental evaluations demonstrate that HyperReCo achieves state-of-the-art retrieval performance among compared methods across three multi-hop question-answering datasets, while also delivering strong downstream QA

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32327v1)
