---
title: AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents
url: http://arxiv.org/abs/2610.02869v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_06-07-37Z_AgentTrap_StatefulFeedbackDeceptionagainstAutonomo.md
generated_at: 2026-10-04 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AgentTrap introduces the first closed-loop honeypot specifically designed to defend against autonomous penetration testing agents that adapt their attack strategies in real time. By combining sentinel endpoints, stateful deception grounded in the protected application, and behavior-guided escalation, AgentTrap reduces the aggregate real-target attack success rate from 95.8% to 79.2% and successfully elicits attacker API keys in 18.8% of evaluation runs, outperforming static deception and fixed-escalation baselines.

## Key Takeaways
- AgentTrap addresses a critical gap in conventional honeypot defenses: static artifacts and predefined responses cannot adapt to the evolving, multi-step attack plans of autonomous penetration testing agents. The system uses sentinel endpoints to avoid interfering with benign traffic while deploying stateful deception that is grounded in the actual protected application, making decoy responses dynamically responsive to the agent's evolving strategy.
- The behavior-guided escalation mechanism sustains engagement with the attacking agent over multiple interaction rounds, collecting agent-side behavioral evidence while maintaining controlled disclosures. This closed-loop design allows the honeypot to learn from the agent's actions and adjust its deception in real time, rather than presenting a fixed set of decoy services.
- Trace analysis reveals that an agent's resistance to counterattacks depends jointly on two factors: model-level recognition of deceptive requests (i.e., whether the LLM powering the agent can identify honeypot artifacts) and architecture-level isolation of sensitive resources (i.e., whether the agent's tooling can access real assets independently of the honeypot). This dual dependency highlights that effective defense requires both cognitive and structural hardening.

## Context
As large language model-driven autonomous agents increasingly automate penetration testing and red-teaming workflows, traditional static honeypots become inadequate because these agents continuously replan and adapt based on target feedback. AgentTrap represents a shift from passive deception to active, stateful defense tailored to agentic attack behavior, bridging the gap between classical honeypot research and the emerging field of agentic AI security.

## Implications
For security practitioners and organizations deploying autonomous penetration testing agents, AgentTrap demonstrates that adaptive honeypot defenses can meaningfully reduce real-target compromise rates and extract actionable intelligence such as attacker API keys, enabling active counterattacks. The finding that defense effectiveness depends on both model-level deception recognition and architectural isolation of sensitive resources suggests that future agentic security systems must integrate deception at the application layer while simultaneously enforcing strict resource-access boundaries in agent tooling architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02869v1)
