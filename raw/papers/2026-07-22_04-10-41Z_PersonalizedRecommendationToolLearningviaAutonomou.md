---
title: Personalized Recommendation Tool Learning via Autonomous Language Agents
published: 2026-07-22T04:10:41Z
authors: Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu
url: http://arxiv.org/abs/2607.19739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personalized Recommendation Tool Learning via Autonomous Language Agents

## Abstract
Although large language models (LLMs) have recently gained traction in recommender systems due to their strong reasoning capabilities and extensive world knowledge, previous LLM-based agents suffer from hallucination and context-length limitations, and thus are not suitable for full-ranking recommendation tasks. To circumvent these limitations through architectural design rather than modifying the LLM itself, we propose an agent-based recommendation framework, memory-based $\textbf{P}$ersonalized $\textbf{R}$ecommendation $\textbf{T}$ool learning via autonomous language $\textbf{A}$gents (PRTA), in which an LLM acts as a central planner interacting with multiple recommendation models as tools. The LLM-based agent is responsible for high-level reasoning and personalized tool selection, while traditional recommendation models perform full-ranking scoring, leveraging their scalability in modeling behavioral patterns. To support personalized tool selection, we design reflection mechanisms that enable the agent to evaluate and compare tools for each user based on user profiles and candidate ranked lists. Extensive experiments across three public datasets demonstrate the superiority of \modelname over traditional recommendation and LLM-based baselines in improving full-ranking recommendation performance.

## Metadata
- **Published**: 2026-07-22T04:10:41Z
- **Authors**: Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19739v1)