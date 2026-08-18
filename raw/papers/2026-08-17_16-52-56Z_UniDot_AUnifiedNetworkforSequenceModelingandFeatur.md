---
title: UniDot: A Unified Network for Sequence Modeling and Feature Interaction in Large-scale Recommendation
published: 2026-08-17T16:52:56Z
authors: Rongcheng Lin, Yan Sun, Jamey Zhang, Guanglei Xiong, Ivan Ji, Xianjie Chen, Shujian Bu
url: http://arxiv.org/abs/2608.16797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniDot: A Unified Network for Sequence Modeling and Feature Interaction in Large-scale Recommendation

## Abstract
Industrial recommenders rely on two model families that have evolved largely independently: feature-interaction models over multi-field user/item features, and sequential models over user-behavior histories. Production systems couple them only loosely. To unify the two, we present UniDot, a novel architecture for post-click conversion prediction built from the factorization-machine (FM) point of view: the embedding inner product---which powers collaborative filtering and lets a recommender generalize to unseen user--item pairs---is the same primitive as attention's query dot key scoring, so a single dot-product of tokens can underlie both feature interaction and sequence modeling. UniDot tokenizes non-sequential fields and multi-domain behavioral sequences into one shared token space and stacks a single macro-block in which a token-mixing bus and a sequence-retrieval bus (item tokens cross-attending the histories) run in parallel and exchange state each layer through an MLP-Mixer fusion, while an FM Highway carries explicit per-layer dot-product interactions around the residual stack directly to the classifier. The sequence side is embedded once per forward pass and shared by all consumers, bounding inference latency. Trained with a dual sparse/dense (Adagrad + Muon) optimizer, an auxiliary conversion-delay head, and multi-path mutual learning, UniDot finished as the runner-up on the Industrial track of the TAAC KDD Cup 2026.

## Metadata
- **Published**: 2026-08-17T16:52:56Z
- **Authors**: Rongcheng Lin, Yan Sun, Jamey Zhang, Guanglei Xiong, Ivan Ji, Xianjie Chen, Shujian Bu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16797v1)