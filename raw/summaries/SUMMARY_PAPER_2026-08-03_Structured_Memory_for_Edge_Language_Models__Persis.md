---
title: Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection
url: http://arxiv.org/abs/2608.02560v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-43-36Z_StructuredMemoryforEdgeLanguageModels_PersistentCo.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PRECOG, a retrieval‑augmented generation framework that eliminates the costly prefill step for state‑space models (SSMs). By pre‑encoding document corpora as fixed‑size hidden states and injecting them at query time, the model achieves O(1) context access. The authors also present SMC, a hierarchical persistent memory that consolidates short‑term episodic states into long‑term semantic memory with O(1) session initialization.

## Key Takeaways
- PRECOG reduces prefill latency from ~27 seconds to under 6 ms on edge hardware, delivering a ~4500× speedup while matching in‑context RAG answer quality.  
- The mechanism leverages the position‑agnostic nature of SSM hidden states, which are O(1) per query and do not depend on context length.  
- SMC provides a persistent memory with adjustable fidelity versus storage, enabling efficient consolidation of episodic information into long‑term knowledge.

## Context
State‑space models have been promoted as alternatives to Transformers because their recurrent hidden states are compact and independent of sequence position. However, RAG systems still suffer from the linear prefill cost that limits interactive use on resource‑constrained devices. This work shows how SSMs can bypass both prefill and KV‑cache growth, opening a path toward truly low‑latency language generation.

## Implications
For developers building edge AI applications, PRECOG enables real‑time responses without heavy context loading, improving user experience dramatically. The approach also suggests new architectures for persistent memory that could be integrated into large language models, potentially reshaping how knowledge is stored and retrieved in deployed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02560v1)
