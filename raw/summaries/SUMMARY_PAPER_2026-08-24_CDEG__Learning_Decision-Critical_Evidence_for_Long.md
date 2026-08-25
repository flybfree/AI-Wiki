---
title: CDEG: Learning Decision-Critical Evidence for Long-Horizon Diagnostic Agents
url: http://arxiv.org/abs/2608.22899v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_07-30-22Z_CDEG_LearningDecision_CriticalEvidenceforLong_Hori.md
generated_at: 2026-08-24 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CDEG, a graph‑based framework that extracts and validates decision‑critical evidence from historical diagnostic trajectories to improve long‑horizon medical diagnosis. By contrasting successful and failed cases, CDEG builds a structured evidence–action graph and uses counterfactual interventions to confirm which pieces of information truly drive diagnoses. Across benchmarks the approach yields up to an 11.5 % accuracy boost over vanilla agents.

## Key Takeaways
- Existing doctor agents often fail because critical evidence is either not acquired or not integrated into their reasoning, leading to suboptimal diagnoses.  
- Reusing historical trajectories can introduce noisy or incidental information and reuse them without checking which evidence actually influences the final decision.  
- CDEG learns reusable decision‑critical evidence by contrasting cases, validates its impact through controlled counterfactuals, and organizes the results into a graph that guides diagnosis and action.

## Context
Long‑horizon diagnosis in clinical practice is inherently sequential: patients provide evidence over multiple rounds before a final judgment is reached. Current AI agents typically treat each trajectory as a whole, reusing past experiences without distinguishing which specific pieces of evidence are truly decisive. This limitation hampers performance when the relevant evidence is missing or overlooked.

## Implications
The findings suggest that reliable long‑horizon diagnosis requires moving beyond simple experience reuse to learning at the level of individual evidence items. Practitioners can leverage CDEG’s structured graph to make agents more precise, reduce diagnostic errors, and integrate evidence‑driven guidance into real‑world medical workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22899v1)
