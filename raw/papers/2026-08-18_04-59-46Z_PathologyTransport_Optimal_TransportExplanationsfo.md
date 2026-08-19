---
title: Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease
published: 2026-08-18T04:59:46Z
authors: Lalit Kumar
url: http://arxiv.org/abs/2608.17370v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease

## Abstract
Generative models promise a route to explainable clinical AI: rather than probe a classifier, model the distributions of healthy and diseased patients and read explanations off the geometry between them. We build such a system - an optimal-transport rectified flow trained between two clinical distributions - and use it to ask a pointed question the field too rarely tests: do the resulting explanation heatmaps actually localize disease? On tabular tumour biomarkers (Breast Cancer Wisconsin) a single flow yields per-patient counterfactuals, an unsupervised malignancy score (AUROC 0.91; 0.93 +/- 0.01 across five seeds), and a label-free attribution that agrees with a supervised classifier (r ~ 0.5) - a compact, honest interpretability engine, though it never out-predicts logistic regression. Moving to chest X-rays, we show the transport heatmap is a population-level signal, not a localiser; a reconstruction-based, identity-preserving variant does localize synthetic lesions (pointing game 0.52), yet on real RSNA radiologist boxes it collapses to chance while only supervised Grad-CAM stays above it. The central result is a synthetic-to-real gap: label-free heatmaps that look compelling on planted lesions are not evidence of real localisation. We contribute a reusable optimal-transport recipe for generative explanations and a controlled benchmark for stress-testing whether they localize.

## Metadata
- **Published**: 2026-08-18T04:59:46Z
- **Authors**: Lalit Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17370v1)