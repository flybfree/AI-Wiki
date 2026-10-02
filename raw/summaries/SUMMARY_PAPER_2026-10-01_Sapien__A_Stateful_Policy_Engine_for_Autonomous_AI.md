---
title: Sapien: A Stateful Policy Engine for Autonomous AI Agents
url: http://arxiv.org/abs/2610.00797v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_22-40-00Z_Sapien_AStatefulPolicyEngineforAutonomousAIAgents.md
generated_at: 2026-10-01 21:25
model: qwen3.6-35b-a3b
---

## Summary
Sapien introduces a stateful policy engine designed to enforce contextual security policies for autonomous AI agents, addressing the challenge that valid actions in multi-step tasks often depend on prior agent behavior and learned information. The system utilizes regular expressions augmented with stateful predicates, deferred policy generation, and scoped semantic checks to define permitted tool-call sequences effectively. Experimental results demonstrate that Sapien maintains utility within a few percent of an unconstrained agent while significantly reducing attack success rates compared to traditional allowlists.

## Key Takeaways
- Sapien policies extend regular expressions with stateful predicates, deferred policy generation, and scoped semantic checks to capture complex dependencies where the validity of a tool call relies on the agent's history and current context rather than just immediate inputs.
- The engine preserves high operational utility by staying within a few percent of an unconstrained agent's performance, ensuring that security constraints do not severely hinder the agent's ability to accomplish tasks effectively.
- Sapien demonstrates superior defense capabilities against hijacking attacks, ruling out 93-95% of attacks on AgentDojo and 62-85% on Toolathlon, which represents a significant improvement over standard tool allowlists, particularly in long-horizon tasks where context is crucial.

## Context
As autonomous AI agents increasingly interact with external tools and environments, ensuring their safety requires moving beyond static constraints to dynamic defenses that adapt to the agent's evolving state. Existing contextual security mechanisms often struggle with multi-step workflows where action validity is inherently sequential and dependent on accumulated knowledge, creating gaps that malicious actors can exploit through hijacking or prompt injection.

## Implications
This approach enables the deployment of more capable and autonomous agents in high-stakes environments by providing a robust framework that balances security enforcement with functional flexibility, reducing the trade

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00797v1)
