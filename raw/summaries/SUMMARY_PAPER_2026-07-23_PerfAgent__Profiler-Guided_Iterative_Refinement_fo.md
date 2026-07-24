---
title: PerfAgent: Profiler-Guided Iterative Refinement for Repository-Level Code Optimization
url: http://arxiv.org/abs/2607.19653v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_01-19-42Z_PerfAgent_Profiler_GuidedIterativeRefinementforRep.md
generated_at: 2026-07-23 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
PerfAgent introduces a profiler‑guided, verifier‑in‑the‑loop workflow that helps coding agents locate real bottlenecks in repository‑level code optimizations. On two benchmark suites it more than doubles the rate of expert‑matching patches compared with OpenHands + GPT‑5.1 and surpasses an oracle best‑of‑five baseline while using less test time.

## Key Takeaways
- Profiler feedback enables agents to discover hidden bottlenecks that are not exposed by simple passing tests, allowing deeper code improvements.
- The method yields a 39.2 % expert‑matching rate on GSO versus 19.6 % for the baseline, more than doubling performance.
- PerfAgent outperforms an oracle best‑of‑five approach at lower cost because it uses profiler evidence rather than exhaustive timing sampling.

## Context
Current large language model agents excel at correctness tasks but often fail to deliver meaningful speedups in repository‑level optimizations. Optimizing code while preserving behavior is challenging, and existing approaches rely heavily on test outcomes which can miss subtle performance issues or cause silent regressions.

## Implications
This work demonstrates that integrating profiler insights into AI‑driven optimization pipelines can substantially boost real‑world impact without requiring extensive manual effort. Practitioners can adopt PerfAgent to achieve more reliable and efficient code improvements, reducing risk of hidden bugs while delivering measurable speed gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19653v1)
