---
title: FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity
url: http://arxiv.org/abs/2608.07393v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_16-37-30Z_FedDOSE_FederatedLearningFrameworkDecomposingSiteE.md
generated_at: 2026-08-09 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FedDOSE, a federated learning framework designed to decompose site‑specific effects when analyzing dynamic functional connectivity (dFC) from multi‑site fMRI data. By integrating a modularity‑guided Tucker decomposition and aligning class prototypes across sites with optimal transport and Procrustes methods, FedDOSE learns robust representations that outperform existing approaches in diagnosing autism spectrum disorder and attention‑deficit hyperactivity disorder on three large resting‑state datasets.

## Key Takeaways
- Site heterogeneity is explicitly modeled through a modularity‑guided Tucker decomposition, capturing high‑dimensional dFC tensors at the spatial level.  
- Class prototypes generated per site are globally aligned using an optimal transport barycenter and Procrustes analysis, reducing variance between sites.  
- Experiments on ABIDE‑I, ABIDE‑II, and ADHD‑200 demonstrate that FedDOSE achieves superior diagnostic performance compared with state‑of‑the‑art methods.

## Context
Federated learning enables collaborative training without sharing raw data, a crucial advantage for sensitive medical imaging. Dynamic functional connectivity adds temporal complexity to fMRI analyses, yet most FL pipelines treat connectivity as static and ignore site differences. This work bridges these gaps by providing a method that handles both dynamic patterns and multi‑site variability.

## Implications
The findings suggest that federated frameworks can deliver reliable neuroimaging insights across diverse clinical sites, supporting personalized diagnostics in mental health research. Practitioners may adopt FedDOSE to improve model robustness and reduce false positives/negatives when integrating data from multiple hospitals or cohorts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07393v1)
