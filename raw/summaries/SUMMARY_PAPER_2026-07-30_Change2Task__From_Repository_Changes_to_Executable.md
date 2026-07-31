---
title: Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments
url: http://arxiv.org/abs/2607.28591v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-44-31Z_Change2Task_FromRepositoryChangestoExecutableCodin.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Change2Task, a system that converts merged pull requests into verified coding tasks by using repository history. It demonstrates high success rates across five task families and reduces pipeline costs.

## Key Takeaways
- Change2Task achieves 79.6% verified task construction from 1,130 source changes across bug fix, feature addition, test generation, API migration, and security repair tasks.
- The system recovers 29.2% more verified tasks than a baseline using pull requests alone.
- Historical and reconstructed cases show up to 98.0% matched outcome agreement under agent evaluation.

## Context
Coding agents need large amounts of executable data for training and benchmarking, but creating fresh environments is costly. Change2Task addresses this by reusing healthy repository revisions as task bases.

## Implications
This approach lowers resource expenditure across the full pipeline, making it feasible to generate many tasks automatically. Practitioners can rely on historical changes to build diverse, verifiable datasets without repeated setup.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28591v1)
