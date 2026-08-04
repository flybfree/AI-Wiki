---
title: Thermalizing Stochastic Programs
published: 2026-08-03T02:44:02Z
authors: Mirko Amico, Andraž Jelinčič, Colin Oscar Nancarrow, Leo Tyrpak, David Roberts, Seth Morton, Dalton Sakthivadivel, Ashwin Gopal, Guillaume Verdon
url: http://arxiv.org/abs/2608.01615v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thermalizing Stochastic Programs

## Abstract
We present a set of tools for mapping general stochastic programs to thermodynamic hardware designed for energy-efficient stochastic sampling. Given a target stochastic program expressed as a Directed Factor Graph (DFG) of stochastic channels, or equivalently as a Parametrized Stochastic Circuit (PSC), we first introduce a method to approximately compile each factor in the DFG to an Energy-Based Model (EBM) that is native to the hardware. We then analyze how the error of the compiled DFG accumulates from the per-factor errors, and introduce two training refinements, context matching and trajectory-level REINFORCE post-training, which can reduce the residual error left by training each factor in isolation. The \texttt{thermalizers} framework takes a stochastic program expressed in the \texttt{torx} library and replaces its factors with thermodynamic kernels implemented and sampled using the \texttt{thrml} library. We demonstrate it on several example applications, including a market simulator that learns the joint day-to-day dynamics of a panel of financial time series from recorded market history alone, a probabilistic model from mathematical ecology, Gibbs sampling of an EBM the hardware cannot natively express, and a sequential Bayesian design loop over a Gaussian stochastic circuit.

## Metadata
- **Published**: 2026-08-03T02:44:02Z
- **Authors**: Mirko Amico, Andraž Jelinčič, Colin Oscar Nancarrow, Leo Tyrpak, David Roberts, Seth Morton, Dalton Sakthivadivel, Ashwin Gopal, Guillaume Verdon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01615v1)