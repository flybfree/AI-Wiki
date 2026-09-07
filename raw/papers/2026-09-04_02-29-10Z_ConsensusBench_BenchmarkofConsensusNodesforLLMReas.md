---
title: ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying
published: 2026-09-04T02:29:10Z
authors: Shi-Qi Yan, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Zhen-Hua Ling
url: http://arxiv.org/abs/2609.04648v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying

## Abstract
Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Relative Policy Optimization (GRPO) and related algorithms have demonstrated strong performance with outcome-level rewards. However, these methods depend solely on the final answer, without feedback regarding which intermediate steps contribute to success or failure. As task complexity and reasoning trajectory length increase, such sparse final-answer rewards become increasingly insufficient. To address this limitation, we introduce ConsensusBench, a novel dataset designed to provide rule-based process-level signals. We posit that a correct final answer relies on a small set of intermediate conclusions throughout the reasoning process, which can be seen as a verifiable sub-outcome. We identify these sub-outcomes by filtering correct trajectories from N rollouts and clustering semantically equivalent intermediate statements. We call these clustered statements as Consensus Nodes. By integrating a rule-based process reward derived from these nodes into GRPO-style algorithms, we develop a new reinforcement learning signal named ConsensusPR. It directly reduces the reward sparsity of outcome reward across long reasoning trajectories. To facilitate systematic process-level evaluation, we introduce three metrics to our benchmark: Final Answer Accuracy (Acc), Node Coverage Rate (NCR), and Tokens per Node (TPN). Experiments across AIME 2024, AIME 2025, GSM8K, MATH-500, and our ConsensusBench demonstrate that the proposed method consistently surpasses GRPO-style approaches, highlighting the practical value of consensus nodes in guiding reasoning.

## Metadata
- **Published**: 2026-09-04T02:29:10Z
- **Authors**: Shi-Qi Yan, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Zhen-Hua Ling
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04648v1)