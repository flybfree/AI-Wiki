---
title: TRUAV: Distributed Multi-Agent Reinforcement Learning for Trajectory Planning and Routing Enhancement in UAV-Aided IoT-Enabled VANETs
url: http://arxiv.org/abs/2607.23734v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_16-06-08Z_TRUAV_DistributedMulti_AgentReinforcementLearningf.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRUAV, a distributed multi‑agent reinforcement learning framework that enables UAVs to plan trajectories and enhance routing in VANET‑enabled IoT networks without relying on global state exchange. The approach uses independent tabular Q‑learning agents per UAV and achieves network coverage and packet delivery ratios comparable to centralized deep RL methods while reducing relay delay and energy consumption.

## Key Takeaways
- Each UAV operates a local Q‑learning agent that only observes its own vehicle density, packet queue states, and neighbor UAV positions, eliminating the need for global state aggregation.  
- A potential‑game inspired reward design promotes spatial diversity among agents and accounts for energy consumption, encouraging efficient positioning.  
- Simulations with 200 mobile vehicles in a large urban area show that TRUAV matches centralized deep RL performance on coverage and delivery ratios while improving relay delay and energy efficiency.

## Context
The paper addresses the scalability challenge of UAV‑assisted VANETs where bandwidth and energy are limited, highlighting how decentralized AI can replace costly central coordination. It contributes to the growing body of work on distributed reinforcement learning for mobile robot networks.

## Implications
For industry stakeholders, TRUAV demonstrates a practical path toward autonomous UAV swarms that support IoT connectivity without sacrificing efficiency. Practitioners can adopt similar local‑agent architectures to reduce infrastructure costs and improve system resilience in smart city deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23734v1)
