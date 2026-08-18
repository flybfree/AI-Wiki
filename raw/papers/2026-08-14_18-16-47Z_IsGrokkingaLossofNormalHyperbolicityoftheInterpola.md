---
title: Is Grokking a Loss of Normal Hyperbolicity of the Interpolation Manifold?
published: 2026-08-14T18:16:47Z
authors: Suvinava Basak
url: http://arxiv.org/abs/2608.14803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is Grokking a Loss of Normal Hyperbolicity of the Interpolation Manifold?

## Abstract
A recent line of work recasts the post-memorization phase of grokking as constrained optimization: once a network interpolates the training set, weight decay drives a slow drift along the zero-loss manifold toward lower norm. In the language of dynamical systems, this is a fast-slow system in which the interpolation manifold plays the role of a slow manifold. We ask a question that this framing makes natural but the existing literature does not address: is the sharp generalization transition a loss of normal hyperbolicity of that manifold: a fold- or bifurcation-like event in which a normal restoring direction goes flat? Or does the manifold stay uniformly attracting while generalization happens by smooth drift? We propose a simple, optimizer-agnostic diagnostic: the smallest nonzero singular value $σ_{\min}^{+}(\mathbf J)$ of the residual Jacobian, which, for the squared loss, equals the slowest normal restoring rate of the manifold. On a two-layer ReLU network trained to grok modular addition under squared loss, $σ_{\min}^{+}(\mathbf J)$ does not collapse at the transition; it is near zero only before memorization and attains its largest values during the transition. The result holds across five seeds, and the six smallest singular values behave identically; there is no subspace-local collapse either. This is preliminary evidence against the bifurcation hypothesis and in favor of the smooth-contraction picture. We are explicit that a single-setting, gradual-transition experiment under Adam optimizer does not prove the absence of a bifurcation; it constrains where one could hide.

## Metadata
- **Published**: 2026-08-14T18:16:47Z
- **Authors**: Suvinava Basak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14803v1)