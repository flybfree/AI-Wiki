---
title: SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale
url: http://arxiv.org/abs/2608.22725v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_02-27-50Z_SEAM_ShotEntity_AttributeMemoryforConsistentShort_.md
generated_at: 2026-08-24 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SEAM, a training-free memory graph that repairs visual continuity in short-dramas by extracting shot-level entity-attribute states and retrieving prior context for prompt rewriting. On SEAM‑Bench the method lifts cross‑episode recall from 0.70 to 0.946 across six text models and achieves a 96.5% director acceptance rate with zero unsafe injections.

## Key Takeaways
- The memory graph stores multi‑dimensional shot states enabling causal retrieval of prior constraints.
- Prompt rewriting injects only surviving continuity constraints, eliminating visual drift between shots.
- Counterfactual analysis shows the method contributes at least 21.9 percentage points to director acceptance.

## Context
Current short‑drama pipelines suffer from accumulated visual breaks as shots are generated independently, making continuity a bottleneck for scaling. This work addresses that by providing a model‑agnostic memory layer that works across diverse text generators.

## Implications
SEAM can be integrated into production pipelines without retraining models, offering a practical solution to maintain consistency in large‑scale content creation and improving audience acceptance metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22725v1)
