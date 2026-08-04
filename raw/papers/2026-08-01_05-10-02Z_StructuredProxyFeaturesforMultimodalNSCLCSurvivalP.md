---
title: Structured Proxy Features for Multimodal NSCLC Survival Prediction from Pretreatment CT
published: 2026-08-01T05:10:02Z
authors: Huu Phong Nguyen, Delower Hossain, Ehsan Saghapour, Zhandos Sembay, Jake Y. Chen
url: http://arxiv.org/abs/2608.00446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structured Proxy Features for Multimodal NSCLC Survival Prediction from Pretreatment CT

## Abstract
Lung cancer results in roughly 1.8 million fatalities annually worldwide, with non-small cell lung cancer (NSCLC) comprising the majority of cases. Despite advancements in treatment, survival stratification remains challenging due to intratumoral heterogeneity inadequately captured by conventional descriptors. Standard radiomic and deep learning techniques regard imaging features as independent quantities, overlooking structured interactions between tumor characteristics. We evaluate whether structured proxy features can enhance multimodal NSCLC survival prediction by augmenting pretreatment computed tomography (CT) representations, radiomics, and clinical variables with six simulation-derived features designed to capture interactions between heterogeneity and morphology. A radiomic-parameterized cellular automaton generates growth-rate and necrosis-ratio proxy features from baseline CT by using entropy and sphericity to compute low-dimensional proxy parameters. The imaging backbone is a Transformer-based Masked Autoencoder (TMAE), which was chosen after a systematic evaluation with alternative encoders within the same pipeline and provides attention-based visualizations that highlight tumor regions receiving higher model attention. On the public Lung1 cohort (n = 390), the primary four-modality fusion attained a C-index of 0.641 (iAUC 0.731, log-rank p < 0.001). The primary result compares favorably with prior multimodal results on Lung1 (C-index 0.631; iAUC 0.592 [15]) under a comparable evaluation protocol, while a separate exploratory coefficient-optimization analysis achieved a best observed C-index of 0.662 (iAUC 0.748). These results indicate that, in addition to conventional radiomic, deep, and clinical representations within the Lung1 benchmark, simulation-derived proxy features may provide complementary predictive information within this fixed Lung1 benchmark.

## Metadata
- **Published**: 2026-08-01T05:10:02Z
- **Authors**: Huu Phong Nguyen, Delower Hossain, Ehsan Saghapour, Zhandos Sembay, Jake Y. Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00446v1)