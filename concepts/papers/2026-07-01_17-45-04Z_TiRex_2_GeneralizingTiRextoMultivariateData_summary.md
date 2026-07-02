# Summary: 2026-07-01_17-45-04Z_TiRex_2_GeneralizingTiRextoMultivariateDataandStre.md
Saved: 2026-07-01 23:00
Source: 2026-07-01_17-45-04Z_TiRex_2_GeneralizingTiRextoMultivariateDataandStre.md
Model: None

---


## Summary  
TiRex-2 is a recurrent xLSTM‑based foundation model that extends the univariate TiRex architecture to multivariate forecasting under streaming conditions, allowing integration of future‑known covariates while preserving strict causality over target variables. It achieves constant per‑patch inference cost and state‑of‑the‑art zero‑shot performance on benchmark datasets such as GIFT‑Eval and fev‑bench. The model leverages 38.4 M active parameters in univariate mode, scaling to an additional 44.1 M for multivariate tasks.

## Key Contributions  
- Introduces a memory‑centric recurrent xLSTM architecture that processes streaming data with constant per‑patch cost.  
- Combines a bidirectional time mixer and an asymmetric grouped‑attention variate mixer to integrate future‑known covariates while maintaining strict causality over target variables.  
- Proposes a synthetic coupling pipeline for scalable multivariate pretraining from large univariate corpora.

## Methodology  
The authors address the limitations of Transformer‑based models by designing TiRex‑2 as a recurrent system that can handle variable‑length streams without recomputing full histories. They employ a bidirectional time mixer to capture past target dependencies and an asymmetric grouped‑attention variate mixer to incorporate future covariates without violating causality. Pretraining is performed via synthetic coupling, generating multivariate samples on the fly from univariate datasets.

## Results  
On GIFT‑Eval and fev‑bench, TiRex‑2 attains state‑of‑the‑art zero‑shot performance across all tasks. It remains stable under streaming with arbitrary context lengths and maintains constant inference cost per patch. The model uses 38.4 M active parameters in univariate mode, scaling to an additional 44.1 M for multivariate forecasting.

## Significance  
This work provides the first time‑series foundation model that simultaneously supports multivariate forecasting, future covariates, streaming operation, and constant per‑patch cost, enabling efficient deployment of complex forecasts in real‑time systems.

## Related Concepts  
- xLSTM  
- Streaming data processing  
- Causal modeling  
- Grouped attention  
- Synthetic coupling  
- Zero‑shot performance
