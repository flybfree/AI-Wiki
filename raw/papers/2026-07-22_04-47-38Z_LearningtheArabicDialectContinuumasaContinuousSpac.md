---
title: Learning the Arabic Dialect Continuum as a Continuous Space: A Regression Approach to Speaker Origin Prediction
published: 2026-07-22T04:47:38Z
authors: Mohamed Aziz Khadraoui, Adel Ammar, Bilel Benjdira, Zahid Khan, Skander Turki, Wadii Boulila
url: http://arxiv.org/abs/2607.19751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning the Arabic Dialect Continuum as a Continuous Space: A Regression Approach to Speaker Origin Prediction

## Abstract
We present a regression-based approach to Arabic dialect geolocation that models dialectal variation as a continuous geographic space rather than discrete categories. Speaker origin is predicted as continuous latitude-longitude coordinates using a hierarchical neural architecture that fuses frame-level XLS-R-300M and Whisper-large-v3 encoder representations with phonotactic descriptors through a Transformer encoder and a learnable attention-pooled query. A spherical geodesic loss directly optimizes great-circle distance on Earth's surface, avoiding distortions inherent to planar coordinate regression. Under a leakage-free 5-fold GroupKFold protocol grouped by source recording, our model attains a pooled median localization error of 481.2 km. Auxiliary country and city heads reach 64.5% and 45.2% accuracy, respectively. A permutation Mantel test on the learned latent space provides quantitative support for the Arabic dialect continuum hypothesis. To probe true generalization, we further introduce a city-masking protocol in which two cities per fold are removed from training but retained in validation. Under this zero-shot regime, the mean error rises to 1173.3 km, a 1.32x degradation relative to seen cities. Our findings establish continuous geographic modeling as a principled framework for Arabic dialect geolocation and quantify both its strengths and the substantial headroom that remains.

## Metadata
- **Published**: 2026-07-22T04:47:38Z
- **Authors**: Mohamed Aziz Khadraoui, Adel Ammar, Bilel Benjdira, Zahid Khan, Skander Turki, Wadii Boulila
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19751v1)