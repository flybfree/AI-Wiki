---
title: Heterogeneous Multi-Agent Reinforcement Learning for Radio Resource Management under Coupled Finite-Horizon Constraints
published: 2026-08-03T06:11:38Z
authors: Yeonseo Jeong, Wonhyeok Ko, Sungweon Hong, Songnam Hong
url: http://arxiv.org/abs/2608.01745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Heterogeneous Multi-Agent Reinforcement Learning for Radio Resource Management under Coupled Finite-Horizon Constraints

## Abstract
Maximizing throughput under proportional fairness in dense wireless networks requires jointly managing user association, scheduling, base station (BS) activation, and handover control under hard finite-horizon energy and handover budgets, which induces a fundamental tension between BS-side energy management and user-side handover regulation. While multi-agent reinforcement learning (MARL) is a natural framework for such distributed sequential control, its application here faces two difficulties: finite-horizon budget constraints cannot be evaluated at each time slot, and the nonlinear proportional fairness utility admits no principled per-slot decomposition. We propose HeLyMARL, a Lyapunov-embedded heterogeneous MARL framework that resolves both via drift-plus-penalty decomposition with virtual queues. The energy and handover constraint pressures are internalized directly into a unified per-slot reward, converting the constrained finite-horizon problem into an unconstrained MARL problem. Comparison against two Lagrangian-based alternatives reveals a timescale separation: Lagrangian relaxation regulates constraints only across training episodes, whereas the virtual queues of HeLyMARL bound cumulative budget consumption at every partial horizon within an episode, a pacing guarantee beyond the reach of greedy Lyapunov-based control. Simulations show that HeLyMARL is the only method that sustains the throughput-fairness balance together with uninterrupted service throughout the horizon, outperforming conventional MARL, Lyapunov-based, and constrained MARL benchmarks without premature budget exhaustion.

## Metadata
- **Published**: 2026-08-03T06:11:38Z
- **Authors**: Yeonseo Jeong, Wonhyeok Ko, Sungweon Hong, Songnam Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01745v1)