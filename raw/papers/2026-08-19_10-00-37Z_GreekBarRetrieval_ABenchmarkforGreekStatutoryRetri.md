---
title: GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval
published: 2026-08-19T10:00:37Z
authors: Ernest Beta, Odysseas S. Chlapanis, Dimitrios Galanis, Ion Androutsopoulos
url: http://arxiv.org/abs/2608.18752v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval

## Abstract
Statutory retrieval is necessary for citation-grounded legal question answering, but remains underexplored for Greek. We introduce GreekBarRetrieval, a public retrieval benchmark derived from, and complementing GreekBarBench, which did not include retrieval. The new benchmark comprises 283 bar-exam questions, each accompanied by the facts of the case it refers to, and 6,308 candidate statutory articles to retrieve from. Questions and facts are stated in everyday language, but need to be mapped to the formal terminology of statutes and their abstract legal concepts. A further complication is that not all of the case facts are relevant to each question of a case. Experimenting with three BM25 variants and nine dense retrievers, we find that vanilla dense retrieval far outperforms vanilla sparse retrieval in Recall@100. However, LLM-based query reformulation helps BM25 close that gap, while also improving dense retrieval. With a ten-round ReAct-like LLM reformulation loop that we introduce, BM25 improves further in Recall@100 and obtains the best nDCG and MAP scores of all tested retrievers. Query reformulation also outperforms pseudo-relevance feedback, sparse-dense fusion, and English translation.

## Metadata
- **Published**: 2026-08-19T10:00:37Z
- **Authors**: Ernest Beta, Odysseas S. Chlapanis, Dimitrios Galanis, Ion Androutsopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18752v1)