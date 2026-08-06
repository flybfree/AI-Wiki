---
title: MINT: Tensor Decomposition on Stacked Recurrence Matrices for Time Series Data Mining
url: http://arxiv.org/abs/2608.04157v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-04_19-11-33Z_MINT_TensorDecompositiononStackedRecurrenceMatrice.md
generated_at: 2026-08-06 00:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MINT, a tensor‑based approach for mining co‑clustered patterns in univariate and multivariate time series using self‑similarity matrices derived from recurrence plots. By constructing dot plots of size N×(n−m+1)³ and applying tensor decomposition, the method identifies regular motifs across multiple sensors or series. Experiments on rapid transit, electricity demand, wind turbine output, and car traffic data show that MINT effectively captures cross‑sensor co‑clusters.

## Key Takeaways
- The method builds a three‑dimensional dot plot from N time series of length n with window m, producing a tensor of shape N×(n−m+1)³ for decomposition. 
- Tensor decomposition is used to mine co‑clustered patterns that appear simultaneously across the N series, revealing regular motifs at fixed intervals. 
- The pipeline demonstrates strong performance on diverse real‑world datasets including mass rapid transit, electricity demand, wind turbine data, and car traffic.

## Context
Time series mining often relies on pairwise similarity measures such as recurrence plots, which limit analysis to two dimensions and struggle with higher‑dimensional patterns. Tensor methods extend this capability by handling multi‑series structures simultaneously, aligning with advances in tensor factorization and deep learning for structured data.

## Implications
MINT provides a scalable framework that can be integrated into automated anomaly detection pipelines where regular sensor patterns need co‑clustering. Practitioners can leverage the method to uncover hidden periodicities across heterogeneous time series without manual feature engineering, accelerating insight generation in domains like energy management and transportation planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04157v1)
