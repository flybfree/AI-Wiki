---
title: PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving
url: http://arxiv.org/abs/2609.08965v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_16-19-06Z_PlannerForge_LLMAgentsforScenario_BasedTestingofMo.md
generated_at: 2026-09-08 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PlannerForge, an LLM‑agent framework that unifies scenario generation to ADS assessment for autonomous driving. Evaluations show high performance on multiple tasks and improved planner success rates compared with existing tools.

## Key Takeaways
- The integrated pipeline achieves best‑per‑task scores between 0.88 and 1.00 across generation, selection, modification, routing, testing and enhancement using ten off‑the‑shelf LLMs under five prompt conditions.
- Open‑source models such as Qwen3.6:35B match commercial APIs on three of the five tasks while retaining 83% to 78% of seed queries when modules are chained end‑to‑end.
- PlannerForge outperforms Scenario Factory 2.0 in natural‑language generation and BM25 at rank‑1 selection, delivering up to 96% of requested city, road and vehicle attributes without fine‑tuning.

## Context
Autonomous driving safety relies on systematic scenario testing that currently uses disconnected tools for each stage. Large language models are being applied to perception, planning and control but lack a cohesive framework for the entire testing workflow. This work bridges that gap by providing an end‑to‑end LLM‑driven pipeline.

## Implications
The unified approach reduces development cost and improves planner reliability without domain‑specific fine‑tuning, offering industry practitioners a scalable solution. As LLMs become more capable, such frameworks could standardize safety validation across diverse autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08965v1)
