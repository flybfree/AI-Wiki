---
title: Group Entropy-Controlled Policy Optimization
published: 2026-07-18T15:13:33Z
authors: Guangran Cheng, Chengqi Lyu, Songyang Gao, Wenwei Zhang, Kai Chen
url: http://arxiv.org/abs/2607.16850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Group Entropy-Controlled Policy Optimization

## Abstract
Entropy control has become an effective tool in reinforcement learning (RL) of large language models (LLMs), helping balance exploration-exploitation trade-off during alignment process. Such RL paradigm is often conducted on mixtures of heterogeneous tasks, which induce distinct entropy regimes under the same policy, making global or token-level entropy regulation insufficient to corresponding heterogeneous needs of exploration. This heterogeneity further makes GRPO-style normalized advantages induce an entropy-dependent bias, making advantage signals across prompt groups statistically non-comparable. To address this issue, we propose Group Entropy-Controlled Policy Optimization (GEPO), a lightweight extension to GRPO that uses group entropy, estimated from existing grouped samples to perform entropy-conditioned asymmetric advantage shaping. GEPO attenuates positive advantages in low-entropy groups to reduce over-exploitation, and negative advantages in high-entropy groups to preserve exploration, with adaptive thresholds derived from historical entropy statistics. Extensive experiments on two base models across thirteen benchmarks spanning mathematics, physics, science, code generation, and instruction following show that GEPO consistently outperforms GRPO and recent entropy-controlled methods, delivering balanced cross-task improvements while preserving task-specific exploration levels throughout training.

## Metadata
- **Published**: 2026-07-18T15:13:33Z
- **Authors**: Guangran Cheng, Chengqi Lyu, Songyang Gao, Wenwei Zhang, Kai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16850v1)