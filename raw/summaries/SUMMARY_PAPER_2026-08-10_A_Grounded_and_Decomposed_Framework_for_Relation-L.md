---
title: A Grounded and Decomposed Framework for Relation-Level Hallucination Evaluation in Abstractive Summarization
url: http://arxiv.org/abs/2608.08180v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_15-16-51Z_AGroundedandDecomposedFrameworkforRelation_LevelHa.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a refined framework to evaluate relation-level hallucinations in abstractive summarization and defines the Relation Hallucination Index (RHI). It combines dependency-aware extraction with lemmatization, entity grounding, passive recovery, negation handling, reporting verb filtering, nominal fallback, clausal propagation, and deduplication. The normalized RHI yields a scale‑invariant faithfulness score across datasets.

## Key Takeaways
- The framework uses lemmatization‑based normalization to align relation terms, reducing spurious matches during evaluation.
- It resolves grounded subjects in passive constructions and models negation‑aware verbs to prevent false attributions.
- A normalized RHI aggregates these components into a single scale‑invariant score for fair model comparison.

## Context
Relation hallucinations are a known weakness of abstractive summarization, affecting trustworthiness especially in medical or legal contexts. Existing metrics often ignore syntactic dependencies and entity grounding, leading to biased scores. This work addresses those gaps by embedding linguistic analysis directly into the evaluation pipeline.

## Implications
For researchers, the RHI provides a reproducible benchmark for relation faithfulness, guiding model improvement. For industry practitioners, it enables automated detection of hallucinated relationships in generated summaries, supporting compliance with factual reporting standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08180v1)
