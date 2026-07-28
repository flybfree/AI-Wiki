---
title: AgentOmnia: Scaling Agentic Models for Full-Scenario Applications
published: 2026-07-25T09:58:24Z
authors: Hao Jiang, Gangtao Xin, Yingdi Huang, Guojie Zhu, Jiangshan Zhang, Xinyuan Lin, Yunkun Xu, Chengyu Shen, Wenlong Fei, Jiawei Li, Yujie Fu, Sichen Kang, Tingyu Xie, Yedi Hu, Jingren Zhang, Hongcheng Gao, Jianshu Zeng, Chong Chen, Chang Guo, Chao Feng, Feng Wang, Fulin Lin, Jinchao Ma, Lang Mei, Li Huang, Liyan Liu, Qing He, Shuting Tao, Siyu Mo, Xiangnan Chen, Xiaohan Yu, Xiaoyang Li, Yanheng Hou, Yanyu Wu, Zhihan Yang, Wentao Zhang, Yang Gao, Zhao Cao
url: http://arxiv.org/abs/2607.23124v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentOmnia: Scaling Agentic Models for Full-Scenario Applications

## Abstract
Large language model agents have advanced rapidly, yet progress remains fragmented across domains, capabilities, task difficulty, and interaction settings. We frame this as full-scenario agentic scaling and present AgentOmnia, a framework coordinating task-space definition, data synthesis, post-training, evaluation, and improvement across To-Consumer (ToC), To-Business (ToB), and To-Employee (ToE) applications. An extensible Domain x Capability x Atomic Difficulty taxonomy aligns these stages and enables fine-grained diagnosis with OmniaBench. AgentOmnia combines bidirectional environment-task synthesis with tool-dependency, program-structured, and solver-based pipelines, constructing 5,018 stateful environments with 255,375 tools and 52,361 tasks. Programs, solvers, and verifiers provide correctness signals, while supervised fine-tuning, online agentic reinforcement learning, and a rollback curriculum support post-training. Evaluation failures translate into Product Requirement Documents (PRDs) for targeted self-evolution. Starting from Qwen3-30B-A3B-Thinking-2507, AgentOmnia raises the pass rate on the OmniaBench challenging subset from 9.16% to 37.11% and the macro-average across OmniaBench, $τ^2$-Bench, DeepPlanning, and VitaBench from 22.86% to 41.69%. Under a unified protocol,it leads the evaluated agentic post-trained baselines on OmniaBench and retains the highest four-benchmark macro-average. It also surpasses Qwen3-235B-A22B-Thinking-2507 on all four benchmarks and exceeds Qwen3.5-35B-A3B on the macro-average. Gains span three application splits, ten capability dimensions, eight atomic-difficulty factors, and 76 of 90 level-1 domains, indicating broad rather than category-specific improvement. A one-round study provides initial evidence for PRD-guided self-evolution, motivating validation at larger scales and in industrial settings.

## Metadata
- **Published**: 2026-07-25T09:58:24Z
- **Authors**: Hao Jiang, Gangtao Xin, Yingdi Huang, Guojie Zhu, Jiangshan Zhang, Xinyuan Lin, Yunkun Xu, Chengyu Shen, Wenlong Fei, Jiawei Li, Yujie Fu, Sichen Kang, Tingyu Xie, Yedi Hu, Jingren Zhang, Hongcheng Gao, Jianshu Zeng, Chong Chen, Chang Guo, Chao Feng, Feng Wang, Fulin Lin, Jinchao Ma, Lang Mei, Li Huang, Liyan Liu, Qing He, Shuting Tao, Siyu Mo, Xiangnan Chen, Xiaohan Yu, Xiaoyang Li, Yanheng Hou, Yanyu Wu, Zhihan Yang, Wentao Zhang, Yang Gao, Zhao Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23124v1)