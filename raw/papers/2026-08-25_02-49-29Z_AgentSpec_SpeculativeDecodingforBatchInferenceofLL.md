---
title: AgentSpec: Speculative Decoding for Batch Inference of LLM Agents
published: 2026-08-25T02:49:29Z
authors: Xin Wang, Ziming Miao, Yi Zhu, Hui Shen, Zhongwei Wan, Fan Yang, Mi Zhang
url: http://arxiv.org/abs/2608.24004v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentSpec: Speculative Decoding for Batch Inference of LLM Agents

## Abstract
Large language model (LLM)-based agent applications often incur high response time. Speculative decoding is a promising solution to improve the inference efficiency of LLM agents without impacting generation quality. However, state-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes, limiting their effectiveness to deploy in real-world agent applications. In this work, we first present a systematic analysis of speculative decoding for LLM agents and identify two dominant factors of speedup degradation: high rejection rate of speculative tokens, and under-utilization of dynamic token budgets.B ased on these observations, we propose AgentSpec, a speculative decoding algorithm that addresses the limitations of existing methods for LLM agents. AgentSpec incorporates structure-isolated drafting that constrains speculation to semantically coherent segments of the agent workflow, reducing the drafts of irrelevant semantic paths and achieving an extremely low rejection rate. Moreover, AgentSpec adopts redundancy-aware budget allocation that exploits agent-level information to better utilize the dynamically-free token budget during the agent inference. We implement and evaluate AgentSpec on five different workloads and four different models from four different LLM families in vLLM. Our results demonstrate the superiority of AgentSpec over state-of-the-arts.

## Metadata
- **Published**: 2026-08-25T02:49:29Z
- **Authors**: Xin Wang, Ziming Miao, Yi Zhu, Hui Shen, Zhongwei Wan, Fan Yang, Mi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24004v1)