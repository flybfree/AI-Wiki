---
title: agent-risk: Risk Assessment for Changes to AI Agents
url: http://arxiv.org/abs/2610.16280v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_07-05-34Z_agent_risk_RiskAssessmentforChangestoAIAgents.md
generated_at: 2026-10-14 01:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces agent-risk, a formal framework for assessing the safety risk of changes to deployed AI agents (such as tightening a safety gate or swapping in a new model) using only existing operational logs. The authors extend classical risk analysis to handle partial records and partial modifications to live systems, proving what must be logged for exact replay and demonstrating through a bash sandbox experiment that logs alone are insufficient to certify safety decisions. Their key finding is that approval of agent changes requires evidence deliberately designed in advance, including specific log fields, saved states, and targeted reruns.

## Key Takeaways
- The agent-risk framework replays logged episodes under the assumption that nothing else changes and the agent does not anticipate the change, settling episodes that would have acted as before, using a declared stop value for stopped episodes, and requiring logged support, saved-state reruns, or bounds for the remainder. The authors formally prove which log fields are necessary for exact replay and which saved states serve a given gate family, establishing a rigorous foundation for log-based risk assessment.
- In a concrete bash sandbox experiment with a 7,200-episode log, the log alone was unable to decide either of two retry gates because the log never showed the agent acting after refusals. However, rerunning only each gate's blocked episodes from saved states successfully reached both live decisions while using only half the agent calls required by a live test sized post hoc, demonstrating that targeted reruns from saved states are dramatically more efficient than full live testing.
- Without per-step harm logging, a stopping gate's certified harm ceiling increased up to 2.5-fold because the log hides whether harm preceded the stop event. This reveals a critical blind spot: incomplete logging can silently inflate the certified risk bound, making approval decisions unreliable unless the log schema is designed with the specific risk question in mind.

## Context
As AI agents are increasingly deployed in production environments—handling code execution, tool use, and multi-step reasoning—organizations face constant pressure to update models, tighten safety gates, or modify agent behavior. Traditional risk analysis assumes complete records and static systems, but deployed agents produce partial logs and undergo incremental changes to running systems. This paper addresses a gap in the AI safety and governance literature by formalizing how to reason about risk under exactly those partial-information conditions, bridging classical statistical risk methods with the practical realities of agent monitoring and change management.

## Implications
For practitioners deploying AI agents, this work demonstrates that ad hoc logging is insufficient for safety approval; organizations must design log schemas, saved-state checkpoints, and rerun protocols before changes are proposed, treating evidence generation as a prerequisite rather than an afterthought. For the broader AI governance field, the finding that a 7,200-episode log failed to certify two simple retry gates underscores that scale of logging does not substitute for structural completeness, and that regulators and internal review boards should require evidence design as part of any agent-change approval process. The efficiency gains from targeted reruns also suggest a practical path toward reducing the computational cost of safety testing without sacrificing certification rigor.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16280v1)
