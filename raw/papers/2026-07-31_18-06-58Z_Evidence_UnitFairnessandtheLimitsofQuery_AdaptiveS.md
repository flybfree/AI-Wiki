---
title: Evidence-Unit Fairness and the Limits of Query-Adaptive Sparse-Dense Fusion in Financial Document Retrieval
published: 2026-07-31T18:06:58Z
authors: Chenyu Wu, You Lin
url: http://arxiv.org/abs/2608.00183v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Unit Fairness and the Limits of Query-Adaptive Sparse-Dense Fusion in Financial Document Retrieval

## Abstract
Retrieval over financial filings is difficult because queries are short and acronym-heavy while the answer-bearing evidence sits inside long, table-dense documents. We study sparse-dense hybrid retrieval on FinDER, a benchmark of expert-annotated questions over corporate 10-K filings. Our first finding is methodological: if the retrieval unit is larger than the dense encoder's input window, the dense model never sees a large share of the labeled evidence, confounding comparison against a full-text sparse baseline. We measure this directly and remove it by segmenting the corpus into encoder-sized windows. On the corrected corpus, fusing BM25 and a compact dense encoder improves reference-level Hit@10 by roughly 28 percent over either component, and training-free, untuned reciprocal rank fusion exceeds the equal-weight blend in an exploratory comparison. We then ask whether choosing the fusion weight per query helps: an oracle over the interpolation-weight grid shows headroom of 21.8 percent, yet none of the three lightweight adaptive routers (a score-confidence heuristic, a random forest over query features, and a ridge regressor over query embeddings) establishes a statistically reliable improvement over the fixed blend under company-grouped cross-validation with cluster-robust inference. Simple fusion is a strong baseline here, and we discuss why per-query weighting does not capture the available headroom.

## Metadata
- **Published**: 2026-07-31T18:06:58Z
- **Authors**: Chenyu Wu, You Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00183v1)