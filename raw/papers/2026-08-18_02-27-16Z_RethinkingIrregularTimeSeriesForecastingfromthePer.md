---
title: Rethinking Irregular Time Series Forecasting from the Perspective of Basis Functions
published: 2026-08-18T02:27:16Z
authors: Rongwen Li, Changjian Chen
url: http://arxiv.org/abs/2608.17284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Irregular Time Series Forecasting from the Perspective of Basis Functions

## Abstract
Irregular time series forecasting is crucial in many domains, such as healthcare and meteorological observation. However, due to the inherent characteristics of irregular time series, including sparse observations and non-uniform sampling, accurately predicting future dynamics remains challenging. In light of these two characteristics, many existing methods aggregate irregular observations into fixed-dimensional estimated response coefficients through predefined basis functions and use these coefficients as sequence representations. Nevertheless, this modeling paradigm still suffers from two key limitations: (i) a potential non-vanishing asymptotic bias caused by ignoring the sampling density of timestamps; and (ii) the limited adaptability of predefined basis functions to diverse temporal patterns. In this study, we propose a Debiased Neural Basis-Function Network (DNBNet) to address these challenges. Its core is a debiased neural basis-function response mechanism, which corrects asymptotic bias through importance sampling while parameterizing basis functions with neural networks to adapt to diverse temporal patterns. In addition, considering the sparsity of irregular data, we design a novel multi-scale decomposition module based on average pooling, together with a mass-aware fusion mechanism, to obtain richer representations. Finally, a dual-branch decoder is employed for forecasting. Extensive experiments on multiple real-world datasets demonstrate the effectiveness of DNBNet and its strong generalizability across diverse irregular time series scenarios. Our code can be obtained at https://github.com/hnu-vis/DNBNet.

## Metadata
- **Published**: 2026-08-18T02:27:16Z
- **Authors**: Rongwen Li, Changjian Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17284v1)