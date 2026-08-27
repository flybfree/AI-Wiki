---
title: A Storage-Retrieval Gap in Parametric Knowledge Graph Memory
published: 2026-08-26T08:02:00Z
authors: Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, Volker Tresp
url: http://arxiv.org/abs/2608.25489v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Storage-Retrieval Gap in Parametric Knowledge Graph Memory

## Abstract
Graph retrieval-augmented generation places retrieved subgraphs into the model's context window at query time, paying a recurring token cost and exposing source data on every call. We study an alternative: compiling a knowledge graph offline into a bank of LoRA adapters, one per entity, that serve as a parametric knowledge layer queried by injecting weights rather than text, at zero query-time context cost. On the MetaQA dataset, we find that subgraph-trained adapters encode context-free factual knowledge that generalizes to unseen questions: on single-valued relations the adapter gains $+0.243$ exact-match score over a base model that is nearly blind closed-book ($0.007$), and only the correct adapter recovers this knowledge (an oracle gap of $+0.283$ over the base model). However, the stored knowledge is not recoverable by similarity: given a query with no subgraph, embedding-based and weight-space geometry retrieval both perform at chance, because a semantically neighbouring entity's adapter does not contain the answer - knowledge is stored locally and does not transfer. Weight geometry correlates with subgraph semantics ($ρ= +0.329$) but not with functional retrievability. We quantify the byte and context-token costs against graph retrieval-augmented generation and discuss deployment implications. Our results establish that parametric knowledge graph memory is feasible for storing knowledge, and identify selecting and composing the right adapters by a mechanism other than semantic similarity as the central open problem - motivating a learned, query-conditioned composition mechanism.

## Metadata
- **Published**: 2026-08-26T08:02:00Z
- **Authors**: Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, Volker Tresp
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25489v1)