---
title: Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations
published: 2026-07-24T19:26:47Z
authors: Kazi Kamruzzaman Rabbi, Md. Zami Al Zunaed Farabe, M. Sohel Rahman
url: http://arxiv.org/abs/2607.22872v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations

## Abstract
Post-training quantization (PTQ) has become a practical solution for deploying deep learning models on resource-constrained edge devices by compressing high-precision floating-point weights into low-precision representations without requiring retraining. Past research has demonstrated that quantization largely preserves classification accuracy; however, whether it also preserves the model's internal reasoning remains an open question. This study presents a systematic evaluation on how static PTQ affects the interpretability / explainability of five widely used CNN architectures: VGG19, ResNet18, EfficientNet-B0, DenseNet161, and MobileNetV2 at INT8 and INT4 precision. We employ a dual interpretability framework that combines Grad-CAM for spatial attention analysis with LIME for input-level feature attribution, and systematically compare full-precision and quantized models on two binary classification datasets. Interpretability is evaluated using three complementary metrics: the Pearson correlation coefficient, structural similarity index, and top-20% IoU to capture distributional and structural variations in model explanations, supplemented by deletion/insertion faithfulness analysis. The results show that classification accuracy is not a reliable indicator of interpretability stability under reduced precision. DenseNet161 maintains strong feature consistency across both precision levels, whereas EfficientNet-B0, despite achieving competitive spatial attention and classification accuracy at INT8 precision, exhibits a substantial degradation in input-level feature attribution. These findings have direct implications for the trustworthy deployment of quantized models in applications with high interpretability requirements, demonstrating that architecture selection is as important as the quantization strategy.

## Metadata
- **Published**: 2026-07-24T19:26:47Z
- **Authors**: Kazi Kamruzzaman Rabbi, Md. Zami Al Zunaed Farabe, M. Sohel Rahman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22872v1)