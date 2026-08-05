---
title: FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection
published: 2026-08-04T12:48:05Z
authors: Amirhossein Taleshinosrati, Yangyang Wang, Atitaya Phoemsuk, Vahid Abolghasemi, Naser Hossein Motlagh, Sadasivan Puthusserypady, Daniel Teichmann, Abdolrahman Peimankar
url: http://arxiv.org/abs/2608.03597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection

## Abstract
Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and is associated with increased risks of stroke, heart failure, and mortality. Recent ECG foundation models offer transferable representations for automated AF detection. However, their relative effectiveness remains unclear because existing studies use different datasets, preprocessing procedures, classifiers, and validation protocols. This study presents FOUND-AF, a unified, leakage-controlled, and deployment-oriented benchmarking framework that evaluates the quality of pretrained ECG representations under identical experimental conditions. Nine publicly available foundation models from five families, including HuBERT-ECG, CLEF, ST-MEM, ECG-JEPA, and ECGFounder, were evaluated across four heterogeneous ECG datasets, namely AFDB, CinC2017, CPSC2021, and LTAFDB. All models were used as frozen feature extractors with standardized preprocessing, model-native resampling, a fixed XGBoost classifier, and recording-level grouped cross-validation. The evaluation included classification metrics, receiver operating characteristic analysis, paired recording-level bootstrap comparisons with Holm correction, embedding-space visualization, and computational efficiency profiling. The ECGFounder model consistently achieved the strongest overall performance across datasets while offering a favorable trade-off between accuracy, model size, inference time, and memory usage. FOUND-AF therefore provides a reproducible framework for selecting ECG foundation models and demonstrates that compact, clinically pretrained encoders can support robust and computationally efficient AF detection across heterogeneous acquisition settings.

## Metadata
- **Published**: 2026-08-04T12:48:05Z
- **Authors**: Amirhossein Taleshinosrati, Yangyang Wang, Atitaya Phoemsuk, Vahid Abolghasemi, Naser Hossein Motlagh, Sadasivan Puthusserypady, Daniel Teichmann, Abdolrahman Peimankar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03597v1)