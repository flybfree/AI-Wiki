---
title: Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure in Heterogeneous Recommendation Graphs
published: 2026-07-22T21:33:02Z
authors: Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi, Farhad Farahani, Prakhar Mehrotra
url: http://arxiv.org/abs/2607.20737v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure in Heterogeneous Recommendation Graphs

## Abstract
Graph Neural Networks trained on heterogenous bipartite graphs form a common basis in recommendation systems. These graphs often express relations that vary in cardinality, for example, user-item preferences are one-to-many and user-attribute features are one-to-one. Traditionally, a unique loss function is applied for all of the network components which is often Bayesian Personalized Ranking (BPR). While BPR works well for the recommendation task, we find that it causes attribute embeddings to collapse to near-random geometry -- a silent failure that leaves standard ranking metrics largely unaffected and therefore invisible to conventional evaluation. This in turn pollutes user node embeddings, which are shaped by both edge types simultaneously, hurting downstream tasks like personalization, segmentation, etc. Here we propose a Cardinality-Decomposed Loss (CDL) that combines both Cross Entropy (CE) and BPR to enable the model to collectively optimize for relations across cardinalities. We confirm this CE-BPR conflict by showing the two losses compete in the shared encoder's parameter space. We evaluate CDL on five datasets spanning two structural configurations -- one-to-one attributes on user nodes (MovieLens-1M, Last.fm-360K, PayPal Audience Factory, BookCrossing) and on item nodes (Yelp) -- and find that CDL consistently improves discriminability in attribute embeddings. We also show that ranking (NDCG) improves when attributes carry meaningful preference signal, but conflicts with it when the correlation is weak. We use a lambda parameter to navigate this trade-off, and a lambda-sweep reveals that dataset behavior is governed by two graph properties -- semantic alignment and topology leakage. Semantic alignment measures whether the attribute predicts preferences, while topology leakage measures whether the graph's connectivity already encodes it.

## Metadata
- **Published**: 2026-07-22T21:33:02Z
- **Authors**: Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi, Farhad Farahani, Prakhar Mehrotra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20737v1)