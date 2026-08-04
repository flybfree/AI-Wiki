---
title: The Fourth Quadrant: A Stylized View of Benign Misfitting
published: 2026-08-02T06:27:55Z
authors: Gireeja Ranade, Anant Sahai
url: http://arxiv.org/abs/2608.01032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Fourth Quadrant: A Stylized View of Benign Misfitting

## Abstract
Training error is what we can observe on a training set; test error is the quantity we actually care about. We study linear regression with squared-error in a deterministic $(d+1)$-dimensional single-spike model. Each stylized training vector has the same informative spike coordinate, of amplitude $\sqrtγ$ with $γ>1$. The remaining directions are nuisance, and the nuisance components of distinct training vectors all have equal norm and are mutually orthogonal. The training labels are all $1$. Fresh test points are drawn from $\vec{x}_{\rm test} \sim \mathcal{N}(\vec{0},\operatorname{diag}(γ,1,\ldots,1))$, with the noise-free test labels being the normalized spike coordinate $x_{\rm test}[1]/\sqrtγ$. We focus on linear predictors in the span of the training vectors, the class naturally reached by zero-initialized linear gradient methods.   We exhibit a range of training-set sizes $n$ in which every span predictor that generalizes well must fit the training data \emph{worse} than the zero predictor. We call this regime \emph{benign misfitting}, or the fourth quadrant. The best span predictor begins to generalize when $n\gg d/γ^2$, while interpolation does not generalize until the later threshold $n\gg d/γ$. In the window $d/γ^2 \ll n \ll d/γ$, useful prediction within the linear span lies beyond interpolation: predictions on the training points overshoot the labels. We show that one-pass stochastic gradient descent (SGD), with a large constant learning rate, reaches small test error throughout this window---matching the best span predictor up to a logarithmic factor. We also verify directly that it indeed has \emph{large} empirical training error (despite the descent premise in its name). Finally, we show that the unavoidable nuisance component responsible for the training misfit also controls the predictor's adversarial sensitivity.

## Metadata
- **Published**: 2026-08-02T06:27:55Z
- **Authors**: Gireeja Ranade, Anant Sahai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01032v1)