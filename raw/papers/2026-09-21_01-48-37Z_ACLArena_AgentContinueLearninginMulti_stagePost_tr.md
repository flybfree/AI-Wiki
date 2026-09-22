---
title: ACLArena: Agent Continue Learning in Multi-stage Post-training
published: 2026-09-21T01:48:37Z
authors: Haixin Wang, Xiaoxuan Wang, Junkai Zhang, Han Zhang, Renliang Sun, Alexander K Taylor, Yidan Shi, Haoran Deng, Chenguang Wang, Jason Cong, Yizhou Sun, Wei Wang
url: http://arxiv.org/abs/2609.23989v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACLArena: Agent Continue Learning in Multi-stage Post-training

## Abstract
Building general-purpose agents for industrial deployment requires integrating multiple capabilities, each typically acquired at a distinct stage of training. Yet there is currently no well-established recipe for Agent Continual Learning (ACL), with little understanding of the trade-offs among existing integration paradigms. To address this gap, we introduce ACLArena, a framework for comprehensively studying, analyzing, and evaluating ACL. We first build a sequential training pipeline and conduct an in-depth analysis that explains the mechanisms of forgetting and generalization from two complementary perspectives, the model level and the token level. Guided by these analyses, we systematically compare multi-teacher on-policy distillation, self-distilled fine-tuning, and model merging to assess their ability to recover previously learned capabilities while preserving newly acquired ones. Through extensive experiments, we develop a detailed understanding of how capabilities transfer across stages. Finally, we propose a new ACL recipe that combines offline replay over high-quality trajectories with a routed network of multiple LoRA experts each specialized via RL, substantially improving the agent's ability to learn across multiple domains. Comprehensive experiments on four reasoning and agentic tasks, evaluated under both in-domain and out-of-domain settings, demonstrate the value of our analysis and the effectiveness of our approach.

## Metadata
- **Published**: 2026-09-21T01:48:37Z
- **Authors**: Haixin Wang, Xiaoxuan Wang, Junkai Zhang, Han Zhang, Renliang Sun, Alexander K Taylor, Yidan Shi, Haoran Deng, Chenguang Wang, Jason Cong, Yizhou Sun, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23989v1)