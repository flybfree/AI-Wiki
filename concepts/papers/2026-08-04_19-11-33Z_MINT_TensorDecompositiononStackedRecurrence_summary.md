# Summary: 2026-08-04_19-11-33Z_MINT_TensorDecompositiononStackedRecurrenceMatrice.md
Saved: 2026-08-06 00:05
Source: 2026-08-04_19-11-33Z_MINT_TensorDecompositiononStackedRecurrenceMatrice.md
Model: None

---

## Summary  
The paper introduces MINT, a tensor‑based framework for mining co‑clustered patterns in time‑series data by extending the primitive of recurrence plots to multivariate and high‑dimensional datasets. It constructs dot‑plot tensors from stacked recurrence matrices and applies tensor decomposition techniques to uncover latent factors that represent regular motifs across multiple sensors or series simultaneously. The goal is to develop a scalable computational pipeline that can discover periodicities and cross‑sensor correlations more efficiently than traditional clustering methods. This work contributes a novel approach that leverages the algebraic structure of tensors for pattern mining in time‑series data.

## Key Contributions  
- Finding 1: A scalable tensorized self‑similarity matrix derived from stacked recurrence plots, enabling joint representation of multiple series.  
- Finding 2: An efficient Tucker decomposition algorithm applied to the N × (n‑m+1)³ tensor, extracting latent factors that correspond to periodic motifs.  
- Finding 3: Demonstrated co‑clustering of cross‑sensor patterns in real datasets (mass rapid transit, electricity demand, wind turbine output, car traffic), achieving higher clustering scores than baseline methods.

## Methodology  
The authors first compute dot‑plot tensors from univariate time series using a subsequence window of length m, producing an N × (n‑m+1)³ tensor where each slice is a pairwise similarity matrix. For multivariate data they extend the construction via Kronecker products, preserving the tensor structure while handling multiple sensors simultaneously. The decomposition step employs Tucker factorization to partition the tensor into three latent factors: one encoding temporal periodicity, another capturing inter‑series correlation, and the third representing residual noise. This pipeline is designed for both single‑ and multi‑dimensional series, with extensions that allow direct application to real‑world sensor networks.

## Results  
Experiments on four distinct datasets show that MINT identifies regular motifs at consistent intervals across sensors, producing co‑clustering scores significantly higher than independent clustering baselines (e.g., 0.78 vs. 0.62). The latent factors extracted by Tucker decomposition align closely with known periodicities such as daily peaks in electricity demand and hourly cycles in wind turbine output. The method reduces the dimensionality of motif extraction, enabling faster downstream analysis while preserving interpretability.

## Significance  
By treating time‑series data as tensors, MINT enables joint pattern discovery across heterogeneous sensor streams, which is especially valuable for domains requiring precise detection of regular patterns such as predictive maintenance and energy forecasting. The approach reduces computational complexity compared to sequential clustering, improves co‑clustering accuracy, and provides interpretable latent factors that can be directly linked to physical cycles.

## Related Concepts  
Recurrence plots, dot‑plot matrices, tensor decomposition (Tucker factorization), multivariate time series clustering, Kronecker product extensions.
