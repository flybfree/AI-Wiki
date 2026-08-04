---
title: Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents
published: 2026-08-02T14:49:24Z
authors: Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li
url: http://arxiv.org/abs/2608.01285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents

## Abstract
The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions. Existing memory systems either compress and structure histories for efficient access or perform deep research over broader trajectories. The former lowers online cost but may omit temporal, causal, or cross-step dependencies, while the latter improves evidence coverage at substantial latency and inference cost. This raises a key question: can a memory system achieve strong answer quality while maintaining low online latency? We introduce Router-Mem, an evidence-conditioned progressive execution framework for long-horizon agent memory. Router-Mem first applies a shared low-cost retrieval prefix to obtain evidence. A lightweight sufficiency router then predicts whether the context supports early termination, which enable a single-token decision at inference time. It is trained with evidence-level supervision and rationale-conditioned representation distillation. When evidence is insufficient, Router-Mem reuses retrieval hits to expand memory blocks and perform deeper analysis and aggregation. Experiments on AMA-Bench and BEAM show that Router-Mem achieves 55.17\% and 38.77\% score while reducing average inference time by 27.3\% and 25.5\% compared with full memory execution.

## Metadata
- **Published**: 2026-08-02T14:49:24Z
- **Authors**: Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01285v1)