---
title: Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards
published: 2026-09-03T04:00:28Z
authors: Leqi Zheng, Jinbo Su, Fang Niu, Chaokun Wang, Weiping Wang, Jiajun Zhang, Shannan Yan, Jie Wu, Zhaolu Kang, Rong Fu, Hang Zhang
url: http://arxiv.org/abs/2609.03342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards

## Abstract
Reinforcement learning from verifiable rewards (RLVR) drives chain-of-thought reasoning in large language models, yet its binary outcome reward cannot distinguish among correct trajectories. Existing dense reward alternatives, from surface heuristics to process reward models, either ignore the expert solutions already present in training corpora or require expensive offline annotation. We propose Gradient-Aligned Reward (GAR), which operates in the policy's own gradient space: truncated backpropagation through the output projection layer extracts a compact gradient vector for each rollout, and cosine similarity with an expert-anchor gradient yields a dense, reasoning-aware reward with less than 9% wall-clock overhead. We prove that this cosine admits a multiplicative decomposition into prediction-error and activation-pattern factors, providing a concrete characterization of what the alignment signal measures. On Qwen3-4B and Qwen3-8B, GAR consistently improves over GRPO and other baselines on competition-level math benchmarks and transfers to GPQA Diamond and MMLU-Pro without domain-specific data. Code and data are available at https://github.com/LQgdwind/GAR.

## Metadata
- **Published**: 2026-09-03T04:00:28Z
- **Authors**: Leqi Zheng, Jinbo Su, Fang Niu, Chaokun Wang, Weiping Wang, Jiajun Zhang, Shannan Yan, Jie Wu, Zhaolu Kang, Rong Fu, Hang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03342v1)