---
title: Exploring Collaboration between a language and a non-language agent
published: 2026-08-31T23:25:10Z
authors: Harini S, Somesh Singh, Yaman K Singla, Rajiv Ratn Shah, David Doermann, Balaji Krishnamurthy
url: http://arxiv.org/abs/2609.00474v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring Collaboration between a language and a non-language agent

## Abstract
LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not language models. Integrating non-language agents with LLMs would require \emph{verbalization}: compressing their rich continuous representations into sparse textual summaries at each interaction step. To study whether verbalization constitutes a bottleneck, we introduce \textsc{LLAMIA-Bench}, a suite of six diverse collaborative chess tasks spanning three facets: behavioral imitation, state assessment, and natural-language explanation. Each task instantiates a well-established chess problem that neither the LLM nor the chess engine can solve alone. To solve LLM collaboration with non-language agents, we introduce \emph{latent state internalization}, which projects the subagent's continuous representations directly into the LLM's token stream as learned state tokens, with dynamic re-encoding as actions advance the environment state. Comparing internalization to verbalized integration, our experiments reveal a consistent \emph{verbalization debt}: the performance gap widens throughout training and persists as the LLM scales from 4B to 14B parameters. A single 14B model, \textsc{LLAMIA}, trained with latent state internalization, matches or exceeds task specialists and frontier models including GPT-5.1 with tool access across all benchmark tasks, and generalizes out-of-distribution where task-specific finetunes collapse

## Metadata
- **Published**: 2026-08-31T23:25:10Z
- **Authors**: Harini S, Somesh Singh, Yaman K Singla, Rajiv Ratn Shah, David Doermann, Balaji Krishnamurthy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00474v1)