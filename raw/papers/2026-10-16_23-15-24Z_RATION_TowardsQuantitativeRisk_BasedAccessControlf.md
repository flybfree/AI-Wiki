---
title: RATION: Towards Quantitative Risk-Based Access Control for AI Agents
published: 2026-10-16T23:15:24Z
authors: Yuntao Du, Harsh Chaudhari, Yuetian Chen, Ron Heichman, Ashish Jayamohan, Kumar Pallav, Mahim Patel, Kaiyuan Zhang, Kyle Polley, Jerry Ma, Ninghui Li
url: http://arxiv.org/abs/2610.24311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RATION: Towards Quantitative Risk-Based Access Control for AI Agents

## Abstract
AI agents increasingly interact with external environments to complete complex user tasks. These interactions can lead to unexpected behavior and expose agents to security threats such as indirect prompt injection. Current agent security systems largely protect agents by restricting their actions, which can result in a substantial security-utility trade-off for complex, open-ended tasks. To address this, we propose a quantitative risk-based approach to access control for AI agents that regulates measurable risks accumulated during task execution. As a concrete realization of this approach, we introduce RATION, a security framework that tracks measurable risks associated with agent actions and enforces quantitative constraints throughout execution. RATION first constructs a task-specific policy by combining explicit constraints derived from the user request with implicit risks calibrated from historical executions of similar tasks. During task execution, RATION continuously tracks the accumulated risks and applies different enforcement strategies depending on the type of risk. Extensive experiments on four security benchmarks show that RATION provides strong security while maintaining high task utility across diverse models and environments.

## Metadata
- **Published**: 2026-10-16T23:15:24Z
- **Authors**: Yuntao Du, Harsh Chaudhari, Yuetian Chen, Ron Heichman, Ashish Jayamohan, Kumar Pallav, Mahim Patel, Kaiyuan Zhang, Kyle Polley, Jerry Ma, Ninghui Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24311v1)