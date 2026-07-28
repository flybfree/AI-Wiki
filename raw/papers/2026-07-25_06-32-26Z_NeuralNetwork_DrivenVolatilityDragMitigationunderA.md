---
title: Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage
published: 2026-07-25T06:32:26Z
authors: Christian Bongiorno, Efstratios Manolakis, Rosario Nunzio Mantegna
url: http://arxiv.org/abs/2607.23068v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage

## Abstract
This paper introduces a compact reformulation of a modular end-to-end neural network for global minimum-variance portfolio optimization that decouples model complexity from both look-back window length and universe size. A five-parameter hyperbolic weighted moving average combined with a saturating exponential replaces the original 2,400-parameter lag-transformation layer, and a bidirectional gated-recurrent-unit eigencleaning module together with a streamlined marginal-volatility network reduce total learnable parameters from 39,586 to just 2,175. In out-of-sample tests against state-of-the-art nonlinear-shrinkage and risk-parity benchmarks, the compact network attains the lowest realized portfolio variance without compromising expected return. Under long-only constraints, the variance reduction supports substantially higher leverage while maintaining comparable drawdown control. Validation in a high-fidelity trading simulator that incorporates realistic margin-call dynamics confirms enhanced over-leverage resilience. These findings demonstrate that end-to-end variance-minimization architectures can achieve substantial parameter efficiency and robust capital-efficiency gains without sacrificing risk-adjusted performance.

## Metadata
- **Published**: 2026-07-25T06:32:26Z
- **Authors**: Christian Bongiorno, Efstratios Manolakis, Rosario Nunzio Mantegna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23068v1)