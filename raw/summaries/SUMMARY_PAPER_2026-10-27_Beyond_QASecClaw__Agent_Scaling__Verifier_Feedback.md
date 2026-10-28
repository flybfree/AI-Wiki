---
title: Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance
url: http://arxiv.org/abs/2610.36947v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_10-06-26Z_BeyondQASecClaw_AgentScaling_VerifierFeedback_andE.md
generated_at: 2026-10-27 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether scaling up the number of specialist language-model contexts improves software assurance outcomes when deterministic tool evidence is already available. Through five experiments spanning Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-COMP assertion verdicts, and misleading evidence packages, the authors find that increasing model contexts from 1 to 50 yields a 49-fold token increase without improving unsafe clearance, and that raw verifier feedback simultaneously raises both correct and incorrect model verdicts. The results collectively support deterministic evidence admission over model-based verdict aggregation for the tested settings.

## Key Takeaways
- Scaling language-model contexts does not improve software assurance outcomes: across eight related development warnings, increasing context count from 1 to 50 increases token consumption 49-fold without any improvement in unsafe clearance, and on 160 OWASP cases, model configurations trade clearance against unresolved outcomes, with the ten-context arm assessing only 96 cases out of 160.
- Raw verifier feedback introduces a critical accuracy-versus-reliability tradeoff: on 32 SV-COMP tasks, providing verifier feedback raises mean correct model verdicts from 12.7 to 22.0 but also raises incorrect verdicts from one to seven, while a deterministic JBMC-plus-JVM validation baseline achieves 26 correct verdicts with only six unresolved outcomes, demonstrating that structured tool-based validation outperforms model-mediated feedback interpretation.
- Construction-specific scope checks outperform model-based evidence evaluation: on two sets of 120 evidence packages, models reject 70-100% of applicable counterexamples, yet deterministic construction-specific scope checks classify every package correctly, and no target defect was discovered in three Defects4J bugs, with one bug unsupported by the test adapter, highlighting gaps in evaluation coverage.

## Context
This work sits at the intersection of large language model deployment and formal software verification, a rapidly growing area where practitioners increasingly ask whether LLMs can augment or replace deterministic static analysis and testing tools. The paper addresses a fundamental question in AI-assisted software engineering: whether the apparent advantage of multi-context, multi-agent LLM pipelines actually translates into better assurance outcomes, or whether deterministic evidence pipelines remain superior. By using a relatively small model (Qwen2.5-Coder-7B-Instruct) and a 1.5B sensitivity analysis, the authors ground their findings in a realistic deployment scenario rather than relying on frontier-scale models, making the results directly relevant to resource-constrained engineering teams.

## Implications
For software assurance practitioners and tool vendors, these findings caution against the assumption that adding more LLM contexts or agent layers will improve defect detection or safety verification, and instead reinforce the value of deterministic evidence admission pipelines such as JBMC-based validation. Industry teams considering LLM integration into CI/CD assurance workflows should prioritize structured verifier feedback loops with explicit scope checks rather than relying on model-mediated verdict aggregation, while also recognizing that current evaluation benchmarks like Defects4J and SV-COMP may not fully capture the failure modes that arise in production settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36947v1)
