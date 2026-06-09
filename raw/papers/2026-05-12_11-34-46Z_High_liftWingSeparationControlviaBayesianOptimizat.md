---
title: High-lift Wing Separation Control via Bayesian Optimization and Deep Reinforcement Learning
published: 2026-05-12T11:34:46Z
authors: Ricard Montalà, Bernat Font, Oriol Lehmkuhl, Ricardo Vinuesa, Ivette Rodriguez
url: http://arxiv.org/abs/2605.11981v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# High-lift Wing Separation Control via Bayesian Optimization and Deep Reinforcement Learning

## Abstract
This study investigates active flow control (AFC) of a 30P30N high-lift wing at a Reynolds number Re$_c$ = 450,000 and angle of attack $α$ = 23$^\circ$ using wallresolved large-eddy simulations (LES). Two optimization strategies are explored: open-loop Bayesian optimization (BO) and closed-loop deep reinforcement learning (DRL), both targeting the mitigation of stall and the improvement of aerodynamic efficiency via synthetic jets on the slat, main, and flap elements. The uncontrolled configuration was validated against literature data, confirming the reliability of the LES setup. The BO framework successfully identified steady jet velocities that increased efficiency by +10.9% through a -9.7% drag reduction while maintaining lift. In contrast, the DRL agent, despite leveraging instantaneous flow information from distributed sensors, achieved only minor improvements in lift and drag, with negligible efficiency gain. Training analysis indicated that the penalty-dominated reward constrained exploration. These results highlight the need for carefully designed rewards and computational acceleration strategies in DRL-based flow control at high Reynolds numbers.

## Metadata
- **Published**: 2026-05-12T11:34:46Z
- **Authors**: Ricard Montalà, Bernat Font, Oriol Lehmkuhl, Ricardo Vinuesa, Ivette Rodriguez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11981v1)