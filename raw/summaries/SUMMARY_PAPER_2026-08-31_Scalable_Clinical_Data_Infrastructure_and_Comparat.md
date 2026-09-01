---
title: Scalable Clinical Data Infrastructure and Comparative ML Evaluation for Hospitalisation Risk Prediction in Elderly Patients with Multiple Long-Term Conditions using CPRD
url: http://arxiv.org/abs/2608.29419v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_19-55-03Z_ScalableClinicalDataInfrastructureandComparativeML.md
generated_at: 2026-08-31 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates deep learning and traditional machine‑learning models for predicting 12‑month emergency hospitalisation risk in elderly patients with multiple chronic conditions using a large electronic health record dataset. While the temporal graph convolutional neural network (TG‑CNN) shows higher mean AUC‑ROC, logistic regression with LASSO regularisation provides better calibration and is recommended for clinical deployment.

## Key Takeaways
- TG‑CNN achieves a marginally higher mean AUC‑ROC (0.712 vs 0.705) but lower test‑set discrimination (0.702) compared to LASSO (0.733).  
- Platt calibration reveals LASSO has an acceptable slope of 0.817, whereas Random Forest (0.759) and TG‑CNN (0.391) are markedly miscalibrated.  
- The highest‑discriminating model is not necessarily the best for clinical use; calibration and interpretability matter more.

## Context
Current AI research often prioritises predictive performance over real‑world applicability, leading to models that fail in clinical settings due to poor calibration. This study bridges that gap by applying rigorous cross‑validation and calibration assessment to a clinically relevant population.

## Implications
For healthcare practitioners, the findings underscore the need for model selection based on calibrated risk rather than raw discrimination. Practitioners should integrate robust data pipelines with clear interpretability criteria when deploying AI in high‑stakes decision support.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29419v1)
