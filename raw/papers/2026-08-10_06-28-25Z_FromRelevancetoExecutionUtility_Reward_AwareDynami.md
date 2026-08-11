---
title: From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents
published: 2026-08-10T06:28:25Z
authors: Liang He, Jingbo Wen, Hongyu Gu, Hao Li, Haoyu Wang, Yixiong Chen, Kangning Cui, Xilu Wang
url: http://arxiv.org/abs/2608.09168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents

## Abstract
Agent skills are increasingly used to equip large language model (LLM) agents with reusable procedural knowledge. Although recent work has substantially improved skill retrieval due to the increasing skill libraries, retrieving a plausible skill bundle does not guarantee that executing it is worthwhile. Since every skill-conditioned rollout is computationally expensive, deciding whether a retrieved bundle should be executed has become an increasingly important challenge. To this end, we introduce the Reward-Aware Dynamic Execution Gate (RADEG), a lightweight, retriever-agnostic decision layer between skill retrieval and agent execution. RADEG learns a low-cost surrogate model that predicts the execution utility of a query--bundle pair before the expensive rollout is launched. To obtain informative supervision while controlling for task difficulty, we locally perturb each retrieved bundle by deleting, adding, or replacing one skill, producing matched same-query rollouts that isolate the effect of bundle composition on verifier reward. During deployment, RADEG updates only a warm-started logistic head as new verifier feedback becomes available, enabling inexpensive adaptation of the execute/skip boundary without retraining either the retriever or the agent. Under a query-level held-out evaluation on 288 collected rollouts, RADEG substantially reduces unnecessary agent executions while preserving a large fraction of the downstream verifier reward. It consistently outperforms relevance-based and random gating across different execution budgets, demonstrating that execution-aware surrogate modeling provides a practical and cost-effective complement to skill retrieval.

## Metadata
- **Published**: 2026-08-10T06:28:25Z
- **Authors**: Liang He, Jingbo Wen, Hongyu Gu, Hao Li, Haoyu Wang, Yixiong Chen, Kangning Cui, Xilu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09168v1)