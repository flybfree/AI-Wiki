---
title: Towards Trustworthy Hypergraph Neural Networks under Label Noise
published: 2026-08-05T02:36:58Z
authors: Mengyao Zhou, Zhiheng Zhou, Xiao Han, Guiying Yan
url: http://arxiv.org/abs/2608.04377v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Trustworthy Hypergraph Neural Networks under Label Noise

## Abstract
Hypergraph neural networks (HGNNs) have demonstrated remarkable capabilities in processing complex higher-order relationships. However, their performance is highly dependent on labeled data, making them vulnerable to label noise. Despite advances in learning with label noise (LLN) and graph learning with label noise (GLN), noisy-label learning on hypergraphs remains underexplored. In this paper, we present a systematic study of hypergraph node classification under label noise. First, we adapt representative LLN and GLN methods to hypergraphs and evaluate them under a unified benchmark, revealing the limitations of existing robust learning strategies for hypergraphs. Building on this, we propose a new hypergraph robust framework, HyperTrust, which first estimates hyperedge trustworthiness through a pretraining-based, entropy-aware strategy, and then incorporates the HyperedgeBoost module to enhance reliable supervision by connecting unlabeled nodes to trustworthy hyperedges, as well as the HyperedgePrune module to suppress noisy propagation by removing untrustworthy node-hyperedge incidences. Finally, two modules work collaboratively to adjust the hypergraph structure and generate final predictions. Extensive experiments and theoretical analysis demonstrate the effectiveness and robustness of HyperTrust on multiple hypergraph datasets under various noisy settings. Our work provides a unified benchmark and an effective solution for hypergraph learning with label noise and lays a foundation for future research in this direction.

## Metadata
- **Published**: 2026-08-05T02:36:58Z
- **Authors**: Mengyao Zhou, Zhiheng Zhou, Xiao Han, Guiying Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04377v1)