---
title: SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents
published: 2026-08-08T10:42:31Z
authors: Fengrong Wan, Chengcan Wu, Ningtao Lyu
url: http://arxiv.org/abs/2608.08055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents

## Abstract
Large language model (LLM) agents that assist users over weeks of conversation must remember what is currently true, not merely what was once said. Flat RAG diaries and Markdown logs optimize needle retrieval but under-serve currency, provenance, and ordered temporal reasoning (Maharana et al. 2024; Wu et al. 2024; Packer et al. 2023; Chhikara et al. 2025). We present SodaMem, an evidence-grounded temporal graph memory that (i) extracts typed FactEvents with mandatory provenance spans, (ii) persists mention time, occurrence time, and validity with SUPERSEDES/CONTRADICTS/UPDATES edges under hybrid lexical-dense indexing, and (iii) answers via a planner-reader loop that gathers citable evidence before composing a final response. On LongMemEval-S, our store-of-record configuration reaches 92.8% accuracy (464/500; best of N=3) at mean $0.00161/question (approximately 18.3k tokens; median $0.00111 / approximately 14.6k) with deepseek-v4-flash. We compile public systems with estimable API cost into a cost table and cost-accuracy map; under these estimates SodaMem sits near the accuracy frontier at Flash-tier spend and strictly dominates several higher-cost, lower-accuracy points. Accuracy uses the same Flash model as reader and judge (self-grading); costs exclude ingest/judge and cross-system comparisons are compiled estimates rather than a single-harness bake-off.Our code is available at https://github.com/SodaMem/SodaMem

## Metadata
- **Published**: 2026-08-08T10:42:31Z
- **Authors**: Fengrong Wan, Chengcan Wu, Ningtao Lyu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08055v1)