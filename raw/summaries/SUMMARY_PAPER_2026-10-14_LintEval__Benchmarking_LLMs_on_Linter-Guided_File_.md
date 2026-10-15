---
title: LintEval: Benchmarking LLMs on Linter-Guided File Refactoring
url: http://arxiv.org/abs/2610.20027v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_11-36-55Z_LintEval_BenchmarkingLLMsonLinter_GuidedFileRefact.md
generated_at: 2026-10-14 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LintEval introduces a multilingual benchmark (C++, Python, Java) containing 13,061 programs and 171,662 lint alerts to evaluate whether large language models can refactor source files to reduce linter warnings while preserving correct functionality. The benchmark jointly measures functionality preservation, lint alert reduction, new alert avoidance, and edit minimality, revealing a persistent trade-off where commercial models achieve high alert reduction but struggle with functional correctness, while smaller open-source models often fail to reduce alerts at all.

## Key Takeaways
- LintEval is the first benchmark explicitly designed to evaluate linter-guided file refactoring, covering 13,061 programs across three languages with 171,662 lint alerts extracted from language-specific linters, filling a gap left by existing code benchmarks that do not test whether models can reduce lint warnings while maintaining correct initial functionality.
- A persistent trade-off exists between alert reduction and functional correctness: closed-source commercial models reach up to 90.4% Reduction@P but only achieve 67.1%–68.3% Pass@1, meaning they frequently break functionality while attempting to clean up lint issues, while several open-source small models show low or even negative Reduction@P scores, indicating they cannot meaningfully improve code quality.
- A controlled fine-tuning study demonstrates that supervision format critically affects outcomes: refactoring-oriented supervised fine-tuning raised Qwen2.5-Coder-7B's Reduction@P from 24.7% to 76.0%, showing that training data structure and task framing matter as much as model scale for code-quality improvement tasks.

## Context
This paper addresses a practical gap in AI code evaluation: existing benchmarks focus on code generation, bug fixing, or unit-test passing, but none systematically measure whether models can perform the incremental, constraint-preserving edits that real-world developers rely on when IDE linters flag style, performance, or error-prone patterns. By formalizing linter-guided refactoring as a benchmarkable task with multiple evaluation axes, LintEval brings the discipline of software maintenance workflows into the LLM evaluation ecosystem, complementing generation-focused benchmarks with a preservation-and-improvement paradigm.

## Implications
For industry practitioners and IDE tool vendors, LintEval provides a rigorous way to assess whether AI-assisted coding tools can safely automate lint-fixing workflows without silently introducing regressions, which is critical for adoption in production codebases where functional correctness is non-negotiable. For the research community, the finding that supervision format dramatically shifts performance (from 24.7% to 76.0% Reduction@P) suggests that future model training pipelines should incorporate refactoring-specific data formats rather than relying solely on general code corpora, potentially enabling smaller open-source models to become viable code-quality assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20027v1)
