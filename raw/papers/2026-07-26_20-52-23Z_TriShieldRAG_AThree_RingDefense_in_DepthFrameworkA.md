---
title: TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation
published: 2026-07-26T20:52:23Z
authors: Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj, Jeenal Chaudhary, Disha Singhania
url: http://arxiv.org/abs/2607.23838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation

## Abstract
Retrieval-Augmented Generation (RAG) lets a large language model answer questions using documents retrieved from an external knowledge base at query time. This makes RAG useful for private data, fast-changing information, and reducing hallucination, but it also means the model's answer is only as trustworthy as whatever the retriever hands it. If the knowledge base accepts writes from more than one party, an attacker needs only a handful of adversarial documents to steer the model toward a chosen wrong answer. PoisonedRAG demonstrated this: as few as five crafted documents flip an undefended system's answer roughly 90% of the time, and three natural single-stage defenses (perplexity filtering, query paraphrasing, knowledge-base expansion) leave attack success at 30% or higher.   We built TriShieldRAG to close that gap. Rather than relying on one checkpoint, we place three independent, formally specified rings across the pipeline: an Ingest Guard that screens documents for lexical and statistical poisoning signatures; a Retrieval Scorer that re-ranks the retrieved set by a provenance and consistency-weighted trust score; and a Cross-LLM Consensus stage that polls three architecturally diverse language models (Claude, Mistral Small, Llama 3.2) and allows one bounded re-retrieval on disagreement.   We derive the conditions under which Rings 2 and 3 are expected to work: a minority-poison assumption and an explicit provenance-tag assumption. Our reported configuration is consistent with this analysis, though we have not yet run the controlled poison-fraction sweep needed to confirm it independently. Evaluated against the non-adaptive attacker from the original PoisonedRAG, over a 5,000-document Wikipedia knowledge base with 10 target questions, the full pipeline reduces attack success rate from roughly 91% to roughly 13% while preserving accuracy on benign queries.

## Metadata
- **Published**: 2026-07-26T20:52:23Z
- **Authors**: Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj, Jeenal Chaudhary, Disha Singhania
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23838v1)