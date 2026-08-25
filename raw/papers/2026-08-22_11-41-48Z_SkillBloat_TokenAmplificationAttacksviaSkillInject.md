---
title: SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents
published: 2026-08-22T11:41:48Z
authors: Yuanjin Zheng, Jingbang Chen
url: http://arxiv.org/abs/2608.21929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

## Abstract
Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted   instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through   skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more   tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of   diverse attack-type conditions across multiple amplification mechanisms and then refines the strongest candidate through   LLM-guided full-document skill rewriting. Evaluated on a real-world skill benchmark, SkillBloat achieves 5.4184x-10.1455x   average best amplification across multiple coding-agent target configurations. An ablation shows that the second-stage   refinement loop consistently improves average best amplification over Phase 1 attack-type screening alone, demonstrating   that iterative optimization provides additional benefit beyond initial attack-type selection. These results show that skill   ecosystems expose a practical resource-amplification attack surface that is orthogonal to existing security-oriented skill   poisoning.

## Metadata
- **Published**: 2026-08-22T11:41:48Z
- **Authors**: Yuanjin Zheng, Jingbang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21929v1)