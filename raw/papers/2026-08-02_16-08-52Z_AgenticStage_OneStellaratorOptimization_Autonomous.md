---
title: Agentic Stage-One Stellarator Optimization: Autonomous Multi-Objective Search for Finite-Beta Equilibria
published: 2026-08-02T16:08:52Z
authors: Tingjia Zhang, Hongke Lu, Zhuoran Meng, Runlai Xu
url: http://arxiv.org/abs/2608.01344v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Stage-One Stellarator Optimization: Autonomous Multi-Objective Search for Finite-Beta Equilibria

## Abstract
Stage-one stellarator design searches a high-dimensional family of three-dimensional plasma boundaries and fixed-boundary MHD equilibria for configurations that jointly meet requirements on confinement, field-line topology, force balance, stability proxies, and geometry. These specifications do not provide a general constructive map to a validated finite-beta equilibrium. High-quality targets are commonly developed through iterative numerical optimization whose outcome depends on the initial configuration, active Fourier resolution, objective priorities, and local solver budget. Coordinating this process is computationally costly and expert-intensive, limiting both design throughput and the production of consistently evaluated data. We present a proof of concept for \emph{agentic} stage-one optimization. A bounded language-model agent diagnoses the current equilibrium and selects the next local optimization experiment, while deterministic DESC execution owns prescribed profiles and flux, symmetry, metric evaluation, solver validity, and acceptance. On a common-budget subset from an expanding finite-beta campaign, the number of gate-valid configurations increases from five inputs to nineteen outputs; median Boozer QS RMS decreases from $2.39\times10^{-4}$ to $1.07\times10^{-4}$, and median maximum principal curvature decreases from $62.56$ to $33.00\,\mathrm{m}^{-1}$. A complementary long route achieves a $9.10\times$ QS reduction while repairing magnetic-well and curvature defects. The system also records every attempted local action as transition evidence, yielding 734 structured parent--action--outcome records in the reported experiments. These results show that agentic outer-loop control can sustain finite-beta, multi-objective search and turn repeated optimization into a scalable source of improved equilibria and reusable decision data.

## Metadata
- **Published**: 2026-08-02T16:08:52Z
- **Authors**: Tingjia Zhang, Hongke Lu, Zhuoran Meng, Runlai Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01344v1)