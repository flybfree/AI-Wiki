---
title: LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling
url: http://arxiv.org/abs/2608.09343v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_09-20-56Z_LLM_GuidedHeuristicDesignfromSimulationTraces_ACas.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an LLM‑guided heuristic design framework that combines repeated simulation runs with event‑level trace analysis to improve dynamic production and AGV scheduling policies. The approach uses a manager agent to generate bottleneck hypotheses from low‑scoring traces, while editing agents apply code‑level revisions between evaluation batches; the best‑so‑far policy is retained only when improvements are verified. Across five optimization runs using Gemini‑3.1‑Pro, mean scores reached 77.51, with trace‑driven changes raising the score from 62.49 to 78.61 and outperforming rolling‑MILP, rule‑based, and metaheuristic baselines on all seeds.

## Key Takeaways
- The framework leverages simulation traces to diagnose specific policy failures, enabling targeted code revisions rather than random search.  
- LLM revision occurs between evaluation batches while a fixed policy controls each run, preserving stability during optimization.  
- Removing either parallel candidate generation or trace‑database access significantly degrades final performance, highlighting the necessity of both components.

## Context
In AI research, simulation‑based optimization often relies on black‑box scoring that obscures why policies degrade, limiting learning opportunities. This work bridges that gap by using language models to interpret event traces and guide precise policy edits, demonstrating how interpretable feedback can enhance automated planning systems.

## Implications
For industry practitioners, the method offers a scalable way to refine real‑world scheduling algorithms without exhaustive re‑optimization, reducing computational cost while maintaining high performance. Practitioners can adopt trace‑driven LLM editing as a practical tool for continuous improvement in complex discrete‑event simulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09343v1)
