---
title: Coded Hankel Polynomial Chaos: Spectral Identification of Dominant Polynomial-Chaos Modes
url: http://arxiv.org/abs/2608.16126v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_05-32-20Z_CodedHankelPolynomialChaos_SpectralIdentificationo.md
generated_at: 2026-08-17 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces coded Hankel polynomial chaos (CH‑PC) as a spectral method for identifying dominant modes in polynomial chaos expansions. By converting PCE coefficients into a generating polynomial and evaluating on geometric phase orbits, the authors obtain finite exponential sums that encode model order and spectral nodes via low‑rank Hankel matrices. The approach enables exact recovery of dominant modes even with limited observations.

## Key Takeaways
- CH‑PC uses a finite generating transform to convert PCE coefficients into a coefficient‑generating polynomial evaluated along geometric phase orbits, producing an exponential sum whose structure reveals the model order and spectral nodes.
- The method encodes model information in low‑rank Hankel matrices while using coordinate phase shifts with root‑of‑unity labels to recover full multi‑indices without assembling large design matrices.
- For finite data, sampling error and observation error are modeled as separate Hankel perturbations, improving stability through discrete decoding and phase voting.

## Context
In AI and uncertainty quantification, polynomial chaos expansion (PCE) is widely used but suffers from high computational cost for sparse models. Identifying dominant modes efficiently remains a challenge due to noise and limited data. This work offers a spectral alternative that reduces matrix assembly and improves robustness.

## Implications
The CH‑PC framework can accelerate model identification in engineering simulations, climate modeling, and AI‑driven risk assessment where only a few measurements are available. Its ability to handle unknown orders via phase persistence makes it suitable for adaptive systems requiring real‑time updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16126v1)
