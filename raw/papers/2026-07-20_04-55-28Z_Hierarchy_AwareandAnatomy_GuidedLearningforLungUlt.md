---
title: Hierarchy-Aware and Anatomy-Guided Learning for Lung Ultrasound Video Classification
published: 2026-07-20T04:55:28Z
authors: Alya Almsouti, Lotfi Mecharbat, Noha Aboukhater, Yousef Alabrach, Siddiq Anwar, Andre Kumar, Ibrahim Almakky, Mohammad Yaqub
url: http://arxiv.org/abs/2607.17551v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchy-Aware and Anatomy-Guided Learning for Lung Ultrasound Video Classification

## Abstract
Lung ultrasound (LUS) is a bedside tool for assessing pulmonary edema in patients at risk due to heart failure or impaired kidney function. However, automated LUS analysis remains challenging because of speckle noise, imaging artifacts, and operator-dependent acquisition variability. In this work, we present a deep learning framework for multi-class LUS video classification that explores two components: hierarchy-aware training, and anatomy-guided learning. Starting from a strong baseline, we introduce hierarchical training strategies and then introduce pleural line mask supervision to guide model attention toward anatomically relevant regions. We study four clinically relevant classes--healthy, B-lines, consolidations, and mixed B-lines with consolidations--using an open-access dataset of 1,886 videos from 219 patients, evaluated with patient-level five-fold cross-validation. Results show that hierarchy-aware training improves pathological separation relative to flat classification, while mask-guided attention supervision achieves the highest mean macro-F1 of 65.7\% and produces more localized attention patterns. Transfer experiments on the external COVID-BLUeS dataset further show competitive and parameter-efficient adaptation while preserving pleural-focused attention behavior. These findings suggest that combining clinically structured objectives with anatomy-guided supervision is a practical approach to robust, interpretable LUS video analysis. Code and model implementations are available at https://github.com/Alya-Almsouti/LUS-video-classification.

## Metadata
- **Published**: 2026-07-20T04:55:28Z
- **Authors**: Alya Almsouti, Lotfi Mecharbat, Noha Aboukhater, Yousef Alabrach, Siddiq Anwar, Andre Kumar, Ibrahim Almakky, Mohammad Yaqub
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17551v1)