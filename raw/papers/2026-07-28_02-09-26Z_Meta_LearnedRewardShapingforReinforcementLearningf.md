---
title: Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback
published: 2026-07-28T02:09:26Z
authors: Yunpeng Chu
url: http://arxiv.org/abs/2607.26094v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback

## Abstract
Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models. This mismatch leads to sparse learning signals and suboptimal alignment. We introduce MeRLa (Meta-Learned Reward Shaping), a principled framework that meta-learns a task-aware shaping function $Φ(x,y;φ)$ across auxiliary tasks before RLHF training. The learned shaping produces a composite reward that preserves policy optimality while providing task-specific learning signals. Our meta-objective combines task discrimination, entropy regularization, and potential-based conservation for stable convergence. We provide theoretical guarantees for policy invariance, analyze representation drift sensitivity, and formally address incentive misalignment from entropy maximization. Experiments on LLaMA-3-8B across four benchmarks show consistent improvements over PPO, DPO, GRPO, and DAPO, achieving a 90.8% length-controlled win rate on AlpacaEval 2.0 and a score of 9.14 on MT-Bench, with 41% less training instability. MeRLa retains its benefits when combined with process-based and rubric-based enhanced rewards.

## Metadata
- **Published**: 2026-07-28T02:09:26Z
- **Authors**: Yunpeng Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26094v1)