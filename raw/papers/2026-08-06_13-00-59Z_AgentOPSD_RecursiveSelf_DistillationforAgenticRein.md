---
title: AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
published: 2026-08-06T13:00:59Z
authors: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
url: http://arxiv.org/abs/2608.05987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

## Abstract
Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in agentic reinforcement learning. AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space. This yields a principled reweighting scheme that converts sparse outcome supervision into turn-level credit signals and identifies pivotal turns through the marginal belief revision between consecutive states. The method is fully compatible with standard policy optimization and requires neither an additional critic nor extra rollouts. We evaluate AgentOPSD on ALFWorld, WebShop, and Search-QA using Qwen2.5 models at two scales (3B and 7B). AgentOPSD outperforms GRPO and strong self-distillation baselines, achieving 89.1% success on ALFWorld with Qwen2.5-7B. Ablation studies attribute the gains to turn-level aggregation and history-dependent recursive belief updates.

## Metadata
- **Published**: 2026-08-06T13:00:59Z
- **Authors**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05987v1)