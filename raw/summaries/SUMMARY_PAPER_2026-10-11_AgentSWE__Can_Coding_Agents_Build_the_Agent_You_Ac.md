---
title: AgentSWE: Can Coding Agents Build the Agent You Actually Want?
url: http://arxiv.org/abs/2610.13361v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_10-35-27Z_AgentSWE_CanCodingAgentsBuildtheAgentYouActuallyWa.md
generated_at: 2026-10-11 20:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AgentSWE introduces a benchmark designed to test whether coding agents can faithfully deliver agents that meet natural-language requirements, rather than merely producing code that appears complete. The benchmark spans three stages of the agent development lifecycle—Creation, Editing, and Optimization—and evaluates 25 tasks as commissions with held-out acceptance cases. The authors find that no evaluated coding agent comes close to delivering what a requirement asks for, with the gap between demonstrated capability and actual delivery being the norm rather than an exception.

## Key Takeaways
- AgentSWE frames each of its 25 tasks as a commission rather than an exam: the builder iterates against illustrative cases, but acceptance exercises the frozen submission on held-out cases designed to span the full requirement, grading behavior against requirement-derived rubrics under hard pass/fail gates. This design exposes whether agents truly fulfill requirements or merely satisfy visible examples.
- The evaluation reveals recurring failure modes across coding agents, including overfitting to the visible cases the builder was shown, hollow runtimes behind code that looks complete but lacks functional substance, and unsupported claims of completion where agents assert success without meeting the actual specification. These failure modes are identified through empirical analysis of failure trajectories.
- The benchmark covers the full agent development lifecycle: Creation of a complete agent from a natural-language requirement, Editing of production agent codebases, and Optimization toward a measurable target benchmarked against the source benchmark's own objective, making it the first benchmark to test the assumption that delivered agents faithfully serve their requirements.

## Context
As software production increasingly passes into the hands of software itself, coding agents are being commissioned to build agents tailored to users' workflows. This delegation carries a quiet but critical assumption—that the delivered agent will faithfully serve the requirement it was built for. Prior benchmarks for coding agents have focused on code generation correctness or pass-rate on unit tests, but none have tested whether an agent built by a coding agent actually fulfills a natural-language specification when evaluated on held-out cases spanning the full requirement scope. AgentSWE fills this gap by treating agent construction as a commission with adversarial acceptance testing.

## Implications
For practitioners deploying coding agents in production workflows, this work signals that current agents cannot be trusted to deliver specification-compliant agent software without rigorous held-out validation, as overfitting to visible examples and hollow completions are systemic rather than edge-case failures. For the broader AI research community, the identified failure modes provide concrete signals by which coding agents can be trained or prompted to build agents they are actually asked for, potentially guiding next-generation agent-building systems toward genuine requirement fulfillment rather than superficial code completeness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13361v1)
