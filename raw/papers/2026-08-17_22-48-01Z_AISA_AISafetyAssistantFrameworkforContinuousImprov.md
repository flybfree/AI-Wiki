---
title: AISA: AI Safety Assistant Framework for Continuous Improvement of Highway Construction
published: 2026-08-17T22:48:01Z
authors: Mason Smetana, Trevor Neece, Lev Khazanovich
url: http://arxiv.org/abs/2608.17184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AISA: AI Safety Assistant Framework for Continuous Improvement of Highway Construction

## Abstract
Job Safety Analysis (JSA) and pre-task planning can benefit from prior incident records, yet historical accident data is often stored as unstructured narratives that are difficult to consult at the point of planning. A novel framework centered on large language models (LLMs) for highway construction safety reporting and planning is proposed as a foundation for future agentic applications, prioritizing deterministic, local inferencing. The first aim is to enable classification and quality scoring of incident narratives for existing and future reporting purposes. The second is to evaluate retrieval of relevant historical accidents, related imagery, and trusted industry documents for incorporation into daily safety plans. Neural probes were trained to classify incidents along four multiclass and two binary Occupational Injury and Illness Classification System (OIICS) fields and to derive an overall quality score, evaluated on a test set of over 15,000 narratives and a held-out set of 100 author-labeled records, benchmarked against a majority-vote LLM ensemble. The retrieval of historical accidents, reference imagery, and industry documents was benchmarked across embedding models using standard information retrieval metrics. OIICS classification reached 75% held-out accuracy, though the two binary flags were degenerate. The quality score, while meaningful on one database, was distorted on out-of-distribution fatalities in the held-out dataset. Accident retrieval recovered relevant incidents far above chance, performing best on lexically distinct construction activities. On document question answering, an open-weight decoder embedding model surpassed proprietary models. Overall, this work provides a new framework rooted in local inferencing and text embedding models for future agentic applications, with emphasis on bridging external data to JSA reports.

## Metadata
- **Published**: 2026-08-17T22:48:01Z
- **Authors**: Mason Smetana, Trevor Neece, Lev Khazanovich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17184v1)