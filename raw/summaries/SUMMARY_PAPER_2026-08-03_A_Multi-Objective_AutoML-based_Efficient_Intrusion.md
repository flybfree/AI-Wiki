---
title: A Multi-Objective AutoML-based Efficient Intrusion Detection System for EV Charging Networks
url: http://arxiv.org/abs/2608.02274v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_14-11-38Z_AMulti_ObjectiveAutoML_basedEfficientIntrusionDete.md
generated_at: 2026-08-03 23:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a Multi-Objective Automated ML (MOO‑AutoML) framework that designs an efficient intrusion detection system for electric vehicle charging networks. By combining lightweight training, automated feature selection with LightGBM, and multi-objective genetic optimization, the method balances detection accuracy, inference latency, and model size.

## Key Takeaways
- The proposed MOO‑AutoML selects compact feature subsets using accumulated feature importance to reduce model complexity while preserving detection performance.
- NSGA‑III jointly tunes the feature selection threshold and LightGBM hyperparameters to maximize weighted F1-score, minimize 99th percentile inference latency ratio, and minimize model size ratio.
- Experiments on CICEVSE2024 and CICIDS2017 demonstrate that the system achieves competitive detection metrics with lower P99 latency and smaller model sizes compared to baseline methods.

## Context
Automated ML pipelines are increasingly used for security applications where real‑time response is critical. Traditional IDS approaches often sacrifice efficiency for accuracy, making them unsuitable for resource‑constrained IoT environments like EV charging stations.

## Implications
The method provides a practical template for deploying accurate yet lightweight models in edge AI scenarios, encouraging industry adoption of efficient intrusion detection solutions that meet both performance and operational constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02274v1)
