---
title: Harnessing the Potential of Optimizing Data Mixtures via Bayesian Domain Reweighting
published: 2026-07-30T09:41:02Z
authors: Xiang Yuan, Kaiqing Lei, Zhenyu Jin, Jun Shu, Deyu Meng, Zongben Xu
url: http://arxiv.org/abs/2607.27928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harnessing the Potential of Optimizing Data Mixtures via Bayesian Domain Reweighting

## Abstract
The performance of Large Language Models (LLMs) is fundamentally influenced by the distributional composition of multi-domain pre-training data. While manual heuristics were prevalent in early models, they increasingly fail to capture the intricate synergies between domains as data complexity grows. To overcome the issue, a dominant approach seeks to fit a proxy function mapping between domain weights and their corresponding validation losses, and then find the optimal domain weights to minimize validation losses. These methods rely on strong structural assumptions, such as rank invariance or scaling laws, which are often violated, resulting in non-negligible estimation bias. A promising approach is to directly optimize the weighting scheme from data. However, it suffers from unstable optimization trajectory and prohibitive computational overhead, limiting its potential to search better domain weights configurations. This paper presents a Bayesian domain weighting method to infer the weights from a Dirichlet distribution via introducing Gamma prior information learned from observations. Experimental results demonstrate that proposed method could achieve stable and efficient domain weights learning, and identifies optimal mixtures while consuming substantially less data than search-based function-fitting methods, revitalizing optimization-based domain weighting for large-scale applications.

## Metadata
- **Published**: 2026-07-30T09:41:02Z
- **Authors**: Xiang Yuan, Kaiqing Lei, Zhenyu Jin, Jun Shu, Deyu Meng, Zongben Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27928v1)