---
title: Agentic Anomaly Detection with ORCA-Style Dynamic Inductive Bias Adaptation in Multimodal Wearable Time Series Data
url: http://arxiv.org/abs/2608.08859v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_18-49-13Z_AgenticAnomalyDetectionwithORCA_StyleDynamicInduct.md
generated_at: 2026-08-11 12:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ORCA, an agentically controlled anomaly detection framework that dynamically adapts the temporal receptive field of multimodal wearable time series data without adding trainable parameters. The method uses a supervisory controller to select among discrete temporal contexts at inference time, achieving AUROC = 0.99 comparable to the strongest fixed-context baselines while removing the need for manual horizon tuning. ORCA also demonstrates conservative generalization on the MIMIC-IV dataset, showing robust performance across heterogeneous clinical conditions.

## Key Takeaways
- The framework dynamically adjusts temporal receptive fields based on lightweight signal statistics rather than relying on fixed horizons.
- ORCA matches or exceeds the performance of top fixed-context anomaly detection models without requiring any retraining or hyperparameter tuning.
- The adaptive approach yields conservative out‑of‑distribution generalization, preserving AUROC across diverse clinical datasets.

## Context
In AI research, inductive bias is often fixed during model design, limiting adaptability to nonstationary data. Wearable physiological signals are inherently heterogeneous and resource‑constrained, making static temporal windows insufficient for reliable anomaly detection. This work addresses the need for a principled, lightweight adaptation strategy that aligns with real‑world deployment constraints.

## Implications
For practitioners developing wearable health monitoring systems, ORCA offers a practical solution to maintain high detection accuracy without extensive computational overhead or manual tuning. The adaptive bias control can be integrated into edge devices, enabling robust anomaly detection across varying physiological regimes and clinical settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08859v1)
