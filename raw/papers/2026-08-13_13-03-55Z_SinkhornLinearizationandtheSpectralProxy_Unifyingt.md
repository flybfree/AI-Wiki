---
title: Sinkhorn Linearization and the Spectral Proxy: Unifying the Statistical and Algorithmic Theory of Feature-Parameterized Inverse Optimal Transport via a Single Spectral Sandwich
published: 2026-08-13T13:03:55Z
authors: Han Dong, Jiaming Li, Yongqiang Gong, Ruixi Li, Yin Liu
url: http://arxiv.org/abs/2608.13201v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sinkhorn Linearization and the Spectral Proxy: Unifying the Statistical and Algorithmic Theory of Feature-Parameterized Inverse Optimal Transport via a Single Spectral Sandwich

## Abstract
We develop the statistical and algorithmic theory of inverse optimal transport (IOT) under the feature-parameterized cost C_theta(i,j) = -theta^T phi(i,j). The core technical contribution is the Sinkhorn linearization -- the implicit-function sensitivity of the entropic OT plan to the cost -- together with its spectral proxy, a formula that is spectrally exact yet geometrically transparent.   The restricted Hessian on the tangent space satisfies the spectral sandwich (pi_min/epsilon) I <= H_T^{-1} <= (pi_max/epsilon) I, yielding the single core bound sigma_min >= (pi_min/(a_max epsilon)) sqrt(lambda_min(Sigma)) that drives the entire theory. On this core we establish four theorems and one observation.   T1 (identifiability): theta is globally injective on the quotient of the gauge kernel, with dimension bound F <= (K-1)^2. T2 (sparsistency): the l1-penalized estimator recovers the true support under irrepresentability and score concentration, with exponential failure probability. T3 (well-posedness): the feature-moment map M(theta) = Phi^T x_theta is strongly monotone, and the inverse is Lipschitz with constant L <= epsilon ||Phi^T S_a||_op / (pi_min lambda_min(Sigma)). T4 (convergence): local strong convexity with mu >= pi_min^2 lambda_min(Sigma) / epsilon^2 guarantees monotone gradient descent convergence. O5 (misspecification): the estimator converges to the OT-model projection of the truth; the Holder continuity of the projection map is assessed numerically, yielding setting-dependent empirical exponents alpha_eff in (0,1).

## Metadata
- **Published**: 2026-08-13T13:03:55Z
- **Authors**: Han Dong, Jiaming Li, Yongqiang Gong, Ruixi Li, Yin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13201v1)