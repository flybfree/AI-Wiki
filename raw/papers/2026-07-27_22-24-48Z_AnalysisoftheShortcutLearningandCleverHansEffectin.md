---
title: Analysis of the Shortcut Learning and Clever Hans Effect in CNN based ECG Image Classification
published: 2026-07-27T22:24:48Z
authors: Abhay Kumar Pathak, Mrityunjay Chaubey, Manjari Gupta, Deepti Mishra
url: http://arxiv.org/abs/2607.25117v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Analysis of the Shortcut Learning and Clever Hans Effect in CNN based ECG Image Classification

## Abstract
Deep learning models for ECG image classification may achieve high accuracy by exploiting non-physiological visual cues instead of ECG waveform morphology. Given the black-box nature of deep learning models, their promise of high predictive performance often remains insufficiently translated into clinical or real-world trust, interpretability, and actionable decision-making. In this study, we examine shortcut learning and Clever Hans effect in a publicly available ECG image dataset using convolutional neural networks. In process we have created six image-derived feature sets (FSs), FS1: raw full ECG images, FS2: cropped waveform-only images, FS3: waveform-masked metadata images, FS4: red-arrow artifact images for the myocardial infarction class, FS5: contrast-enhanced images for the abnormal heartbeat class and FS6: Gaussian-blurred images for the normal class. These controlled representations were used to test whether classification performance persists when waveform information is removed or when artificial class-specific artifacts are introduced. Shortcut retention score, prediction consistency and confidence divergence across Feature-Set Representations have been calculated to assess the transparency about the learning pattern. Along with factual results, average Integrated Gradients and occlusion sensitivity test results are presented to inspect whether model attribution focused on ECG-relevant waveform regions or on non-clinical artifacts. Performance changes across feature sets and attribution patterns were used to identify potential Clever Hans behavior. This study evaluates whether ECG image classifiers learn clinically meaningful morphology or shortcut cues introduced by report layout, metadata, contrast, blur, or artificial markers.

## Metadata
- **Published**: 2026-07-27T22:24:48Z
- **Authors**: Abhay Kumar Pathak, Mrityunjay Chaubey, Manjari Gupta, Deepti Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25117v1)