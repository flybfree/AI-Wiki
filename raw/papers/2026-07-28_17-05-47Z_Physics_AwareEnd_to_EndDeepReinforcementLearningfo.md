---
title: Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics
published: 2026-07-28T17:05:47Z
authors: Ya-Chia Shen, Woei-Leong Chan
url: http://arxiv.org/abs/2607.25985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics

## Abstract
Unmanned aerial vehicles (UAVs), particularly quadcopters, present unique challenges for autonomous control due to their underactuated dynamics: only four available control inputs must govern six degrees of freedom. This paper investigates a physics-aware, end-to-end deep reinforcement learning (DRL) approach that acts directly on low-level body inputs, total thrust and body torques $(T, τ_x, τ_y, τ_z)$, and closes the loop through a high-fidelity Simulink environment. Our simulator integrates a 12-state rigid-body model (MATLAB Level-2 S-Function) with (i) an Action2RPM allocation based on the Moore-Penrose pseudo-inverse of a coefficient matrix derived from thrust and drag terms, and (ii) first-order actuator dynamics for each motor (time constant $T_m = 0.076$ s), including rotor gyroscopic coupling. A shaped reward balances goal-reaching and stability using an exponential position well, attitude penalties, and quadratic velocity costs. Four DRL algorithms, DDPG, TD3, PPO, and SAC, are evaluated in two stages: (S1) thrust-only hover and (S2) hover with pitch torque and a translated goal. Results show that SAC and TD3 achieve superior stability and exploration efficiency, while PPO is less sample-efficient. The study highlights the significance of modeling actuator lags and aerodynamic moments for stable low-level control and provides a reproducible benchmark for quadcopter DRL.

## Metadata
- **Published**: 2026-07-28T17:05:47Z
- **Authors**: Ya-Chia Shen, Woei-Leong Chan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25985v1)