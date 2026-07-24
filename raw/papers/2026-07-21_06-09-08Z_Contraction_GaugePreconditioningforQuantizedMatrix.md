---
title: Contraction-Gauge Preconditioning for Quantized Matrix Multiplication
published: 2026-07-21T06:09:08Z
authors: Piyush Sao, Narasinga Miniskar, Pedro Valero-Lara, Keita Teranishi, Sudip Seal
url: http://arxiv.org/abs/2607.18745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contraction-Gauge Preconditioning for Quantized Matrix Multiplication

## Abstract
We study low-precision computation of C=AB with both factors quantized. We derive an exact finite-dimensional identity for the expected squared product error under independent, zero-mean entrywise errors with known variance fields; it holds exactly for non-overloading subtractive dither and for independent stochastic rounding, and we empirically assess deterministic round-to-nearest (RTN). Using the product-preserving equivalence AB=(AT)(T^{-1}B), we formulate contraction-gauge preconditioning: jointly choosing a factor representation and its sharing pattern before quantization. Preconditioning can reduce product error but may require extra transformed, quantized copies of the opposite operand: a shared transform needs one copy, a block-specific transform up to one per block. Within the bounded family of positive diagonal gauges (folds), a geometric program computes a globally optimal shared fold and a linear program decides whether the identity fold is already optimal. For other families we derive computable selection statistics -- tail index for scaling, profile spread for partitioning, coherence and weighted-Gram energy for rotations, slice-energy covariance for hierarchy depth -- with upper bounds for ranking heuristic candidates. Across twelve linear products from a trained three-block image classifier, median within-product rank correlations between dither-model predictions and deterministic-RTN errors are 0.937 at 8 bits and 0.918 at 4 bits. The GP fold cuts held-out product error over the identity fold by 18.0% (8-bit) and 20.5% (4-bit) in geometric mean, beats a SmoothQuant-style grid baseline at both precisions and on ten of twelve products, and lowers composed logit MSE by 15.4% and 26.4%. We thus provide exact stochastic product-error accounting, certified selection within the diagonal family, and a common objective for evaluating reusable transform candidates under RTN.

## Metadata
- **Published**: 2026-07-21T06:09:08Z
- **Authors**: Piyush Sao, Narasinga Miniskar, Pedro Valero-Lara, Keita Teranishi, Sudip Seal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18745v1)