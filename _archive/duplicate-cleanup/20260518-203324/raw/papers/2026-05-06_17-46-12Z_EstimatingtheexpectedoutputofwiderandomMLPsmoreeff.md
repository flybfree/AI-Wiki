---
title: Estimating the expected output of wide random MLPs more efficiently than sampling
published: 2026-05-06T17:46:12Z
authors: Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano
url: http://arxiv.org/abs/2605.05179v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Estimating the expected output of wide random MLPs more efficiently than sampling

## Abstract
By far the most common way to estimate an expected loss in machine learning is to draw samples, compute the loss on each one, and take the empirical average. However, sampling is not necessarily optimal. Given an MLP at initialization, we show how to estimate its expected output over Gaussian inputs without running samples through the network at all. Instead, we produce approximate representations of the distributions of activations at each layer, leveraging tools such as cumulants and Hermite expansions. We show both theoretically and empirically that for sufficiently wide networks, our estimator achieves a target mean squared error using substantially fewer FLOPs than Monte Carlo sampling. We find moreover that our methods perform particularly well at estimating the probabilities of rare events, and additionally demonstrate how they can be used for model training. Together, these findings suggest a path to producing models with a greatly reduced probability of catastrophic tail risks.

## Metadata
- **Published**: 2026-05-06T17:46:12Z
- **Authors**: Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.05179v1)