---
title: Rethinking Medical Landmark Localization with Prototype Learning-based Progressive Offset Correction
published: 2026-08-10T06:49:16Z
authors: Jingxian Xu, Yuhao Huang, Rusi Chen, Yanfeng Zhou, Dong Ni
url: http://arxiv.org/abs/2608.09182v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Medical Landmark Localization with Prototype Learning-based Progressive Offset Correction

## Abstract
Accurate landmark localization in medical images is a fundamental step for quantitative clinical measurement and downstream analysis. Existing localization methods have advanced, among which multi-stage refinement is a superior solution. Although this strategy mitigates the anatomical ambiguity inherent in single-stage global predictions, its high computational cost limits practical applicability. In this work, we propose a parameter-economic model, PPOC-LL, which leverages Prototype learning-based Progressive Offset Correction for Landmark Localization. Our contribution is three-fold. First, to drive coarse-to-fine landmark optimization, we introduce a multi-scale dynamic perception strategy for patch-level feature pyramid modeling. Second, to effectively handle anatomically similar patterns, we design a similarity-driven prototype learning mechanism that captures informative local semantics for robust offset prediction. Last, to stabilize the model learning and improve the overall performance, we incorporate a novel error-aware reliability regularization via tolerance-based balancing. We collected a large validation cohort, including two public and one private datasets spanning X-ray and ultrasound modalities, covering cephalometric, symphysis-fetal head, and fetal heart landmarks. Extensive experiments demonstrate that PPOC-LL achieves satisfactory performance with a favorable trade-off between accuracy and model complexity.

## Metadata
- **Published**: 2026-08-10T06:49:16Z
- **Authors**: Jingxian Xu, Yuhao Huang, Rusi Chen, Yanfeng Zhou, Dong Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09182v1)