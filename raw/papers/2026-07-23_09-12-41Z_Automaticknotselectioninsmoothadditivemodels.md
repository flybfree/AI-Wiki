---
title: Automatic knot selection in smooth additive models
published: 2026-07-23T09:12:41Z
authors: Nicolás Carrizosa, Vanesa Guerrero, María Durbán
url: http://arxiv.org/abs/2607.21083v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automatic knot selection in smooth additive models

## Abstract
B-spline regression constitutes a widely used framework for nonparametric modeling. The performance of this methodology depends on specifying the number and placement of changepoints, known as knots, prior to the estimation process. Such knot sequence determines the dimension of the B-spline basis used to represent the regression function and the number of coefficients to be estimated. Therefore, the knots' choice affects the model's flexibility, influencing its smoothness and goodness-of-fit. Traditionally, this problem has been addressed either by explicitly selecting knots, via knot-selection algorithms, or by regularization methods, such as P-splines, which automatically tune the regressor's smoothness. The latter have become the standard in generalized additive models (GAMs). In contrast, knot-selection techniques, frequently neglected because of computational or modeling limitations, provide certain advantages which can be valuable in some contexts. In this work, we introduce a novel explicit knot-selection technique for GAMs based on an extension of the adaptive splines (A-splines) knot selection methodology, combined with a customized Fellner-Schall scheme for tuning the associated parameters. Our approach is evaluated on various synthetic and real datasets and compared with P-splines and state-of-the-art knot-selection techniques. The results indicate comparable performance, while producing models built on a substantially smaller number of basis elements.

## Metadata
- **Published**: 2026-07-23T09:12:41Z
- **Authors**: Nicolás Carrizosa, Vanesa Guerrero, María Durbán
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21083v1)