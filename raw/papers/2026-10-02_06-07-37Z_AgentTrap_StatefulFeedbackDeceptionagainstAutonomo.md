---
title: AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents
published: 2026-10-02T06:07:37Z
authors: Yuelin Wang, Jiongchi Yu, Yanbang Sun
url: http://arxiv.org/abs/2610.02869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents

## Abstract
Autonomous penetration testing agents conduct multi-step attacks by continuously adapting their plans and actions to target responses. As a common defense, honeypots can be deployed to divert these agents from real assets by presenting decoy services, while also supporting attack tracing and active counterattacks. However, conventional honeypots rely primarily on static artifacts and predefined responses, leaving them unable to adapt to the evolving attack strategies of autonomous penetration testing agents. To this end, we present AgentTrap, the first closed-loop honeypot tailored for autonomous penetration testing agents. AgentTrap uses sentinel endpoints to avoid benign interference, stateful deception grounded in the protected application, and behavior-guided escalation to sustain engagement and collect agent-side behavioral evidence with controlled disclosures.   We evaluate AgentTrap against eight autonomous penetration-testing agents in a deployed web application containing a real application endpoint and a separate honeypot endpoint configured under three defense strategies. Compared with no defense, AgentTrap reduces the aggregate real-target attack success rate from 95.8% to 79.2% and successfully elicits attacker API keys in 18.8% of the runs, outperforming static deception and fixed escalation. Furthermore, trace analysis shows that resistance to such counterattacks depends jointly on model-level recognition of deceptive requests and architecture-level isolation of sensitive resources.

## Metadata
- **Published**: 2026-10-02T06:07:37Z
- **Authors**: Yuelin Wang, Jiongchi Yu, Yanbang Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02869v1)