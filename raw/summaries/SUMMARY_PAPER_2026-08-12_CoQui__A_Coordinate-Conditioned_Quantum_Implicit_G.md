---
title: CoQui: A Coordinate-Conditioned Quantum Implicit Generative Adversarial Network for End-to-End Image Generation
url: http://arxiv.org/abs/2608.11884v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_10-10-22Z_CoQui_ACoordinate_ConditionedQuantumImplicitGenera.md
generated_at: 2026-08-12 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoQui, a coordinate‑conditioned quantum implicit generative adversarial network that generates images by evaluating a variational quantum circuit at each spatial pixel. By embedding coordinates and latent variables into classical parameters and reading color qubits directly, the method decouples image resolution from address‑qubit usage and avoids shared probability constraints. Simulations demonstrate superior visual and quantitative quality compared to existing QGAN baselines while using fewer qubits.

## Key Takeaways
- CoQui replaces amplitude encoding with a coordinate‑conditioned approach that queries a dedicated color qubit per pixel, eliminating the need for high‑resolution address registers.  
- The design removes shared probability normalization across pixels, allowing independent intensity control and reducing resource growth with image size.  
- A specialized variational circuit provides structural inductive bias, improving generation fidelity over FRQI‑based and PQWGAN methods.

## Context
Quantum generative models aim to leverage quantum circuits for image synthesis while mitigating the exponential qubit scaling of classical approaches. This work advances implicit learning techniques in quantum settings, offering a pathway toward scalable quantum AI beyond limited amplitude‑based schemes.

## Implications
CoQui’s coordinate‑conditioned framework could enable practical quantum image generation on near‑term devices with modest qubit counts. Practitioners may adopt this model to design efficient quantum generative pipelines that balance fidelity and resource constraints in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11884v1)
