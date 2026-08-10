---
title: QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting
published: 2026-08-07T16:05:21Z
authors: Junkai Lin, Siqi Hou, Raymond Lee
url: http://arxiv.org/abs/2608.07363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting

## Abstract
Forecasting non-stationary time series remains difficult due to long-range dependencies, local volatility bursts, structural shifts, and nonlinear oscillatory behaviors. Although Transformer-based forecasters are effective for modeling long-term temporal dependencies, their feed-forward blocks typically rely on smooth static activations that are insufficiently sensitive to abrupt regime changes. Motivated by quantitative Transformer designs and oscillator-based nonlinear activations, we propose QFCQT, short for Quantum-Fractal-inspired Chaotically Gated Quantformer, for robust forecasting under complex volatile dynamics. Here, "quantum-fractal-inspired" denotes a computational analogy based on soft oscillator superposition and multi-scale nonlinear responses, rather than a formal quantum-mechanical or fractal-theoretic derivation. QFCQT consists of three main components: (1) a Quantformer-style numerical encoder that directly processes multivariate inputs via linear embedding; (2) a learnable Lee-oscillator activation module that maps scalar pre-activations to dynamic oscillatory responses and summarizes them through Max-over-Time pooling; and (3) a smooth-chaotic gated fusion mechanism that adaptively balances conventional smooth activations and chaos-sensitive responses. Furthermore, instead of using a single fixed oscillator, QFCQT employs a soft superposition of eight parameterized Lee oscillator families to adaptively capture different nonlinear response patterns across regimes. Experiments on ETTh1, ETTh2, and A-share Stock Index benchmarks show that QFCQT consistently outperforms strong baselines, including Informer, LogTrans, LSTMa, HAT, and COTN.

## Metadata
- **Published**: 2026-08-07T16:05:21Z
- **Authors**: Junkai Lin, Siqi Hou, Raymond Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07363v1)