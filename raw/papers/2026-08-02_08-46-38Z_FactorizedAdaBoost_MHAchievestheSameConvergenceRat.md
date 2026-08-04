---
title: Factorized AdaBoost.MH Achieves the Same Convergence Rate as AdaBoost.MH
published: 2026-08-02T08:46:38Z
authors: Xin Zou, Jingyuan Xu
url: http://arxiv.org/abs/2608.01091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Factorized AdaBoost.MH Achieves the Same Convergence Rate as AdaBoost.MH

## Abstract
AdaBoost.MH reduces multi-class classification to a collection of binary subproblems and enjoys the classical boosting-type convergence guarantee under a weak learning condition. A more structured variant, Factorized AdaBoost.MH, uses base classifiers of the form $\mathbf{h}(x)=α\mathbf{v} \bm{\varphi}(x)$, where a single binary classifier $\bm{\varphi}$ is shared across all classes and the label dependence is carried by a vote vector $\mathbf{v} \in\{\pm1\}^K$. This factorization is algorithmically attractive and achieves better performance in practice, but its convergence depends on whether one can always choose a vote vector with sufficiently large induced binary weight mass. Previous work resolved this question with a lower bound $\max\{1/n,1/\sqrt{2K}\}$, which still leaves a dimension-dependent slowdown relative to the original AdaBoost.MH analysis. In this paper, we sharpen this combinatorial step. For the minimax quantity $\mathfrak{W}_{n,K}$ governing the factorized edge, we prove $\max\{1/n,C_K\}\le\mathfrak{W}_{n,K}\le C_{\min\{n,K\}}$, where $C_q=1$ for $q=1$, $C_q=q/(3q-4)$ for even $q\ge2$, and $C_q=(q+1)/(3q-1)$ for odd $q\ge2$. Since $C_q\downarrow 1/3$, our bounds show that $\mathfrak{W}_{n,K}=Θ(1)$ uniformly over $n$ and $K$. Consequently, Factorized AdaBoost.MH achieves the same boosting-type convergence rate as AdaBoost.MH up to a universal constant factor, removing the previously suggested additional dependence on $n$ or $K$ in the number of boosting rounds.

## Metadata
- **Published**: 2026-08-02T08:46:38Z
- **Authors**: Xin Zou, Jingyuan Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01091v1)