---
title: CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection
published: 2026-10-14T11:52:03Z
authors: Qichen Zhao, Shengfang Zhai, Qingni Shen, Zhonghai Wu, Jiaheng Zhang
url: http://arxiv.org/abs/2610.20049v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection

## Abstract
Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent difficult to identify through individual-package auditing. We introduce CoRedSkill, a compositional red-teaming method that forms stealthy attacks through cooperating skills while preserving their original utility. CoRedSkill decomposes an existing workflow into interdependent skills and embeds attack operations in task functions through abstract syntax tree (AST) rewriting, with skill instructions guiding the agent to autonomously select and invoke the relevant skills, and workflow dependencies and intermediate artifacts connecting the injected operations during task execution. We construct a benchmark of 150 cases covering 50 tasks and three attack objectives to evaluate attack success, task completion, and audit detection. In the main evaluation, CoRedSkill achieves 98.0% attack success and 95.3% task success with a 3.3% detection rate, and a joint success rate of 90.7% (attack success, task completion, and audit evasion in the same case) compared with 6.7--42.7% for the four baselines. Skill compositions can therefore complete legitimate tasks while carrying out unauthorized operations that evade auditing.

## Metadata
- **Published**: 2026-10-14T11:52:03Z
- **Authors**: Qichen Zhao, Shengfang Zhai, Qingni Shen, Zhonghai Wu, Jiaheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20049v1)