---
title: Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning
published: 2026-07-30T03:30:18Z
authors: Wentao Zhang, Wentao Mo
url: http://arxiv.org/abs/2607.27626v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning

## Abstract
Safety-critical IoT systems such as industrial closed-loop control, V2X coordination, and remote teleoperation require every sensor's peak Age of Information (peak AoI, also abbreviated PAoI) to stay below a hard per-slot deadline, not merely an average bound. Existing approaches meet this requirement only under restrictive assumptions: stochastic channels for Whittle-index AoI, simulator rollouts for deep reinforcement learning, or sublinear cumulative violation for long-term constrained online convex optimization. Under adversarial coefficients, OCO-PAoI-Hard guarantees zero per-slot violation of the modeled AoI state under one-step viability and O(sqrt(T)) regret against any static safe comparator; packet-level safety requires stronger service assumptions. Our key observation is that the fractional peak-AoI deadline collapses exactly to an affine half-space constraint on the resource-allocation vector, turning hard real-time scheduling into time-varying constrained online convex optimization over a polyhedral safe set. A strictly causal proposal-shield-update loop enforces feasibility through one Euclidean projection per slot, the gradient step preserves no-regret behavior, and the classical virtual queue is reduced to an a-posteriori certificate. We establish closed-form static and dynamic regret bounds, a matching Omega(sqrt(T)) minimax lower bound, a margin-safe variant against execution noise, and a deadline-induced competitive ratio. On a four-sensor adversarial fluid-model trap channel, OCO-PAoI-Hard attains zero modeled-state deadline violations across all ten seeds, while four representative baselines miss between 1.65 percent and 64.0 percent of slots, and the empirical normalized regret stays below the theoretical envelope across two orders of magnitude in T.

## Metadata
- **Published**: 2026-07-30T03:30:18Z
- **Authors**: Wentao Zhang, Wentao Mo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27626v1)