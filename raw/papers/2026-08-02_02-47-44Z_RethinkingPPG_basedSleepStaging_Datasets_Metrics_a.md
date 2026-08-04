---
title: Rethinking PPG-based Sleep Staging: Datasets, Metrics, and Benchmarks
published: 2026-08-02T02:47:44Z
authors: Shuntian Zheng, Jiawei Wang, Cong Fu, Huan Yu, Chen Chen, Yu Guan, Sai Gu
url: http://arxiv.org/abs/2608.00943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking PPG-based Sleep Staging: Datasets, Metrics, and Benchmarks

## Abstract
Automated sleep staging assigns discrete stage labels to successive time epochs throughout an overnight recording; conventionally each window spans at least 30 seconds, reflecting the minimum temporal resolution of the clinical scoring standard. Wearable photoplethysmography (PPG) has attracted sustained interest as an ambulatory alternative to laboratory-based polysomnography, which relies on electroencephalography (EEG) and other recording modalities that are impractical outside clinical environments. Yet PPG-based staging trails EEG-based methods by a substantial margin, and we argue this gap largely reflects a mismatch between signal and task. Within a stable stage, PPG's inter-stage feature differences are more subtle than those in EEG; yet at stage boundaries, PPG's principal cardiovascular features, heart rate variability and pulse morphology, shift sharply within seconds. The conventional practice of assigning one label to each 30-second epoch therefore suppresses feature that is concentrated near boundaries. We address this gap in two steps. First, we develop a label expansion pipeline based on Hidden Semi-Markov Models that converts coarse epoch labels into sec-level annotations. To assess whether these expanded labels are reliable enough for downstream supervision, we validate them on a separate expert-reviewed dataset and through an auxiliary sleep-wake task whose labels are independent of the expansion pipeline. Second, we use the resulting sec-level supervision on MESA to improve conventional four-class epoch-level staging across four architecturally diverse baselines by 3.7--5.7\,pp in accuracy against the original epoch labels, with supplementary zero-shot evaluation on CFS showing that the transfer benefit persists under cohort and annotation-protocol shift.

## Metadata
- **Published**: 2026-08-02T02:47:44Z
- **Authors**: Shuntian Zheng, Jiawei Wang, Cong Fu, Huan Yu, Chen Chen, Yu Guan, Sai Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00943v1)