---
title: KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents
published: 2026-09-03T09:35:14Z
authors: Yaxing Lyu, Shengjie Zhou, Binbin Toh, Pengyu Zhu, Lijun Li
url: http://arxiv.org/abs/2609.03588v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents

## Abstract
As LLMs increasingly act through tools, they must reconcile user instructions, parametric knowledge, and dynamic environmental observations before taking actions. We introduce KC-Bench, a controlled multi-turn benchmark for measuring this capability across world-knowledge conflicts, input inconsistencies, and multi-source temporal conflicts. Its 238 tasks are manually screened from more than 1,000 generated candidates and combine a user simulator, stateful tools, deterministic environment assertions, an open-source natural-language evaluator, and human trajectory verification. Evaluation of nine models, including DeepSeek-V4-Flash, GLM-5.2, and MiniMax-M3, shows substantial cross-domain variation: no model handles factual correction, identity consistency checking, and temporal conflict resolution reliably across all settings. In the simulated environments, missed conflicts can propagate to tool calls or synthetic protected-data flows. KC-Bench isolates this model-level behavior rather than ranking complete agent frameworks, and provides a reproducible diagnostic for developing conflict-aware reasoning and execution safeguards.

## Metadata
- **Published**: 2026-09-03T09:35:14Z
- **Authors**: Yaxing Lyu, Shengjie Zhou, Binbin Toh, Pengyu Zhu, Lijun Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03588v1)