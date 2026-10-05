---
title: OpenGameEval: Benchmarking Agentic Programming and Exploration in a Stateful Game Engine
url: http://arxiv.org/abs/2610.02563v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_22-56-10Z_OpenGameEval_BenchmarkingAgenticProgrammingandExpl.md
generated_at: 2026-10-04 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
OpenGameEval introduces a benchmark and evaluation framework for testing language model agents performing game development tasks inside Roblox Studio, using reproducible stateful sessions scored by executable checks on both edited scenes and simulated play sessions. The benchmark evaluates 13 frontier models across 84 human-curated tasks, revealing that even the best model achieves only 51.7% single-attempt pass rates, and demonstrates that exploration behavior—specifically inspecting objects before acting on them—strongly predicts task success.

## Key Takeaways
- The benchmark separates observation tools from editing tools within an eight-tool action space, enabling direct measurement of exploration behavior rather than only scoring final task success, which distinguishes it from most existing agentic coding benchmarks that conflate exploration with execution.
- Frontier models struggle significantly: the best model solves 51.7% of tasks on a single attempt and only 39.4% across five consecutive attempts, with no tested model solving six tasks. Models at the frontier reach similar aggregate pass rates by solving entirely different tasks, with top-five models spread by 5.0 percentage points on script-authoring tasks and 12.5 percentage points on scene-change tasks, indicating no single model dominates across task categories.
- Exploration behavior is a strong predictor of success independent of model or task: runs that inspect every object a reference solution touches before acting pass 13.4 percentage points more often on scene-only tasks and 9.8 percentage points more often on script-only tasks compared to runs that inspect none of them, suggesting that structured exploration is a critical capability for agentic programming.

## Context
This paper addresses a growing gap in AI evaluation: existing agentic coding benchmarks such as SWE-bench or HumanEval primarily measure final output correctness without capturing how agents navigate and understand complex stateful environments. As language models are increasingly deployed as autonomous agents in software engineering, game development, and interactive systems, the ability to explore, observe, and reason about a stateful environment before making changes becomes as important as the code generation itself. OpenGameEval fills this gap by providing a reproducible, executable evaluation harness inside a real game engine, setting a precedent for benchmarking agentic behavior in interactive, multi-step environments rather than static code repositories.

## Implications
For practitioners building agentic coding systems, the finding that exploration behavior predicts success by 10–13 percentage points suggests that prompt engineering and tool design should prioritize structured inspection workflows before editing actions, rather than optimizing solely for code generation quality. For the AI research community, the task-category split revealing that different models excel at different kinds of work signals that aggregate leaderboard scores mask meaningful capability differences, and future benchmarks should report performance disaggregated by task type. The MIT-licensed release of the full task suite, place files, annotations, and a Roblox Studio plugin provides a reproducible foundation for evaluating agentic systems in stateful interactive environments beyond traditional code editing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02563v1)
