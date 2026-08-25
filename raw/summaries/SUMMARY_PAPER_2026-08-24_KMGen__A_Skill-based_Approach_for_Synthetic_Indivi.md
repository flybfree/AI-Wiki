---
title: KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation
url: http://arxiv.org/abs/2608.22618v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_21-43-01Z_KMGen_ASkill_basedApproachforSyntheticIndividualPa.md
generated_at: 2026-08-24 21:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KMGen, an end-to-end framework that automates the extraction of Kaplan-Meier curves from published plots and generates synthetic adverse-event streams for individual patient data. It achieves a mean Integrated Absolute Error of 0.0151 on a benchmark spanning clean, edge-case, and adversarial conditions while preserving the marginal survival distribution exactly.

## Key Takeaways
- The automated pipeline extracts KM steps via agent-generated code, achieving a mean Integrated Absolute Error of 0.0151 on 32 plots under clean, edge‑case, and adversarial conditions.
- It generates synthetic AE trajectories using clinical archetypes, bootstrap rank‑correlation coupling to the empirical KM curve, and cycle‑based scheduling with an induction/maintenance split.
- Across three oncology trials, the framework maintains a mean integrated KM absolute difference ≤0.051, sex/ECOG JSD ≤0.013 on 5 of 6 demographic slots, and recovers ≥71% of top‑15 AEs by exact MedDRA term under a single fixed parameter set.

## Context
This work addresses the dual gap in IPD generation where only KM curves are reconstructed manually while adverse-event streams remain absent. By integrating AI agents for extraction and LLM‑driven patient archetype distillation, it demonstrates scalable synthetic data production without human intervention.

## Implications
The framework enables researchers to create realistic IPD datasets for survival analysis and safety studies, reducing reliance on manual digitization. It also supports regulatory compliance by generating traceable AE events, potentially accelerating drug development pipelines and meta‑analysis efforts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22618v1)
