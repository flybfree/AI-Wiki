---
title: TRACE-Memory: Public-Conditioned Retrieval and Utility-Aware Evidence Admission for Personalized Generation
published: 2026-08-09T03:30:02Z
authors: Jing Wang, Zhu Wang, Yifan Guo, Yulong Yang, Yunji Liang
url: http://arxiv.org/abs/2608.08446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE-Memory: Public-Conditioned Retrieval and Utility-Aware Evidence Admission for Personalized Generation

## Abstract
Personalized generation systems retrieve user history by request--memory relevance and inject it into the model context. Yet relevant history may concern the wrong preference aspect, duplicate public information, or provide insufficient support. We argue that personal memory should be used only when it adds utility beyond a public-only response. We propose TRACE-Memory, a two-stage framework for selective personalization. Stage 1 queries for user-specific information missing from the request and public context, then retrieves a coverage-oriented candidate pool. Stage 2 admits a compact subset of source-traceable evidence units, or the empty set, according to response-level incremental utility. We progressively train the query-generation and evidence-admission policies through structured SFT initialization, reduced-space stage-wise GRPO warm-up, and nested multi-sample Joint GRPO. Across 4,500 Controlled and Natural tasks from Goodreads, Amazon Reviews, and Reddit, TRACE-Memory consistently outperforms random and lexical memory use, improves over semantic retrieval, remains competitive with frontier-LLM memory pipelines as local generator capacity increases, and conditions evidence admission on public-context sufficiency, supporting selective rather than default personalization.

## Metadata
- **Published**: 2026-08-09T03:30:02Z
- **Authors**: Jing Wang, Zhu Wang, Yifan Guo, Yulong Yang, Yunji Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08446v1)