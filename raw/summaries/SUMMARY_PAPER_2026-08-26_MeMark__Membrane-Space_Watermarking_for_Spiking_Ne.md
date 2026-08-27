---
title: MeMark: Membrane-Space Watermarking for Spiking Neural Networks
url: http://arxiv.org/abs/2608.25738v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_12-50-09Z_MeMark_Membrane_SpaceWatermarkingforSpikingNeuralN.md
generated_at: 2026-08-26 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MeMark, a watermarking technique that embeds multi‑bit identifiers into the membrane states of selected Leaky Integrate-and-Fire neurons within Spiking Neural Networks. The watermark survives checkpoint reuse and fine‑tuning while remaining verifiable through a simple threshold check without requiring a learned decoder.

## Key Takeaways
- MeMark stores ownership evidence in internal neuron membranes rather than output heads, preventing attackers from removing verification signals by replacing the head.  
- Verification is performed via a fixed 51/64 rule using the same firing threshold that set each bit, eliminating the need for a decoder.  
- The watermark remains intact across extensive modifications such as pruning, quantization, and output‑head replacement, passing all 20 independent 64‑bit keys.

## Context
Spiking Neural Networks are gaining traction as lightweight, energy‑efficient models that can be distributed as pretrained checkpoints. Existing verification methods rely on output signatures, which become ineffective when the network backbone is reused or heavily altered, creating a gap in protecting model provenance.

## Implications
MeMark offers a practical solution for ensuring ownership of neural checkpoint derivatives across diverse architectures and deployment environments. Practitioners can embed provenance without compromising model performance, fostering trustworthy AI ecosystems where models are shared and repurposed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25738v1)
