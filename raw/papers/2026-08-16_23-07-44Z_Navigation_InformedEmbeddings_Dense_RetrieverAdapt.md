---
title: Navigation-Informed Embeddings: Dense-Retriever Adaptation from Agent Search Traces
published: 2026-08-16T23:07:44Z
authors: Shrey Shah, Levent Ozgur
url: http://arxiv.org/abs/2608.15956v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Navigation-Informed Embeddings: Dense-Retriever Adaptation from Agent Search Traces

## Abstract
Agentic retrieval workflows produce query, retrieval, and stopping traces as a byproduct of answering questions. We study how these traces can adapt a deployed dense retriever to changing workflow distributions without new relevance labels, synthetic queries, or LLM judgments. We introduce Navigation-Informed Embeddings (NIE), a family of trace-derived objectives. NIE-Stop turns the stopping document into a soft positive; NIE-Path additionally uses preceding path documents as hard comparisons and imposes ordinal constraints with geometric decay. A BGE encoder adapted from retained source trajectories improves support Recall@20 on an independent target benchmark from 72.2 to 78.0 overall. NIE-Stop reaches 76.9 overall and 52.3 on long paths; NIE-Path raises long-path performance to 55.4, compared with 46.7 for the unadapted encoder. A shuffled-order control under the full path objective loses 3.2 points. Without public-benchmark training, the same adapter also improves nDCG@10 by 1.9 points on standard BEIR HotpotQA. NIE therefore provides a lightweight adaptation channel for settings where trajectories are already retained, with zero incremental labeling cost.

## Metadata
- **Published**: 2026-08-16T23:07:44Z
- **Authors**: Shrey Shah, Levent Ozgur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15956v1)