---
title: SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based AutoFE
url: http://arxiv.org/abs/2608.17948v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-04-18Z_SIGMA_SHAP_GuidedImplicit_TrajectoryGenerationforM.md
generated_at: 2026-08-18 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SIGMA, a framework that generates feature trajectories using large language models without relying on metadata. It uses SHAP values to guide group feature generation and an exposed‑feature Implicit Trajectory (EXIT) mechanism to keep prompts within constant length. Experiments show performance matching SOTA with far fewer features and much lower duplicate rates.

## Key Takeaways
- SHAP values replace semantic metadata, providing task‑aware signals that steer the model toward coherent feature groups.
- The EXIT approach maintains a fixed prompt size by representing the trajectory implicitly through exposed features, preventing context overflow.
- Duplicate generation drops from 37.2% to 6.8%, and average feature count falls to 5.4, yielding high efficiency.

## Context
LLM‑driven AutoFE aims to automate feature engineering but is limited by long prompt histories that exceed model contexts or lack metadata. This work addresses those bottlenecks with a constant‑context strategy that leverages gradient‑based SHAP signals and implicit trajectory modeling.

## Implications
Practitioners can deploy LLM AutoFE at scale without costly data preprocessing, reducing both compute cost and feature redundancy. The method opens pathways for real‑time optimization in domains where metadata is unavailable or expensive to maintain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17948v1)
