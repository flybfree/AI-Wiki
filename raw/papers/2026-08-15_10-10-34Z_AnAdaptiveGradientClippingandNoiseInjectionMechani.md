---
title: An Adaptive Gradient Clipping and Noise Injection Mechanism for Differentially Private Federated Learning
published: 2026-08-15T10:10:34Z
authors: Wenjing Wei, Alla Jammine, Farid Nait-Abdesselam
url: http://arxiv.org/abs/2608.15153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Adaptive Gradient Clipping and Noise Injection Mechanism for Differentially Private Federated Learning

## Abstract
Differentially private federated learning must balance privacy protection against model accuracy and training efficiency. Static gradient clipping applies a fixed threshold throughout training and across model layers, which can cause excessive clipping when the threshold is too small or unnecessarily large noise when it is too large. This paper presents DDP-SA-adaptive, an adaptive gradient clipping and noise adding mechanism for differentially private federated learning with secure aggregation. At each communication round, every client determines a separate clipping threshold for each model layer from the median of its per-sample gradient norms. The resulting layer-wise thresholds adapt to the evolving gradient distributions and calibrate the Laplace noise added before the updates are encoded and secret-shared among intermediate aggregation servers. We evaluate the proposed mechanism on a federated regression task in terms of efficiency, accuracy, privacy, convergence, clipping norm, and noise magnitude. Compared with the static DDP-SA baseline, DDP-SA-adaptive reduces the number of communication rounds by 6.81%, total training time by 19.21%, and average per-round training time by 13.33%, leading to improved training efficiency. It also reduces test loss by 98.74% and increases test R2 by 3.41%, leading to improved model accuracy. To attain R2 = 0.99, the adaptive mechanism operates with a privacy budget of approximately epsilon = 0.1, compared with epsilon = 0.4 for static DDP-SA, thus providing stronger privacy protection and achieving stronger privacy guarantees. These results demonstrate that round-wise, layer-wise adaptation can improve the privacy-accuracy-efficiency trade-off of differentially private federated learning.

## Metadata
- **Published**: 2026-08-15T10:10:34Z
- **Authors**: Wenjing Wei, Alla Jammine, Farid Nait-Abdesselam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15153v1)