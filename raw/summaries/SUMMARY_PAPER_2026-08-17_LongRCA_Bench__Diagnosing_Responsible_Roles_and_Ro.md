---
title: LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures
url: http://arxiv.org/abs/2608.15242v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_14-06-02Z_LongRCABench_DiagnosingResponsibleRolesandRootCaus.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LongRCA Bench, a dataset of 1,140 long‑horizon agent trajectories that fail without injected errors, to study how failures propagate across hundreds of steps. Human labels identify the responsible role and the earliest decisive root‑cause step, showing that current baselines achieve only about 13 % exact root‑step accuracy on median 145‑step traces. A training‑free method RCTA improves performance to 51 % for responsible‑role attribution and 24 % for exact root‑step localization.

## Key Takeaways
- The benchmark demonstrates that existing failure‑attribution methods struggle with long trajectories, achieving low accuracy on both role assignment and precise step identification.  
- RCTA leverages segment summaries to trace candidate error steps back to earlier handoff instructions without retraining the model, significantly boosting attribution performance.  
- Separate evaluation of responsible‑role accuracy versus exact root‑step accuracy is essential for long‑horizon failure diagnosis.

## Context
Long‑horizon agents generate extensive execution traces where failures may originate far from the final output, making pinpointing the decisive step challenging. Current research often focuses on short traces, neglecting the complexity of multi‑step reasoning and error propagation that characterizes real‑world deployments.

## Implications
Practitioners must adopt benchmarks like LongRCA Bench to measure both role attribution and exact root‑cause localization, guiding model design toward more reliable long‑term behavior. This research pushes the field toward robust failure analysis in AI systems where extended interactions are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15242v1)
