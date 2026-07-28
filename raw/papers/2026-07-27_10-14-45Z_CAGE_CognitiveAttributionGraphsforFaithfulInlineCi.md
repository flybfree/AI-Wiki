---
title: CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering
published: 2026-07-27T10:14:45Z
authors: Zhichao Yan, Shizhao Li, Jiapu Wang, Haoran Luo, Qingang Zhang, Jiaoyan Chen, Ru Li, Jeff Z. Pan
url: http://arxiv.org/abs/2607.24236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering

## Abstract
Long-form question answering increasingly relies on retrieved evidence to make LLM outputs verifiable, with inline citations tracing claims to source documents. However, existing systems often attach citations that are topically related but insufficient to support their claims. We identify attribution ambiguity as a structural challenge: end-to-end generation must implicitly resolve combinatorial claim--document assignments, obscuring evidential boundaries and increasing the risk of evidence-boundary overrun, where claims exceed cited support. To address this challenge, we propose CAGE (Cognitive Attribution Graphs for Citation Generation), a two-stage framework that introduces an explicit cognitive attribution map before answer generation. CAGE first trains a plug-and-play Cognitive Map Induction Model to construct answer-centered support subgraphs, aligning each semantic answer unit with supporting documents through explicit relations. A Structured Citation Reasoning Model then realizes these units as sentence-level claims with map-aligned citations. Experiments on ASQA, ELI5, and ExpertQA show that CAGE achieves state-of-the-art performance, demonstrating the effectiveness of attribution-space contraction and map-guided citation generation.

## Metadata
- **Published**: 2026-07-27T10:14:45Z
- **Authors**: Zhichao Yan, Shizhao Li, Jiapu Wang, Haoran Luo, Qingang Zhang, Jiaoyan Chen, Ru Li, Jeff Z. Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24236v1)