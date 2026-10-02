---
title: Harness Annealing: Learning to Act with Less External Control
url: http://arxiv.org/abs/2610.01235v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_07-35-39Z_HarnessAnnealing_LearningtoActwithLessExternalCont.md
generated_at: 2026-10-01 21:21
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces harness internalization, a framework where language agents learn to assume control responsibilities typically managed by external harnesses, such as workflow organization and decision-making, without relying on them during inference. The authors propose Harness Annealing Training (HAT), which combines explicit control supervision with a curriculum of teacher trajectories collected under progressively weaker harnesses to facilitate this transition. Experiments demonstrate that models trained with HAT can achieve performance comparable to baselines using full harness support when operating with tools alone, though the benefits depend on model scale and deployment configuration.

## Key Takeaways
- Harness Annealing Training (HAT) integrates explicit control supervision with a curriculum learning strategy, utilizing teacher trajectories gathered from progressively weaker harnesses to systematically train the model to make internal decisions regarding investigation, revision, and termination criteria.
- Evaluation on SWE-QA and SWE-QA-Pro benchmarks reveals that annealed checkpoints for 9B and 35B models operating with tools alone can match the performance of baseline checkpoints deployed with full harness support, demonstrating successful transfer of control logic from external systems to the model.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01235v1)
