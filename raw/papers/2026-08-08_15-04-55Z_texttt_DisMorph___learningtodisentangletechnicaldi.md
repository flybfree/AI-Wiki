---
title: $\texttt{DisMorph}$: learning to disentangle technical distortions from true biological change
published: 2026-08-08T15:04:55Z
authors: Jingru Fu, Kathleen E. Larson, Douglas N. Greve, Bruce Fischl, Malte Hoffmann
url: http://arxiv.org/abs/2608.08173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $\texttt{DisMorph}$: learning to disentangle technical distortions from true biological change

## Abstract
Longitudinal MRI enables sensitive measurement of structural brain change for studying aging and neurodegenerative disease. Deformable image registration is a key tool for estimating such change by computing a dense deformation that captures geometric differences between longitudinal scans. However, MRI scanners introduce geometric distortions that vary across acquisition systems and protocols, such as gradient non-linearity (GNL) distortion. Existing registration methods estimate a single field that conflates biological and technical effects, potentially biasing downstream morphometric measurements if distortions remain (partially) uncorrected. We propose $\texttt{DisMorph}$, a registration framework trained entirely on synthetic data that explicitly decomposes longitudinal deformation into technical and anatomical transforms. It predicts two dense deformations, each encoding one effect. During training, a novel generative model synthesizes both effects separately to provide disentanglement supervision, while domain randomization promotes generalization across imaging protocols. We evaluate our method in three complementary settings. On simulated data with known ground truth, our method detects anatomical change more accurately and consistently than conventional registration. On real image pairs that differ only by GNL distortion, our method assigns most geometric change to the distortion field, demonstrating specificity in the absence of anatomical change. On longitudinal Alzheimer's disease (AD) pairs, our method detects anatomical change in AD-related brain structures while identifying residual distortion left after standard correction. By disentangling MRI-induced distortion from biological change in the longitudinal deformation, our method paves the way for more accurate longitudinal morphometry in clinical settings where maintaining acquisition consistency is challenging.

## Metadata
- **Published**: 2026-08-08T15:04:55Z
- **Authors**: Jingru Fu, Kathleen E. Larson, Douglas N. Greve, Bruce Fischl, Malte Hoffmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08173v1)