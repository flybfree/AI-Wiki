---
title: End-to-End Neural Decomposition with Koopman Operators for Time-Series Forecasting
published: 2026-08-09T16:08:54Z
authors: De-Yan Lu, Xugang Lu, Yu Tsao, Jian-Jiun Ding
url: http://arxiv.org/abs/2608.08788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# End-to-End Neural Decomposition with Koopman Operators for Time-Series Forecasting

## Abstract
Koopman theory offers a linear-operator view of nonlinear sequence dynamics by lifting observations into a space where evolution is governed by a linear time-invariant Koopman operator. While the Koopman operator provides a linear representation of nonlinear dynamics, it is generally infinite dimensional and defined under time-invariant assumptions. To model non-stationary signals with frequency-dependent behavior, a frequency-varying extension is required. In recent years, deep learning has been increasingly employed to exploit its powerful function-approximation ability for learning the Koopman operator. In this study, we propose a novel approach called neural decomposition Koopman (NDKoop), an end-to-end architecture that integrates a learnable signal decomposition module with both frequency-independent and frequency-dependent Koopman based networks for sequence forecasting. To the best of our knowledge, this is the first work to jointly realize end-to end Koopman modeling and signal decomposition within a unified neural framework. We demonstrate that decomposing a signal into a frequency-independent trend component and a frequency-dependent periodic component, each governed by a corresponding Koopman operator, improves prediction accuracy when perfect linearization is unattainable. Numerical experiments across several forecasting benchmarks indicate that the proposed NDKoop provides strong performance.

## Metadata
- **Published**: 2026-08-09T16:08:54Z
- **Authors**: De-Yan Lu, Xugang Lu, Yu Tsao, Jian-Jiun Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08788v1)