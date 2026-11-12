---
title: On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents
url: http://arxiv.org/abs/2611.11506v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-08_17-20-48Z_OntheRelativeSecurityofPromptInjection_MechanisedD.md
generated_at: 2026-11-11 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PlanTERS, a formal framework for evaluating the security of LLM agents against prompt injection attacks by defining security relative to a reference agent that never obeys untrusted content. Rather than applying overly strict noninterference conditions, the author formalizes a notion of relative security where an agent is considered secure if every information leak it produces is already present in the reference agent's behavior. The framework is mechanized in Isabelle/HOL and proves or refutes security guarantees for agents equipped with fences, budgets, approvals, loops, and dual-LLM architectures.

## Key Takeaways
- The paper argues that traditional noninterference is too strong a security criterion for useful LLM agents, because a functional agent must allow untrusted content to influence its actions and may intentionally disclose user data, making declassification policies task-specific and impractical to write generically.
- The PlanTERS framework instantiates relative security from speculative execution security literature, combining a small agent language where the attacker controls how the model follows instructions, composition with runtime monitors, and multiple attacker models differing in observational power, enabling systematic formal analysis of agent security properties.
- A central "fence theorem" demonstrates that revoking injectable tools at the first untrusted read and never granting them back guarantees relative security at the event level on finite runs for any model behavior where each injection is a single call obeying a fixed schedule, with a fairness condition extending this guarantee to possibly infinite runs.

## Context
Prompt injection remains one of the most pressing open security problems for deployed LLM agents that process untrusted inputs such as emails, web pages, or tool outputs. Existing security analyses often rely on informal threat models or overly restrictive formal definitions that do not match how agents are actually built and deployed. This paper bridges that gap by adapting relative security concepts from speculative execution and hardware security into the LLM agent domain, providing a mechanized, machine-checked foundation for reasoning about what defenses actually guarantee.

## Implications
For practitioners building LLM agents, the fence theorem offers a concrete, provable defense strategy: revoke all injectable tools upon encountering untrusted content and never restore them, which formally guarantees relative security under stated model-behavior assumptions. For the broader AI safety and security community, mechanized proofs in Isabelle/HOL set a precedent for moving beyond empirical red-teaming toward formally verified agent architectures, potentially informing standards for agent deployment in regulated or high-stakes environments where provable security guarantees are required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.11506v1)
