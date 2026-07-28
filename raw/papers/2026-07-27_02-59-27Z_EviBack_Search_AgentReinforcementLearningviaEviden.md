---
title: EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff
published: 2026-07-27T02:59:27Z
authors: Xiao Ma, Zhiquan Hu, Yi Wei, Chenchen Zhao, Yijun Chen, Jicheng Zhao, Yuming Li Chuang Dai
url: http://arxiv.org/abs/2607.23955v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff

## Abstract
Reinforcement learning enables Agentic RAG systems to learn multi-turn search from verifiable outcome rewards, but all- zero rollout groups provide no comparative signal and may hide useful search behavior. We present EviBack, an evidence- constrained Teacher backoff that supplies auxiliary super- vision to such groups while preserving verifiable Actor re- wards. It separates evidence assessment from answer refine- ment, preventing reference answers from overriding evidence- insufficiency judgments. A fully automated, end-to-end GPT- 5.5-assisted APE pipeline starts from a manually authored single-prompt dual-task Teacher, automatically partitions and labels rollout data, and performs ablation, task decomposition, evaluation, and selection to produce a gated two-stage Teacher. Compared with the manual design, the resulting Teacher im- proves downstream F1 and valid-answer rate while reduc- ing search, duplicate queries, and forced termination. Across seven open-domain QA benchmarks and three Qwen3 scales, EviBack improves F1 over Search-R1 and raises both single- and multi-hop macro F1. We guarantee that the code will be made publicly available at a later stage.

## Metadata
- **Published**: 2026-07-27T02:59:27Z
- **Authors**: Xiao Ma, Zhiquan Hu, Yi Wei, Chenchen Zhao, Yijun Chen, Jicheng Zhao, Yuming Li Chuang Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23955v1)