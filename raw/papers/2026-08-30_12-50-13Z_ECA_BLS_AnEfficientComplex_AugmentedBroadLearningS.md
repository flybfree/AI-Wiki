---
title: ECA-BLS: An Efficient Complex-Augmented Broad Learning System
published: 2026-08-30T12:50:13Z
authors: A. Rahaman, A. Quadir, M. Sajid, M. Akhtar, M. Tanveer
url: http://arxiv.org/abs/2608.29763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECA-BLS: An Efficient Complex-Augmented Broad Learning System

## Abstract
Broad Learning System (BLS) is an efficient alternative to deep architectures due to its fast training, analytical learning, and strong generalization under limited data. However, existing BLS variants are confined to real-valued representations, restricting their ability to capture nonlinear interactions and second-order statistical dependencies inherent in real-world data. Notably, no prior BLS model fully exploits the complete second-order statistics that naturally emerge when data are embedded in the complex domain. To address this limitation, this paper introduces the first complex augmented Broad Learning System (CA-BLS), which transforms real-valued inputs into phase-encoded complex representations and adopts widely linear modeling to jointly leverage covariance and pseudo-covariance information via complex conjugate augmentation. This enables effective modeling of latent nonlinearities, coherence structures, and second-order dependencies inaccessible to conventional BLS formulations. To mitigate the additional computational cost of complex augmentation, an Efficient Complex Augmented BLS (ECA-BLS) is further developed, reformulating CA-BLS entirely in the real domain while preserving its exact decision function, achieving up to 75\% fewer multiplications and over 60\% fewer additions. A rigorous theoretical analysis proves the mathematical equivalence between CA-BLS and ECA-BLS, ensuring zero theoretical loss. Extensive experiments on 26 benchmark datasets from the UCI and KEEL repositories demonstrate that ECA-BLS consistently outperforms classical BLS and recent state-of-the-art randomized neural networks in accuracy, average rank, and statistical significance, establishing augmented second-order modeling as a critical and previously missing dimension of BLS research.

## Metadata
- **Published**: 2026-08-30T12:50:13Z
- **Authors**: A. Rahaman, A. Quadir, M. Sajid, M. Akhtar, M. Tanveer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29763v1)