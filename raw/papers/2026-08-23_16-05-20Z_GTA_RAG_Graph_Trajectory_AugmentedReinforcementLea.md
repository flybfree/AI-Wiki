---
title: GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning
published: 2026-08-23T16:05:20Z
authors: Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, Qin Zhang, Ziyue Qiao, Xiao Luo
url: http://arxiv.org/abs/2608.22479v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning

## Abstract
Retrieval-augmented generation (RAG) enables LLMs to access external knowledge for answering knowledge-intensive questions. For complex multi-hop questions, multi-turn retrieval-augmented reasoning extends RAG into an iterative process that repeatedly searches for and integrates evidence across documents. However, existing reinforcement-learning (RL) approaches for agentic RAG are typically optimized with final-answer rewards, which provide sparse supervision and overlook whether the model actually retrieves the required evidence chain. We present \textsc{GTA-RAG}, a graph-trajectory-augmented RL framework for multi-turn retrieval-augmented reasoning. From an entity--document graph, we sample connected document paths, synthesize multi-hop QA trajectories, and validate them with the deployed retriever to obtain executable trajectory-level supervision. We then optimize the retrieval policy with Group Relative Policy Optimization (GRPO) and a trajectory-guided reward that encourages both accurate answers and acquisition of target evidence documents, followed by answer-reward training on natural QA instances. Experiments on three multi-hop and two simple QA benchmarks show that \method{} consistently outperforms RL-based RAG baselines with both Qwen2.5-3B and Qwen2.5-7B backbones, while substantially improving evidence-chain coverage. Our code is available at https://github.com/cjcj46262/GTA-RAG.

## Metadata
- **Published**: 2026-08-23T16:05:20Z
- **Authors**: Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, Qin Zhang, Ziyue Qiao, Xiao Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22479v1)