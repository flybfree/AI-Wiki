---
title: SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation
url: http://arxiv.org/abs/2609.08950v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_16-08-43Z_SQLMorph_QueryMutationandFine_GrainedMetricsforTex.md
generated_at: 2026-09-08 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SQLMorph, a framework for evaluating Text-to-SQL systems using query mutation and fine-grained metrics. It shows that join expansion degrades accuracy and linguistic perturbations cause brittleness up to 17%. The new metrics provide finer analysis across systems.

## Key Takeaways
- Join Query Expansion increases query coverage but reveals accuracy degradation as the number of joins grows, highlighting structural complexity challenges.
- Textual Query Augmentation demonstrates that heavy abbreviation can reduce accuracy by up to 17%, exposing linguistic brittleness.
- Execution Precision and Recall give fine-grained scores beyond binary metrics, enabling analysis of over‑ and under‑prediction.

## Context
The field struggles with evaluation reproducibility due to limited benchmarks; SQLMorph addresses this by generating diverse queries automatically. This aligns with the trend toward robust LLM evaluation practices that reflect real-world complexity.

## Implications
Practitioners can use these metrics to debug systems and improve robustness, leading to better alignment of research with industry needs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08950v1)
