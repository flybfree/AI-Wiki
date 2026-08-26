---
title: GATNextHop: A GAT for Shortest Path Routing with Cross-Topology Generalization
published: 2026-08-24T23:50:52Z
authors: Chia-Hong Chou, Katerina Potika
url: http://arxiv.org/abs/2608.23917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GATNextHop: A GAT for Shortest Path Routing with Cross-Topology Generalization

## Abstract
Common shortest-path algorithms, such as Dijkstra's (SPF), that OSPF uses, provide exact routing solutions but must be recomputed for each network topology, limiting scalability in dynamic or large-scale networks. This paper proposes the GATNextHop model to determine whether a Graph Neural Network, namely the Graph Attention Network, can approximate shortest paths and generalize across topologies. By training on synthetic graphs and evaluating on real-world Internet Service Provider networks from the Internet Topology Zoo, we aim to benchmark our model's ability to learn routing heuristics that transfer across network structures. Performance will be evaluated in terms of accuracy, inference speed, and generalization, comparing the GNN against Dijkstra's algorithm to quantify trade-offs between learned and classical routing approaches.

## Metadata
- **Published**: 2026-08-24T23:50:52Z
- **Authors**: Chia-Hong Chou, Katerina Potika
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23917v1)