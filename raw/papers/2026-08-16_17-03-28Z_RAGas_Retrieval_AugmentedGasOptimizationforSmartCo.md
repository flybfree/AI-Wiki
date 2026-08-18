---
title: RAGas: Retrieval-Augmented Gas Optimization for Smart Contracts with Continuous Knowledge Integration
published: 2026-08-16T17:03:28Z
authors: Yishun Wang, Wenjin Yi, Wenkai Li, Zongwei Li, Xiaoqi Li
url: http://arxiv.org/abs/2608.15857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAGas: Retrieval-Augmented Gas Optimization for Smart Contracts with Continuous Knowledge Integration

## Abstract
Ethereum is now integral to mission-critical sectors, including finance, healthcare, and supply chain management. Execution fees, commonly referred to as Gas, scale with the computational complexity of their functions. Smart contracts on Ethereum incur execution fees, known as Gas, which increase with computational complexity. Thus, optimizing Gas-intensive code while preserving functional equivalence significantly lowers deployment costs. No existing system continuously exploits evolving Gas usage patterns. We systematically analyze syntactic and semantic constructs that drive excessive Gas use. This yields six high-level categories covering twelve fine-grained antipatterns underpinning a curated knowledge base. We operationalize these insights with RAGas, a three-stage retrieval-augmented generation framework that uses a large language model to pinpoint and automatically fix Gas inefficiencies. Experiments on deployed contracts demonstrate that RAGas reduces Gas usage by up to 11% and achieves high precision and recall in detecting code snippets exhibiting Gas wastage.

## Metadata
- **Published**: 2026-08-16T17:03:28Z
- **Authors**: Yishun Wang, Wenjin Yi, Wenkai Li, Zongwei Li, Xiaoqi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15857v1)