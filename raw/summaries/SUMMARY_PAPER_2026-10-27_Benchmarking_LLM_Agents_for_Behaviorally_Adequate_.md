---
title: Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements
url: http://arxiv.org/abs/2610.36584v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_03-41-55Z_BenchmarkingLLMAgentsforBehaviorallyAdequateTestGe.md
generated_at: 2026-10-27 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Req2Test-Bench, a benchmark of 5,086 execution-validated instances derived from developer-authored behavior-driven development (BDD) artifacts across 8 open-source projects, 5 programming languages, and 4 BDD frameworks. The benchmark evaluates whether LLM agents can generate tests that are behaviorally adequate—meaning they kill every mutant that a ground-truth developer-written test kills—when given only a natural-language requirement and target interfaces. The central finding is a stark gap between execution success and behavioral adequacy: the best configuration (Codex with DeepSeek-V4.1-Flash) achieves 82.8% passing tests but only 33.8% behavioral adequacy, revealing that current agents produce syntactically valid but semantically insufficient test implementations.

## Key Takeaways
- Scaling up agent complexity and reasoning effort yields sharply diminishing returns in behavioral adequacy relative to generation cost, suggesting that brute-force agent scaling is not a viable path to semantically correct test generation and that more targeted, requirement-grounded strategies are needed.
- Under-specified requirements create a fundamental information gap: ambiguous setup conditions and implicit expected outcomes in natural-language requirements prevent agents from inferring the full behavioral contract, leading to tests that pass execution but fail to validate the intended behavior.
- Behavioral adequacy is rigorously defined as kill-completeness via mutation testing, and the benchmark demonstrates that passing a test suite is a necessary but grossly insufficient proxy for behavioral correctness, exposing a critical blind spot in current agent evaluation methodologies.

## Context
As LLM agents increasingly generate repository-level code from natural-language specifications, the need for requirement-to-test generation as a validation harness has become a critical bottleneck in AI-assisted software engineering. Existing benchmarks predominantly address white-box testing or code-level correctness, leaving a significant gap in evaluating whether generated tests semantically align with the behavioral intent expressed in requirements documents. This paper addresses that gap by grounding evaluation in developer-authored BDD artifacts and mutation-based behavioral adequacy, providing a more faithful measure of whether an agent truly understands and validates required behavior rather than merely producing executable code.

## Implications
For practitioners deploying LLM agents in software development pipelines, the 82.8%-to-33.8% gap between passing tests and behavioral adequacy signals that current agent-based test generation cannot be trusted as a standalone validation mechanism without additional semantic verification layers. For the research community, the findings motivate the development of requirement-grounded harnesses that constrain agent non-determinism and explicitly surface implicit behavioral expectations, pointing toward structured prompting and specification-aware generation as promising directions. Industry adoption of AI-assisted testing must therefore incorporate mutation-testing-based adequacy checks rather than relying on pass/fail execution metrics alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36584v1)
