---
title: IQ-JEPA: A Joint-Embedding Predictive Architecture with a Hermitian Vision Transformer for Sound Speed and Attenuation Estimation from Ultrasound IQ Data
url: http://arxiv.org/abs/2607.22351v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_14-31-54Z_IQ_JEPA_AJoint_EmbeddingPredictiveArchitecturewith.md
generated_at: 2026-07-26 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IQ-JEPA, a joint‑embedding predictive architecture that learns to estimate sound speed and attenuation from ultrasound in‑phase and quadrature (IQ) data. By combining unlabeled fullwave simulations with a small set of labeled maps, the method achieves high accuracy while using far fewer labels than conventional supervised solvers.

## Key Takeaways
- The Hermitian vision transformer encoder pretrained on 63,435 unlabeled acquisitions reaches an average sound speed of 15.60 m/s with only 10,000 labeled simulations, showing a threefold improvement in label efficiency over supervised training.
- Sound speed is encoded as the phase difference between IQ channels, which the transformer reads invariantly through equivariant attention and conjugate‑product feed‑forward layers.
- The frozen encoder’s latent features directly expose sound speed and attenuation, allowing cross‑distribution pretraining between layered and abdominal phantoms with minimal loss.

## Context
Self‑supervised learning has become a dominant strategy for building foundation models that require little or no labeled data. In medical imaging, this approach promises to reduce the need for costly ground truth labels while improving robustness across different phantom types.

## Implications
For ultrasound practitioners, IQ-JEPA offers a practical way to estimate tissue properties without additional measurements, potentially speeding up diagnosis and guiding probe placement. The method’s foundation‑model nature could be extended to other quantitative imaging modalities that rely on complex signal representations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22351v1)
