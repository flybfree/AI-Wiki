---
title: Towards Better Exploration in Sequential Test-Time Scaling
url: http://arxiv.org/abs/2609.39632v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_12-39-00Z_TowardsBetterExplorationinSequentialTest_TimeScali.md
generated_at: 2026-09-30 22:06
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates limitations in test-time scaling for language models, specifically highlighting how sequential methods often stagnate by entering "attractors," which are answer sets that halt further exploration. The authors demonstrate that a simple model-mixing intervention effectively mitigates this issue, allowing sequential approaches to surpass parallel baselines in solution coverage and accuracy over longer timescales. These findings suggest a strategic shift toward refining sequential scaling techniques for long-horizon reasoning tasks.

## Key Takeaways
- Sequential test-time scaling frequently suffers from premature convergence into "attractors," where the model gets trapped in a set of answers that prevents exploration of novel solutions; analysis across 27 method-model-benchmark combinations reveals that 53.8% of trajectories enter an attractor within just four iterations, explaining why sequential methods often fail to improve over long horizons.
- Introducing a model-mixing intervention significantly enhances exploration by reducing the attractor hit rate by an average of 21.2 percentage points, which enables sequential methods to expand solution coverage beyond what is achievable with compute

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39632v1)
