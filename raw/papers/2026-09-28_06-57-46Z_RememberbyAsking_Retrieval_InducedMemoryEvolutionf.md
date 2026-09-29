---
title: Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents
published: 2026-09-28T06:57:46Z
authors: Wanqi Zhou, Jiawei Lu, Yang Wang, Zhaolong Xing, Zhen Chen, Ai Han, Haoyue Shi
url: http://arxiv.org/abs/2609.34438v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents

## Abstract
Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions. Existing memory systems mainly use retrieval at read time, while write-time memory formation still relies on direct extraction or compression. However, when future information needs are unknown, compressing an entire interaction in one pass can overlook locally important details that may matter later. To this end, we introduce RIME, a retrieval-induced memory framework that shifts memory construction from monolithic compression toward evidence-centered integration. RIME uses generic self-questions to retrieve focused dialogue evidence and grounds memory formation in both the retrieved evidence and relevant historical memories, which are jointly reconciled into an evolving memory bank with temporal and provenance information. At inference time, compressed memory serves as the primary rather than the sole source of evidence: when it cannot support an answer, RIME retrieves relevant source dialogue together with its local context to recover information omitted during memory formation, without resorting to full-history processing. Extensive experiments on LoCoMo with Qwen3-235B-A22B and GPT-5.6 Sol show that RIME consistently achieves the best performance across all three quality metrics among the compared methods, while requiring substantially fewer query-time LLM tokens.

## Metadata
- **Published**: 2026-09-28T06:57:46Z
- **Authors**: Wanqi Zhou, Jiawei Lu, Yang Wang, Zhaolong Xing, Zhen Chen, Ai Han, Haoyue Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34438v1)