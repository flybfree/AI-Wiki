---
title: Enhancing Irregular Time Series Forecasting with Continuous-Time Modeling Framework
published: 2026-07-30T11:18:18Z
authors: Tianen Shen, Zhengyu Li, Yutong Li, Xiangfei Qiu, Xingjian Wu, Bin Yang, Jilin Hu
url: http://arxiv.org/abs/2607.28035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Irregular Time Series Forecasting with Continuous-Time Modeling Framework

## Abstract
Irregular multivariate time series are widely encountered in applications such as healthcare monitoring, human activity recognition, and environmental sensing. Their core challenges stem from asynchronous observations, non-uniform sampling intervals, and the fact that temporal patterns themselves carry critical dynamic information. Existing approaches either rely on discretization-based preprocessing (e.g., interpolation, imputation, or aggregation), which disrupts the underlying continuous-time semantics, or adopt continuous-time modeling via ODE-based frameworks, which typically require specialized architectures and incur substantial computational overhead due to numerical solvers. To address these limitations, we propose WrapFlow, a continuous-time modeling framework for irregular time series forecasting. On the input side, WrapFlow introduces Continuous-Time Tokenization, which directly encodes raw observation events and explicitly models long unobserved intervals via gap-aware tokens. The resulting continuous-time tokens are then processed by a standard Transformer backbone to capture long-range temporal dependencies. On the output side, we develop a simulation-free training paradigm for Residual Flow Matching, which learns conditional residual vector fields around base predictions while avoiding numerical-solver simulation and backpropagation during training. This design enables high-quality continuous forecasting using only a small number of fixed rollout steps at inference. Extensive experiments on multiple real-world datasets demonstrate that WrapFlow achieves state-of-the-art performance.

## Metadata
- **Published**: 2026-07-30T11:18:18Z
- **Authors**: Tianen Shen, Zhengyu Li, Yutong Li, Xiangfei Qiu, Xingjian Wu, Bin Yang, Jilin Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28035v1)