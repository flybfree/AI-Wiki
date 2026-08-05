---
title: PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
url: http://arxiv.org/abs/2608.04003v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-58-05Z_PAST_Bench_BenchmarkingtheFoundationsofRecursiveSe.md
generated_at: 2026-08-05 01:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PAST‑Bench, a benchmark that tests whether personal AI agents improve over time by retaining experience across sessions. The study runs 26 scenarios and 204 episodes with seven base models and four agent frameworks, showing real gains but uneven performance. A follow‑up model Hermes+ adds five interventions to boost average gain and clarify the save‑retrieve‑update pathway.

## Key Takeaways
- Agents show measurable later‑task improvements when experience is retained, yet these gains are not uniform across all capabilities or models.  
- The same headline improvement can be achieved without evidence of the intended save‑retrieve‑update pathway, indicating that retention alone does not guarantee systematic progress.  
- Hermes+ raises average gain and provides clearer pathway evidence, especially for tasks requiring outdated state replacement.

## Context
The research addresses a core challenge in recursive self‑improvement: ensuring that persistent agents convert accumulated knowledge into better behavior rather than merely storing it. By isolating retention effects through controlled experiments, the work contributes to understanding how memory and procedural reuse influence long‑term performance.

## Implications
For practitioners developing personal AI agents, PAST‑Bench offers a standardized tool to evaluate whether experience truly drives improvement, guiding design choices such as intervention points in the agent loop. The findings suggest that targeted mechanisms are needed to translate retained data into consistent gains across diverse models and tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04003v1)
