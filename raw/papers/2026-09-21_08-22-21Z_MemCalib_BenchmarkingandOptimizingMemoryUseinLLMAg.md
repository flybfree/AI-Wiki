---
title: MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents
published: 2026-09-21T08:22:21Z
authors: Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Yifei Zhao, Han Zhang, Li Xiao
url: http://arxiv.org/abs/2609.24259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents

## Abstract
The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory appropriately. They frequently over-use or under-use memory rather than matching each proposition's actual use to its target level, leading to biased, low-quality responses. Experiments with common post-training algorithms, including group relative policy optimization and on-policy self-distillation, further reveal a clear directional skew: trained models improve in one direction while deteriorating in the other. We therefore propose MemCalib-RL, an ordered bidirectional counterfactual credit-assignment algorithm that separates over- and under-use signals and localizes their credit to response tokens through exact atom ablation. Results across model families and scales (Qwen3-8B, Ministral-3-8B-Instruct, and Qwen3.5-35B-A3B) show that MemCalib-RL achieves the best overall performance while better balancing over-use and under-use, with gains generalizing beyond MemCalib in external benchmark evaluation. Further experiments support its design choices and robustness and provide insight into its training dynamics.

## Metadata
- **Published**: 2026-09-21T08:22:21Z
- **Authors**: Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Yifei Zhao, Han Zhang, Li Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24259v1)