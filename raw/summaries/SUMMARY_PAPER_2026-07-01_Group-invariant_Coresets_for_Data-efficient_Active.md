---
title: "Summary: Group-invariant Coresets for Data-efficient Active Learning"
url: http://arxiv.org/abs/2607.01089v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_15-46-16Z_Group_invariantCoresetsforData_efficientActiveLear.md
generated_at: 2026-07-01 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GRINCO, a group-invariant coreset method that selects samples based on their orbit in the quotient space induced by a transformation group. By operating on orbits rather than raw instances it reduces redundancy and improves label efficiency. Experiments show better coverage and performance especially when symmetry causes substantial overlap.

## Key Takeaways
- The method defines a quotient metric using either canonical representatives or learned invariant embeddings to evaluate acquisition over entire orbits.
- It combines k-center selection in the quotient space with an orbit-averaged loss for training, ensuring invariance during optimization.
- A derived generalization bound links excess risk to coverage, label uncertainty and intra-orbit variability.

## Context
Active learning seeks to minimize labeling effort by targeting informative samples. Traditional coresets ignore symmetries leading to wasted queries on transformed duplicates. This work addresses the inefficiency caused by group actions in high‑dimensional data where rotations or scaling produce identical visual content.

## Implications
For practitioners, GRINCO offers a principled way to respect known symmetries when building active learning pipelines. In industry, this can reduce labeling costs and improve model performance on datasets with inherent redundancy such as medical imaging or autonomous vision tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01089v1)
