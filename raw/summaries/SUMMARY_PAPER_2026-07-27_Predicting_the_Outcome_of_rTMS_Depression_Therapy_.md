---
title: Predicting the Outcome of rTMS Depression Therapy using EEG Signals and CNN
url: http://arxiv.org/abs/2607.22776v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_08-23-26Z_PredictingtheOutcomeofrTMSDepressionTherapyusingEE.md
generated_at: 2026-07-27 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper aims to predict rTMS depression therapy outcomes using EEG signals and a convolutional neural network. It compares two time‑frequency representations—Fourier‑Bessel Series Expansion with Euclidean Distance and Discrete Wavelet Transform—and shows the FBSE‑ED method yields 93.60% accuracy, beating DWT and outperforming several deep learning models. The study also validates the model on an independent private rTMS database, confirming robustness across datasets.

## Key Takeaways
- The FBSE‑ED representation achieves 93.60% classification accuracy, surpassing the traditional DWT method and demonstrating superior performance in distinguishing treatment response.
- The proposed CNN architecture with FBSE‑ED outperforms several deep learning models (EEGNet, DeepConvNet, SleepEEGNet) by 3.62–10.72%, indicating a significant advantage over existing EEG‑specific networks.
- The model also exceeds performance on pretrained architectures such as Xception, DenseNet201, and MobileNetV2 by 23.03–27.35%, highlighting the benefit of using a custom representation.

## Context
In AI for medical imaging, combining signal decomposition with neural networks is a growing trend to improve interpretability and efficiency. This work demonstrates that lightweight CNN can achieve state‑of‑the‑art performance on EEG data. The integration of advanced signal decomposition with deep learning aligns with efforts to create interpretable AI tools for clinical decision support.

## Implications
Clinicians could use this model to decide early treatment response, reducing unnecessary sessions. The approach’s low computational cost makes it feasible for local clinics without large infrastructure. Future work could explore real‑time deployment and regulatory pathways for such predictive models in mental health care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22776v1)
