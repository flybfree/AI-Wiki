---
title: Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs
published: 2026-07-29T19:31:50Z
authors: Xu Zheng, Chaohao Lin, Zhuomin Chen, Weijieying Ren, Haifeng Chen, Wei Cheng, Dongsheng Luo
url: http://arxiv.org/abs/2607.27415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs

## Abstract
Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs). However, for agents, these approaches suffer from a critical inefficiency, operating in a stateless manner and engaging in redundant search processes. Existing memory mechanisms largely rely on the reasoning capabilities of LLMs, leading to prohibitive computational costs. In this paper, we propose a novel framework, \textit{GAMER}~(Graph-based Action-centric Memory with Episodic Reasoning), that bridges the gap between inference scaling and episodic memory. Our approach models historical reasoning as a dynamic \textit{Action-Centric Graph}. By decoupling the memory mechanism from LLMs, our method can save token/money usage by providing less memory context than memory mechanism baselines. To extract knowledge from the graph effectively, we use a dual-stream Temporal Difference learning mechanism to estimate the positive~(suggestion) and negative~(avoidance) value of action nodes based on past successes and failures. During the inference phase, this learned value function optimizes decision-making bi-directionally, so that positive values provide action suggestions, while negative values indicate high-risk actions. By performing efficient searches on the graph, our method significantly improves the efficiency of inference scaling. Experiments on multiple benchmarks demonstrate that \textit{GAMER} achieves superior performance by \textbf{20.81\%/6.17\%} for success/progress rate compared to vanilla baselines.

## Metadata
- **Published**: 2026-07-29T19:31:50Z
- **Authors**: Xu Zheng, Chaohao Lin, Zhuomin Chen, Weijieying Ren, Haifeng Chen, Wei Cheng, Dongsheng Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27415v1)