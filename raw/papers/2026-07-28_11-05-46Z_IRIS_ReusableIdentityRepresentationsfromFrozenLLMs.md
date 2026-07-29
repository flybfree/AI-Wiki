---
title: IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment
published: 2026-07-28T11:05:46Z
authors: Xinran Liu, Shengtao Li, Shouqian Shi, Ge Wang, Xin-Wei Yao
url: http://arxiv.org/abs/2607.25579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment

## Abstract
Entity alignment (EA) identifies entities across knowledge graphs (KGs) that refer to the same real-world object. Conventional EA methods mainly exploit explicit graph structures and textual fields, which often provide insufficient semantic understanding to recognize the same entity under heterogeneous descriptions and distinguish it from semantically similar entities. Although large language models (LLMs) offer deeper entity understanding, existing LLM-based EA methods largely use this capability for auxiliary generation or candidate-conditioned decisions. Consequently, such understanding is not distilled into a stable and directly comparable identity space, leaving alignment tied to specific KG pairs or candidate sets and requiring repeated processing as the matching context changes. To address these limitations, we propose IRIS (Identity Representations from Internal States), a training-free framework that constructs for each entity an iris-like signature encoding its distinctive and stable identity characteristics. IRIS derives these signatures by eliciting identity-oriented contextual representations from a frozen LLM, thereby forming a shared space in which each entity is encoded once and can be aligned across different KGs through direct similarity comparison, without pair-dependent representation construction or candidate-wise LLM inference. Across four established EA benchmarks and two frozen LLM backbones, the best IRIS variants achieve Hits@1 scores of 100.00, 99.38, 98.31, and 97.99 on D-Y-15K V2, DBP-WIKI, ICEWS-WIKI, and ICEWS-YAGO, respectively.

## Metadata
- **Published**: 2026-07-28T11:05:46Z
- **Authors**: Xinran Liu, Shengtao Li, Shouqian Shi, Ge Wang, Xin-Wei Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25579v1)