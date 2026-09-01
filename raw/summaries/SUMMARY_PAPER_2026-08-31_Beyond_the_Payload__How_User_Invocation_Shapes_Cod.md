---
title: Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning
url: http://arxiv.org/abs/2608.30686v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_12-26-01Z_BeyondthePayload_HowUserInvocationShapesCodingAgen.md
generated_at: 2026-08-31 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how everyday choices made by users of coding agents influence the vulnerability of those agents to repository poisoning attacks. By systematically varying user-side prompt configurations, the authors demonstrate that vulnerability is not fixed but emerges from specific task types and phrasing patterns. The study introduces CIPR, a benchmark showing up to four‑fold differences in attack success across tasks.

## Key Takeaways
- Task type creates large ASR variations: test‑execution tasks achieve high attack success with low alert rates, forming a silent attack surface.
- Underspecified prompts lower ASR by limiting execution depth, reducing the chance of malicious code being executed fully.
- Noisy or vague prompt expressions can suppress alerts because they make malicious content less conspicuous to the agent.

## Context
Repository poisoning remains a critical threat for software engineers who rely on third‑party code. Prior research focused mainly on attacker control over injection vectors, overlooking how user interaction shapes risk. This work bridges that gap by showing that human prompting is a controllable factor in security outcomes.

## Implications
Developers must treat prompt design as part of secure coding practices, not just the agent’s logic. Industry tools should flag or mitigate prompts that could enable silent attacks, especially on test‑execution tasks where vulnerabilities are most exploitable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30686v1)
