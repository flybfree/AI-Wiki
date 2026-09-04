---
title: A Two-Stage Forecasting System for CPU Workload Prediction in Private Clouds
url: http://arxiv.org/abs/2609.03457v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-15-44Z_ATwo_StageForecastingSystemforCPUWorkloadPredictio.md
generated_at: 2026-09-03 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a two‑stage forecasting system that predicts CPU workload in private clouds by first estimating customer service requests (TPS) and then deriving CPU usage from those forecasts. The model uses XGBoost within a cascaded architecture with adaptive online retraining, achieving Symmetric Mean Absolute Percentage Error below 7 % across ten applications and an R² of 0.9185 for the best case.

## Key Takeaways
- The two‑stage approach separates service demand forecasting from CPU prediction, capturing the dependency that conventional direct methods miss.
- Adaptive online retraining with expanding windows mitigates concept drift, preserving forecast stability over a 60‑step horizon while keeping error accumulation controlled.
- Experimental results show SMAPE under 7 % and an MAE of 0.7372 for top applications, outperforming baseline direct CPU forecasting.

## Context
Accurate resource prediction is a core challenge in cloud computing where workloads evolve rapidly. Machine‑learning models like XGBoost are widely used for time‑series tasks, but their performance degrades when underlying data distributions shift. This work demonstrates how cascaded learning and online retraining can improve both accuracy and adaptability.

## Implications
Practitioners can leverage this two‑stage framework to automate proactive resource provisioning, reducing costs and maintaining QoS in private clouds. The method’s interpretability and computational efficiency make it suitable for integration into existing auto‑scaling pipelines across cloud environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03457v1)
