---
title: Language-Routed RAG and Direct Option Scoring for Multilingual Financial QA: DS@GT at FinMMEval
published: 2026-07-24T18:31:11Z
authors: Justice Ayela, Kabir Sahni
url: http://arxiv.org/abs/2607.22841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language-Routed RAG and Direct Option Scoring for Multilingual Financial QA: DS@GT at FinMMEval

## Abstract
We present DS@GT's submission to FinMMEval 2026 Task 1, a multilingual financial exam question answering benchmark spanning English, Spanish, Greek, Chinese, and Hindi. Financial certification exams such as the CFA, EFPA, and CPA demand structured domain reasoning that standard NLP benchmarks do not capture, and this challenge compounds across languages where retrieval and representation infrastructure is underdeveloped. We build a retrieval-augmented pipeline on LangGraph that detects query language and retrieves semantically relevant exemplars from a 30,209-entry multilingual knowledge base using BGE-M3 embeddings and FAISS indexing. The system then scores answers via Retrieval-Augmented Direct Scoring (RADS), reading next-token log-probabilities over candidate option letters rather than generating free-form output. For low-resource languages, we fuse per-language and cross-lingual retrieval indices using weighted Reciprocal Rank Fusion. Model selection is language-routed: Qwen3-14B for Arabic, Chinese, and Hindi; Qwen2.5-14B for English; and Llama-3.1-8B for Greek, a routing derived from empirical ablations that reveal substantial language-asymmetric performance gaps. Notably, chain-of-thought prompting significantly degrades Greek accuracy (90.7% to 20.9%), and enabling Qwen3's default thinking mode collapses Arabic RADS performance to near-chance levels. Our results indicate that effective multilingual financial reasoning requires language-aware retrieval, model routing, and deliberate scoring strategy selection.

## Metadata
- **Published**: 2026-07-24T18:31:11Z
- **Authors**: Justice Ayela, Kabir Sahni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22841v1)