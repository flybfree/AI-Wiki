---
title: One Qubit Can Beat One Bit: Quantum Advantage for Post-Training Quantization
published: 2026-08-05T14:04:50Z
authors: Yuma Ichikawa, Moeto Mishima
url: http://arxiv.org/abs/2608.05240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Qubit Can Beat One Bit: Quantum Advantage for Post-Training Quantization

## Abstract
One-bit post-training quantization represents each weight using only its sign, requiring all deployment contexts to share the same binary weight matrix even when their activation statistics favor different sign patterns. We study this shared-sign constraint and introduce Quantum Random Access Quantization (QRAQ). This framework encodes context-dependent signs in a quantum random-access code and retrieves them via context-matched Pauli measurements. Under an explicit fresh-copy logical readout model, QRAQ produces an unbiased, context-specific binary surrogate with a tractable shot-noise penalty. We prove a row-wise separation from shared-sign one-bit PTQ with signed per-row scales. When the optimal context-wise signs are incompatible, QRAQ achieves a strictly lower ideal reconstruction risk. We also derive finite-shot and calibrated-noise conditions under which this separation is retained. Fixed-readout quantum schemes are classically simulable, so the relevant resource in this model is measurement incompatibility rather than quantization alone. Finally, we characterize the role of scale granularity, provide finite-sample certificates, and evaluate the predicted ideal, finite-shot, noisy, and multi-context regimes in simulator experiments.

## Metadata
- **Published**: 2026-08-05T14:04:50Z
- **Authors**: Yuma Ichikawa, Moeto Mishima
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05240v1)