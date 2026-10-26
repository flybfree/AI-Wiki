---
title: Decode Late, Multiply Once: Rethinking the Dot Product for Quantized Weights
published: 2026-10-22T21:05:59Z
authors: Jonathan Tapson
url: http://arxiv.org/abs/2610.31913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decode Late, Multiply Once: Rethinking the Dot Product for Quantized Weights

## Abstract
Large neural networks are increasingly deployed with 1-4 bit weights and 16- or 32-bit activations, yet their dot products still use one multiplier per element. We show that a length-n dot product with k-bit weight codes can be computed with n+2^k additions and at most 2^k decodes and 2^k multiplications. Each weight code is used directly as an address offset that selects one of 2^k accumulators; each activation is added into the selected accumulator; and the accumulated sums are decoded and multiplied only once, at the end, in a fused decode-and-multiply step. The decoded weight vector is never formed. The refactoring is exact for integer arithmetic, works with integer or floating-point operands and with arbitrary, including nonlinear, decoders, and extends to group-wise scales and to matrix and tensor products. The multiplier count falls by n/2^k, while total arithmetic energy improves by a smaller, bounded factor that we quantify with a cost model. We describe a scatter-accumulate processing element (SA-PE) that replaces the MAC unit in a weight-stationary systolic array, with a load/stream/reduce/drain schedule in which a small, time-shareable multiplier runs only 2^k times per tile. Because decoded weights are not stored, local weight memory shrinks by up to w_d/k for w_d-bit decoded weights. An RTL implementation synthesized for FPGA and compared with a matched MAC array shows that an unshared SA-PE is larger than a MAC PE, and that the saving appears when the reduction multiplier is shared across PEs. Software models confirm exact integer equivalence and floating-point error no worse than the conventional pipeline. We do not claim the underlying identity is new, and we discuss related work on weight sharing and lookup-based kernels.

## Metadata
- **Published**: 2026-10-22T21:05:59Z
- **Authors**: Jonathan Tapson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31913v1)