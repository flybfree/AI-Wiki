---
title: SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents
published: 2026-08-25T15:52:10Z
authors: Shidong Yang, Ziyu Ma, Tongwen Huang, Xucong Wang, Renda Li, Yiming Hu, Yong Wang, Xiangxiang Chu
url: http://arxiv.org/abs/2608.24747v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents

## Abstract
Large language model (LLM) agents are trained with reinforcement learning (RL) for complex decision-making tasks. However, most RL-trained agents remain episodic and cannot accumulate reusable knowledge across episodes. Recent skill-based approaches, such as SkillRL, attempt to address this issue by extracting skills from raw trajectories, but treat the skill bank as an append-only repository without verifying whether stored skills remain effective. In this paper, we propose SkillForge, a framework for continuous skill evolution that enables skills to be verified and refined through environment interaction. By making skill usage explicit during agent interaction, RL can directly optimize both environment actions and skill invocation decisions. SkillForge further introduces evidence-based skill verification and multi-pathway skill induction, allowing the skill bank to continuously grow while maintaining its quality. Extensive experiments on ALFWorld, WebShop, and AppWorld show that SkillForge consistently outperforms SkillRL, demonstrating the effectiveness of continuously verified skills in training stronger LLM agents.

## Metadata
- **Published**: 2026-08-25T15:52:10Z
- **Authors**: Shidong Yang, Ziyu Ma, Tongwen Huang, Xucong Wang, Renda Li, Yiming Hu, Yong Wang, Xiangxiang Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24747v1)