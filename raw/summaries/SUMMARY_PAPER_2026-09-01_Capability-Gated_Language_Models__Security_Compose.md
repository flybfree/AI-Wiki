---
title: Capability-Gated Language Models: Security Composes, Utility Does Not
url: http://arxiv.org/abs/2609.00445v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_22-35-49Z_Capability_GatedLanguageModels_SecurityComposes_Ut.md
generated_at: 2026-09-01 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces capability-gated deployment for language models, allowing different users to have distinct access levels within a single model weight set. It shows that security can be composed by merging restrictions while utility does not compose, leading to potential harm even when individual profiles are benign.

## Key Takeaways
- Security composes: under a monotone-elicitation assumption the combined restriction meets is provably stronger than any single pointwise restriction.
- Utility does not compose: multiple harmless user profiles can together cause retention and fluency damage with no known bound.
- The model uses sparse rank gating over nested factorisation to implement per‑principal access control inside one weight set.

## Context
Current AI safety research treats model configurations as external filters that are applied uniformly, ignoring the possibility of internal capability segregation. This work challenges that view by showing how internal composition can affect outcomes, highlighting a gap in existing deployment practices.

## Implications
For practitioners, this means security measures must be designed to compose safely while avoiding utility degradation from combined user profiles. The findings urge research into bounded compositional guarantees and more nuanced access control mechanisms within deployed models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00445v1)
