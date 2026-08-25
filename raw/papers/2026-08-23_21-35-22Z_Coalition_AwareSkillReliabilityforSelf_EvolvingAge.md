---
title: Coalition-Aware Skill Reliability for Self-Evolving Agents
published: 2026-08-23T21:35:22Z
authors: Qiyan Zhao, Xiaofeng Zhang, Bo Liu, Minda Chen, Wei Xiong, Jingyang Chen, Guanting Ye, Wenhao Yu, Xiaosong Yuan, Shijie Han, Da-Han Wang, Jianmin Ji, Fei Huang, Xu-Yao Zhang
url: http://arxiv.org/abs/2608.22610v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coalition-Aware Skill Reliability for Self-Evolving Agents

## Abstract
Agent skills, structured artifacts distilled from interaction trajectories and dynamically reused from skill banks, have become a central mechanism for enabling large language model (LLM)-based self-evolving agents to learn from past experience. Yet existing work has largely focused on the operational aspects of skills, such as acquisition, evolution, and retrieval, while leaving a more fundamental reliability question unresolved: Do accumulated skills in an agent's skill bank actually make positive mechanistic contributions? We investigate this question through systematic skill-bank audits across alternative bank compositions and deployment domains, measuring the resulting changes in agent behavior. These audits reveal two recurring reliability failures: coalition pollution, where bank-level gains conceal negative coalition-level skill contributions, and cross-domain utility reversal, where source-beneficial skills reverse their effects after transfer. These findings motivate two reliability interventions: coalition-aware skill selection during skill accumulation and label-free skill masking after transfer. Coalition-Aware Skill Selection (CASS) selects more reliable candidate skills for the current bank using sampled Shapley marginals. Unsupervised Skill-Masked Coalition Optimizer (u-SMCO) masks transferred skills whose exclusion improves retrieval quality on unlabeled target-domain data. Agentic experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld show that CASS and u-SMCO consistently improve task performance and cross-domain generalization over strong skill-based self-evolving agent baselines. Beyond accuracy, coalition-conditioned reliability modeling reduces sensitivity to noisy outcome-reward fluctuations during reinforcement learning and exposes the limits of isolation-based skill evaluation.

## Metadata
- **Published**: 2026-08-23T21:35:22Z
- **Authors**: Qiyan Zhao, Xiaofeng Zhang, Bo Liu, Minda Chen, Wei Xiong, Jingyang Chen, Guanting Ye, Wenhao Yu, Xiaosong Yuan, Shijie Han, Da-Han Wang, Jianmin Ji, Fei Huang, Xu-Yao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22610v1)