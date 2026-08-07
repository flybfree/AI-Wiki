---
title: One Qubit Can Beat One Bit: Quantum Advantage for Post-Training Quantization
url: http://arxiv.org/abs/2608.05240v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_14-04-50Z_OneQubitCanBeatOneBit_QuantumAdvantageforPost_Trai.md
generated_at: 2026-08-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Quantum Random Access Quantization (QRAQ) which overcomes the limitation of one-bit post-training quantization by encoding context-dependent sign patterns in a quantum random-access code. It shows that QRAQ can achieve lower ideal reconstruction risk than shared-sign PTQ when optimal signs differ across contexts, using Pauli measurements and a fresh-copy logical readout model.

## Key Takeaways
- The framework encodes each weight's sign according to its activation context into a quantum random-access code, allowing retrieval via context-matched Pauli measurements.
- QRAQ provides an unbiased binary surrogate with a tractable shot-noise penalty under the fresh-copy logical readout assumption, separating row-wise scales from shared-sign constraints.
- When optimal signs are incompatible across contexts, QRAQ yields strictly lower reconstruction risk than one-bit PTQ, and this advantage holds under finite-shot and calibrated-noise conditions.

## Context
This work addresses a fundamental bottleneck in deploying quantized AI models where weight quantization must be uniform across different inference scenarios. By leveraging quantum measurement resources to resolve context-specific sign information, the paper demonstrates that quantum hardware can provide advantages beyond classical simulation limits.

## Implications
For practitioners, QRAQ suggests that quantum-enhanced quantization schemes could enable more accurate and efficient model deployment without sacrificing performance. Industry adoption may be limited by current hardware constraints, but the theoretical separation highlights a path toward hybrid classical-quantum inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05240v1)
