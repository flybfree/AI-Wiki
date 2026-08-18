---
title: Spectral Gaps of Hit-and-Run and Coordinate Hit-and-Run
url: http://arxiv.org/abs/2608.16878v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-57-11Z_SpectralGapsofHit_and_RunandCoordinateHit_and_Run.md
generated_at: 2026-08-17 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper derives a spectral gap for the Hit-and-Run and Coordinate Hit-and-Run Markov chains using dual certificates linked to functional isoperimetric constants, improving convergence rates compared to conductance‑based proofs. It shows the gap is Ω(1/(n^2 C_PI)) and provides explicit mixing time bounds.

## Key Takeaways
- The spectral gap of Hit-and-Run is bounded by O(n^2 C_PI log(M/ε)), replacing the earlier O(n^2 R^2) bound.
- For nearly isotropic bodies, the complexity becomes O(n^2 log n log(M/ε)) thanks to KLS conjecture progress.
- Coordinate Hit-and-Run gains a much improved mixing time of O(n^3 C_PI log(M/ε)).

## Context
The work addresses a longstanding challenge in random walk analysis by connecting spectral properties to geometric constants, similar to the Ball walk study. This dual‑certificate approach offers a more principled foundation than conductance estimates.

## Implications
These results enable faster convergence of Hit-and-Run algorithms in high‑dimensional settings and open pathways for optimizing sampling methods that rely on such walks. Practitioners can leverage tighter bounds to reduce computational cost when approximating uniform distributions over convex bodies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16878v1)
