---
title: When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems
url: http://arxiv.org/abs/2610.24545v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_08-14-37Z_WhenCodeBecomesanLLMCall_AnEmpiricalStudyofCall_Si.md
generated_at: 2026-10-19 20:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an empirical study examining how agentic systems enforce contracts around LLM call sites, analyzing 496 call sites across 40 open-source agentic systems totaling 13.4 million lines of code. The authors find that while most call sites include some form of pre- and post-call checking, only 5.3% fully satisfy their expected contracts, revealing a fundamental gap between the guarantees agentic systems need and the guarantees their code actually provides.

## Key Takeaways
- Nearly half (48%) of LLM outputs in agentic systems flow directly into control flow or execution logic, and 73% of those outputs never pass through a human review step, meaning model-generated decisions silently drive program behavior without human oversight or validation.
- Programs enforce 78% of their constraints in code, but within prompts, 67% of constraints are merely requested from the model rather than enforced programmatically, creating a false sense of safety where the model is trusted to self-regulate rather than being constrained by deterministic code.
- Although 82% of call sites perform some checking before or after the LLM call, 63% of expected constraints remain unmet, and ten recurring patterns account for 99% of these gaps. Thirty-eight distinct runtime mechanisms behind these gaps can all be resolved by a small code fix that enforces the expected constraint, demonstrating that the presence of checks is a poor indicator of their adequacy.

## Context
Agentic systems increasingly replace deterministic program logic with LLM calls for decision-making tasks such as tool selection, action validation, and code generation. This shift undermines traditional software quality assurance methods, which rely on fixed specifications and deterministic testing. The paper addresses a critical gap in understanding how these systems can maintain reliability when their core logic is non-deterministic and steerable by input, establishing a framework for analyzing contractual guarantees at each model invocation point.

## Implications
For agent developers and framework maintainers, the findings indicate that adding validation checks around LLM calls is insufficient without verifying that those checks actually enforce the required constraints, and that a small targeted code fix can resolve the vast majority of contract violations. For researchers, the work establishes a methodology for auditing agentic systems at scale and highlights the need for new verification tools and standards that account for the non-deterministic nature of LLM-driven logic in production software systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24545v1)
