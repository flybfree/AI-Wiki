---
title: Hierarchical Solomonoff Induction: An Unbounded Machine Learning Model
published: 2026-08-02T05:22:30Z
authors: Nathan Young
url: http://arxiv.org/abs/2608.01005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Solomonoff Induction: An Unbounded Machine Learning Model

## Abstract
Solomonoff Induction, or SolInd, provides an ideal unbounded model of a priori sequence prediction but cannot naturally describe extrapolation from a given training dataset, as performed by Large Language Models. We apply de Finetti's theorem on exchangeable distributions to SolInd to produce what we call Hierarchical Solomonoff Induction, or HSI, which maintains a hyperprior over all Solomonoff priors that can be conditioned on previously observed sequences.   We extend Wood et al.'s proof that universal mixtures of semimeasures are equivalent to SolInd to show that universal mixtures of these mixtures are also equivalent, proving that HSI=SolInd. We also prove that HSI's excess error on any distribution, compared to its true generator, is bounded by that generator's complexity in the hyperprior. This result is directly comparable to SolInd's prediction error being bounded by the Kolmogorov complexity of the sequence being predicted, and forces HSI's average excess error to converge to 0 as a dataset grows, leading to optimal prediction in the limit. We claim that HSI is an ideal unbounded model of sequence prediction given a dataset in the same way that SolInd is ideal over individual sequences.

## Metadata
- **Published**: 2026-08-02T05:22:30Z
- **Authors**: Nathan Young
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01005v1)