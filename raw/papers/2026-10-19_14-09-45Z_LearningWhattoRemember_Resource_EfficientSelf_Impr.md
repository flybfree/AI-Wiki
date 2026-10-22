---
title: Learning What to Remember: Resource-Efficient Self-Improvement for Lifelong Agents
published: 2026-10-19T14:09:45Z
authors: Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye
url: http://arxiv.org/abs/2610.26453v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning What to Remember: Resource-Efficient Self-Improvement for Lifelong Agents

## Abstract
Self-improving agents aim to continuously improve their behavior by learning from experience after deployment. However, accumulating and reusing more experience does not necessarily lead to better decisions, particularly when generation, interaction, and memory resources are jointly constrained. Under such stringent constraints, we find that several existing lifelong-memory methods provide limited benefits over simple retrieval or even no-memory agents. This reveals a fundamental challenge for resource-efficient self-improvement: agents must learn not only which past experiences are relevant, but which are actually worth reusing to improve future decisions. When memory capacity and opportunities for reasoning and recovery are limited, retrieving an ineffective experience can consume scarce resources and hinder downstream execution. To address this challenge, we propose TokenWorth, a lightweight feedback-driven memory adaptation framework that learns query-dependent memory worth from sparse execution feedback. Without updating the backbone model, TokenWorth uses the learned worth to guide both experience retrieval and bounded memory management, enabling the agent to continually adapt how it reuses accumulated experience. Across three LifelongAgentBench environments and both local and API-based deployments, TokenWorth achieves the highest task success rate while using the fewest output tokens among the evaluated methods under the specified resource budgets. These results suggest that effective self-improvement under resource constraints depends not on accumulating more experience, but on learning what is worth remembering. Our code is publicly available at https://github.com/AIGNLAI/TokenWorth.

## Metadata
- **Published**: 2026-10-19T14:09:45Z
- **Authors**: Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26453v2)