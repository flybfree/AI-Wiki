---
title: DashArena: Benchmarking LLMs on Interactive Analytic Dashboard Generation
url: http://arxiv.org/abs/2608.10567v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-54-37Z_DashArena_BenchmarkingLLMsonInteractiveAnalyticDas.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents DashArena, a benchmark for generating interactive analytic dashboards and replayable interaction trajectories from natural‑language goals. It evaluates models by having a browser executor replay the trajectory and a vision‑language model judge compare outputs, producing a leaderboard via Bradley–Terry aggregation. Human evaluations confirm that including interaction evidence improves judge agreement.

## Key Takeaways
- The benchmark requires both a dashboard and a full interaction trail to be generated, turning an open‑ended task into a reproducible workflow.
- Evaluation uses visual and execution evidence to capture failures beyond static appearance or successful rendering alone.
- Including interaction evidence in the judge leads to higher alignment with human judgments.

## Context
Interactive dashboards are central to data‑driven decision making, yet current models often produce only static outputs. Existing evaluation methods ignore how users actually navigate and act on generated interfaces, limiting insight into real‑world usefulness.

## Implications
Practitioners must adopt interaction‑aware metrics when assessing dashboard generators, as they reveal hidden flaws in both design and execution. The open‑weight DashJudge-8B offers a lightweight tool to integrate such evaluation into model development pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10567v1)
