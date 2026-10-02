---
title: No One Architecture Fits All: A Cross-Environment Evaluation of Hierarchical Red Team Agents
published: 2026-09-30T18:32:50Z
authors: Ayan Javeed Shaikh, Arunesh Sinha, Nathaniel D. Bastian, Ankit Shah
url: http://arxiv.org/abs/2610.00557v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# No One Architecture Fits All: A Cross-Environment Evaluation of Hierarchical Red Team Agents

## Abstract
Autonomous red team agents increasingly stress-test AI-enabled cyber defenses by planning strategy and executing multistage attacks. Reinforcement learning (RL) and large language models (LLMs) offer complementary mechanisms for the planning and execution such agents require, and prior work has combined them in hybrid hierarchies. Yet a given architecture is typically developed and evaluated within a single environment, leaving open whether an observed advantage reflects a generally stronger decision mechanism or merely alignment with a particular setting. We address this gap with a controlled cross-environment comparison of two homogeneous hierarchical red team architectures: an RL planner with an RL executor (RL+RL) and an LLM planner with an LLM executor (LLM+LLM). We evaluate both against expert autonomous defenders in CybORG CAGE-4 and in Cyberwheel at two network scales, across 18 configurations under one unified disruption metric. We find a pronounced environment-dependent inversion. RL+RL wins the compact, densely rewarded CAGE-4 (78.5% disruption success versus 18.0% for the strongest LLM configuration) and the 100-host Cyberwheel network (81.0% versus 50.5%), while a pretrained cybersecurity LLM agent wins the larger, escalation-gated 1010-host Cyberwheel network (55.0% versus 0.0% for RL). A kill-chain analysis explains the inversion through architecture-specific bottlenecks that aggregate success rates conceal.In the 1010-host Cyberwheel network, RL discovers and compromises hosts but stalls at privilege escalation, whereas in CAGE-4, LLM agents obtain privileged access but rarely convert it into operational impact. These results indicate that conclusions drawn in a single environment may not generalize, and that hybrid planner-executor designs should be motivated by specific failure modes rather than the assumption that one architecture is universally preferable.

## Metadata
- **Published**: 2026-09-30T18:32:50Z
- **Authors**: Ayan Javeed Shaikh, Arunesh Sinha, Nathaniel D. Bastian, Ankit Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00557v1)