---
title: Gaussian Meta-Space Augmentation for Stacking Ensembles in Multimodal IPMN Risk Stratification
published: 2026-08-11T22:17:32Z
authors: Max A. Nelson, Eminenur Sen Tasci, Zhixiang Wang, Zongwei Zhou, Halil Ertugrul Aktas, Andrea M. Bejar, Elif Keles, Ziliang Hong, Sıtkı Safa Taflan, Muhammed Enes Tasci, Frank H. Miller, Michael B. Wallace, Rajesh N. Keswani, Gorkem Durak, Ulas Bagci
url: http://arxiv.org/abs/2608.11472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gaussian Meta-Space Augmentation for Stacking Ensembles in Multimodal IPMN Risk Stratification

## Abstract
Pancreatic cancer is among the most lethal malignancies; risk stratification of intraductal papillary mucinous neoplasms (IPMNs) offers a crucial opportunity for early intervention but typically requires invasive tissue biopsy. Dominant vision-based approaches, including radiomics and deep learning, provide promising but initially separate discrimination opportunities. Similarly, multisequence MRI (T1W/T2W) and anatomically decomposed (head, body and tail) analysis of the pancreas provide additional and potentially complementary signals. Effective fusion of this information is crucial in ordinal IPMN dysplasia risk prediction and can be accomplished via a meticulously regularized and calibrated ensemble stacking combiner. We present cUPMI, a class-conditional Gaussian augmentation of a combiner's log-probability meta-features, and test it on various prediction paradigms. In our multi-center analysis, we find cUPMI adds limited value to properly regularized L2-logistic binary classification stacks, but consistently regularizes higher-capacity tree combiners in the binary and radiomics-only setting (RF +0.015 and XGBoost +0.024 binary AUC, positive in all seeds). Its cleanest ordinal benefit appears for XGBoost on an 8-stream radiomics task (3-class no < low < high, +0.022 QWK in all seeds). Separately, fold-locked fusion of radiomics and 2.5D CNN streams yields the strongest overall model, an RF stack reaching QWK 0.595 (95% CI [0.54, 0.64]) and binary AUC 0.839, surpassing radiomics, 2.5D ResNet, and 3D DenseNet-121 baselines.

## Metadata
- **Published**: 2026-08-11T22:17:32Z
- **Authors**: Max A. Nelson, Eminenur Sen Tasci, Zhixiang Wang, Zongwei Zhou, Halil Ertugrul Aktas, Andrea M. Bejar, Elif Keles, Ziliang Hong, Sıtkı Safa Taflan, Muhammed Enes Tasci, Frank H. Miller, Michael B. Wallace, Rajesh N. Keswani, Gorkem Durak, Ulas Bagci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11472v1)