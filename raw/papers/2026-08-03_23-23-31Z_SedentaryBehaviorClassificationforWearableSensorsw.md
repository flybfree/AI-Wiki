---
title: Sedentary Behavior Classification for Wearable Sensors with a CNN-BiLSTM Model
published: 2026-08-03T23:23:31Z
authors: Yuliang Chen, Weiwei Shi, Jingjing Zou, Rong Zablocki, Animesh Kumar, Jordan A. Carlson, Sheri J. Hartman, Mikael Anne Greenwood-Hickman, Paul R. Hibbing, Marta Jankowska, Jay Yang, Arun Kumar, Loki Natarajan
url: http://arxiv.org/abs/2608.02946v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sedentary Behavior Classification for Wearable Sensors with a CNN-BiLSTM Model

## Abstract
Accurate detection of sedentary behavior is important for studying health risks related to prolonged sitting, but posture-based classification remains challenging with wearable sensors, especially at the wrist. We study whether a deep learning model trained on hip-worn accelerometer data can transfer to wrist-worn accelerometer data for sitting versus non-sitting classification. We use CHAP, a CNN-BiLSTM model originally developed for hip accelerometers, and evaluate its zero-shot performance on wrist data as well as its adaptation through finetuning with varying amounts of labeled wrist data. Experiments are conducted on the iWatch dataset with ground-truth posture labels derived from wearable cameras. The hip-trained model performs strongly on hip data without retraining, but accuracy drops on wrist data due to sensor placement shift. Finetuning CHAP provides consistent advantages over transformer models trained from scratch. These findings suggest that hip-based pretraining provides a useful starting point for wrist deployment, while highlighting the need for wrist-specific adaptation to handle higher signal variability.

## Metadata
- **Published**: 2026-08-03T23:23:31Z
- **Authors**: Yuliang Chen, Weiwei Shi, Jingjing Zou, Rong Zablocki, Animesh Kumar, Jordan A. Carlson, Sheri J. Hartman, Mikael Anne Greenwood-Hickman, Paul R. Hibbing, Marta Jankowska, Jay Yang, Arun Kumar, Loki Natarajan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02946v1)