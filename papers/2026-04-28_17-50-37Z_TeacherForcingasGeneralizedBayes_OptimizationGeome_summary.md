---
title: "Summary: Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics"
date: 2026-04-28
tags: ['paper', 'research', 'ai']
---
# Summary: Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics


**Source**: [Original Paper](http://arxiv.org/abs/2604.25904v1)
Saved: 2026-05-08 03:29
Source: 2026-04-28_17-50-37Z_TeacherForcingasGeneralizedBayes_OptimizationGeome.md

---

## Summary
Analyzes identity teacher forcing as a generalized Bayes update whose optimization geometry can differ from the free-running marginal likelihood in switching recurrent models for chaotic dynamics. In Lorenz-63 experiments, evidence fine-tuning improves held-out evidence but can reduce quantities of interest relative to teacher-forcing-pretrained models.

## Key Takeaways
- Compares the curvature of teacher-forcing and marginal-likelihood objectives.
- Shows how missing-information effects change the geometry of switching models.
- Warns that better evidence does not always mean better dynamical QoIs.

## Context
The paper studies deterministic recurrent surrogates for chaotic dynamical systems.

## Implications
Training and fine-tuning choices should account for objective geometry, not just held-out evidence.

## Original Reference
- Title: Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics
- Authors: Andre Herz, Daniel Durstewitz, Georgia Koppe
- Published: 2026-04-28T17:50:37Z
- URL: http://arxiv.org/abs/2604.25904v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-28_17-50-37Z_TeacherForcingasGeneralizedBayes_OptimizationGeome.md

## Related Concepts

- [[concepts/prompting/prompting-hub.md|Prompting Hub]]
- [[concepts/ai-infrastructure/ai-infrastructure-hub.md|AI Infrastructure Hub]]
- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
