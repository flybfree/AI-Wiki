---
title: EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents
url: http://arxiv.org/abs/2610.03153v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_11-22-36Z_EvoRiskBench_AnEvolvingBenchmarkforRuntimeSecurity.md
generated_at: 2026-10-04 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EvoRiskBench introduces an evolving benchmark designed to evaluate runtime security risks in workspace agents—systems that combine large language models with execution harnesses to perform stateful, multi-step tasks involving external resources. The paper presents a structured EP-Path-EF framework linking risk entry points to technical effects through agent-mediated paths, and evaluates nine model-harness configurations across 450 adversarial tasks, revealing substantial vulnerabilities with attack success rates reaching 68.44% in the most vulnerable configuration.

## Key Takeaways
- The EP-Path-EF framework organizes runtime security risks into nine entry-point categories and five effect categories, connected through agent-mediated risk paths. A 20-participant study validated the interpretability and classification consistency of these categories on representative cases, providing a structured taxonomy for understanding how workspace agents can introduce security failures during execution.
- The benchmark evaluates nine configurations spanning three models (GPT-5.6 Sol, DeepSeek-V4-Pro-0813, Claude Opus 5) and three harnesses (Claude Code, Codex, OpenClaw). The most vulnerable pairing—Codex with DeepSeek-V4-Pro-0813—achieved a 68.44% attack success rate, demonstrating that no single configuration choice guarantees secure autonomous execution and that model selection has a larger impact on vulnerability than harness selection.
- An automated end-to-end workflow constructs and executes risk cases in isolated environments, independently verifying outcomes through runtime traces and environment states. This design addresses a critical gap in existing benchmarks by providing executable, reproducible coverage of runtime security risks rather than static or theoretical assessments, with 450 adversarial tasks across six scenarios.

## Context
As workspace agents increasingly deploy in production environments—performing file operations, API calls, code execution, and multi-step reasoning chains—their runtime security surface expands beyond what traditional model-level safety evaluations capture. Existing benchmarks tend to assess static model outputs or isolated tool calls, leaving a gap in understanding how stateful, multi-step agent executions introduce compounding risks through interactions between models, harnesses, and external environments. EvoRiskBench addresses this gap by providing an evolving, executable benchmark that tracks how model capabilities, harness architectures, and threat landscapes shift over time.

## Implications
For practitioners deploying workspace agents in enterprise or developer-tooling contexts, this research demonstrates that security risk is not a fixed property of a model but emerges from the interaction between model behavior and harness design, meaning configuration choices must be evaluated empirically rather than assumed safe. The finding that attack success rates vary more across models than harnesses suggests that model selection is the primary lever for reducing runtime vulnerability, while harness safety depends heavily on which model is paired with it. For the broader AI safety community, the evolving-benchmark paradigm and the EP-Path-EF taxonomy offer a reusable methodology for continuously stress-testing agent systems as capabilities and threats evolve, setting a template for future agent safety evaluation infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03153v1)
