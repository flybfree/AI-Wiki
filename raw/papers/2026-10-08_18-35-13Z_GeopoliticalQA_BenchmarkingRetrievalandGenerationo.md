---
title: GeopoliticalQA: Benchmarking Retrieval and Generation over Intelligence Reports
published: 2026-10-08T18:35:13Z
authors: Veronika Solopova, Ivan Havlytskyi, Viktoria Skorik, Ostap Vykhopen
url: http://arxiv.org/abs/2610.12617v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeopoliticalQA: Benchmarking Retrieval and Generation over Intelligence Reports

## Abstract
Geopolitical and strategic intelligence reports constitute a rich source of expert knowledge and have increasing value in the current political climate, but their heterogeneity and analytical complexity pose challenges for retrieval-augmented question answering. We introduce a benchmark for grounded question answering over 415 open-source geopolitical and strategic intelligence reports, comprising 5,525 document-grounded question-answer pairs spanning factual, inferential, comparative, and risk-oriented questions. We propose a document-aware generation pipeline that profiles reports before generating questions and validate dataset quality through expert annotation and an LLM-as-judge protocol. Using the benchmark, we evaluate 15 retrieval systems and six open-weight LLMs for RAG. We find that models perform similarly on document-level retrieval, while at the harder chunk level retrieval quality is not driven by embedding-model scale: bge-m3, a mid-size open encoder matches an order of magnitude larger ones and outperforms commercial embedding APIs. In contrast, answer generation remains challenging even given the gold evidence, particularly for inferential and risk-oriented questions.

## Metadata
- **Published**: 2026-10-08T18:35:13Z
- **Authors**: Veronika Solopova, Ivan Havlytskyi, Viktoria Skorik, Ostap Vykhopen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12617v1)