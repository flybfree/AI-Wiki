---
title: A cylindrical neural approximation theorem for conditional laws of McKean-Vlasov equations with common noise
published: 2026-08-08T09:56:54Z
authors: Nacira Agram, Reda Hmioui, Jan Rems
url: http://arxiv.org/abs/2608.08040v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A cylindrical neural approximation theorem for conditional laws of McKean-Vlasov equations with common noise

## Abstract
We introduce conditional cylindrical neural networks for approximating functionals of conditional laws in McKean-Vlasov equations with common noise. Fourier moments of the initial law and truncated signatures of the time augmented common noise are mapped by a mixture density network to a Gaussian mixture approximation of the conditional law. A cylindrical neural network then evaluates the target functional through analytic integrals against this predicted measure.   Rough path well posedness and stability provide a conditional law map that is continuous in the initial distribution and the rough driver and agrees almost surely with the classical conditional law at the Itô Brownian lift. Combining this continuity with Fourier separation, signature uniqueness, Wasserstein density of Gaussian mixtures, and neural universal approximation, we prove an $L^2$ universal approximation theorem for continuous square integrable functionals.   The numerical study implements the resulting two stage procedure on six examples, including non Gaussian initial laws, nonlinear drift, multiplicative common noise, and a two dimensional state. Independent particle references are used when no closed form law is available. The learned conditional law and functional approximations consistently improve on the empirical particle plug in, and additional experiments examine feature sensitivity, training from one terminal observation per common noise scenario, and Itô--Stratonovich consistency.

## Metadata
- **Published**: 2026-08-08T09:56:54Z
- **Authors**: Nacira Agram, Reda Hmioui, Jan Rems
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08040v1)