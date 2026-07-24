---
title: Deep Shape Regression for Planar Curves with Multimodal Covariates
published: 2026-07-21T22:04:17Z
authors: Manuel Pfeuffer, Roshan Prakash Rane, Hadya Yassin, Kerstin Ritter, Sonja Greven
url: http://arxiv.org/abs/2607.19600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep Shape Regression for Planar Curves with Multimodal Covariates

## Abstract
The shape of a planar curve is the geometric information that remains once translation, rotation, scale and reparametrisation are removed and is of interest in many health applications, e.g. in neuroimaging. We propose a deep shape regression model for open planar curves that admits multimodal and high-dimensional covariates. Representing curves as complex-valued functions, we show that the conditional full Procrustes mean is the leading eigenfunction of the conditional covariance. To estimate this covariance surface, we propose a novel deep conditional covariance smoother with modality-specific encoders - e.g. splines for scalar covariates and convolutional networks for images, which classical spline smoothers cannot accommodate. Our model is by construction invariant to the translation, rotation and scaling of the input curves and handles sparsely and irregularly sampled curves. We further provide an algorithm for elastic mean estimation that also removes parametrisation by iterating covariance smoothing, rotational alignment and parametrisation alignment. We illustrate the method on simulated outlines with known conditional mean and multimodal covariates, and give a first application to hippocampal outlines from the ADNI cohort, recovering covariate effects consistent with the literature. Code is available at https://github.com/mpff/dnn-shapes.

## Metadata
- **Published**: 2026-07-21T22:04:17Z
- **Authors**: Manuel Pfeuffer, Roshan Prakash Rane, Hadya Yassin, Kerstin Ritter, Sonja Greven
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19600v1)