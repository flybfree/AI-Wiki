---
title: AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing
published: 2026-08-30T07:31:19Z
authors: Xinke Jiang, Yue Fang, Zhibang Yang, Jiaran Gao, Zhixin Zhang, Tao Feng, Rihong Qiu, Wentao Zhang, Hongxin Ding, Ruizhe Zhang, Yongxin Xu, Yuheng Huang, Xu Chu, Junfeng Zhao, Yasha Wang
url: http://arxiv.org/abs/2608.29622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing

## Abstract
Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learning (RL)-based agentic RAG methods partially alleviate this issue, but typically rely on coarse-grained action spaces and trajectory-level rewards, resulting in weak reward assignment and a bias toward short-horizon, stereotyped reasoning template. To address, we propose AgenticRag-R1, a RL framework that deeply integrates reasoning, retrieval, and memory via a memory stack and fine-grained action space, supported by hierarchical action-aware rewards and an information-aware trajectory rejection strategy to enable effective long-horizon learning. Experiments across a diverse set of multi-hop, open-domain, and agentic reasoning benchmarks, spanning multiple backbone model sizes, demonstrate that AgenticRag-R1 consistently outperforms strong baselines. Moreover, AgenticRag-R1 learns more robust, interpretable, and memory-aware reasoning behaviors, highlighting the effect of fine-grained action modeling and information-aware optimization for long-horizon reasoning. Our code is anonymous available at https://github.com/jiangxinke/Harness-RL/tree/AgenticRAG-R1-Whitebox.

## Metadata
- **Published**: 2026-08-30T07:31:19Z
- **Authors**: Xinke Jiang, Yue Fang, Zhibang Yang, Jiaran Gao, Zhixin Zhang, Tao Feng, Rihong Qiu, Wentao Zhang, Hongxin Ding, Ruizhe Zhang, Yongxin Xu, Yuheng Huang, Xu Chu, Junfeng Zhao, Yasha Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29622v1)