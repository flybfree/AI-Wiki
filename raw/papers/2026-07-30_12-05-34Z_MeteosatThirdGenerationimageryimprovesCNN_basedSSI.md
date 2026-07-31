---
title: Meteosat Third Generation imagery improves CNN-based SSI retrieval
published: 2026-07-30T12:05:34Z
authors: Gordei Pribõtkin, Piia Post, Velle Toll
url: http://arxiv.org/abs/2607.28093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meteosat Third Generation imagery improves CNN-based SSI retrieval

## Abstract
Accurate Surface Solar Irradiance (SSI) estimation is increasingly important for photovoltaic energy monitoring and forecasting. The recently introduced Meteosat Third Generation (MTG) satellite constellation provides imaging data with higher spatial resolution compared to the Meteosat Second Generation (MSG) satellite constellation, but its benefits for machine-learning-based SSI retrieval have not been well established. In this work, we introduce a multi-imager and multi-resolution convolutional neural network architecture for 10-minute SSI retrieval over Northern Europe (Estonia) using MSG/SEVIRI and MTG/FCI satellite imagery together with solar-geometry and clear-sky irradiance features. Model performance is evaluated against ground-based pyranometer measurements from eight Estonian meteorological stations using site-based cross-validation and multiple training seeds. Model performance is also compared with the SARAH-3 physics-based satellite SSI product. The hybrid SEVIRI-FCI model significantly outperformed the SEVIRI-only model under overcast and cloudy conditions, reducing RMSE by 8.2 W m$^{-2}$ and 5.7 W m$^{-2}$, respectively. However, under partly cloudy or clear skies, no statistically significant difference in RMSE was observed between the SEVIRI-FCI hybrid and the SEVIRI-only models. Compared with physics-based SARAH-3, the hybrid model yielded skill scores of 35 % under overcast conditions, 21 % under cloudy conditions, and 20 % overall. Furthermore, both models underperformed SARAH-3 in clear-sky conditions. These results show that higher-resolution MTG/FCI imagery improves CNN-based SSI retrieval when clouds dominate irradiance variability, but also indicate that higher spatial resolution alone is insufficient to address clear-sky limitations in machine-learning-based SSI retrieval.

## Metadata
- **Published**: 2026-07-30T12:05:34Z
- **Authors**: Gordei Pribõtkin, Piia Post, Velle Toll
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28093v1)