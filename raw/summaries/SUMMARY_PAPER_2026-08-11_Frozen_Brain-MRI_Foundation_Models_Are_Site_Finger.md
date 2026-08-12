---
title: Frozen Brain-MRI Foundation Models Are Site Fingerprints
url: http://arxiv.org/abs/2608.10295v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_23-03-21Z_FrozenBrain_MRIFoundationModelsAreSiteFingerprints.md
generated_at: 2026-08-11 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits frozen foundation‑model (FM) embeddings for brain‑MRI and discovers that acquisition site is a major intrinsic component of the representation. Across two independent cohorts and three encoder types, site is linearly decodable with roughly 0.9 balanced accuracy at deep layers, surpassing all clinical or demographic variables. This effect originates from low‑level image statistics preserved by any encoder, not from pretraining.

## Key Takeaways
- Site is linearly decodable with ~0.9 balanced accuracy at deep layers across three encoders and network depths.
- Even a randomly initialized encoder already behaves as a site classifier, indicating the fingerprint reflects low‑level image statistics that any encoder preserves rather than a product of pretraining.
- Removing the site subspace via null‑space projection or ComBat reduces decodability to near zero, showing a distinct site subspace entangled with anatomy.

## Context
Foundation models are widely adopted for brain‑MRI analysis, often assumed to capture only anatomical content. This work reveals that these models also encode acquisition site information, challenging the assumption of pure content representation and highlighting potential biases in model outputs.

## Implications
Practitioners must audit frozen FM embeddings for site bias before using them in shared or federated settings. While post‑hoc removal can suppress site signals, it is not free because site and anatomy share a linear subspace; thus, careful handling of this entangled component is essential for fair and reliable AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10295v1)
