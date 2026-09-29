---
title: MetaBench-Harness: Unlocking End-to-End Optimization of Benchmark Harnesses
url: http://arxiv.org/abs/2609.33411v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_09-45-54Z_MetaBench_Harness_UnlockingEnd_to_EndOptimizationo.md
generated_at: 2026-09-28 21:53
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces MetaBench-Harness, a dual-loop search framework designed to optimize the end-to-end workflow of benchmark generation, addressing the critical issue of static benchmarks saturating due to rapid Large Language Model advancements. By employing an inner loop for benchmark creation and an outer meta-harness layer that iteratively refines harness implementations based on historical trajectories, the method enables multi-dimensional evolution beyond rigid task perturbations. Experimental results on CodeContests and AIME-2024 demonstrate that MetaBench-Harness produces challenging, discriminative benchmarks that steadily improve in reasonableness, competency, and evaluator robustness across successive rounds.

## Key Takeaways
- MetaBench-Harness implements a dual-loop architecture where the inner loop generates new benchmarks via a harness in each iteration, while the outer meta-harness layer orchestrates the search by refining harness implementations based on historical evolution trajectories, allowing for end-to-end optimization of the generation workflow rather than isolated task perturbations.
- When applied to competitive programming (CodeContests) and Olympiad mathematics (AIME-2024) datasets, the evolved benchmarks prove highly challenging and discriminative for frontier models, with trajectory analyses confirming steady improvements in evolution reasonableness, benchmark competency, and evaluator robustness over successive rounds.
- Case studies reveal that the framework effectively utilizes diverse difficulty levers to reframe problems, elevating required capabilities and demonstrating multi-dimensional evolution that addresses benchmark saturation by continuously adapting problem structures rather than relying on hard-coded generation rules.

## Context
As Large Language Models rapidly advance, static evaluation benchmarks risk becoming obsolete or too easy, leading

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33411v1)
