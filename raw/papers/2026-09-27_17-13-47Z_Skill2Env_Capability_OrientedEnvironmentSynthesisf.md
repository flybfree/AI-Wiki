---
title: Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents
published: 2026-09-27T17:13:47Z
authors: Weiyi Xu, Xiaowen Yang, Wen Da, Hang Xu, Canwei Li, Hongjie You, Pusen Dong, Yucheng Zeng, Zhaokai Luo, Mu Chuan
url: http://arxiv.org/abs/2609.33772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents

## Abstract
Executable environments are critical for post-training agents on tasks that require tool use and multi-step interaction, but constructing executable tasks together with their environments remains difficult to scale. Skills provide reusable domain knowledge, operational procedures, and tool-use instructions, but a substantial gap remains between the information contained in a skill and a concrete, challenging task with a complete executable environment. To address this gap, we introduce Skill2Env, a capability-oriented framework that starts from a skill and uses agent capability demands to guide task and environment synthesis. Skill2Env represents these demands through reusable difficulty patterns and instantiates them into task blueprints that specify objectives, challenges, environment facts, information boundaries, and acceptance criteria. These blueprints guide the joint construction of task instructions, execution substrates, workspaces, and rubric-based evaluators around source skills. We further propose Iterative Task Hardening, which uses solver execution evidence to identify insufficiently challenging task designs, strengthen or extend their difficulty-pattern instantiations, and revise the corresponding blueprints and environments. Using 1.5K high-scoring trajectories generated from Skill2Env environments for supervised fine-tuning, we observe consistent improvements across a broad range of agent benchmarks, demonstrating the effectiveness of capability-oriented environment synthesis for agent post-training.

## Metadata
- **Published**: 2026-09-27T17:13:47Z
- **Authors**: Weiyi Xu, Xiaowen Yang, Wen Da, Hang Xu, Canwei Li, Hongjie You, Pusen Dong, Yucheng Zeng, Zhaokai Luo, Mu Chuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33772v1)