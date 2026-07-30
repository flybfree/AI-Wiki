---
title: CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG
url: http://arxiv.org/abs/2607.26470v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_04-50-41Z_CMT_RAG_ComplementaryMemoryTracesforMulti_turnMult.md
generated_at: 2026-07-29 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper CMT-RAG addresses the challenge of multi-turn multi-hop retrieval-augmented generation by aligning conversational memory with query structure. It proposes a state-space trace generator that creates sub‑question level traces, grounding them with evidence and storing them in a session DAG. Experiments show it outperforms five RAG baselines on both MuMu-QA and corpus benchmarks.

## Key Takeaways
- CMT-RAG uses a recurrent state as runtime memory to capture recent dialogue context and decompose queries into structured trace drafts containing retrieval‑oriented sub‑questions.
- The framework grounds each draft with retrieved evidence, creating persistent memory traces stored in a session‑level directed acyclic graph for later recovery.
- On MuMu-QA and broader RAG benchmarks CMT-RAG achieves higher answer accuracy than baselines that rely on raw dialogue history or unstructured summaries.

## Context
Current RAG systems struggle to maintain coherent reasoning across conversation turns because they treat memory as flat text. This limits their ability to retrieve specific prior sub‑questions and evidence, leading to fragmented answers in complex queries.

## Implications
For developers building conversational agents, CMT-RAG offers a principled way to encode multi‑turn reasoning into retrievable structures, improving accuracy without heavy compute overhead. Practitioners can adopt the trace‑based memory design to create more reliable chatbots that understand and answer multi‑hop questions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26470v1)
