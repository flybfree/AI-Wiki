---
title: Joint UAV Flight and Opportunistic Routing under Reinforcement Learning for Delay-Tolerant Networks
url: http://arxiv.org/abs/2608.04590v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_08-51-41Z_JointUAVFlightandOpportunisticRoutingunderReinforc.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper aims to jointly optimize controllable unmanned aerial vehicle (UAV) flight and decentralized opportunistic routing using reinforcement learning, thereby enlarging future contacts in delay‑tolerant networks. Simulation results show effective gains over PRoPHET and MaxProp while retaining contact‑limited decentralized execution. The method uses PPO to learn a policy that balances UAV heading changes with routing decisions, ensuring both timely and efficient message delivery.

## Key Takeaways
- Joint optimization of decentralized opportunistic routing and controllable UAV flight enlarges future contacts through discrete UAV headings.
- Per‑node replication is enabled under contact‑limited observations via factored POMDP with sequential motion‑routing coupling.
- Simulation results demonstrate effective gains over PRoPHET and MaxProp while retaining contact‑limited decentralized execution.

## Context
This work showcases reinforcement learning for real‑world network control, integrating physical actuation (UAV flight) with data routing to illustrate a factorization between training and execution that is scalable. Such approaches reduce the burden on individual nodes, allowing them to operate autonomously while benefiting from global learning signals.

## Implications
The framework improves end‑to‑end performance in IoT and satellite communications where delays are tolerated but reliability matters. It offers an adaptable model for other mobile platforms, reducing reliance on centralized control and valuable for edge computing deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04590v1)
