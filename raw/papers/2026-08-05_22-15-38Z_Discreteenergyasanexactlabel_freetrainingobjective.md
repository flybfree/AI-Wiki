---
title: Discrete energy as an exact label-free training objective for finite-element surrogates
published: 2026-08-05T22:15:38Z
authors: Ruifeng Cao, Xidan Song
url: http://arxiv.org/abs/2608.05437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discrete energy as an exact label-free training objective for finite-element surrogates

## Abstract
Supervised training of finite-element (FE) surrogate models requires reference solutions, and each reference solution is obtained by solving the system that the surrogate is intended to replace. The assembled discrete potential energy provides a training signal that requires no reference solution. This note records, with proofs, the identities that make this signal exact for linear elastostatics: the difference between the energy of a prediction and the energy of the reference solution equals one half of the squared stiffness-norm error, and the gradient of the energy equals the stiffness-weighted error. Label-free discrete-energy minimisation and supervised regression in the stiffness norm therefore have the same unique minimiser and identical gradients at every point. Around this central result, the note states a conditioning lemma that bounds the displacement error by the energy gap, a modewise contraction identity that explains why the Euclidean displacement error is an unsuitable primary metric, the Chebyshev bound that governs conjugate-gradient post-processing of surrogate predictions, and a conditional latent-separation proposition for joint-embedding predictive architecture (JEPA) pretraining on a shared stiffness operator, with an explicit numerical counterexample that delimits its scope. Every claim with numeric content is implemented as an executable falsification check; the checks were executed twice, on synthetic test problems and on a probe set of 16 instances from the validation split of a pre-registered experimental run, and every inequality holds, with the measured tightness reported. A closing section explains why the construction does not extend to elastodynamics through direct minimisation of the action functional, and which time-discrete formulation restores exactness.

## Metadata
- **Published**: 2026-08-05T22:15:38Z
- **Authors**: Ruifeng Cao, Xidan Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05437v1)