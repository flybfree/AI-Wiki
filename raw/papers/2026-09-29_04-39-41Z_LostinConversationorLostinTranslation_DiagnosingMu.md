---
title: Lost in Conversation or Lost in Translation? Diagnosing Multi-Turn Degradation in RAG
published: 2026-09-29T04:39:41Z
authors: Pranav Handa, Ariful Azad
url: http://arxiv.org/abs/2609.36700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lost in Conversation or Lost in Translation? Diagnosing Multi-Turn Degradation in RAG

## Abstract
When conversing with large language models (LLMs), users often begin with a simple question and build towards a multi-hop question through follow-up turns. Retrieval-augmented generation (RAG) and its graph-based variant (GraphRAG) have become the dominant approaches for grounding LLM responses in external evidence, yet both are evaluated almost exclusively on single-turn, fully specified queries. We systematically investigate this evaluation mismatch through a large-scale simulation study. Building on prior work on multi-turn LLM evaluation, we transform questions from multi-hop question answering (QA) benchmarks into underspecified conversations and evaluate ten LLM assistants with eight retrieval systems across 1.5 million simulated conversations. Our findings reveal that multi-turn interaction causes widespread performance degradation, incurring relative performance drops of up to 21% and increasing unreliability by 47%, making RAG systems simultaneously less accurate and less reliable. We identify two distinct failure modes behind this degradation. Systems are either lost in translation, where conversational rephrasing distorts the retrieval query, or lost in conversation, where retrieval succeeds but the LLM fails to synthesize evidence distributed across turns.

## Metadata
- **Published**: 2026-09-29T04:39:41Z
- **Authors**: Pranav Handa, Ariful Azad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36700v1)