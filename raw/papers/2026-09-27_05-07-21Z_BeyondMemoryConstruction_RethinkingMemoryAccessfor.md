---
title: Beyond Memory Construction: Rethinking Memory Access for LLM-based Conversational Agents
published: 2026-09-27T05:07:21Z
authors: Donghua Cai, Yongheng Deng, Yifei Wang, Zijun Shen, Ju Ren
url: http://arxiv.org/abs/2609.33226v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Memory Construction: Rethinking Memory Access for LLM-based Conversational Agents

## Abstract
Memory is a core component of conversational agents, enabling coherent and context-aware behavior over long interactions. Recent approaches commonly rely on LLM-based memory construction, where raw interactions are rewritten into structured memory units and later retrieved via a RAG pipeline. While effective in controlled settings, we show that this paradigm breaks down in long-horizon, high-entropy conversations: memory construction becomes increasingly lossy and unstable as context length and information complexity grow, and incurs prohibitive cost due to repeated LLM invocation. To address these limitations, we propose Threader, a memory system that shifts the focus from memory construction to efficient, structure-aware access over raw interactions. Instead of rewriting interactions, Threader preserves them as first-class memory, organizes them into topic-coherent segments via lightweight incremental segmentation, and enables accurate retrieval through multi-view representation. At query time, it performs multi-signal retrieval that combines segment-level access with localized evidence matching, ensuring both completeness and coherence. Extensive experiments demonstrate that Threader consistently improves answer accuracy and evidence recall, while significantly reducing the memory construction overhead.

## Metadata
- **Published**: 2026-09-27T05:07:21Z
- **Authors**: Donghua Cai, Yongheng Deng, Yifei Wang, Zijun Shen, Ju Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33226v1)