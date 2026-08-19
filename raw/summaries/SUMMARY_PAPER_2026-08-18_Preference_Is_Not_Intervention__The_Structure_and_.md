---
title: Preference Is Not Intervention: The Structure and Stability Boundaries of Reader-Specific Evidence Utility
url: http://arxiv.org/abs/2608.17781v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_13-45-17Z_PreferenceIsNotIntervention_TheStructureandStabili.md
generated_at: 2026-08-18 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how reader-specific evidence utility varies across retrieval‑augmented generation tasks and tests whether stable structural components can be transferred between readers. By comparing nine readers’ disagreement rates, variance explained by reader‑query interactions versus a null model, and self‑selected evidence effects, the authors identify three measurable objects—evidence activity, ordinal preference, and conditional signed direction—and find that only the ordinal geometry remains consistent across multiple settings.

## Key Takeaways
- The 29.8 % variance explained by reader×query interaction is far larger than the 8.4 % permutation null, indicating genuine reader‑specific effects beyond random noise.  
- Ordinal reader similarity (ρ≈0.60–0.83) holds across leave‑one‑out interventions, PRISM preferences, RAMDocs, and RAGuard, showing stable preference geometry that is not tied to task or evidence type.  
- Signed direction of utility is weak in open‑ended QA (ρ≈0.14–0.35) especially with misleading evidence but strong in binary fact‑checking (ρ=0.75), revealing a task‑bounded signature that cannot be explained by sparsity or metric artifacts.

## Context
In AI systems, the usefulness of model‑specific knowledge depends on whether its impact is reusable across queries rather than being tied to particular inputs. Understanding which aspects of this effect are stable helps design interventions that benefit many users without overfitting to specific contexts. This work bridges preference modeling and intervention analysis in large language models.

## Implications
For practitioners, the finding that ordinal similarity does not guarantee transferability means that helping one reader may harm another when the underlying signed direction differs. Designing RAG pipelines should therefore focus on preserving stable ranking signals rather than assuming uniform evidence utility across users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17781v1)
