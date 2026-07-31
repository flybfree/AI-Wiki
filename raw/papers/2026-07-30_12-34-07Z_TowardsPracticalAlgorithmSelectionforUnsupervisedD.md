---
title: Towards Practical Algorithm Selection for Unsupervised Domain Adaptation in Medical Imaging
published: 2026-07-30T12:34:07Z
authors: Yiheng Xiong, Luisa Gallée, Daniel Santak Wolf, Heiko Hillenhagen, Michael Götz
url: http://arxiv.org/abs/2607.28125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Practical Algorithm Selection for Unsupervised Domain Adaptation in Medical Imaging

## Abstract
Numerous unsupervised domain adaptation (UDA) algori-thms exist, but for clinical practice, selecting the best-suited one along with proper hyperparameters often remains unclear, as the unlabeled deployment (target) domain prevents direct evaluation. We propose a label-free criterion that jointly selects the algorithm and hyperparameters for UDA. Given a pool of candidate models from multiple algorithms trained with different hyperparameters, our approach scores each candidate against an agreement reference, and selects the one with the highest score. The agreement reference is constructed in two levels without using target labels. First, we leverage multiple label-free selection signals, using each to nominate a model within every algorithm. Second, the nominated models are aggregated across algorithms to form a reference prediction for each unlabeled target sample. The candidate whose predictions agree most with this reference is then selected for deployment. Experimental results on four brain MRI and four chest X-ray datasets across seven clinically relevant transfer scenarios show that our method achieves better selection performance than other methods and remains effective across different algorithm pools. Our approach takes a step towards practical, label-free algorithm selection for clinical deployment of UDA.

## Metadata
- **Published**: 2026-07-30T12:34:07Z
- **Authors**: Yiheng Xiong, Luisa Gallée, Daniel Santak Wolf, Heiko Hillenhagen, Michael Götz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28125v1)