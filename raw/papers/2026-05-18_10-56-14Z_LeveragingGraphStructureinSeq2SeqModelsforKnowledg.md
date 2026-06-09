---
title: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
published: 2026-05-18T10:56:14Z
authors: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
url: http://arxiv.org/abs/2605.18211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction

## Abstract
We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.

## Metadata
- **Published**: 2026-05-18T10:56:14Z
- **Authors**: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18211v1)