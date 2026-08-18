---
title: Disentangling Homophily and Rarity: Explaining Failure in Graph Neural Networks
published: 2026-08-14T18:52:32Z
authors: Preben M. Ness, Fariz Ikhwantri, Dusica Marijan
url: http://arxiv.org/abs/2608.14823v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Homophily and Rarity: Explaining Failure in Graph Neural Networks

## Abstract
Are heterophilic nodes in a graph harder to classify because they are heterophilic or because they are rare? Some existing work frames classification of such nodes as a subgroup generalisation problem, where a model performs well on the majority group at the expense of the rare group. Others explain this as a problem of neighbourhood aggregation in graph neural networks (GNNs). We assess these two viewpoints through a detailed evaluation of six GNNs on five datasets of varying homophily, and find that homophilic nodes tend to be easier to classify, even when they are rare---challenging the subgroup framing. However, our findings also nuance existing beliefs about how GNNs misrepresent heterophilic nodes. We demonstrate that the information needed to classify heterophilic nodes correctly is often recoverable by retraining the classification head of a model, or even just the final linear classification layer.

## Metadata
- **Published**: 2026-08-14T18:52:32Z
- **Authors**: Preben M. Ness, Fariz Ikhwantri, Dusica Marijan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14823v1)