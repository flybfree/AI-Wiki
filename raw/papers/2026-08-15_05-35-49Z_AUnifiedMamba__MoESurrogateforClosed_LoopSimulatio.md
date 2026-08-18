---
title: A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients
published: 2026-08-15T05:35:49Z
authors: Haoguang Wang, Huy Hoang Le, Akhila Kandivalasa, Christian Moya, Marcos Netto, Guang Lin
url: http://arxiv.org/abs/2608.15051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients

## Abstract
This paper proposes a Mamba surrogate model with mixture-of-experts (MoE) routing to represent the transient dynamics of inverter-based resources. A Mamba surrogate model is a predictive machine learning model built on the Mamba architecture. MoE routing uses a router network to assign data-dependent weights to specialized subnetworks (experts). The resulting Mamba--MoE surrogate can perform two tasks: (i) closed-loop simulation and (ii) measurement-window forecasting of inverter transients. A single Mamba backbone with task conditioning and expert routing serves both tasks, replacing two separate specialists. Task-matched objectives fit each prediction form, and an adaptive conformal layer provides prediction intervals for both tasks. For the considered grid-following inverter, the unified surrogate model remains in the same low-error regime as a Mamba specialist pair while using 13% fewer parameters. The prediction intervals achieve 94--96% empirical mean marginal coverage across the two tasks. For transient dynamics---that is, beyond the vicinity of an equilibrium point---our surrogate model with MoE routing yields lower errors across all outputs in both tasks compared to a shared Mamba backbone without expert routing. A controller hardware-in-the-loop simulation validates our results and shows that adapting only the shared output head with limited measured data reduces held-out forecasting error.

## Metadata
- **Published**: 2026-08-15T05:35:49Z
- **Authors**: Haoguang Wang, Huy Hoang Le, Akhila Kandivalasa, Christian Moya, Marcos Netto, Guang Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15051v1)