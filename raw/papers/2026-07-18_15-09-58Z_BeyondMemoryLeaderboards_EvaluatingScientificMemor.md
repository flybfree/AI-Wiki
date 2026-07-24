---
title: Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration
published: 2026-07-18T15:09:58Z
authors: Maksim Sheverev, David Finkelstein, Sergey Nikolenko
url: http://arxiv.org/abs/2607.16848v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration

## Abstract
Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers. We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions). We evaluate eight memory/retrieval systems, including our own proposed Theoria, plus a no-retrieval baseline. Our results show that memory leaderboards are not interpretable without the full protocol: ingestion granularity, raw-text preservation, retrieval budget, retrieval modality, rubric audit, and judge choice all affect the outcome. For example, on PAIM Graphiti wins convincingly but uses 2.6M characters of retrieved context per query, and after controlling for retrieval budget the lead disappears. On PTr, for the systems where BM25 retrieval can be added cleanly, the sparse-dense hybrid is the single most significant intervention: hybrid variants of Simple RAG, Mem0, and Theoria tie for the lead within 0.03 points. Multi-judge and human side-by-side calibration show that LLM-as-a-judge rankings are consistent across frontier judges and agree with human evaluation, with an effective resolution of roughly one point on a ten-point scale. We argue that scientific memory should be evaluated as budgeted, modality-aware context restoration rather than as an unconstrained architecture leaderboard, and we release the datasets, harness, raw outputs, judgments, and scripts to reproduce our results and serve as tools for such evaluation. Our code is available at http://gitlab.com/quantellence/research/scientific-recall-bench , and the datasets are available at http://huggingface.co/datasets/quantellence/srb-data .

## Metadata
- **Published**: 2026-07-18T15:09:58Z
- **Authors**: Maksim Sheverev, David Finkelstein, Sergey Nikolenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16848v1)