---
title: Sapien: A Stateful Policy Engine for Autonomous AI Agents
published: 2026-09-30T22:40:00Z
authors: Corinn Tiffany, Wen Zhang, Eugene Bagdasarian, Lillian Tsai
url: http://arxiv.org/abs/2610.00797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sapien: A Stateful Policy Engine for Autonomous AI Agents

## Abstract
Contextual security defenses prevent AI agents from taking rogue actions by synthesizing a task-specific policy and enforcing it on the agent's tool calls. In multi-step tasks, however, which actions are valid often depends on what the agent has already done and learned. We present Sapien, a policy engine for enforcing stateful contextual policies. A Sapien policy specifies permitted tool-call sequences using a regular expression extended with stateful predicates, deferred policy generation, and scoped semantic checks. We show that Sapien stays within a few percent of an unconstrained agent's utility. Even if the agent is fully hijacked, Sapien's policies rule out 93-95% of attacks on AgentDojo and 62-85% on Toolathlon (twice as many as tool allowlists on long-horizon tasks).

## Metadata
- **Published**: 2026-09-30T22:40:00Z
- **Authors**: Corinn Tiffany, Wen Zhang, Eugene Bagdasarian, Lillian Tsai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00797v1)