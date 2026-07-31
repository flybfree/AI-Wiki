---
title: Driving up Inference Energy on SNNs: Per-Sample and Universal Sponge Attacks
url: http://arxiv.org/abs/2607.27990v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_10-36-41Z_DrivingupInferenceEnergyonSNNs_Per_SampleandUniver.md
generated_at: 2026-07-30 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how spiking neural networks can suffer from energy‑intensive attacks that increase the number of synaptic operations per inference while preserving accuracy. It introduces two attack models: a per‑sample sponge attack that optimizes custom spike trains and a universal sponge attack that applies a fixed binary perturbation to all inputs. The results show SynOps inflation ranging from 1.09–2.6 times, translating into overheads of up to 13 mJ per inference on Loihi‑1 hardware.

## Key Takeaways
- A per‑sample sponge attack can raise SynOps by 1.5–2.6× on NMNIST, SHD and IBM DVS Gesture datasets while keeping classification accuracy above 98%.
- The universal sponge attack inflates SynOps by 1.09–1.24× across all three datasets without requiring per‑input optimization.
- Estimated Loihi‑1 energy overheads from these attacks range from 14 μJ to 13.24 mJ per inference, highlighting a non‑negligible battery drain.

## Context
Spiking neural networks are designed for ultra‑low power edge deployment, yet their sparse event‑based communication can be exploited without compromising correctness. This work demonstrates that the energy savings of SNNs may be offset by hidden computational burdens introduced through input‑space attacks.

## Implications
For hardware designers and system integrators, these findings stress the need to consider attack vectors when evaluating real‑world battery performance. Practitioners must adopt robust monitoring beyond mere accuracy checks to detect and mitigate such efficiency‑draining perturbations in always‑on devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27990v1)
