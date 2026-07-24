---
title: REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning
published: 2026-07-21T13:36:23Z
authors: Yunjie Chen, Xiaoxin Chen, Fang Wang
url: http://arxiv.org/abs/2607.19450v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning

## Abstract
Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs). However, continuing to scale it across vast task domains of interest remains challenging in both computational infrastructure and cost, especially when considering RL as merely a one-off learning stage. Recently, a widely used technique for distilling knowledge across various domains and training stages, multi-teacher on-policy distillation (MOPD), helps to decouple the RL stage, saving costs, while maintaining generality across vast domains. Nonetheless, similar to online RL, MOPD requires coupled inference and backward passes, which continues to limit its scalability and computational efficiency. To address these challenges, we propose REGEN: Replay-recycling for Expert-to-Generalist Distillation with Offline RL. Instead of distilling from multiple teacher models, REGEN trains a generalist by simply recycling the replay memory -- the free by-product of the teachers' specialized RL training -- and employing offline RL algorithms. REGEN completely decouples the rollout sampling from the backward training process and thus greatly reduces the training cost. Across mathematical reasoning, code generation, and instruction following, REGEN matches the accuracy of MOPD at substantially lower cost. It potentially turns online RL into a data synthesis process instead of a one-off learning stage, and can potentially be extended to large-scale post-training without requiring heavy computational load.

## Metadata
- **Published**: 2026-07-21T13:36:23Z
- **Authors**: Yunjie Chen, Xiaoxin Chen, Fang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19450v1)