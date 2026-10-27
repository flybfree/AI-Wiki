---
title: IntentDelta: A Human-Constructed Benchmark for Evolving User Intent
url: http://arxiv.org/abs/2610.33806v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_17-10-48Z_IntentDelta_AHuman_ConstructedBenchmarkforEvolving.md
generated_at: 2026-10-26 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
IntentDelta introduces a human-constructed multi-turn benchmark designed to evaluate how language-model agents adapt when users revise their requirements and priorities during complex tasks. The benchmark comprises 638 trajectories and 3,766 turns across WebShop and TravelPlanner environments, pairing user utterances with cumulative intention states and human reference actions. Evaluation of eleven agents reveals severe performance gaps, with average Intention Recovery scores of 33.1% in TravelPlanner and 44.7% in WebShop, and Action Scores of 31.6% and 41.0% respectively, demonstrating that current agents fail to track evolving user constraints and translate recovered intentions into correct actions.

## Key Takeaways
- The benchmark reveals that agents struggle fundamentally with preserving earlier user requirements as conversations progress, and they cannot reliably distinguish soft preferences (nice-to-have features) from must-have constraints (hard requirements), leading to systematic failures in intention recovery across both shopping and travel planning domains.
- Even when agents correctly recover the user's evolving intention state, this does not translate into successful execution, exposing a critical disconnect between understanding what a user wants and actually performing the correct actions in a task environment.
- The trajectories are cross-verified and specifically designed to cover feasibility-driven changes (where constraints shift due to practical limitations) and preference-driven changes (where priorities shift due to user taste), making the benchmark more ecologically valid than static single-turn evaluations.

## Context
This paper addresses a critical gap in agent evaluation methodology. Most existing benchmarks test agents on static, single-turn tasks where user intent is fixed from the start. In real-world deployments, users iteratively refine their goals, add constraints, and shift priorities mid-task. IntentDelta fills this gap by providing a human-constructed, cross-verified multi-turn benchmark that mirrors the dynamic nature of actual user-agent interactions, setting a new standard for evaluating adaptive agent behavior rather than one-shot task completion.

## Implications
For practitioners building agentic systems, these results signal that current architectures are not yet robust enough for production use in interactive, multi-turn settings where users naturally revise their needs. The findings suggest that future agent development must prioritize persistent state tracking, constraint classification, and intention-to-action translation as first-class capabilities rather than afterthoughts. Industry teams deploying assistants for shopping, travel, or complex planning tasks should treat intention drift as a primary failure mode requiring dedicated evaluation infrastructure before deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33806v1)
