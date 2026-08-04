---
title: CeQe: Grounding Lexical Retrieval in Semantic Evidence
published: 2026-08-01T05:27:20Z
authors: Adam Kahirov, Umesh Deshpande, Swaminathan Sundararaman
url: http://arxiv.org/abs/2608.00452v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CeQe: Grounding Lexical Retrieval in Semantic Evidence

## Abstract
Lexical retrieval (BM25) captures exact keyword matches and weights terms by corpus-wide significance, but it is blind to the semantic vocabulary gap: when a relevant document phrases an answer differently from the query, BM25 never retrieves it, and no amount of downstream reranking or fusion can recover a document that was never in the candidate set. We present Cross-Encoder Query Expansion (CE-QE), which reads the per-token relevance attributions of a cross-encoder applied to top semantic search results, selects the terms the cross-encoder treats as decisive, and appends them to the BM25 query. Unlike classical pseudo-relevance feedback, which reuses BM25's own (possibly wrong) top results, CE-QE seeds expansion from the semantic retriever's results, avoiding self-reinforcing query drift. Unlike recent generative query expansion (HyDE, Query2doc), which prompts a large language model to hallucinate text from its parametric knowledge, every CE-QE expansion term is copied verbatim from a retrieved passage, so it cannot introduce vocabulary the corpus does not contain, and its only added cost is attribution extraction on a cross-encoder a hybrid pipeline already runs for reranking. On seven BEIR datasets, CE-QE improves lexical recall substantially where query and answer vocabulary diverge (e.g., NQ Recall@100 from 0.32 to 0.47), and its score-fusion variant (SESF) beats cross-encoder score fusion by 2.5% on Recall@100 and beats SPLADEv2 and ColBERTv2 by 5.3% and 4.6% on nDCG@10, while leaving the underlying BM25 index completely unmodified.

## Metadata
- **Published**: 2026-08-01T05:27:20Z
- **Authors**: Adam Kahirov, Umesh Deshpande, Swaminathan Sundararaman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00452v1)