---
title: RELTA-SGLD: Relative-Growth Localized Taming for Nonconvex Stochastic-Gradient Langevin Learning
published: 2026-07-21T19:43:54Z
authors: Yiwei Zhou, Ziheng Chen
url: http://arxiv.org/abs/2607.19544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RELTA-SGLD: Relative-Growth Localized Taming for Nonconvex Stochastic-Gradient Langevin Learning

## Abstract
We introduce RELTA-SGLD, a taming scheme that stabilizes superlinear stochastic-gradient updates while reducing unnecessary suppression of the original learning drift. A threshold determines where the taming turns on, while a relative-growth principle derived from the one-step Lyapunov stability condition determines the required taming strength. Together, they produce a lighter $λ$-scale denominator and preserve a nonvanishing far-tail return. As a consequence, we prove polynomial moment stability and first-order stationary accuracy in both $W_1$ and $W_2$ for nonconvex SGLD with superlinearly growing stochastic-gradient oracles, improving the corresponding half-order and quarter-order bounds for comparable stochastic-gradient tamed schemes. On Fashion-MNIST under active stabilization pressure, RELTA improves the mean learning metrics over both untamed SGLD and TUSLA and remains competitive with a tuned AdamW reference. In an ordinary-training regime, its lighter localized denominator reduces unnecessary perturbation of the original update and maintains nearly untamed learning dynamics.

## Metadata
- **Published**: 2026-07-21T19:43:54Z
- **Authors**: Yiwei Zhou, Ziheng Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19544v1)