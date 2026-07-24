---
title: Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents
url: http://arxiv.org/abs/2606.31270v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-06-30_07-44-37Z_LearningfromFailure_Inference_TimeSelf_Improvement.md
generated_at: 2026-07-23 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a failure‑driven self‑improvement loop for computer‑use agents that converts failed trajectories into useful upgrades. By having an LLM diagnose errors, suggest inference‑time solutions, and generate lightly verified code patches, the method improves the OpenCUA‑72B model’s success rate from 42.3 % to 48.9 % on OSWorld without extra training cost.

## Key Takeaways
- The authors replace the conventional success‑only fine‑tuning loop with a complementary failure‑based pipeline that leverages diagnostic LLM reasoning and human‑light verification of patches.
- Their approach yields a measurable boost in task completion (6.6 percentage points) while keeping inference overhead modest and avoiding additional training.
- The method demonstrates that failures, often discarded, can be systematically turned into actionable improvements for agent performance.

## Context
Computer‑use agents rely on multimodal large language models to navigate virtual environments, yet obtaining high‑quality data is limited by the scarcity of successful trajectories. Most existing systems discard failed attempts, missing valuable insights about model weaknesses that could guide targeted updates.

## Implications
This failure‑driven paradigm offers a cost‑effective way to continuously refine agents without retraining from scratch, encouraging more robust and reliable automation tools. Practitioners can integrate such loops into their pipelines to unlock incremental gains in performance with minimal resource expenditure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.31270v1)
