---
title: Sphere Retraction Normalizations
url: http://arxiv.org/abs/2608.02668v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-02_13-23-49Z_SphereRetractionNormalizations.md
generated_at: 2026-08-05 01:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates alternative retraction maps for spherical residual connections, showing that the family collapses to a single scalar parameter p. It demonstrates Proj‑SpheretNorm and Cay‑SpheretNorm as norm‑preserving algebraic replacements for GeoNorm and exponential map. The optimal performance occurs at finite p.

## Key Takeaways
- The entire family of retraction maps on the hypersphere is determined only by how update magnitude translates to rotation angle within the span of hidden state and update.
- Euclidean residual connections and GeoNorm are unified in this framework, with Proj‑SpheretNorm (metric projection) and Cay‑SpheretNorm (Cayley) as specific instances at p=1 and p=2 respectively.
- The identity map and GeoNorm emerge only as limits of the one‑parameter family, indicating exponential mapping is just one end.

## Context
Deep neural networks rely on residual connections that can be interpreted geometrically. Traditional methods like Geodesic Normalization preserve Euclidean norm but use costly exponential maps; lightweight alternatives are needed for efficient training.

## Implications
These results provide a simple scalar parameter to replace expensive retraction operations, enabling faster and more stable training. Practitioners can tune p to balance stability and performance without altering model architecture.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02668v1)
