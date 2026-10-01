---
title: Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents
published: 2026-09-30T07:15:10Z
authors: Kaixing Zhang, Changming Li, Yingdong Shi, Zheng Zhang, Kaitao Song, Wenjie Shi, Jingang Wang, Kan Ren
url: http://arxiv.org/abs/2609.39149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents

## Abstract
Textual skills enable large language model (LLM) based agents to accumulate reusable procedural knowledge without updating model parameters. Yet existing skill evolution remains largely confined to the text space: an optimizer must diagnose success and failure patterns, and revise skills solely from long execution trajectories and sparse task outcomes. This text-only paradigm leaves the agent's internal representations, which contain rich records of its evolving execution state, outside the skill optimization loop. We ask whether an agent can improve its external textual skills by reflecting on its own internal representations. We introduce Rep2Skill, a representation-guided framework for self-evolution on agent skills. Specifically, upon the collected agent rollouts, Rep2Skill models their internal model representation trajectories to localize turns that deviate from successful execution dynamics, and it further interprets these signals alongside the execution contexts as actionable textual feedback for targeted skill revision. Experiments on two agent environments with two open-source LLMs show that Rep2Skill consistently outperforms text-only approaches in the self-evolution setting, where the same LLM serves as both executor and optimizer without a stronger external model. This establishes a promising direction moving agent self-improvement beyond text-only reflection.

## Metadata
- **Published**: 2026-09-30T07:15:10Z
- **Authors**: Kaixing Zhang, Changming Li, Yingdong Shi, Zheng Zhang, Kaitao Song, Wenjie Shi, Jingang Wang, Kan Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39149v1)