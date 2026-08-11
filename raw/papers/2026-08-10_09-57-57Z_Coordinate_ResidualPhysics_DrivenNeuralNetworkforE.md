---
title: Coordinate-Residual Physics-Driven Neural Network for Electromagnetic Inverse Scattering
published: 2026-08-10T09:57:57Z
authors: Yutong Du, Zicheng Liu, Bo Qi, Yali Zong, Peixian Han
url: http://arxiv.org/abs/2608.09382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coordinate-Residual Physics-Driven Neural Network for Electromagnetic Inverse Scattering

## Abstract
Electromagnetic inverse scattering is a nonlinear and ill-posed problem, where accurate reconstruction is challenging due to measurement limitations, noise, and high computational costs, especially for 3-D imaging. Although physics-driven neural networks (PDNNs) reduce the dependence on labeled training data, existing accelerated PDNN frameworks often rely on preliminary reconstruction-based region selection, which may introduce instability when the selected region is inaccurate. In this paper, a coordinate-residual physics-driven neural network (CRPDNN) is proposed for 3-D electromagnetic inverse scattering. The proposed solver directly reconstructs the unknown contrast distribution using normalized spatial coordinates and a residual convolutional network, without requiring a preliminary reconstruction. For the reported noise-free 3-D synthetic cases, CRPDNN achieves an average relative error of 2.10\%, compared with 7.97\% for CSI and 3.99\% for $L_{2/3}$-FBE-WCIE, while providing approximately 5.5- and 12.1-fold speedups over the two baselines, respectively. Supplementary 2-D comparisons further confirm its stability and computational efficiency relative to existing PDNN frameworks. CRPDNN also maintains reliable reconstruction performance under noisy measurements, and the 3-D Fresnel experiments further indicate its potential for practical imaging applications. The related code is available at https://github.com/Physics-driven-methods.

## Metadata
- **Published**: 2026-08-10T09:57:57Z
- **Authors**: Yutong Du, Zicheng Liu, Bo Qi, Yali Zong, Peixian Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09382v1)