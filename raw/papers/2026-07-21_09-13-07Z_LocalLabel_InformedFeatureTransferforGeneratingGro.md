---
title: Local Label-Informed Feature Transfer for Generating Ground-Truth Medical Images: A Comparison of GAN- and Diffusion-Based Approaches
published: 2026-07-21T09:13:07Z
authors: Rick Wilming, Irem Ozseker, Luca Matteo Cornils, Ahcène Boubekki, Benedict Clark, Danny Panknin, Stefan Haufe
url: http://arxiv.org/abs/2607.18882v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Local Label-Informed Feature Transfer for Generating Ground-Truth Medical Images: A Comparison of GAN- and Diffusion-Based Approaches

## Abstract
Validating Explainable Artificial Intelligence (XAI) methods in medical imaging requires ground-truth data with known locations of informative features. However, current approaches rely on expert annotations, which are prone to labeling errors, or on hand-crafted artificial perturbations superimposed onto healthy images to mimic lesions or malignant features, which lack clinical realism. We present Local Label-Informed Feature Transfer (LLIFT), a framework for generating semi-synthetic brain magnetic resonance images with realistic lesions placed in user-controlled regions, which does not require pixel-level lesion annotations during training. We implement LLIFT with two generative paradigms: LLIFT-GAN, a custom GAN that learns pathological features from binary class labels alone, and LLIFT-DM, a diffusion-based inpainting pipeline conditioned on bounding-box masks via ControlNet. Both approaches are evaluated on brain magnetic resonance imaging data derived from the Human Connectome Project. In evaluations, both achieve Fréchet Inception Distance scores, with respect to the real pathological distribution, that are comparable to the inter-class reference between healthy and pathological images in the given dataset. Furthermore, qualitative inspection confirms the realism of lesion structures. The resulting benchmark datasets provide spatially controlled ground truth data for evaluating XAI methods in medical imaging.

## Metadata
- **Published**: 2026-07-21T09:13:07Z
- **Authors**: Rick Wilming, Irem Ozseker, Luca Matteo Cornils, Ahcène Boubekki, Benedict Clark, Danny Panknin, Stefan Haufe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18882v1)