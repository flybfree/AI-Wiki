---
title: EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks
url: http://arxiv.org/abs/2609.31906v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_18-49-33Z_EmailBench_ABenchmarkforEvaluatingLLMAgentsonEnter.md
generated_at: 2026-09-28 22:11
model: qwen3.6-35b-a3b
---

## Summary
EmailBench introduces a comprehensive benchmark designed to evaluate large language model agents on enterprise email and productivity tasks, addressing the lack of self-contained environments with typed workflows in existing research. The study presents 206 scenarios across 16 categories, utilizing a deterministic synthetic corpus and a hybrid evaluation protocol combining static assertions and LLM rubrics. Results reveal that even the best-performing models achieve only a 33.5% pass rate, highlighting a significant disconnect between successful tool execution and actual task completion in complex email workflows.

## Key Takeaways
- EmailBench provides a self-contained evaluation framework featuring 206 scenarios across 16 task categories, supported by a typed email API specification and a deterministic synthetic Enron-inspired corpus to ensure reproducibility and provider-neutral naming conventions.
- The benchmark employs a rigorous hybrid evaluation protocol that integrates 258 executable static assertions with 211 LLM rubrics, enabling precise measurement of both structural correctness and semantic alignment in agent outputs across diverse productivity tasks.
- Evaluation of eight LM configurations demonstrates a critical performance gap where the top model passes only 33.5% of scenarios despite 99.7% of tool calls succeeding without API errors, proving that valid tool execution does not guarantee successful task completion or handling of multi-step coordination challenges.

## Context

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31906v1)
