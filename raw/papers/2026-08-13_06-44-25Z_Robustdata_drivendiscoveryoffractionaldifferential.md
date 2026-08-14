---
title: Robust data-driven discovery of fractional differential equations via weak formulations and Pareto-based subset selection
published: 2026-08-13T06:44:25Z
authors: Pongpisit Thanasutives, Yoshinobu Kawahara
url: http://arxiv.org/abs/2608.12879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust data-driven discovery of fractional differential equations via weak formulations and Pareto-based subset selection

## Abstract
Fractional partial differential equations describe nonlocal dynamics, but discovering them from noisy data is difficult because fractional differentiation amplifies high-frequency measurement noise and the derivative orders are unknown. We propose Weak-Pareto, which combines an adjoint-consistent weak formulation of fractional terms with Pareto-based subset selection over discrete term types and continuous fractional orders. For linear right-hand-side terms, the adjoint transfers fractional operators from measured fields to smooth test functions, replacing noise-sensitive pointwise differentiation with smoothing integration; for nonlinear terms, the noise-suppression effect is partial yet useful. Coefficients are fitted by ridge regression within a branch-aware differential-evolution search over the orders. The support size is then selected at the validation-error-complexity elbow. We show that the variance of fixed linear right-hand-side weak features vanishes under grid refinement, whereas noise amplification in pointwise fractional features increases with derivative order. Across fractional advection-diffusion, reaction-diffusion, and Burgers benchmarks, Weak-Pareto recovers parsimonious structures from clean and noisy measurements. In controlled advection-diffusion and Burgers comparisons, it retains the correct support at every tested multiplicative-noise level, whereas the unregularised strong-form counterpart largely fails once noise is introduced; this advantage persists under additive Gaussian noise. Ablations show that the weak library drives noise robustness and that continuous-order Pareto search avoids the support-selection failure of a dense fixed dictionary. On the advection-diffusion benchmark, Weak-Pareto yields more consistent operator recovery and substantially lower measured runtime than a contemporary neural baseline.

## Metadata
- **Published**: 2026-08-13T06:44:25Z
- **Authors**: Pongpisit Thanasutives, Yoshinobu Kawahara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12879v1)