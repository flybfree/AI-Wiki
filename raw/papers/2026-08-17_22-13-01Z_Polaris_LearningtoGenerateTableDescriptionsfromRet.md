---
title: Polaris: Learning to Generate Table Descriptions from Retrieval Feedback
published: 2026-08-17T22:13:01Z
authors: Ting Cai, Tuan Minh Phan, AnHai Doan
url: http://arxiv.org/abs/2608.17171v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Polaris: Learning to Generate Table Descriptions from Retrieval Feedback

## Abstract
Many table-centric NLP tasks such as NL2SQL first retrieve relevant tables from large collections using keyword search. Recent work uses LLMs to generate natural-language table descriptions to improve retrieval, but they are typically optimized for fluency rather than retrieval effectiveness. We present Polaris, a system that trains an LLM to generate table descriptions directly from retrieval feedback. Our key insight is that existing table retrieval benchmarks already contain the supervision needed for this task: given query-table relevance judgments, we generate multiple candidate descriptions for each table, rank them by their BM25 retrieval effectiveness, and use the resulting preference pairs to fine-tune the LLM with Direct Preference Optimization (DPO). Polaris further expands abbreviated table and column names before generation to reduce vocabulary mismatch. Extensive experiments show that Polaris outperforms the state-of-the-art AutoDDG solution, often by a significant margin. More broadly, our results demonstrate that retrieval benchmarks can be repurposed as supervision for training LLMs to generate retrieval-oriented metadata.

## Metadata
- **Published**: 2026-08-17T22:13:01Z
- **Authors**: Ting Cai, Tuan Minh Phan, AnHai Doan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17171v1)