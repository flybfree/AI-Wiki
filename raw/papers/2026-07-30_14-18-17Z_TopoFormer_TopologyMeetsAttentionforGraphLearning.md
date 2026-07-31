---
title: TopoFormer: Topology Meets Attention for Graph Learning
published: 2026-07-30T14:18:17Z
authors: Md Joshem Uddin, Astrit Tola, Cuneyt Gurcan Akcora, Baris Coskunuzer
url: http://arxiv.org/abs/2607.28259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TopoFormer: Topology Meets Attention for Graph Learning

## Abstract
We introduce Topoformer, a lightweight and scalable framework for graph representation learning that encodes topological structure into attention-friendly sequences. At the core of our method is Topo-Scan, a novel module that decomposes a graph into a short, ordered sequence of topological tokens by slicing over node or edge filtrations. These sequences capture multi-scale structural patterns, from local motifs to global organization, and are processed by a Transformer to produce expressive graph-level embeddings. Unlike traditional persistent homology pipelines, Topo-Scan is parallelizable, avoids costly diagram computations, and integrates seamlessly with standard deep learning architectures. We provide theoretical guarantees on the stability of our topological encodings and demonstrate state-of-the-art performance across graph classification and molecular property prediction benchmarks. Our results show that Topoformer matches or exceeds strong GNN and topology-based baselines while offering predictable and efficient compute. This work opens a new path for parallelizable and unifying approaches to graph representation learning that integrate topological inductive biases into attention frameworks.

## Metadata
- **Published**: 2026-07-30T14:18:17Z
- **Authors**: Md Joshem Uddin, Astrit Tola, Cuneyt Gurcan Akcora, Baris Coskunuzer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28259v1)