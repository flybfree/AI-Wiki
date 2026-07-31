---
title: MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory
published: 2026-07-30T08:15:02Z
authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
url: http://arxiv.org/abs/2607.27834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory

## Abstract
Persistent memory lets long-running large language model agents reuse information across sessions and tasks. Yet errors in writable memory can persist and corrupt future behavior. Existing systems improve storage and retrieval, but they do not provide a transaction boundary for reliable updates and recovery. We therefore propose MemTxn, a governance layer outside the answer model. MemTxn verifies whether an update is supported by its source. It also selects the visible version when facts conflict and restores the application-visible state after a fault. The system uses Ordered PatchTest to validate writes, a Temporal Resolver to select versions, and a durable snapshot journal to recover state. On an item-disjoint audit, MemTxn accepts all 60 supported originals and rejects all 179 hard negatives. Under persistent multi-key faults on LongMemEval-S and LoCoMo states, it restores the complete declared active map without knowing the actual physical write set. On MemoryAgentBench FactConsolidation, MemTxn achieves the highest average F1 across all twelve answer-model configurations. It outperforms Dense by 17.06--24.07 points in five representative settings.

## Metadata
- **Published**: 2026-07-30T08:15:02Z
- **Authors**: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27834v1)