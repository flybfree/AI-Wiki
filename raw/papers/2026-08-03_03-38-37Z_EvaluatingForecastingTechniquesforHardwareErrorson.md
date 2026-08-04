---
title: Evaluating Forecasting Techniques for Hardware Errors on a Large-scale HPC System
published: 2026-08-03T03:38:37Z
authors: Kaiyuan Liao, Xiwei Xuan, Tanwi Mallick, Kevin Brown, Christopher D. Carothers, Kwan-Liu Ma
url: http://arxiv.org/abs/2608.01648v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Forecasting Techniques for Hardware Errors on a Large-scale HPC System

## Abstract
Hardware error logs in high-performance computing (HPC) systems provide early signals of abnormal behavior, yet there remain challenges in effectively forecasting these errors using modern predictive methods. This work investigates the boundaries of applying time series forecasting to HPC hardware error dynamics. We use seven years of production logs from the Theta supercomputer to evaluate the predictive efficacy of classical statistical and deep learning models. Our results show that forecasting effectiveness depends strongly on the temporal structure of the error series: regularly occurring and structurally stable errors can be modeled accurately, particularly by LSTM and Transformer architectures with temporal features, while sparse and burst-dominated errors remain difficult to predict. Rather than proposing a deployment-ready failure prediction framework, this study provides empirical guidance on when forecasting is effective and highlights potential directions for improving forecasting accuracy in HPC hardware error analysis.

## Metadata
- **Published**: 2026-08-03T03:38:37Z
- **Authors**: Kaiyuan Liao, Xiwei Xuan, Tanwi Mallick, Kevin Brown, Christopher D. Carothers, Kwan-Liu Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01648v1)