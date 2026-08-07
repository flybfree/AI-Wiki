---
title: Provably Efficient Self-Calibrating Quantum Fault Tolerance
published: 2026-08-06T07:22:20Z
authors: Weiyuan Gong, Hong-Ye Hu
url: http://arxiv.org/abs/2608.05686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Provably Efficient Self-Calibrating Quantum Fault Tolerance

## Abstract
Quantum error correction protects logical information only when every physical operation remains below the fault-tolerance threshold, a condition that must be maintained continuously rather than only at the initial calibration. In practice, however, analog control parameters inevitably drift because of environmental fluctuations. As future fault-tolerant quantum computations are expected to run for days or even months, interrupting computation for repeated recalibration becomes fundamentally impractical. A promising alternative is to integrate calibration directly into computation by repurposing syndrome measurements as a calibration signal (Sivak et al, Nature 2026), but whether such self-calibration can be achieved with provable efficiency remains an open question. Here we establish a theoretical framework for self-calibrating quantum fault tolerance. We prove that, for a broad class of control-induced errors, the detection rate defines a locally strongly convex surrogate objective for analog calibration with high probability. This geometric property enables efficient online optimization using only syndrome measurements collected during normal error correction. We prove convergence to an $\varepsilon$ detection rate within $O(1/\varepsilon^2)$ epochs for time-independent drifts and also establish guarantees for time-dependent drifts. We further show that the convergence rate is independent of the code distance for quantum low-density parity-check (LDPC) codes. Pulse-level simulations of neutral-atom arrays and large-scale circuit-level Clifford simulations confirm these theoretical predictions. Our results establish self-calibrating fault tolerance as a provably efficient paradigm in which the same syndrome measurements simultaneously protect logical information and stabilize the underlying hardware.

## Metadata
- **Published**: 2026-08-06T07:22:20Z
- **Authors**: Weiyuan Gong, Hong-Ye Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05686v1)