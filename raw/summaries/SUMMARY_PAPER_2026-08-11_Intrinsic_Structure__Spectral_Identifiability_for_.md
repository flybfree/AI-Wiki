---
title: Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability
url: http://arxiv.org/abs/2608.10172v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_19-42-01Z_IntrinsicStructure_SpectralIdentifiabilityforMecha.md
generated_at: 2026-08-11 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a framework for mechanistic interpretability based on spectral identifiability, showing that the spectrum of a Koopman operator applied to model activations is a coordinate‑free property of the network. It proves that this spectrum can be recovered from M calibration samples at rate M^{-1/2} up to permutation and provides lower bounds and a dissociation theorem linking variance directions across depth.

## Key Takeaways
- The forward pass is treated as a controlled dynamical system with depth as time, allowing the Koopman operator to produce a finite linear realisation whose spectrum is independent of sampling seeds or width. - Recovery of this spectrum from M calibration samples follows a rate M^{-1/2} up to permutation, establishing an identifiability theorem for mechanistic interpretability. - The spectrum separates activation variance directions from information‑carrying directions when the realisation is non‑normal.

## Context
Mechanistic interpretability seeks to locate circuit‑like patterns in neural networks but often relies on stochastic decoding that may produce artefacts rather than intrinsic features. This work shifts focus to a deterministic, model‑intrinsic invariant—the spectrum—offering a more reliable diagnostic for circuit analysis.

## Implications
For researchers and practitioners, the identifiability theorem provides a quantitative error bar for interpreting network dynamics, reducing reliance on random seeds or width variations. It also suggests that spectral methods can complement traditional decomposition techniques by offering a model‑specific fingerprint with predictable performance across models like GPT‑2 small, Gemma‑2‑2B, and Qwen3‑8B.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10172v1)
