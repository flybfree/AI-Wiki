---
title: Bounded Agents: Delegation Security for Multi-Agent AI Systems
published: 2026-08-16T18:38:00Z
authors: Xabier Muruaga
url: http://arxiv.org/abs/2608.15888v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bounded Agents: Delegation Security for Multi-Agent AI Systems

## Abstract
LLM-based agents can act on behalf of a user to access cloud services, call tools, or invoke agents. At session start, the agent's permissions are set but remain static, and each request is evaluated independently, without considering prior actions. Within its permissions, an agent may act contrary to the delegated task, combine individually permitted actions into a prohibited outcome, or delegate authority to a sub-agent without limiting it. A prompt injection poses a risk only if the agent has authority to perform such actions; this is therefore a problem of authorization architecture, not just the model. The Agentic Principal Chain (APC) tracks delegated authority from one principal to the next. APC evaluates each request against the accumulated session state using six authorization checks. APC carries forward and restricts delegated scope and budgets. Using composition closure, APC checks requests against prior actions to prevent prohibited combinations and enforces the decision outside the model. We prove Blast Radius Monotonicity and Composition Soundness for APC implementations; Composition Soundness is limited to prohibited combinations under a complete restriction set and serialized admission. We evaluated 3,154 instances including InjecAgent, AgentDojo, and ASB. Our compromised-model evaluation tests APC independently of model behavior by inserting the ground-truth attack call after the first legitimate tool call. AgentDojo exfiltration fell from 75-100% to 0% across all four domains; APC blocked all 544 InjecAgent data-stealing cases. Intent binding reduced destruction from 38.6% to 4.0% and manipulation from 90.5% to 12.1%. Authorization latency was 0.24 ms at the 99th percentile on an idle host; across 949 AgentDojo task-injection pairs, utility was 8.6 and 13.9 percentage points lower in the two settings. Implementation, evaluation tools, and data are publicly available.

## Metadata
- **Published**: 2026-08-16T18:38:00Z
- **Authors**: Xabier Muruaga
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15888v1)