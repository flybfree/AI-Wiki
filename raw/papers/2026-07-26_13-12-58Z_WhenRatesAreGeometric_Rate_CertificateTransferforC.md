---
title: When Rates Are Geometric: Rate-Certificate Transfer for Contact Splittings in Optimization
published: 2026-07-26T13:12:58Z
authors: George A Kevrekidis
url: http://arxiv.org/abs/2607.23642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Rates Are Geometric: Rate-Certificate Transfer for Contact Splittings in Optimization

## Abstract
Discrete optimization algorithms are often analyzed through continuous-time limiting ODEs, but a convergence certificate for the ODE is not automatically one for the discrete algorithm. We develop contact Hamiltonian systems as a setting where the transfer can be made precise. A contact Hamiltonian $H$ on $J^1(\mathbb{R}^n)$ obeys the intrinsic decay identity $\dot H = -H\,\partial_s H$, so an augmented energy $\mathcal{E}$ built from $H$, together with the conformal rate $\partial_s H$, is a continuous-time rate certificate whenever $\mathcal{E}$ controls the objective gap. Our main theorem states, under three named and independently checkable hypotheses, that an order-$r$ contact splitting with step $h$ transfers this certificate over the finite horizon set by backward error analysis. The discrete decay envelope is governed by the modified conformal factor up to $O(h^r)$ perturbations plus a backward-error shadowing defect, and the mechanism is inherited exactly because the modified Hamiltonian is itself a contact Hamiltonian. Quadratic heavy ball is a fully solvable example: its projected dissipative-leapfrog spectrum agrees with established conformal-symplectic optimization theory, while the augmented contact Hamiltonian yields a sharp objective-to-certificate comparison that verifies the transfer hypotheses. For strongly convex objectives with state-dependent damping, an explicit Bregman-type Lyapunov certificate instead transfers by an auxiliary-shadowing corollary. The decomposition $H=K+V+D$ into kinetic, objective-encoding potential, and dissipation terms serves as a design template, with a catalogue of closed-form sub-flows including contact-specific damping families. Numerical experiments confirm the predicted conformal-factor tracking orders and show competitive performance on ill-conditioned benchmarks and deep-learning tasks.

## Metadata
- **Published**: 2026-07-26T13:12:58Z
- **Authors**: George A Kevrekidis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23642v1)