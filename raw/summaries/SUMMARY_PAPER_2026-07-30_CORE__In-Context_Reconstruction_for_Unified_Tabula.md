---
title: CORE: In-Context Reconstruction for Unified Tabular Anomaly Detection
url: http://arxiv.org/abs/2607.27615v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_03-08-49Z_CORE_In_ContextReconstructionforUnifiedTabularAnom.md
generated_at: 2026-07-30 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CORE, an in-context reconstruction framework for unified tabular anomaly detection that aligns heterogeneous features while preserving semantics and avoids labeled anomalies. It demonstrates that reconstruction errors can serve as a universal anomaly signal across diverse datasets. The approach eliminates the need for synthetic or labeled outliers.

## Key Takeaways
- CORE uses a decorrelated feature alignment module to map different tables into one space without losing original meaning.
- The model treats anomaly detection as an in-context reconstruction task, using normal samples to reconstruct each input and measuring error magnitude.
- This method works on unseen datasets without requiring any external labeling or synthetic anomalies.

## Context
Unified anomaly detection aims to apply a single model across heterogeneous data sources, a goal challenged by feature mismatch. CORE’s in-context approach aligns with recent trends toward self-supervised learning where context provides supervision.

## Implications
Practitioners can deploy CORE on any tabular dataset without building separate models or generating anomalies. This simplifies deployment pipelines and reduces reliance on costly labeling efforts, making anomaly detection more accessible across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27615v1)
