---
title: EEGForceFusion: Joint Tokenised-Continuous Representation Learning for Subject-Independent Grasp Force Decoding
url: http://arxiv.org/abs/2607.24126v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_08-08-08Z_EEGForceFusion_JointTokenised_ContinuousRepresenta.md
generated_at: 2026-07-27 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EEGForceFusion, a hybrid model that learns both continuous and tokenised representations of neural activity to decode grasp force subject‑independently. It combines convolutional‑recurrent networks, quantisation‑based tokenisation, and transformer temporal modelling within a unified regression architecture. Experiments on WAY‑EEG‑GAL show high R² scores in offline and simulated real‑time settings.

## Key Takeaways
- The model jointly captures fine‑grained neural dynamics through continuous signals while also representing them as discrete tokens for long‑range dependencies, improving temporal resolution.
- Quantisation‑driven tokenisation reduces data dimensionality without losing information, enabling efficient transformer processing of EEG sequences.
- Leave‑one‑subject‑out evaluation yields R² = 0.817 offline and R² = 0.793 in real‑time simulation, demonstrating strong cross‑subject generalisation.

## Context
Current brain‑machine interfaces rely on either purely continuous or tokenised representations, each with limitations in handling temporal complexity or inter‑subject variability. This work bridges the gap by integrating both modalities within a single framework, aligning with trends toward modular yet unified deep learning architectures for neuro‑control tasks.

## Implications
The findings provide a practical pathway for real‑time EEG force decoding that can be deployed in assistive robotics and neuro‑rehabilitation systems where latency is critical. Practitioners can adopt the hybrid tokenisation strategy to balance accuracy with computational efficiency, fostering scalable human‑machine interaction solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24126v1)
