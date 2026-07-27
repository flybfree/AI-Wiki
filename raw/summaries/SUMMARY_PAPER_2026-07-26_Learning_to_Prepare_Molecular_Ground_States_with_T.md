---
title: Learning to Prepare Molecular Ground States with Transformer Models
url: http://arxiv.org/abs/2607.22468v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_16-32-40Z_LearningtoPrepareMolecularGroundStateswithTransfor.md
generated_at: 2026-07-26 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ADAPT-GQE, an AI framework that learns to generate quantum circuits for ground-state preparation in electronic structure calculations. The method trains a transformer model on reference circuits from ADAPT-VQE and uses reinforcement learning to improve circuit accuracy beyond the training data. ADAPT-GQE reduces generation time by orders of magnitude while maintaining or improving state‑preparation accuracy, demonstrated on imipramine hardware.

## Key Takeaways
- The framework leverages ADAPT-VQE generated reference circuits as targets for a transformer model to synthesize new ground-state preparation circuits.
- Reinforcement learning is employed to iteratively improve circuit proposals and scores, achieving higher accuracy than the original training data alone.
- Circuit generation time drops by orders of magnitude compared with ADAPT-VQE while preserving or enhancing state‑preparation fidelity.

## Context
The work advances AI‑driven quantum chemistry by automating the design of complex quantum circuits that are otherwise computationally expensive. It bridges the gap between high‑level algorithmic requirements and practical hardware constraints.

## Implications
This approach enables rapid circuit synthesis for larger molecules relevant to drug discovery and materials science. By cutting generation time, it makes quantum chemistry simulations more feasible on near‑term quantum devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22468v1)
