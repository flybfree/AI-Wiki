---
title: TREA-Net: A Transferable Residual Epidemiological Adaptation Network for Dengue Incidence Forecasting
published: 2026-07-29T12:37:19Z
authors: Inesh Shukla, Madhurima Panja, Tanujit Chakraborty, Chittaranjan Hens
url: http://arxiv.org/abs/2607.26854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TREA-Net: A Transferable Residual Epidemiological Adaptation Network for Dengue Incidence Forecasting

## Abstract
Accurate multi-week dengue forecasting supports timely vector-control interventions, outbreak preparedness, and healthcare resource allocation. However, newly established surveillance systems often lack the historical data needed to train reliable neural forecasting models. Although pretrained time-series models offer promising zero-shot forecasts, their cross-domain training may not capture local epidemiological dynamics. We propose TREA-Net, a Transferable Residual Epidemiological Adaptation Network for dengue forecasting under limited data. TREA-Net augments neural forecasting backbones with projections from an Environmental Time-Series Susceptible-Infected-Recovered model and learns a lightweight gated residual correction transferable from data-rich to data-scarce regions. Its node-invariant design accommodates surveillance systems with different numbers of locations, while target adaptation requires learning only two global parameters. We transfer knowledge from long-running dengue surveillance in Colombia and Nicaragua to 8-week-ahead forecasting in Mexico and Malaysia using only 78 or 104 weeks of target data. Across five neural backbones and ten transfer settings, TREA-Net improves the corresponding backbone in 9 out of 10 settings, with statistically significant gains. When integrated with TiRex, a foundation model for forecasting, it achieves the lowest mean absolute error across all target datasets. Conformal prediction further maintains empirical coverage while reducing 8-week prediction-interval width by 29.6% in Mexico. These results demonstrate TREA-Net's potential as a lightweight and portable early-warning framework for health agencies with limited surveillance data.

## Metadata
- **Published**: 2026-07-29T12:37:19Z
- **Authors**: Inesh Shukla, Madhurima Panja, Tanujit Chakraborty, Chittaranjan Hens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26854v1)