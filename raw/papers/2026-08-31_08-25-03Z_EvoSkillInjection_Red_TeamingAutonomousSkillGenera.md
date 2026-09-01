---
title: EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents
published: 2026-08-31T08:25:03Z
authors: Doyun Kim, Chanwoo Kim, Sugyeong Eo, Yeo-Chan Yoon, Chanjun Park
url: http://arxiv.org/abs/2608.30429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents

## Abstract
LLM-based agent systems increasingly adopt skill-based architectures to reduce repetitive reasoning costs and improve stable, efficient task execution. Recent studies propose self-evolving agents that autonomously generate, refine, and reuse skills from past experiences to enable continuous capability evolution. However, autonomous skill evolution introduces a new attack surface in which malicious capabilities are generated, stored, and reused as legitimate skills. In this paper, we define EvoSkill Injection as a threat model targeting the autonomous skill generation and evolution pipeline of self-evolving agents. We further propose SARGE (Red-teaming Autonomous Skill Generation and Evolution in self-evolving agents), a red-teaming framework for evaluating this threat model through iterative generation, escalation, and reinforcement interactions. To support our framework, we construct EvoSkillBench, a benchmark dataset of malicious interaction trajectories for inducing malicious skill formation in self-evolving agents, and introduce EvoSkillSafetyBench, a post-attack benchmark for evaluating whether injected malicious skills are subsequently retrieved and activated as harmful behaviors. Our evaluation shows that SARGE induces malicious skill formation and that injected skills are persistently stored and repeatedly activated, highlighting the risk of persistent capability corruption.

## Metadata
- **Published**: 2026-08-31T08:25:03Z
- **Authors**: Doyun Kim, Chanwoo Kim, Sugyeong Eo, Yeo-Chan Yoon, Chanjun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30429v1)