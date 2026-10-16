---
title: RAC: A Relational Agent Contract for Constraint-Governed Engineering Tasks
url: http://arxiv.org/abs/2610.20935v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_21-02-57Z_RAC_ARelationalAgentContractforConstraint_Governed.md
generated_at: 2026-10-15 22:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RAC (Relational Agent Contract), a harness-agnostic contract framework that restructures how engineering agents interact with constraint-governed tasks by separating semantic decision-making from mechanical consequence derivation. The core finding is that when agents specify which relations an artifact must satisfy while delegating concrete geometry, timing, and scheduling outputs to specialized tools, clean-pass rates improve dramatically across PCB design, job-shop scheduling, and embedded-code generation tasks.

## Key Takeaways
- RAC defines a five-component action and feedback layer—authoritative observations, semantic actions, tool-based realization, independent verification, and repair evidence—that decouples the agent's role (deciding which relations an artifact should satisfy) from the tools' role (deriving concrete consequences such as precise geometry or timing). This separation addresses a fundamental failure mode in existing engineering agent systems where agents must simultaneously make semantic decisions and derive mechanical consequences, leading to constraint violations.
- On PCB placement, routing, and repair tasks, RAC achieved the highest clean-pass rate across all nine evaluated models, averaging 90.9% compared to 74.0% for the strongest baseline (requirements-only delegation). In job-shop scheduling, direct relational actions achieved 96.3% quality pass versus 59.6% for code-mediated delivery even when both approaches had access to the same scheduling backend, demonstrating that the action contract itself—not just tool access—is the critical differentiator.
- Evaluations across 141 embedded-code tasks spanning four microcontroller platforms identified the action contract as a genuine source of agent capability. The principle of preserving semantic control while delegating mechanically derivable outputs was shown to systematically improve the reliability of constrained artifacts, suggesting that contract design, not model capability alone, governs engineering agent performance.

## Context
This work sits at the intersection of LLM-based agent systems and formal engineering verification, addressing a persistent gap where language models struggle with tasks requiring exact, coupled constraints such as geometric tolerances, timing requirements, and scheduling feasibility. As AI agents are increasingly deployed in hardware design, manufacturing scheduling, and embedded systems development, the failure modes of purely semantic or purely code-mediated approaches have become bottlenecks for real-world adoption. RAC contributes to the growing body of research on structured agent contracts and tool delegation, offering a principled alternative to ad-hoc prompt engineering or monolithic code generation for constraint-heavy domains.

## Implications
For practitioners building AI-assisted engineering pipelines, RAC suggests that investing in well-defined action contracts and verification layers yields larger reliability gains than upgrading model capabilities alone, which has direct cost and deployment implications for PCB design firms, manufacturing schedulers, and embedded-systems developers. For the broader AI research community, the finding that contract structure acts as a source of agent capability challenges the prevailing assumption that scaling model size or fine-tuning data is the primary path to improving engineering agent performance, redirecting attention toward harness design, tool interfaces, and verification protocols as first-class research targets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20935v1)
