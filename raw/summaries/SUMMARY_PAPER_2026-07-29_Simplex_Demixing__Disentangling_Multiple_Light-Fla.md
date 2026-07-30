---
title: Simplex Demixing: Disentangling Multiple Light-Flavor Jets at Colliders
url: http://arxiv.org/abs/2607.24921v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-27_18-00-02Z_SimplexDemixing_DisentanglingMultipleLight_FlavorJ.md
generated_at: 2026-07-29 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a machine‑learning method called simplex demixing that can separate several jet flavors from mixed data without imposing strict limits. It first tests the approach on synthetic mixtures of down, up, and gluon jets to recover true fractions, then applies it in dijet production experiments. The results show that the number of distinct categories depends on sample abundance and available hadron information.

## Key Takeaways
- The framework extracts T jet flavors from M data samples by finding maximally separable clusters, turning a classifier into a geometric object with T vertices.
- Identifiability is limited by how abundant each flavor is in the mixture and what hadronic features the model can use.
- The method generalizes beyond two‑jet categories to any number of light‑flavor topics.

## Context
In collider physics, separating jet flavors from noisy data remains a challenge because traditional definitions assume fixed numbers of jets. Machine‑learning approaches offer flexible ways to uncover hidden patterns in large datasets, but they often require careful preprocessing and assumptions about the underlying structure.

## Implications
This work provides a practical tool for extracting multiple light‑flavor signatures at future colliders where precise flavor information is valuable for new physics searches. Practitioners can apply simplex demixing to improve tagging efficiency without redesigning entire analysis pipelines, opening up data‑driven strategies across experimental domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24921v1)
