---
title: Expressivity In Multimodal Contrastive Learning
url: http://arxiv.org/abs/2608.17203v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_23-29-17Z_ExpressivityInMultimodalContrastiveLearning.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the expressive power of multimodal contrastive learning architectures by framing representational capacity as a problem of approximating joint distributions with parameterized densities. It demonstrates that while simple two‑tower CLIP can approximate any joint distribution, a pairwise‑sum loss used in three‑plus modality models cannot, though it still matches all conditional relationships. The authors introduce Hadamard‑CLIP, which restores universal approximation for any number of modalities.

## Key Takeaways
- Two‑tower CLIP is a universal approximator for binary modalities, meaning its parameterized densities can approximate the joint distribution to arbitrary accuracy.
- Pairwise similarity summation in three‑plus modality models cannot represent all possible joint distributions but retains expressivity sufficient to capture every pairwise conditional mapping.
- Adding a single learned weight vector (Hadamard‑CLIP) to existing encoders restores universal approximation across any number of modalities while keeping the fast, precomputable embedding retrieval.

## Context
The study addresses a longstanding gap in multimodal AI where model capacity is not fully characterized despite widespread use. Understanding expressivity helps researchers design more flexible architectures without sacrificing computational efficiency.

## Implications
For practitioners, Hadamard‑CLIP offers a simple upgrade that unlocks full joint distribution approximation, potentially improving retrieval and generation quality across diverse modalities. Industry adoption could lead to better multimodal systems with minimal engineering effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17203v1)
