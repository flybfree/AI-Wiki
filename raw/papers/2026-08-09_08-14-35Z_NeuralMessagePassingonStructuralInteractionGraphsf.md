---
title: Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks
published: 2026-08-09T08:14:35Z
authors: Omer Yom Tov, Avigdor Gal
url: http://arxiv.org/abs/2608.08567v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks

## Abstract
A central obstacle in building graph foundation models is the input heterogeneity in terms of feature space dimensionality, semantics, and structure. Such heterogeneity limits the capability of graph neural networks to generalize to new graphs with unseen feature spaces. We address the transferability challenge with SIGIL, a framework that maps any attributed graph to a unified representation space of fixed dimension. Given a graph, SIGIL lifts it to a structural interaction graph, where nodes are the input feature dimensions and weighted, typed edges encode feature alignment across multiple orders of the graph's connectivity. A relational message-passing network embeds each feature dimension into a shared space, transforming the original node features, of arbitrary dimensionality, into representations transferable to any downstream graph. By construction, SIGIL is equivariant to permutations of nodes, feature dimensions, and labels. Additionally, when the input features are one-hot indicators of discrete relations, SIGIL recovers and strictly generalizes existing foundation models for knowledge graph reasoning. A single SIGIL model, pretrained on one graph, delivers strong fully-inductive link prediction. Also, SIGIL can be used to implement existing knowledge graph foundation models. As such, SIGIL unifies several existing regimes in graph foundation model design under a single framework

## Metadata
- **Published**: 2026-08-09T08:14:35Z
- **Authors**: Omer Yom Tov, Avigdor Gal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08567v1)