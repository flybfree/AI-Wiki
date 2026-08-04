---
title: From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy
published: 2026-08-01T11:56:50Z
authors: Viacheslav Barkov, Jonas Schmidinger, Robin Gebbers, Martin Atzmueller
url: http://arxiv.org/abs/2608.00608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy

## Abstract
Visible and near-infrared (vis-NIR) and mid-infrared (MIR) spectroscopy enable rapid, cost-effective prediction of soil properties. Yet, translating high-dimensional, highly collinear spectra into accurate soil property predictions remains challenging, particularly when employing machine learning. We systematically investigated regression models and dimensionality reduction approaches for spectroscopic modeling across 85 regression tasks from open benchmark datasets in pedometrics spanning field-scale digital soil mapping and a global soil spectral library. We compared an in-context learning tabular foundation model (TabPFN), a convolutional neural network (CNN), rule-based regression (Cubist), Random Forest, and partial least squares regression (PLSR) using full spectra as well as features derived from principal component analysis (PCA) and partial least squares (PLS) latent variables. TabPFN consistently delivered the best overall performance across scales, including large spectral library tasks with tens of thousands of soil samples. Notably, TabPFN applied directly to full spectra already surpassed all classical baselines, showing that explicit dimensionality reduction is not strictly required for strong performance. Further improvements were achieved through PLS, which proved to be an effective dimensionality reduction strategy for all models. Combining PLS latent variables with TabPFN yielded the best predictions overall. Our findings provide evidence-based guidance for spectroscopic calibration model selection across operational scales, demonstrating that the long-standing advantages of PLSR and modern tabular foundation models complement each other in chemometrics.

## Metadata
- **Published**: 2026-08-01T11:56:50Z
- **Authors**: Viacheslav Barkov, Jonas Schmidinger, Robin Gebbers, Martin Atzmueller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00608v1)