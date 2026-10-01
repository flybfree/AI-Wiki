---
title: MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate
published: 2026-09-30T08:41:08Z
authors: Jiaming Zhang, Yuwan Liu, Yue Huang, Sisi Duan
url: http://arxiv.org/abs/2609.39297v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate

## Abstract
Autonomous agents powered by large language models (LLMs) are rapidly evolving into an open agentic ecosystem. To support trustworthy collaboration, industry initiatives increasingly assess agent reputation from past behavior and provide performance leaderboards. However, reputation derived from past performance may not reliably predict an agent's behavior on new tasks, particularly when malicious agents can adapt their behavior and influence other agents during collaboration.   We study reputation in multi-agent debate (MAD), where multiple agents answer the same query, debate to improve their answers, and aggregate them into a final output. We present MiniRep, a reputation-based aggregation system for MAD under malicious agents. To ground our threat model in established research, we construct an attack taxonomy drawing on reputation-system attacks and software-testing mutation operators, covering strategic exploitation of reputation and subtle corruption of agent proposals. Guided by this taxonomy, MiniRep evaluates agents based on both their behavior on the current task and their reputation over time, while preventing groups of agents with highly similar responses from dominating the final decision. We assess MiniRep across diverse tasks, LLM-agent compositions, corruption placements, and attack types drawn from our taxonomy. Our experimental results show that, MiniRep outperforms both conventional MAD aggregation and conventional reputation-based approaches on MATH no matter being attacked or not. Also, under a heterogeneous 10-agent setting on MATH, MiniRep outperforms all baselines in all 28 attack conditions.

## Metadata
- **Published**: 2026-09-30T08:41:08Z
- **Authors**: Jiaming Zhang, Yuwan Liu, Yue Huang, Sisi Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39297v1)