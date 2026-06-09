---
title: Bayesian Fine-tuning in Projected Subspaces
published: 2026-05-08T13:14:24Z
authors: Viktar Dubovik, Patryk Marszałek, Jacek Tabor, Tomasz Kuśmierczyk
url: http://arxiv.org/abs/2605.07706v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bayesian Fine-tuning in Projected Subspaces

## Abstract
Low-Rank Adaptation (LoRA) enables parameter-efficient fine-tuning of large models by decomposing weight updates into low-rank matrices, significantly reducing storage and computational overhead. While effective, standard LoRA lacks mechanisms for uncertainty quantification, leading to overconfident and poorly calibrated models. Bayesian variants of LoRA address this limitation, but at the cost of a significantly increased number of trainable parameters, partially offsetting the original efficiency gains. Additionally, these models are harder to train and may suffer from unstable convergence. In this work, we propose a novel framework for parameter-efficient Bayesian fine-tuning, demonstrating that effective uncertainty quantification can be achieved in very low-dimensional parameter spaces. The proposed method achieves strong performance with improved calibration and generalization while maintaining computational efficiency. Our empirical findings show that, with the appropriate projection of the weight space uncertainty can be effectively modeled in a low-dimensional space, and weight covariances exhibit low ranks.

## Metadata
- **Published**: 2026-05-08T13:14:24Z
- **Authors**: Viktar Dubovik, Patryk Marszałek, Jacek Tabor, Tomasz Kuśmierczyk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.07706v1)