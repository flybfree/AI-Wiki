---
title: AudioTQ: A Data-Oblivious 6-Bit CPU Audio Codec via Randomized Hadamard Rotation and Lloyd-Max Quantization
url: http://arxiv.org/abs/2608.15369v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_18-44-27Z_AudioTQ_AData_Oblivious6_BitCPUAudioCodecviaRandom.md
generated_at: 2026-08-17 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AudioTQ, a data‑oblivious lossy audio codec that operates directly in the time domain without relying on psychoacoustic models or frequency transforms. By applying a randomized Fast Walsh‑Hadamard Transform (FWHT) rotation and an offline‑trained 6‑bit Lloyd‑Max quantizer with a residual correction layer, AudioTQ achieves up to 74.4 % physical size reduction while maintaining an SQNR of about 30 dB. The codec is designed for real‑time single‑threaded execution on standard CPU registers.

## Key Takeaways
- Uniformizes volatile time‑domain amplitudes into a predictable standard normal distribution using an orthonormal, randomized Fast Walsh‑Hadamard Transform (FWHT) rotation.
- Utilizes an offline‑trained, MSE‑optimal 6‑bit Lloyd‑Max quantizer complemented by a 1‑bit Quantized Joint Least‑Squares residual correction layer to produce 7‑bit virtual indices packed into native 8‑bit containers.
- Demonstrates up to 74.4 % physical size reduction and an SQNR of ~30 dB, enabling efficient real‑time audio processing without hardware accelerators.

## Context
AudioTQ’s approach mirrors techniques from Large Language Model weight quantization such as TurboQuant, where random rotations and offline training are used to reduce bit depth while preserving quality. This demonstrates that similar mathematical principles can be applied across domains, highlighting a trend toward data‑oblivious compression in AI research.

## Implications
For the audio industry, AudioTQ offers a lightweight codec suitable for streaming services and low‑power devices, reducing bandwidth and power consumption without sacrificing perceptibility. Practitioners can adopt its simple pipeline—randomized FWHT rotation followed by Lloyd‑Max quantization—to create efficient data‑oblivious compressors for other signal types.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15369v1)
