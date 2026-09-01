---
title: Self-Supervised Pretext Tasks for Infant Cry Analysis: A Controlled Comparison and a Cautionary Result on Donateacry
published: 2026-08-31T08:43:48Z
authors: Luigi Simeone
url: http://arxiv.org/abs/2608.30456v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Supervised Pretext Tasks for Infant Cry Analysis: A Controlled Comparison and a Cautionary Result on Donateacry

## Abstract
We compare six self-supervised pretext tasks for infant cry analysis under a fixed budget, meaning the same compact encoder of 1.17M parameters, the same 115 hours of license-verified public pretraining audio, and the same evaluation protocol for every candidate. On cry detection the reconstructive objectives dominate, and a linear probe over a masked-spectrogram encoder reaches 0.988 AUC with subject-wise splits even though the encoder never observed a cry during pretraining. On cry-reason classification over donateacry, the de facto public benchmark for cry reasons, every encoder performs at chance (0.38 to 0.54 macro AUC over 5 classes), and neither domain adaptation on 1.8 hours of real cries nor end-to-end fine-tuning moves the result. Since a frozen HuBERT-base with 80 times more parameters shows the same pattern, the bottleneck must sit in the labels and not in model capacity. We then reproduce the 90\%+ accuracies of the donateacry literature on our own system by changing nothing but the evaluation protocol: clip-wise splits raise accuracy to 85.2% (barely above the 83.8% majority-class baseline), and applying augmentation before splitting raises it to 97.9%, matching the reported state of the art, from the same model that measures 0.49 macro AUC under subject-wise splits. Under leakage-free splits, a twentyfold augmentation of the labeled set (vocoder speaker perturbation and noise mixing, 21 hours) leaves cross-subject AUC unchanged: for this task the effective sample size is the number of infants. We release code, seeds and per-clip license manifests.

## Metadata
- **Published**: 2026-08-31T08:43:48Z
- **Authors**: Luigi Simeone
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30456v1)