---
title: Orbit-Planner: Towards Latent World Models for On-Orbit Obstacle Avoidance of Satellite Agents
url: http://arxiv.org/abs/2608.16651v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_14-49-07Z_Orbit_Planner_TowardsLatentWorldModelsforOn_OrbitO.md
generated_at: 2026-08-17 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Orbit-Planner, a two-stage latent world model designed to help satellite agents avoid on‑orbit obstacles by predicting future states in an unseen latent space. It learns action‑conditioned dynamics and uses a physics probe to translate imagined trajectories back into physical spacecraft states. Experiments show long‑horizon rollouts and a 91.7% success rate in obstacle avoidance using Isaac Sim.

## Key Takeaways
- Orbit-Planner learns action‑conditioned spacecraft dynamics to generate future‑state rollouts directly in latent space, enabling the model to plan without relying on predefined maps.
- The physics probe decodes imagined latent trajectories into realistic physical state changes, bridging the gap between abstract planning and actual satellite behavior.
- In closed‑loop obstacle avoidance tests, Orbit-Planner achieved a 91.7% success rate, demonstrating its capability for long‑horizon navigation in simulated environments.

## Context
Latent world modeling aims to represent unobserved dynamics that influence perception and action, allowing agents to plan beyond immediate sensor data. This approach is relevant because real satellite missions involve unpredictable debris and other spacecraft, making static maps insufficient. By learning these hidden dynamics, planners can adapt to changing conditions autonomously.

## Implications
For space agencies and satellite operators, Orbit-Planner offers a scalable method to integrate robust obstacle avoidance into onboard AI systems without extensive mapping resources. Practitioners can leverage the model’s ability to generate long‑horizon plans, reducing mission risk and improving operational safety in crowded low‑Earth orbits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16651v1)
