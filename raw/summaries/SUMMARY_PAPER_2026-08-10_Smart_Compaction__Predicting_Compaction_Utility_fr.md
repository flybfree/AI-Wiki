---
title: Smart Compaction: Predicting Compaction Utility from Lakehouse Table Metadata
url: http://arxiv.org/abs/2608.08639v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_11-15-21Z_SmartCompaction_PredictingCompactionUtilityfromLak.md
generated_at: 2026-08-10 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a simulation framework to predict the utility of compaction for lakehouse tables by analyzing metadata without loading data. Using XGBoost on Iceberg table manifests, it discovers that a single partition‑level threshold determines whether compaction is beneficial, while cross‑schema validation shows strong generalisation across TPC‑H datasets.

## Key Takeaways
- The continuous file‑reduction ratio (R2 = 0.998) can be predicted accurately from metadata alone, with an RMSE of only 0.013.  
- Binary compaction decisions are trivially separable by the threshold max_files_per_partition > 4, meaning no learned model is needed for this decision.  
- Compaction improves performance on metadata‑heavy queries but can degrade full‑scan aggregations by reducing task parallelism.

## Context
Lakehouse platforms accumulate small files over time, leading to performance bottlenecks that traditional threshold‑based compaction cannot optimise. AI techniques are increasingly applied to extract predictive insights from structured metadata, yet few studies have demonstrated how well such models translate across diverse data schemas and workloads.

## Implications
For practitioners, this work suggests that simple static thresholds may suffice for many lakehouse environments, reducing reliance on complex AI models. The findings also highlight the need to consider query patterns when deciding whether compaction harms overall system efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08639v1)
