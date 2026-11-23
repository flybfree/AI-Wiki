---
title: Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material
url: http://arxiv.org/abs/2611.27139v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_05-19-59Z_DoSeniorAgentsDoTheirJob_MeasuringRoleIntegrityinH.md
generated_at: 2026-11-22 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the concept of "role integrity" to evaluate whether senior agents in multi-agent LLM systems genuinely fulfill their assigned responsibilities when processing subordinate agents' reports, rather than merely aggregating them into a fluent final answer. The authors develop RI-Bench, a behavioral benchmark grounded in three institutional hierarchies—peer review, appellate adjudication, and parliamentary inquiry—and demonstrate through over 12,000 agentic episodes across eight LLMs that senior agents frequently fail to weigh, verify, or relay subordinate material as their roles demand, with failure rates reaching up to 71% in certain conditions.

## Key Takeaways
- The authors formalize "role integrity" as the preservation of an agent's functional responsibilities when acting on subordinates' material, and they construct RI-Bench using three real-world institutional structures whose rules explicitly assign duties (weigh, verify, relay) to senior roles, enabling rule-based checks and rubric-guided LLM judges calibrated against human annotation to measure behavioral compliance rather than output correctness.
- Empirical results reveal a striking asymmetry in failure modes: senior agents rarely adopt a planted procedural error (only 2.9% of rulings), but they frequently follow a majority of generic reviews (up to 71% of decisions) or drop witnesses' stated limitations (up to 65% of cited claims), indicating that aggregation and omission are far more common failure patterns than outright error adoption.
- Adding obligation prompts to system instructions reduces these role-integrity failures but does not eliminate them, and the prompts also shift behavior in control conditions, suggesting that explicit role instructions are insufficient to guarantee faithful role execution and that direct, obligation-specific evaluation is necessary rather than inferring integrity from general capability benchmarks.

## Context
This work addresses a critical blind spot in the rapidly growing field of multi-agent LLM orchestration, where systems increasingly decompose complex tasks into subagent pipelines with a coordinating "senior" agent synthesizing outputs. Existing evaluation frameworks predominantly assess final-answer quality, which can mask whether the senior agent performed its intended deliberative, verification, or relay functions. By grounding evaluation in institutional rules with explicit duty assignments, RI-Bench provides a methodological template for auditing agent behavior at the level of process rather than product, filling a gap between capability benchmarks and deployment safety requirements.

## Implications
For practitioners deploying multi-agent LLM pipelines in high-stakes domains such as legal adjudication, scientific peer review, or legislative oversight, these findings warn that fluent, well-cited outputs from a senior agent do not guarantee that subordinate evidence was faithfully weighed or limitations preserved. The paper motivates a shift toward obligation-specific evaluation protocols in both research and production settings, urging system designers to instrument role-compliance checks directly rather than relying on role instructions or general capability scores to assume proper agent behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27139v1)
