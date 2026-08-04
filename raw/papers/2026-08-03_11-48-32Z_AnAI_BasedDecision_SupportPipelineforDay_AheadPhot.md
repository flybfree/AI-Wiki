---
title: An AI-Based Decision-Support Pipeline for Day-Ahead Photovoltaic Forecasting
published: 2026-08-03T11:48:32Z
authors: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier, Masood Nazari
url: http://arxiv.org/abs/2608.02088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An AI-Based Decision-Support Pipeline for Day-Ahead Photovoltaic Forecasting

## Abstract
Reliable photovoltaic (PV) forecasts are needed for low-carbon energy systems, but newly deployed sites often have short, imperfect records. This makes standard day-ahead forecasting difficult: persistence and physical baselines can be sensitive to calibration and timestamp alignment, while single machine-learning models may capture only one structure in the data and overstate skill under non-temporal validation. We study this problem at a United Kingdom charging-station site, where PV forecast errors affect charging availability, storage scheduling, and downstream control. Using measured inverter output and publicly available meteorological inputs, we develop a deployment-oriented environmental-AI pipeline for day-ahead hourly PV forecasting. The pipeline corrects timestamp conventions, constructs leakage-safe solar-geometry and clearness-index features, adds short-term atmospheric context, and combines complementary predictors through validation-learned stacking. Against smart persistence, a clear-sky baseline that adjusts recent PV output using expected clear-sky irradiance, the best ensemble reduces daylight normalised RMSE by about 32% under random day-blocked evaluation and 9% under the stricter rolling-origin protocol. It also reduces daylight RMSE relative to the strongest individual machine-learning baseline by 6.6% and 6.4%, respectively. The results show that physics-aware stacking can support PV forecasts from limited site data, but its value depends on model class, evaluation protocol, and deployment context.

## Metadata
- **Published**: 2026-08-03T11:48:32Z
- **Authors**: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier, Masood Nazari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02088v1)