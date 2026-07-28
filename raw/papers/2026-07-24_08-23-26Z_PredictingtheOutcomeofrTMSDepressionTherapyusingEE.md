---
title: Predicting the Outcome of rTMS Depression Therapy using EEG Signals and CNN
published: 2026-07-24T08:23:26Z
authors: Wael Korani, Md Fahimul Kabir Chowdhury, Sadam AlQadi, Priyan Malarvizhi kumar, Reza Rostami, Reza Kazemi
url: http://arxiv.org/abs/2607.22776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Predicting the Outcome of rTMS Depression Therapy using EEG Signals and CNN

## Abstract
Repetitive transcranial magnetic stimulation (rTMS) is a non invasive therapy for Major Depressive Disorder (MDD). In this study, we generate images using two time frequency methods to represent EEG signals: Fourier-Bessel Series Expansion with Euclidean Distance (FBSE-ED) and Discrete Wavelet Transform (DWT). We propose an efficient deep learning classifier to predict the outcome of rTMS depression therapy. In this study, we use a private rTMS databases to train a lightweight custom Convolutional Neural Network (CNN) using 10-fold cross validation strategy in order to avoid any bias in our results. The results show that the FBSE-ED representation achieves the highest classification accuracy of 93.60\%, outperforming traditional time-frequency technique (DWT). In addition, the proposed architecture with FBSE-ED image representation technique outperforms more complex EEG-Specific deep learning models (EEGNet, DeepConvNet, SleepEEGNet) by 3.62-10.72% and pretrained models (Xception, DenseNet201, and MobileNetV2) by 23.03-27.35%. For more experiments, we utilize another private rTMS database as test database to show the robustness of the proposed model. Our results suggest that integrating advanced signal decomposition with deep learning can facilitate early prediction of rTMS treatment response and support more targeted clinical decision-making. The proposed framework is interpretable, computationally efficient, and well-suited for deployment in real-world local psychiatric clinics.

## Metadata
- **Published**: 2026-07-24T08:23:26Z
- **Authors**: Wael Korani, Md Fahimul Kabir Chowdhury, Sadam AlQadi, Priyan Malarvizhi kumar, Reza Rostami, Reza Kazemi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22776v1)