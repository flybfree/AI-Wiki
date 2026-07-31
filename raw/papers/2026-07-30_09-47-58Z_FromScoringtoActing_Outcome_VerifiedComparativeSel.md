---
title: From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents
published: 2026-07-30T09:47:58Z
authors: Xu Xia, Jinghua Piao, Min Yang, Xiaochong Lan, Jiaju Chen, Yong Li
url: http://arxiv.org/abs/2607.27937v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents

## Abstract
Recent work on LLM agents is shifting from external capability elicitation to capability internalization, enabling agents to retain useful skills without retrieval at inference time. On-policy self-distillation (OPSD) offers a promising direction, but many existing methods typically supervise students by scoring actions along student-generated trajectories. Such supervision has two limitations: teacher preferences are not validated by environment outcomes, and action-level scores underuse information from student rollouts, teacher rollouts, and their behavioral relationship. We therefore advocate outcome-verified teacher supervision and comparative learning over teacher-student trajectories. Based on this view, we propose Outcome-Verified Comparative Self-Distillation (OVCSD). OVCSD organizes failed student rollouts into a prefix tree, adaptively invokes a skill-conditioned teacher from student-reached states, and retains only outcome-verified successful continuations. It then applies localized comparative learning at the first state-aligned divergence and distills the post-divergence teacher suffix to transfer completion behavior. Experiments on ALFWorld and WebShop across three model scales show that OVCSD consistently outperforms skill-free RL and existing self-distillation baselines, achieving up to 29.7 and 5.4 absolute success-rate gains over the strongest baselines on ALFWorld and WebShop, respectively, while adding less than 3% privileged interaction during training.

## Metadata
- **Published**: 2026-07-30T09:47:58Z
- **Authors**: Xu Xia, Jinghua Piao, Min Yang, Xiaochong Lan, Jiaju Chen, Yong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27937v1)