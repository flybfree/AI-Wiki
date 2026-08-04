---
title: CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning
url: http://arxiv.org/abs/2608.01802v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-10-38Z_CoNav_UAV_CooperativeDual_AltitudeAerialNavigation.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoNav‑UAV, a cooperative aerial navigation system that treats high‑altitude and low‑altitude UAVs as a Stackelberg leader‑follower pair. The authors demonstrate that iterative learning between the two agents yields higher success rates than single or dual‑agent baselines on urban VLM tasks.

## Key Takeaways
- Iterative Stackelberg Learning enables the high‑level vision‑language reasoning of the leader to be refined through memory‑based in‑context updates while the follower’s motion control is distilled from expert trajectories.  
- The alternating updates drive both agents toward a Stackelberg equilibrium, producing complementary gains that improve task success by up to 30.8 points on the learning scene and 9.0 points under cross‑scene transfer.  
- Using about three times less adaptation data than previous dual‑agent approaches shows that mutual adaptation is more efficient.

## Context
Cooperative aerial navigation requires agents to balance global exploration with precise close‑range approach, a challenge amplified by limited sensor data. Existing solutions often rely on external assistance or privileged information, limiting scalability and adaptability in real‑world VLM applications.

## Implications
The Stackelberg framework offers a principled way to allocate learning responsibilities between high‑level reasoning and low‑level control. Practitioners can adopt this model to reduce adaptation data needs and enhance mission reliability across diverse urban environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01802v1)
