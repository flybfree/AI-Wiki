---
title: Scalable Clinical Data Infrastructure and Comparative ML Evaluation for Hospitalisation Risk Prediction in Elderly Patients with Multiple Long-Term Conditions using CPRD
published: 2026-08-29T19:55:03Z
authors: Asra Aslam, Volodymyr Chapman, Maurice M. O'Connell, Aseel S. Abuzour, Michael Abaho, Danushka Bollegala, Gary Leeming, Eduard Shantsila, Andrew Clegg, Lauren E. Walker, Iain Edward Buchan, Samuel D. Relton
url: http://arxiv.org/abs/2608.29419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable Clinical Data Infrastructure and Comparative ML Evaluation for Hospitalisation Risk Prediction in Elderly Patients with Multiple Long-Term Conditions using CPRD

## Abstract
Deep learning architectures are increasingly proposed for patient trajectory modeling in electronic health records (EHRs), yet their advantage over simpler, more interpretable models is rarely subjected to rigorous empirical scrutiny in real-world clinical settings. We present a comprehensive patient timeline pipeline applied to elderly patients in CPRD Aurum, incorporating 260 clinical conditions classified via a three-tier automated framework including specialised detection logic for 17 complex conditions. Using this infrastructure, we benchmark Temporal Graph Convolutional Neural Networks (TG-CNN) against Logistic Regression with LASSO regularisation and Random Forests for predicting 12-month all-cause emergency hospitalisation risk, motivated by (but not filtered to) the elevated risk of adverse drug reactions. Under cross-validation, TG-CNN achieves a marginally higher mean AUC-ROC than LASSO (0.712 vs. 0.705), whereas on the held-out test set LASSO achieves the highest discrimination of three models (AUC-ROC 0.733, versus 0.710 for Random Forest and 0.702 for TG-CNN). We show, that discrimination alone is an incomplete criterion for clinical deployment: after Platt calibration, LASSO is the only model with an acceptable calibration slope (0.817), while Random Forest (0.759) and, TG-CNN (0.391) remain substantially miscalibrated. We argue that LASSO, not the highest-discriminating model, is the model best suited to direct clinical deployment. We present lessons for the machine learning and healthcare community regarding data infrastructure, model selection, and value of calibration and interpretability in high-stakes decision support.

## Metadata
- **Published**: 2026-08-29T19:55:03Z
- **Authors**: Asra Aslam, Volodymyr Chapman, Maurice M. O'Connell, Aseel S. Abuzour, Michael Abaho, Danushka Bollegala, Gary Leeming, Eduard Shantsila, Andrew Clegg, Lauren E. Walker, Iain Edward Buchan, Samuel D. Relton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29419v1)