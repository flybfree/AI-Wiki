---
title: Label-Free Finite-Volume-Residual Training of Attention Graph Neural Networks for Coupled Thermo-Fluid Fields
published: 2026-07-22T16:07:09Z
authors: Tianyu Li, Zhiwei Cao, Qingang Zhang, Ruihang Wang, Binyang Song, Yonggang Wen
url: http://arxiv.org/abs/2607.20321v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Label-Free Finite-Volume-Residual Training of Attention Graph Neural Networks for Coupled Thermo-Fluid Fields

## Abstract
Neural surrogates are widely used in scientific machine learning for fast prediction of three-dimensional (3D) thermo-fluid fields. However, generating training data using conventional numerical solvers often incurs substantial computational and storage costs. We propose to train an attention graph neural network by minimizing the finite-volume method (FVM) residuals of the governing equations. These residuals are evaluated directly on the mesh, requiring no labeled data. We evaluate the trained surrogates against computational fluid dynamics (CFD) references and a data-supervised baseline across four scenarios. On the two steady-state benchmarks, the FVM-loss model achieves an all-field normalized root-mean-square error (nRMSE) of 2.3-2.8%. It demonstrates close agreement with the CFD references, including the buoyancy-energy coupling. On the two parametric transient cases, the FVM-loss model outperforms the supervised baseline in terms of accuracy, while avoiding the data-generation cost entirely. These results indicate that the FVM loss can provide a practical training signal for neural surrogates and reduce the model development cost.

## Metadata
- **Published**: 2026-07-22T16:07:09Z
- **Authors**: Tianyu Li, Zhiwei Cao, Qingang Zhang, Ruihang Wang, Binyang Song, Yonggang Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20321v2)