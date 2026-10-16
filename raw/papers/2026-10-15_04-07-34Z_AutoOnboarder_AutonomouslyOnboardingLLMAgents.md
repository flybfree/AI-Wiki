---
title: AutoOnboarder: Autonomously Onboarding LLM Agents
published: 2026-10-15T04:07:34Z
authors: Tanay Arora, Cong Liu
url: http://arxiv.org/abs/2610.21218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoOnboarder: Autonomously Onboarding LLM Agents

## Abstract
Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the way a trainer onboards a new employee. It places the agent under the supervision of an intelligent ``Onboarder'' coding agent, which iteratively tailors its foundation model, prompt, and harness source code to simultaneously improve performance and decrease cost. Like a real onboarding process, the Onboarder is only given tens of examples, and all evaluation data is isolated on a separate virtual machine to prevent leakage. We report the lessons learned from building and testing AutoOnboarder on genomic-sequencing prior authorization form submission. Autonomously onboarded agents are able to match or exceed the performance of a Gemini 3.5 Flash baseline at up to 29$\times$ lower costs. However, these agents remain imperfect, and the Onboarding process varies greatly in terms of final performance. We conclude that future Onboarding systems require a robust environment for the Onboarder, including a structured thought interface, (controlled) internet access, and a wide model search space.

## Metadata
- **Published**: 2026-10-15T04:07:34Z
- **Authors**: Tanay Arora, Cong Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21218v1)