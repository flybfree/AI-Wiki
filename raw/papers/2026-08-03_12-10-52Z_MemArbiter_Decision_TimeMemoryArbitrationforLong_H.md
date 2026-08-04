---
title: MemArbiter: Decision-Time Memory Arbitration for Long-Horizon LLM Agents
published: 2026-08-03T12:10:52Z
authors: Jiajun Dong, Yutao Hu, Fengrui Fan, Shihan Dou, Yueming Wu, Deqing Zou
url: http://arxiv.org/abs/2608.02113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemArbiter: Decision-Time Memory Arbitration for Long-Horizon LLM Agents

## Abstract
Large language model (LLM) agents must retain and use cross-step information to act coherently in long-horizon tasks. Existing methods improve memory accessibility, yet action-relevant information may still fail to guide the current decision because it is poorly formed, organized, prioritized, or presented. We call this post-access failure the Memory-Action Gap. We propose MemArbiter, a function-aware memory arbitration framework that addresses the memory-management-induced component of this gap. MemArbiter decomposes interaction histories into atomic items, organizes them into five functional Memory Banks, and combines bank-level demand, item-level relevance, focal-ambient representations, and a temporal presentation gate to dynamically control memory salience. We evaluate MemArbiter on ALFWorld against Flat Retrieval and Flat Recency under unified per-step memory budgets. With an open-weight action-generation model, MemArbiter achieves success rates of 82.8% and 92.5% under 500- and 750-token budgets, outperforming the strongest baseline by 20.9 and 25.4 percentage points, respectively. It also improves post-failure recovery and reduces failed-action repetition and state-action recurrence. These results show that function-aware memory arbitration enables accessible information to guide actions more effectively.

## Metadata
- **Published**: 2026-08-03T12:10:52Z
- **Authors**: Jiajun Dong, Yutao Hu, Fengrui Fan, Shihan Dou, Yueming Wu, Deqing Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02113v1)