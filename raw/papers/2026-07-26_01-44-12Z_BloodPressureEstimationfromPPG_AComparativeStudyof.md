---
title: Blood Pressure Estimation from PPG: A Comparative Study of Direct and ECG-Mediated Deep Learning Pipelines
published: 2026-07-26T01:44:12Z
authors: Bo Wu, Haoling Wang, Zhuodiao Kuang, Kateryna Shapovalenko
url: http://arxiv.org/abs/2607.23406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Blood Pressure Estimation from PPG: A Comparative Study of Direct and ECG-Mediated Deep Learning Pipelines

## Abstract
Continuous cuffless blood pressure (BP) monitoring is essential for connected health systems and wearable devices, enabling early detection, longitudinal tracking, and personalized management of cardiovascular disease. Many prior approaches attempt to estimate BP indirectly by reconstructing electrocardiography (ECG) from photoplethysmography (PPG), assuming ECG provides a stronger physiological link to BP. However, ECG sensing is less accessible in wearable settings and may introduce unnecessary complexity.   In this work, we first perform a large-scale physiological correlation analysis on the MIMIC-III waveform database, revealing that PPG exhibits substantially stronger coupling with arterial blood pressure (ABP) ($|r|=0.247$, $p<0.001$) than ECG does ($r=0.018$, $p=0.187$), challenging the assumption that ECG provides a superior intermediate representation. Motivated by this insight, we conduct a systematic comparison between direct PPG-to-BP prediction and ECG-mediated pipelines using multiple state-of-the-art deep learning models.   Across 1.74M segments from 3,127 patients, direct PPG-to-BP prediction achieves British Hypertension Society Grade A performance ($\mathrm{MAE}_{\mathrm{SBP}} = 4.82 mmHg$, $\mathrm{MAE}_{\mathrm{DBP}} = 4.31 mmHg$), outperforming all ECG-mediated approaches, which achieve only Grade B accuracy.   Our findings suggest that accurate continuous BP monitoring can be achieved directly from wearable PPG signals, enabling simpler, more efficient pipelines for real-world connected health systems.

## Metadata
- **Published**: 2026-07-26T01:44:12Z
- **Authors**: Bo Wu, Haoling Wang, Zhuodiao Kuang, Kateryna Shapovalenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23406v1)