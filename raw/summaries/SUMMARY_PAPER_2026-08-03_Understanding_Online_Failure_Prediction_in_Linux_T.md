---
title: Understanding Online Failure Prediction in Linux Through Complementary Multi-View Explainability
url: http://arxiv.org/abs/2608.00651v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_13-12-59Z_UnderstandingOnlineFailurePredictioninLinuxThrough.md
generated_at: 2026-08-03 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an explainable online failure prediction (OFP) pipeline for Linux operating systems that combines feature selection, temporal onset analysis, and causal diagnostics to interpret model alerts. Evaluated under cross‑workload conditions with frozen training artifacts, the system achieved 91–94% detection on unseen workloads while keeping false alarms below 1%. However, failure mode diagnosis was highly sensitive to workload shifts, and some diagnostic mechanisms failed to generalize across modes.

## Key Takeaways
- Detection generalizes more robustly than diagnosis across workload changes, indicating that the model can reliably flag failures even when specific causal interpretations break down.  
- Early‑warning capability varies widely with failure mode, ranging from 38 seconds up to 215 seconds, showing that response time depends on the underlying process rather than a uniform metric.  
- Unseen failure modes are not reliably diagnosable from related training modes alone, yielding 0% accuracy in Leave‑One‑Mode‑Out (LOMO) evaluation.

## Context
Accurate prediction of system failures is essential for operational reliability, yet current AI models often lack interpretability that operators can trust. This work bridges the gap by integrating multiple explainability techniques to provide both a reliable signal and meaningful insight into why a failure was predicted.

## Implications
For practitioners, this research underscores the need for layered explainability rather than relying on a single diagnostic output. Industry adoption of such pipelines could improve confidence in AI‑driven monitoring systems and reduce costly false alarms caused by model drift under workload variation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00651v1)
