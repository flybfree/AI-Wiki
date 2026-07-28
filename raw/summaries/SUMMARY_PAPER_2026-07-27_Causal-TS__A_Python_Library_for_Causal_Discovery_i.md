---
title: Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary Time Series
url: http://arxiv.org/abs/2607.24673v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_17-14-48Z_Causal_TS_APythonLibraryforCausalDiscoveryinHigh_D.md
generated_at: 2026-07-27 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Causal‑TS, an open‑source Python library that enables causal discovery for high‑dimensional and nonstationary multivariate time series. It bundles four specialized algorithms—CDNOTS, CDNOTS+, CEDAR, and GRACE—along with wrappers for GES, Granger, LASSO‑VAR, and LGES, all built on a unified conditional independence test layer accelerated by PyTorch. A regime discovery pipeline detects structural breaks using pluggable changepoint detectors and runs per‑regime analyses with tailored parameters, providing an end‑to‑end workflow from raw series to causal effect estimates.

## Key Takeaways  
- Causal‑TS combines multiple causal inference algorithms in a single Python package, allowing flexibility for different data structures and nonstationary dynamics.  
- The library leverages PyTorch GPU acceleration to handle high‑dimensional time series efficiently, reducing computational bottlenecks typical of traditional methods.  
- A modular regime detection pipeline enables automatic identification of structural breaks and subsequent per‑regime causal analysis, improving robustness in changing data environments.

## Context  
Causal inference for multivariate time series remains a challenging problem due to high dimensionality and the presence of nonstationary trends. Existing tools often assume stationarity or require extensive preprocessing, limiting their applicability to real‑world streaming data. Causal‑TS addresses these limitations by offering scalable algorithms that operate directly on raw, irregularly changing data.

## Implications  
For researchers, Causal‑TS provides a practical toolkit to extract causal relationships from noisy, high‑dimensional time series without sacrificing performance. In industry, it enables automated detection of causal drivers in operational logs and market trends, supporting data‑driven decision making and regulatory compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24673v1)
