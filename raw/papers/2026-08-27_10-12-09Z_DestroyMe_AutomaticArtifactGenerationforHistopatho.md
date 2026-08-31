---
title: Destroy Me: Automatic Artifact Generation for Histopathology Images
published: 2026-08-27T10:12:09Z
authors: Zuzanna Krawczyk-Borysiak, Adam Krawczyk, Mateusz Miller, Gabriela Kaczmarek, Sławomir Pakuło, Małgorzata Sokół, Żaneta Swiderska-Chadaj
url: http://arxiv.org/abs/2608.27516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Destroy Me: Automatic Artifact Generation for Histopathology Images

## Abstract
Deep learning's diagnostic utility in pathology is constrained by model vulnerability to real-world data imperfections. While current strategies favor "perfect data" by filtering low-quality regions, which can lead to the loss of valuable diagnostic context, we propose a paradigm shift: engineering models to thrive in imperfect environments using "Destroy Me", a hybrid framework for realistic artifact synthesis and robust data augmentation. Our approach combines Stable Diffusion, fine-tuned to preserve morphological continuity by realistically integrating artifacts with the underlying tissue architecture, with physics-based procedural modeling to synthesize six common artifact types: tissue folds, precipitates, blur, stitching errors, dust, and pen markers. Artifact fidelity is assessed using Kernel Inception Distance (KID) and color Wasserstein distance metrics. Validating this strategy on lung adenocarcinoma pattern classification with an nnU-Net, we confirm that models trained on "destroyed" patches consistently outperform baselines on independent real-world datasets. Specifically, we observed a 10.5% relative improvement in macro F1-score and a 15% relative increase in the Cohen's Kappa ($κ$) coefficient. Crucially, our results demonstrate that selective, impact-weighted augmentation is vital for balancing practical robustness with the preservation of subtle diagnostic features.

## Metadata
- **Published**: 2026-08-27T10:12:09Z
- **Authors**: Zuzanna Krawczyk-Borysiak, Adam Krawczyk, Mateusz Miller, Gabriela Kaczmarek, Sławomir Pakuło, Małgorzata Sokół, Żaneta Swiderska-Chadaj
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27516v1)