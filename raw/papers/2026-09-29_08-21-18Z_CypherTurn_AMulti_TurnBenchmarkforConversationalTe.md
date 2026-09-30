---
title: CypherTurn: A Multi-Turn Benchmark for Conversational Text-to-Cypher Evaluation and the Autonomy Divergence
published: 2026-09-29T08:21:18Z
authors: Yuzhe Zhang, Weijie Zhu, Haolin Yang, Ziyun Zhang, Xianwei Xue, Mengke Chen, Qiutong Pan, Huaqian Cai
url: http://arxiv.org/abs/2609.36987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CypherTurn: A Multi-Turn Benchmark for Conversational Text-to-Cypher Evaluation and the Autonomy Divergence

## Abstract
Graph databases are increasingly queried through natural language, yet every existing benchmark evaluates isolated single-turn queries rather than the multi-turn sessions through which analysts actually work. We introduce CypherTurn, the first benchmark for conversational Text-to-Cypher evaluation, comprising 721 sessions and 5,927 turns across 7 knowledge graphs and 13 conversational phenomena. We evaluate 15 models under a guided oracle protocol and a fully autonomous agentic protocol, yielding four findings. First, the best model reaches only 64.7% execution accuracy, and session-level correctness remains below 5%. Second, despite strong overall rank correlation, frontier models exhibit a consequential reordering of the top of the leaderboard under autonomous operation, a phenomenon we term the Autonomy Divergence, which reveals error-management as a partially independent capability from raw generation skill. Third, scaling action budgets from x3 to x10 fails to close the autonomy gap, as the strongest frontier models self-limit to approximately two actions per turn regardless of available budget. Fourth, single-turn Cypher fine-tuning degrades multi-turn instruction following, while architecture-appropriate specialization outperforms several frontier models. These results establish CypherTurn as an open challenge for conversational graph database reasoning. Code and data are available at https://github.com/BarryQ/CypherTurn.

## Metadata
- **Published**: 2026-09-29T08:21:18Z
- **Authors**: Yuzhe Zhang, Weijie Zhu, Haolin Yang, Ziyun Zhang, Xianwei Xue, Mengke Chen, Qiutong Pan, Huaqian Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36987v1)