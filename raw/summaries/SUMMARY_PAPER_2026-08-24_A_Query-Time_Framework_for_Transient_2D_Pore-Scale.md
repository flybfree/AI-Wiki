---
title: A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design
url: http://arxiv.org/abs/2608.22235v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_06-13-10Z_AQuery_TimeFrameworkforTransient2DPore_ScaleFlowPr.md
generated_at: 2026-08-24 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a query‑time framework that predicts transient pore‑scale flow for two‑dimensional porous structures without re‑running lattice Boltzmann simulations. By training a continuous‑time surrogate model on 7 606 geometry–state pairs, the method achieves low relative velocity errors and modest permeability inaccuracies, enabling fast design screening of thousands of generative candidates.

## Key Takeaways
- The CT‑PoreFlow surrogate integrates topology‑aware encoding, compressed spectral mixing, and log‑time conditioning to approximate flow with a 0.2248 L2 error on unseen geometries.  
- Frozen morphology audits confirm cross‑geometry robustness without fine‑tuning the model.  
- Embedding the surrogate in an inverse design workflow screened 9 216 GAN and diffusion candidates, yielding 98.11% through‑connectivity and 72.28% conditional success rates.

## Context
This work advances AI‑driven porous media engineering by replacing expensive LBM simulations with a learned surrogate that respects the underlying topology. The approach aligns with broader trends in physics‑informed neural networks, where surrogate models accelerate inverse optimization problems across complex geometries.

## Implications
Engineers can now evaluate thousands of design alternatives within minutes, reducing computational cost and time to market for filtration, oil recovery, and environmental remediation systems. Practitioners gain a scalable tool that bridges generative design with accurate transient flow predictions without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22235v1)
