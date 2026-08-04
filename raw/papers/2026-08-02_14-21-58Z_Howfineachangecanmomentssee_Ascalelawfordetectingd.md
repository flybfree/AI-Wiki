---
title: How fine a change can moments see? A scale law for detecting distribution shift, with a kernel calibration rule
published: 2026-08-02T14:21:58Z
authors: Adel Kaleche
url: http://arxiv.org/abs/2608.01268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How fine a change can moments see? A scale law for detecting distribution shift, with a kernel calibration rule

## Abstract
Detecting that a stream of high-dimensional embeddings has changed is usually framed as a choice of statistic. We give a scale law that constrains any moment-based choice and test it against topological alternatives. The law: certifying a feature of spatial scale eps carrying mass fraction f requires polynomial tests of degree N* >= log(1/f)/(2 eps), proved via the Chebyshev extremal problem; a Gauss-quadrature construction gives N* >= 4b-1 for a b-scale topology, so cost is set by feature fineness, not feature count. The law is one-sided: we exhibit an annulus whose mean, covariance and all fourth-order moments equal those of a filled disk, yet H_1 is nonzero.   Its practical content is a calibration rule. The upper bound is attained by Gaussian test functions, the RKHS witness of an RBF kernel, so the law predicts which bandwidth an MMD test should use: the feature scale. On real embedding streams we measure sigma*/eps with median 1.12 (IQR 1.01-1.52, n=26) over three settings and three scales, and a data-driven bandwidth reaches AUC >= 0.95. Against an adversary optimised against the defender's statistics (mean, covariance, k-NN, kurtosis), only a bandwidth-matched kernel test still detects.   For persistent homology the verdict is mixed and depends on choices usually left implicit. The summary matters more than the filtration: total persistence attains recall 0.75 at FPR 1% where the first persistence landscape attains 0.00. What survives is a cost gap, not a power gap: where persistence works it costs 116x kurtosis, which works at least as well. We conclude not that topological summaries are useless, but that on this task a kernel test whose bandwidth the law sets dominates them.

## Metadata
- **Published**: 2026-08-02T14:21:58Z
- **Authors**: Adel Kaleche
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01268v1)