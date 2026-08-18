---
title: Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine
published: 2026-08-17T10:32:38Z
authors: Marta Sumyk, Oleksandr Kosovan, Iryna Voitsitska
url: http://arxiv.org/abs/2608.16380v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine

## Abstract
Monitoring war-induced damage to agricultural land in Ukraine is important for understanding threats to food security, environmental stability, and post-war recovery. However, the development of computer-vision systems for satellite-based damage analysis is limited by the scarcity of labeled imagery, especially for damaged agricultural fields. This work investigates synthetic data augmentation as a method for improving classification under limited and imbalanced training data. We train class-conditional Generative Adversarial Network (GAN) and Denoising Diffusion Probabilistic Model (DDPM) architectures on real satellite images and use them to generate additional bombed and not-bombed agricultural-field samples. The generated images are used only for training augmentation, while all downstream evaluation is performed on an exclusively real test set. A Vision Transformer classifier is trained under multiple real and synthetic data configurations to measure the practical utility of each generative approach. The best configuration, based on balanced DDPM augmentation, improves accuracy from 84\% to 88\%, balanced accuracy from 67\% to 81\%, macro F1 from 65\% to 78\%, and recall for the underrepresented not-bombed class from 41\% to 69\%. These results demonstrate the potential of synthetic satellite imagery for data-scarce geospatial applications in war-affected regions.

## Metadata
- **Published**: 2026-08-17T10:32:38Z
- **Authors**: Marta Sumyk, Oleksandr Kosovan, Iryna Voitsitska
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16380v1)