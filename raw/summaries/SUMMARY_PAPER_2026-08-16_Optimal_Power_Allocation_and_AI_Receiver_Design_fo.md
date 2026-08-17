---
title: Optimal Power Allocation and AI Receiver Design for Superimposed DMRS and Data Transmission
url: http://arxiv.org/abs/2608.13809v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_22-42-42Z_OptimalPowerAllocationandAIReceiverDesignforSuperi.md
generated_at: 2026-08-16 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of transmitting superimposed demodulation‑reference‑symbol (DMRS) and data in OFDM MIMO systems by deriving an analytical framework for the iterative behavior between channel estimation error mean‑square errors and detection error. The framework enables optimal power allocation and pilot pattern design, which are then applied to a transformer‑based AI receiver that incorporates the same iterative CE‑MD process. Simulations show the AI‑ICED receiver with SI‑DMRS yields higher spectral efficiency than conventional non‑overlapped schemes.

## Key Takeaways
- The analytical framework quantifies how mean‑square errors of channel estimation and MIMO detection evolve during an iterative CE‑MD loop, providing a basis for power allocation decisions.  
- Optimal power is allocated between DMRS pilot symbols and data symbols to balance error reduction with spectral efficiency gains in SI‑DMRS transmission.  
- The transformer encoder receiver leverages the same iterative structure, achieving superior SE compared to traditional receivers that lack such iteration.

## Context
The integration of AI components into communication receivers reflects a broader trend toward adaptive signal processing that can exploit complex channel dynamics. By embedding an iterative CE‑MD loop within a neural network architecture, the system learns optimal pilot usage in real time, moving beyond static equalization methods.

## Implications
For wireless network designers, this work offers a practical blueprint for boosting spectral efficiency without sacrificing reliability. Practitioners can implement transformer‑based receivers that automatically adjust power between DMRS and data streams, delivering tangible performance improvements across MIMO deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13809v1)
