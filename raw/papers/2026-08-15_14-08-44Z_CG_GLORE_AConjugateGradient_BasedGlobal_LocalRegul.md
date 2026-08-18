---
title: CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction
published: 2026-08-15T14:08:44Z
authors: Tran Xuan Hieu Le, Doanh C. Bui, Vu Trung Duong Le, Hoai Luan Pham, Khang Nguyen, Mai K. Nguyen, Tu Bao Ho, Yasuhiko Nakashima
url: http://arxiv.org/abs/2608.15246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction

## Abstract
Sparse-view computed tomography (CT) reduces radiation dose by acquiring fewer projection views, but the resulting inverse problem is highly ill-posed and often produces severe streak artifacts. Existing deep reconstruction methods have achieved promising performance, yet many rely on first-order updates or large regularization networks, which can be less effective in ill-conditioned settings. We propose \textbf{CG-GLORE}, a compact deep unrolling framework inspired by second-order optimization for sparse-view CT reconstruction. Each unrolled stage uses a CG-solved linear system based on a structured Hessian surrogate: it retains the physics-induced curvature of the data-fidelity term while using an identity approximation for the learned regularization term. Thus, the method is second-order-inspired rather than an exact Newton method for the full learned objective. To model image priors, we design a Global-Local Regularization Network (GLORE), which combines convolutional local feature extraction with a Long-Range Dependency Representation module based on sparse patchification and Nyström attention. This design captures anatomical details and non-local dependencies while maintaining practical complexity. Experiments on AAPM and DeepLesion under multiple sparse-view and noise settings show that CG-GLORE achieves strong quantitative performance, stable convergence, lower noise power, and improved visual fidelity compared with representative reconstruction methods.

## Metadata
- **Published**: 2026-08-15T14:08:44Z
- **Authors**: Tran Xuan Hieu Le, Doanh C. Bui, Vu Trung Duong Le, Hoai Luan Pham, Khang Nguyen, Mai K. Nguyen, Tu Bao Ho, Yasuhiko Nakashima
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15246v1)