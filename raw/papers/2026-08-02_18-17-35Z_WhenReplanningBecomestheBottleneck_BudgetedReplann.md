---
title: When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents
published: 2026-08-02T18:17:35Z
authors: Shuaijun Liu, Feiyang You, Xingwei Chen, Ningxin Su
url: http://arxiv.org/abs/2608.01428v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents

## Abstract
Embodied agents replan frequently to recover from execution drift, partial observability, and coordination hazards, but each LLM-based replanning call can consume an accumulated textual context that grows over time and across agents. Once this context becomes large, replanning latency develops heavy tails and can miss real-time deadlines even when task success remains high, a failure mode that is hard to detect from average latency or success alone. We present BRACE, a controller that formulates replanning as a budgeted control loop by deciding whether to replan, selecting a replanning mode, and allocating an explicit token budget and latency service-level objective (SLO) while accounting for optional efficiency modules. As a reusable component, we introduce E-RECAP, a cost-aware progressive token pruning method that predicts token utility and prunes replanning contexts across transformer layers while preserving critical head and tail tokens. Across Meta Habitat, RoboFactory, and AirSim, BRACE with E-RECAP reduces replanning-call token counts by 62-92% and SLO violation rates from 85.5-100.0% to 4.7-50.0% in settings where task success is already saturated. In a harder RoboFactory setting where open-loop, frozen-plan, and No BRACE all fail, BRACE + E-RECAP reaches 80.0% success with 4.6% SLO violations, demonstrating that tail-aware per-call budgeting is effective across embodied platforms.

## Metadata
- **Published**: 2026-08-02T18:17:35Z
- **Authors**: Shuaijun Liu, Feiyang You, Xingwei Chen, Ningxin Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01428v1)