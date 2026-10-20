---
title: Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents
published: 2026-10-18T11:05:37Z
authors: Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien
url: http://arxiv.org/abs/2610.25179v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents

## Abstract
Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query. We argue that reliable memory requires governance over both state formation and query-time influence. We introduce PLACE, a factorized governance layer that adds write-side state certification and read-side authorization to a memory backend. A factorial evaluation on Mem0 with Qwen2.5-3B and Qwen2.5-7B isolates the contribution of each mechanism. Results show that write-side governance substantially improves lifecycle state correctness, while read-side governance eliminates measured causal leakage from ineligible memory in the state-correct setting. Their combination achieves the strongest joint performance while preserving query-relevant support. These findings show that reliable persistent memory requires explicit control over both maintained state and query-time information influence.

## Metadata
- **Published**: 2026-10-18T11:05:37Z
- **Authors**: Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25179v1)