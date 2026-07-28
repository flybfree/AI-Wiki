---
title: Robust Conformalized Selection with Noisy Responses
published: 2026-07-25T01:51:46Z
authors: Chengyao Yu, Hongxin Wei, Bingyi Jing
url: http://arxiv.org/abs/2607.22985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Conformalized Selection with Noisy Responses

## Abstract
Conformalized selection has been widely applied to select high-quality candidates from large datasets with rigorous uncertainty quantification, such as reliable labeling, drug discovery, and the alignment of large language models. Nevertheless, existing methods assume clean responses on calibration data, an assumption that rarely holds in practice. In this paper, we formulate the above tasks as selecting candidates with true predicted labels or with responses exceeding certain values. We demonstrate that existing conformal selection methods fail to control the false discovery rate (FDR) or suffer from severe power loss under contaminated calibration data. To that end, we propose Robust Conformalized Selection (RCS), a unified framework for selective classification with valid FDR control under general label contamination. The key insight of RCS lies in a novel statistical reduction: by separately conditioning on different classes, we translate the intractable label noise into a localized covariate shift problem, which then enables a covariate-adjusted empirical-Bayes-type estimate of the number of false selections. Statistical properties such as the asymptotic FDR control, power optimality, and robustness of RCS are established. We further develop an instantiation of RCS under randomized response model, and also apply RCS to the task of selecting candidates with large response values. Extensive experiments on both simulated and real-world datasets demonstrate the effectiveness of RCS.

## Metadata
- **Published**: 2026-07-25T01:51:46Z
- **Authors**: Chengyao Yu, Hongxin Wei, Bingyi Jing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22985v1)