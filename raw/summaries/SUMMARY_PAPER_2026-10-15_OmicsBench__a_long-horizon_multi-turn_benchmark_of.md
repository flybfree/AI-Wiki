---
title: OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics
url: http://arxiv.org/abs/2610.21074v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_01-23-57Z_OmicsBench_along_horizonmulti_turnbenchmarkofAIage.md
generated_at: 2026-10-15 22:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
OmicsBench introduces a long-horizon, multi-turn benchmark designed to evaluate AI agents on research-study-scale bioinformatics tasks, addressing the gap left by existing benchmarks that test only single short tasks with single-shot prompts. The benchmark comprises 97 tasks structured as directed acyclic graphs with 662 dependent subtasks, evaluated across 12 models on three harnesses, revealing that no agent combination approaches saturation, with mean scores ranging from 0.43 to 0.67 out of 1.0. The authors also introduce an unsupervised failure mode discovery pipeline that clusters agents' failed attempts to surface qualitative shortcomings in how agents perform bioinformatics analyses.

## Key Takeaways
- The benchmark structure fundamentally changes evaluation outcomes: because subtasks are linked as a directed acyclic graph, agents score measurably lower on subtasks that depend on earlier subtasks, revealing a dependency-cascade failure mode invisible to single-shot evaluations. In-context feedback partially recovers this loss, but the gap between no-feedback scores (0.43–0.57) and with-feedback scores (0.54–0.67) confirms that agents struggle with sustained multi-turn reasoning chains.
- No model-harness combination saturates the benchmark even with substantial compute budgets, as the slowest agent averages 3.6 hours per task, indicating that current AI agents remain far from reliably completing realistic research-study-scale bioinformatics workflows that span hours of dependent analysis.
- The unsupervised failure mode discovery pipeline moves beyond deterministic scoring to expose qualitative failure patterns, including agents substituting their own statistical filters for specified ones and agents writing entire answers from memorized knowledge rather than performing actual computational analysis, highlighting a fundamental gap between pattern-matching and genuine analytical reasoning.

## Context
As computational biology increasingly delegates substantial analytical work to AI agents operating in extended, multi-turn sessions, the evaluation infrastructure has lagged behind, relying on single-task, single-shot benchmarks that fail to capture the sequential, dependency-heavy nature of real research workflows. OmicsBench fills this gap by modeling tasks as interconnected subtask graphs, aligning evaluation methodology with how practitioners actually interact with AI agents over hours-long sessions. This shift from isolated prompts to chained reasoning mirrors broader trends in AI evaluation toward agentic, tool-use, and long-horizon task benchmarks across domains.

## Implications
For bioinformatics practitioners and computational biology labs, these findings signal that current AI agents cannot yet be trusted to autonomously execute multi-step research analyses without human oversight, particularly when later steps depend on the correctness of earlier ones. The identified failure modes—such as agents inventing their own statistical criteria or answering from memory rather than computing—suggest that deployment pipelines need guardrails, verification checkpoints, and structured feedback loops rather than treating agents as black-box analysts. For benchmark developers and AI safety researchers, the failure mode discovery pipeline offers a transferable methodology for diagnosing qualitative agent shortcomings beyond numeric scores, applicable to agentic evaluation in other scientific and professional domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21074v1)
