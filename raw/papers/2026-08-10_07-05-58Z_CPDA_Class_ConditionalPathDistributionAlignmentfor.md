---
title: CPDA: Class-Conditional Path Distribution Alignment for Unsupervised Time-Series Domain Adaptation
published: 2026-08-10T07:05:58Z
authors: Felix Ott, Christopher Mutschler
url: http://arxiv.org/abs/2608.09193v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CPDA: Class-Conditional Path Distribution Alignment for Unsupervised Time-Series Domain Adaptation

## Abstract
Unsupervised time-series domain adaptation (DA) addresses the challenge of transferring a classifier from a labeled source domain to an unlabeled target domain under distribution shifts induced by different users, sensors, devices, acquisition conditions, or temporal dynamics. Existing methods typically mitigate this shift by aligning marginal feature distributions through adversarial training, optimal transport, or moment-based discrepancies. In this paper, we propose Class-Conditional Path Distribution Alignment (CPDA), a non-adversarial discrepancy-based framework that aligns source and target class-conditional latent path distributions rather than only global feature marginals. CPDA introduces a composite signature-spectral kernel that jointly captures pooled semantic features, temporal path structure, frequency-domain information, and low-rank path-signature dynamics, while using source labels and target soft pseudo-labels to perform class-preserving alignment. We further provide a theoretical analysis showing that CPDA defines a valid kernel discrepancy, admits existing moment-matching methods as restricted cases, and yields a class-conditional target-risk bound. Extensive experiments with CNN, ResNet18, and TCN backbones on 13 different time-series DA benchmarks demonstrate the effectiveness of CPDA against 30 discrepancy, adversarial, and pseudo-labeling baselines.

## Metadata
- **Published**: 2026-08-10T07:05:58Z
- **Authors**: Felix Ott, Christopher Mutschler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09193v1)