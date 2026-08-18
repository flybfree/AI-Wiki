---
title: QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents
published: 2026-08-17T06:34:24Z
authors: Heng Wang, Yifei Li, Lingling Zhang, Pengyu Li, Xinyu Che, Xinyu Zhang, Zesheng Yang
url: http://arxiv.org/abs/2608.16168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents

## Abstract
Large language model (LLM) agents increasingly use external memory systems to support personalization by drawing on long and evolving interaction histories, in which user preferences may be distributed across time, change with context, and conflict with earlier evidence. However, existing systems face three limitations: fixed-turn, fixed-token, or session-based boundaries can mix unrelated dialogue or split an event from its causes, decisions, and outcomes; storing multiple pieces of user information from the same interaction as a single memory binds together items that serve different functions and should be independently retrievable; and treating the current task as a single top-$k$ retrieval query can return fragments that are individually relevant but fail to jointly capture preference evolution, temporal validity, and contextual applicability. We introduce \textsc{QUMem}, a structured memory framework for query-conditioned user-state inference. \textsc{QUMem} first segments interaction histories into variable-length episodes according to semantic continuity, then decomposes each episode into independently retrievable factual, preference, and transferable insight memories while preserving temporal positions and source evidence. At inference time, three sequential agents identify task-specific information needs, plan multi-query retrieval over the typed memory stores, and jointly infer a temporally and contextually valid user state for downstream response generation. \textsc{QUMem} achieves state-of-the-art performance on both PersonaMem and KnowU-Bench, demonstrating the effectiveness of query-conditioned user-state inference for long-term personalization.

## Metadata
- **Published**: 2026-08-17T06:34:24Z
- **Authors**: Heng Wang, Yifei Li, Lingling Zhang, Pengyu Li, Xinyu Che, Xinyu Zhang, Zesheng Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16168v1)