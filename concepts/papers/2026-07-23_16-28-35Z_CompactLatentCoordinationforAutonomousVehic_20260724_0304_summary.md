# Summary: 2026-07-23_16-28-35Z_CompactLatentCoordinationforAutonomousVehiclesatUn.md
Saved: 2026-07-24 03:04
Source: 2026-07-23_16-28-35Z_CompactLatentCoordinationforAutonomousVehiclesatUn.md
Model: None

---

## Summary  
The paper tackles the coordination of autonomous vehicles at unsignalized intersections, a problem that traditional multi‑agent reinforcement learning (MARL) systems often cannot solve due to combinatorial action spaces or reliance on privileged information. It introduces a hierarchical deep reinforcement learning architecture called MAPS in which a centralized Master agent creates compact continuous proto‑plans that encode global coordination strategies. These proto‑plans are then fused with local observations by decentralized Worker agents, separating strategic intent from tactical execution. Experiments on 72 configurations in HighwayEnv show collision‑free navigation and significant travel‑time reduction. Moreover, the learned proto‑plans generalize to zero‑shot scenarios, achieving a ~94 % success rate when moving from three to five agents.

## Key Contributions  
- [Finding 1] Provide a hierarchical deep reinforcement learning architecture where a central Master agent generates continuous proto‑plan embeddings that encode global coordination.  
- [Finding 2] Decouple strategic intent from tactical execution, allowing decentralized worker agents to optimize locally while using the proto‑plan as guidance.  
- [Finding 3] Demonstrate robust zero‑shot generalization: a three‑agent trained system achieves ~94 % success rate when deployed on unseen five‑agent intersections.

## Methodology  
The authors approached the problem by modeling unsignalized intersection coordination as a multi‑agent reinforcement learning task. They built MAPS, consisting of a centralized Master agent that learns to produce compact continuous proto‑plans via DRL and multiple Worker agents that fuse these embeddings with their local sensor data to generate vehicle‑specific control actions. Training is performed in the HighwayEnv simulation across 72 intersection configurations, using hierarchical RL objectives: collision‑free navigation while minimizing travel time. The architecture enables scalable learning without explicit agent communication.

## Results  
MAPS achieved collision‑free operation on all 72 test intersections with an average travel‑time reduction of roughly 30 % compared to baselines. The learned proto‑plans generalize well: a system trained with three agents reaches ~94 % success rate when zero‑shot transferred to five‑agent environments, outperforming state‑of‑the‑art MARL methods. Experiments also confirm that the compact embedding reduces communication overhead and permits independent optimization of each module.

## Significance  
This work matters because unsignalized intersections are ubiquitous in urban traffic, where safe coordination is essential for autonomous vehicle deployment. MAPS offers a hierarchical, data‑driven framework that avoids privileged information or rigid agent designs, addressing key limitations of existing MARL approaches. The demonstrated generalization suggests a scalable solution for future multi‑vehicle systems.

## Related Concepts  
- Multi‑agent reinforcement learning (MARL)  
- Hierarchical RL  
- Deep embedding / proto‑plan  
- Decentralized control  
- Zero‑shot transfer learning
