# Summary: 2026-07-23_16-28-35Z_CompactLatentCoordinationforAutonomousVehiclesatUn.md
Saved: 2026-07-24 02:55
Source: 2026-07-23_16-28-35Z_CompactLatentCoordinationforAutonomousVehiclesatUn.md
Model: None

---

## Summary  
The paper addresses the coordination of autonomous vehicles at unsignalized intersections using a hierarchical deep reinforcement learning framework. It introduces the Master‑Agent Proto‑plan System (MAPS) where a central master generates a compact continuous proto‑plan encoding global strategy, while decentralized workers use it locally to execute vehicle‑specific control. This decouples strategic intent from tactical execution and enables independent optimization of each module.

## Key Contributions  
- [Finding 1] MAPS reduces the combinatorial action space by replacing discrete joint actions with a single continuous proto‑plan.  
- [Finding 2] The hierarchical architecture separates high‑level coordination (master) from low‑level vehicle control (workers), enabling modular optimization.  
- [Finding 3] Empirically, MAPS achieves collision‑free navigation across 72 configurations and generalizes to five agents with a 94% success rate.

## Methodology  
The authors design a centralized master agent trained via multi‑agent reinforcement learning to produce proto‑plans as outputs of a deep network. Workers receive the proto‑plan together with local sensor data, then run their own DRL policies that map this embedding into vehicle maneuvers. Experiments are conducted in HighwayEnv with varying numbers of agents and intersection topologies.

## Results  
In 72 test configurations, MAPS achieved zero collisions and reduced average travel time compared to baselines. Zero‑shot transfer tests showed a 94% success rate when moving from three‑agent to five‑agent scenarios, confirming robustness.

## Significance  
This work provides a scalable framework for coordinating many autonomous vehicles without traffic signals, addressing key MARL challenges such as combinatorial explosion and lack of generalization, which could improve real‑world deployment and safety.

## Related Concepts  
Hierarchical reinforcement learning, latent coordination, proto‑plan encoding, decentralized control, multi‑agent RL, highway simulation environment.
