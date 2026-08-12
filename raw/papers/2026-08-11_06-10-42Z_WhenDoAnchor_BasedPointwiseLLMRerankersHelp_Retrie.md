---
title: When Do Anchor-Based Pointwise LLM Rerankers Help? Retriever Quality, Statistical Scope, and Anchor Design
published: 2026-08-11T06:10:42Z
authors: Utshab Kumar Ghosh, Shubham Chatterjee
url: http://arxiv.org/abs/2608.10528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Anchor-Based Pointwise LLM Rerankers Help? Retriever Quality, Statistical Scope, and Anchor Design

## Abstract
Anchor-based pointwise LLM reranking scores each candidate against a shared reference passage to recover cross-document context at pointwise cost. We study when this actually helps, using GCCP/PAGC as a representative method. Our study is reproduction-first. We use reproduction as a starting point for a controlled component-level stress test of anchor-based pointwise reranking. Our initial reimplementation, based only on the paper text, achieves 0.24 nDCG@10 instead of the reported 0.66, revealing that several undocumented implementation details are necessary to reproduce the method. After identifying and recovering eight such details, we reproduce the reported results within 1.6% and use the validated implementation for controlled analysis.   We find that the core contrastive scoring idea is robust under rigorous statistical correction. However, two design choices held fixed in the original paper are less reliable. First, we find that combining the contrastive score with the standard pointwise relevance score helps when the first-stage retriever is BM25, but gives little or no benefit when the first-stage retriever is a stronger dense model such as E5. Second, the paper's more complex method for constructing the anchor is unnecessary. A much simpler anchor, built by interleaving the top-ranked sentences, matches or outperforms it across datasets. These findings are consistent across different LLM backbones, including a 4-bit quantized 72B model. Overall, anchor-based pointwise reranking is effective, but its gains come mainly from contrastive scoring rather than from the more complex aggregation and anchor-construction choices, and they appear under narrower conditions than the original evaluation suggests.

## Metadata
- **Published**: 2026-08-11T06:10:42Z
- **Authors**: Utshab Kumar Ghosh, Shubham Chatterjee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10528v1)