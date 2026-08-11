---
title: Metadata Reconstruction from Values Alone: Recovering Column Semantics in Undocumented Warehouses
url: http://arxiv.org/abs/2608.07946v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_06-12-18Z_MetadataReconstructionfromValuesAlone_RecoveringCo.md
generated_at: 2026-08-10 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Rosetta, a system that recovers column semantics from raw data values in undocumented warehouses. By combining deterministic evidence extraction with a language model, it produces calibrated metadata with provenance and confidence bounds. On paired columns across BIRD databases, the harness achieves higher accuracy than the model alone when it commits to predictions.

## Key Takeaways
- The deterministic layer acts as a competence detector that decides whether the system should speak, increasing coverage by 0.257 without improving precision on committed propositions.
- Human documentation is outperformed only in selected columns; the harness writes no better prose than the model alone when both arms agree, highlighting selection over amplification.
- A code‑enforced commit gate eliminates false positives, achieving zero no‑evidence coverage across backbones and a blind i2b2 warehouse where 95.5% of ICD‑9 codes are decoded while NDC drug codes remain abstained.

## Context
This work addresses the gap between well‑documented AI benchmarks and real‑world production databases that lack metadata, a common challenge for automated data understanding tools. It demonstrates how evidence‑driven prompting can improve reliability in low‑resource settings where human annotations are unavailable or costly.

## Implications
For practitioners, Rosetta offers a pragmatic path to query translation systems by gating model output with confidence thresholds, reducing errors without sacrificing coverage. The approach underscores that better documentation is less about richer prose and more about selective activation of reliable knowledge.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07946v1)
