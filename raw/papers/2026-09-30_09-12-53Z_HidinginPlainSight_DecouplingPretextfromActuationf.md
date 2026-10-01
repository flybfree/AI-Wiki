---
title: Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents
published: 2026-09-30T09:12:53Z
authors: Wenxin Wu, Lingyong Yan, Lei Sha, Shuaiqiang Wang, Jiashu Zhao
url: http://arxiv.org/abs/2609.39352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents

## Abstract
LLM agents increasingly rely on reusable Skills for complex, multi-step tasks, creating a critical supply-chain attack surface where poisoned Skill content steers agent decision loops under benign requests. Existing skill poisoning attacks either colocate actuation with its contextual pretext or distribute actuation across multiple Skills, but do not explicitly separate the rationale for execution from the operation itself. In this work, we reveal that untrusted agent decisions fundamentally depend on two conceptually distinct Risk-Realization Factors (RRFs): an actuation factor (specifying what concrete operation is performed) and a pretext factor (providing the situational rationale for why the agent must perform it). Guided by this abstraction, we propose a coordination-based attack paradigm: decoupling pretext from actuation. Rather than fragmenting the malicious actuation, we preserve it as an intact operation within a downstream Steering Skill, while delegating the pretext factor to an upstream Grounding Skill that subtly alters persistent environment artifacts through routine utility operations. The intact actuation thus hides in plain sight, appearing completely legitimate and task-driven only when evaluated against the fabricated pretext. Building on this formulation, we develop an automated framework that discovers authentic execution dependencies, synthesizes coordinated pretext-actuation skill pairs, and iteratively refines poisoned skill instructions via runtime closed-loop feedback. Extensive evaluations across single-session and persistent cross-lifecycle scenarios demonstrate that decoupled skill poisoning achieves high attack success, exposing a critical blind spot in isolated Skill security audits. Our automated framework code is available at https://github.com/Wenxin-buaa/CoordPoison.git.

## Metadata
- **Published**: 2026-09-30T09:12:53Z
- **Authors**: Wenxin Wu, Lingyong Yan, Lei Sha, Shuaiqiang Wang, Jiashu Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39352v1)