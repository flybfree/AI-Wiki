---
title: CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG
published: 2026-07-29T04:50:41Z
authors: Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao
url: http://arxiv.org/abs/2607.26470v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG

## Abstract
Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns. However, existing RAG systems typically represent conversational memory as raw dialogue history, rewritten queries, or unstructured summaries, making it difficult to recover the specific prior reasoning steps and evidence required for follow-up queries. Our key insight is to align conversational memory with retrieval by representing dialogue context as sub-question-level reasoning traces. Building on this insight, we introduce MuMu-QA, a benchmark for multi-turn multi-hop RAG with explicit cross-turn sub-question dependency annotations, and CMT-RAG, a complementary memory framework for this setting. At each turn, CMT-RAG employs a state-space trace generator, whose recurrent state serves as runtime memory, to incorporate recent conversational context and decompose the current query into structured trace drafts containing retrieval-oriented sub-questions and dependencies on earlier traces. It then grounds these drafts with retrieved evidence and stores them as persistent memory traces in a session-level DAG, enabling future turns to efficiently recover relevant prior reasoning and evidence. Experiments on MuMu-QA and corpus-level RAG benchmarks show that CMT-RAG consistently outperforms five categories of RAG baselines in answer accuracy.

## Metadata
- **Published**: 2026-07-29T04:50:41Z
- **Authors**: Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26470v1)