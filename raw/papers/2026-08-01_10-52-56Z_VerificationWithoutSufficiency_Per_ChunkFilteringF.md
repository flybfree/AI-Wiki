---
title: Verification Without Sufficiency: Per-Chunk Filtering Fails on Multi-Hop RAG, and Decomposition Repairs It
published: 2026-08-01T10:52:56Z
authors: Randhir Kumar
url: http://arxiv.org/abs/2608.00585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verification Without Sufficiency: Per-Chunk Filtering Fails on Multi-Hop RAG, and Decomposition Repairs It

## Abstract
Verification for retrieval-augmented generation usually scores each retrieved chunk and drops the ones that fail. We show this cannot work for multi-hop questions, and show what does. Per-chunk scoring assumes one chunk is a sufficient premise for the answer. Multi-hop questions are built so that none is, and the paragraph carrying the answer is the one the question does not name. Entailment scoring reaches 0.643, 0.523 and 0.560 AUC on HotpotQA, 2WikiMultihopQA and MuSiQue, against 0.951 on single-hop SQuAD. Seven controls rule out model capacity, premise length, hypothesis template, decision threshold, retriever, answer-matching criterion and prompt. End to end across three datasets, three generator sizes and two prompts, per-chunk gating is significantly worse than not filtering at all in every cell, and its penalty grows with generator capability. The repair is to condition verification on the decomposed sub-question rather than the original query. Using MuSiQue's gold decomposition, entailment on a later hop rises from 0.546, which is chance, to 0.840, a paired lift of +0.355 with a bootstrap interval of [0.331, 0.382]. An off-the-shelf Qwen2.5-7B decomposer, given the question and the top retrieved paragraph, reaches 0.637 and captures 31% of that ceiling; decomposing without retrieval reaches 0.533, below the original question. Iterative retrieval systems already produce such decompositions and discard them before verifying.

## Metadata
- **Published**: 2026-08-01T10:52:56Z
- **Authors**: Randhir Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00585v1)