---
title: Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics
url: http://arxiv.org/abs/2607.25985v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_17-05-47Z_Physics_AwareEnd_to_EndDeepReinforcementLearningfo.md
generated_at: 2026-07-28 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a physics‑aware end‑to‑end deep reinforcement learning method for quadcopter control that directly manipulates low‑level thrust and torque inputs while using a high‑fidelity Simulink model. It evaluates four DRL algorithms on hover tasks and finds SAC and TD3 perform best in stability and exploration.

## Key Takeaways
- The controller uses the Moore‑Penrose pseudoinverse of a coefficient matrix to allocate thrusts, enabling realistic actuator dynamics including rotor gyroscopic coupling.
- A shaped reward that combines exponential position well, attitude penalties, and quadratic velocity costs balances goal achievement with stability.
- Four DRL algorithms are compared in two stages; SAC and TD3 achieve superior performance while PPO is less sample‑efficient.

## Context
This work addresses the challenge of integrating physics into reinforcement learning for real‑world UAV control, where accurate low‑level dynamics are essential. By using a 12‑state rigid‑body model with actuator lags in a Simulink environment, the study demonstrates how modeling fidelity improves DRL outcomes.

## Implications
For industry practitioners, the benchmark provides reproducible results and guidance for designing robust quadcopter controllers that account for motor delays and aerodynamic moments. The findings suggest that physics‑aware RL can lead to safer, more efficient autonomous flight systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25985v1)
