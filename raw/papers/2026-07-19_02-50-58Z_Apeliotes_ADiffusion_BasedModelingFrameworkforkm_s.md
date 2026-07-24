---
title: Apeliotes: A Diffusion-Based Modeling Framework for km-scale Multi-Level Atmospheric Fields
published: 2026-07-19T02:50:58Z
authors: Evangelia Rafaela Frastali, Achyut Paudel, Maryam Golbazi, Frank Liu
url: http://arxiv.org/abs/2607.17037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Apeliotes: A Diffusion-Based Modeling Framework for km-scale Multi-Level Atmospheric Fields

## Abstract
High-resolution atmospheric data are required to resolve mesoscale and localized meteorological structures, however such datasets remain limited in many regions of the world. Existing high-resolution weather products are typically produced through dynamical downscaling, which is computationally expensive and difficult to scale across locations, variables, and forecast scenarios. These limitations motivate machine-learning-based downscaling systems that can generate multiple weather variables stochastically while producing new high-resolution fields directly. In this paper we present Apeliotes, a framework for high-resolution weather forecasting. Built on the global re-analysis atmospheric data, a pre-trained global weather foundation model, and a regionally trained generative diffusion model, Apeliotes not only provides accurate kilometer-scale weather variables, but also multi-level atmospheric fields which are not directly available in the existing global atmospheric data. Our comprehensive evaluation demonstrates that Apeliotes achieves highly competitive performance. The model predicts vertical wind profile with less than 3\% error between truth and predicted fields, achieving correlations of 0.91 for 10-m wind speed and 0.99 for 2-m temperature, with NRMSE values of 0.42 and 0.17, respectively.

## Metadata
- **Published**: 2026-07-19T02:50:58Z
- **Authors**: Evangelia Rafaela Frastali, Achyut Paudel, Maryam Golbazi, Frank Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17037v1)