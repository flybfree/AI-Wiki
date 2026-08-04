---
title: CeQe: Grounding Lexical Retrieval in Semantic Evidence
url: http://arxiv.org/abs/2608.00452v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_05-27-20Z_CeQe_GroundingLexicalRetrievalinSemanticEvidence.md
generated_at: 2026-08-03 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Cross‑Encoder Query Expansion (CE‑QE) to close the semantic vocabulary gap that limits lexical retrieval methods like BM25. By extracting decisive terms from cross‑encoder relevance attributions and appending them to the original query, CE‑QE boosts recall when queries and answers use different words.

## Key Takeaways
- The method seeds expansion with verbatim terms from retrieved passages rather than generating new ones, ensuring all added vocabulary exists in the corpus. 
- Unlike pseudo‑relevance feedback that reuses possibly inaccurate top results, CE‑QE uses semantic retriever outputs to avoid self‑reinforcing drift. 
- On BEIR datasets, CE‑QE raises NQ Recall@100 from 0.32 to 0.47 and its fusion variant outperforms SPLADEv2 and ColBERTv2 on nDCG@10.

## Context
Lexical retrieval remains a bottleneck in semantic search because exact keyword matching fails when paraphrasing occurs, limiting the usefulness of BM25‑based pipelines. This work demonstrates that augmenting queries with semantically informed terms can significantly improve recall without altering the underlying index.

## Implications
For practitioners building search systems, CE‑QE offers a lightweight way to enrich query relevance without costly model fine‑tuning. The approach could be integrated into existing hybrid pipelines to boost performance on diverse user queries and reduce false negatives in information retrieval tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00452v1)
