---
title: Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences
published: 2026-10-21T22:08:49Z
authors: Jialin Li, Zhenhao Chen, Hanjun Luo, Hanan Salam
url: http://arxiv.org/abs/2610.30485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences

## Abstract
Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden. Reducing this burden requires agents to remember how users want to be assisted. However, existing memory benchmarks focus on factual recall and personalized answers and rarely test how agents learn and act on interaction preferences. We introduce MemPABench, an interactive environment for on-policy evaluation of memory in personal agents. MemPABench poses long-horizon tasks requiring agents to decide when to clarify, confirm, or act autonomously. Four grounded simulated users hold 14 preferences across work and personal contexts. Their feedback spans 99 sessions over four months, with five event-driven changes per user testing memory updates. We evaluate preference selection, delivered behavior, and sensitivity to context and preference change. Evaluating four memory systems across four LLM backbones, we find that current memory brings limited gains in preference selection. Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts. Our analysis shows that current memory struggles to retrieve interaction preferences and adapt to preference changes. Even with the correct preference available, overriding the agent's default interaction habits remains challenging. The environment and dataset are available at https://mempabench.com.

## Metadata
- **Published**: 2026-10-21T22:08:49Z
- **Authors**: Jialin Li, Zhenhao Chen, Hanjun Luo, Hanan Salam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30485v1)