---
title: State Propagation Also Satisfies: A Complex-Valued State-Space Model for Deterministic State Tracking
published: 2026-08-04T10:16:24Z
authors: Xiaohe Li, Yang Lu
url: http://arxiv.org/abs/2608.03425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# State Propagation Also Satisfies: A Complex-Valued State-Space Model for Deterministic State Tracking

## Abstract
Transformer-based architectures have dominated sequence modeling, largely due to the expressive power of attention mechanisms. However, for a class of deterministic state tracking tasks---such as parity checking, modular counting, and parenthesis matching---attention may be overkill. In this paper, we show that \textbf{state propagation alone is sufficient}.   We propose the \textbf{Complex State Propagator (CSP)}, a minimalistic recurrent architecture that \textbf{only propagates hidden states} across layers without output projections at intermediate steps. The state is represented as a complex-valued vector, updated via input-dependent rotations in the complex domain. To enable deep propagation without gradient vanishing or degradation, we introduce a \textbf{block-level skip connection} alongside element-wise complex normalization and SiLU activation at sequence boundaries. Applied with Focal Loss, CSP achieves \textbf{100\% accuracy} with perfect F1 scores across canonical tasks.

## Metadata
- **Published**: 2026-08-04T10:16:24Z
- **Authors**: Xiaohe Li, Yang Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03425v1)