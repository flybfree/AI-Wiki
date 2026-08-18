---
title: Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors
url: http://arxiv.org/abs/2608.15965v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_23-39-42Z_BeattheCounterFirst_ABaselineforTemporal_GraphAnom.md
generated_at: 2026-08-17 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SimpleCount, a minimal one‑feature reference for temporal‑graph anomaly detection that outperforms several complex models on five public datasets and two synthetic ones. The authors demonstrate that SimpleCount matches or exceeds SLADE on three datasets while exceeding IsoForest on all six, despite requiring far less compute time.

## Key Takeaways
- SimpleCount selects a single scalar feature per dataset from a fixed pool of counts, recencies, first‑occurrence indicators, and count‑derived transforms, achieving comparable detection performance to high‑complexity models.  
- The computational advantage is substantial: SLADE needs 23 to 133 times more wall‑clock time than SimpleCount while delivering no clear gain in accuracy on most datasets.  
- On synthetic graphs where the true signal is a triangle, SimpleCount recovers it with AUC up to 0.955, whereas all evaluated detectors remain near random.

## Context
The field of streaming graph anomaly detection has seen rapid advances in model complexity, yet empirical evaluations often overlook baseline simplicity. This work highlights that performance gains are not universally attributable to richer architectures and underscores the importance of computational efficiency alongside accuracy.

## Implications
For practitioners, SimpleCount offers a lightweight, parameter‑free alternative that can be deployed at edge devices with minimal latency. The paper’s call for reporting compute cost alongside any claimed gain encourages more honest benchmarking in AI research and industry practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15965v1)
