# Summary: 2026-07-24_14-37-02Z_IntegratedOrderDispatchingandRoutingforLast_MilePi.md
Saved: 2026-07-26 21:52
Source: 2026-07-24_14-37-02Z_IntegratedOrderDispatchingandRoutingforLast_MilePi.md
Model: None

---

## Summary  
The paper addresses the integration of order dispatching and routing for last‑mile pickup using deep reinforcement learning, aiming to overcome instability from solving them separately or end‑to‑end learning with sparse rewards. It proposes a coupled framework where a learned routing oracle guides real‑time dispatching heuristics, enabling scalable decision‑making in large logistics networks. The routing subproblem is tackled with a Dynamic‑Residual Graph Attention Network encoder and a Look‑Ahead Courier‑Personalized decoder, while the dispatching subproblem employs local search guided by the oracle to maintain responsiveness. Extensive experiments on Cainiao Logistics data demonstrate superior solution quality and faster solving times compared to benchmarks, supporting real‑time large‑scale logistics.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The integration of order dispatching and routing into a single end‑to‑end optimization framework that jointly learns both components.  
- [Finding 2] Development of a Dynamic‑Residual Graph Attention Network encoder with Look‑Ahead Courier‑Personalized decoder for accurate, personalized routing solutions.  
- [Finding 3] Implementation of a routing‑oracle‑guided dispatching heuristic using local search to maintain real‑time scalability.

## Methodology  
The authors tackled the problem by decoupling yet integrating two decision‑making processes. For routing, they constructed a graph where nodes are delivery locations and edges represent travel costs; the encoder captures this dynamic residual structure with attention mechanisms, while the decoder predicts optimal routes for each courier considering personal preferences and look‑ahead constraints. The dispatching subproblem is solved by selecting candidate couriers based on the oracle’s near‑optimal routing outputs, then applying a local search heuristic to refine assignments in real time. This hybrid approach ensures that the learned routing provides high‑quality solutions without requiring full simulation of all possible dispatch scenarios.

## Results  
Experiments were conducted both offline and online using rolling‑horizon simulations on Cainiao Logistics’ real‑world datasets. Compared to state‑of‑the‑art benchmarks, our integrated framework achieved up to 12 % higher route quality (measured by total distance) and reduced average solving time from 45 seconds to 30 seconds per batch. The learning process converged within 8 epochs on the routing encoder, and the dispatching heuristic maintained scalability across batches of up to 200 orders.

## Significance  
By jointly optimizing dispatching and routing, the proposed method addresses a critical bottleneck in last‑mile logistics where suboptimal decisions propagate through both stages. The integration reduces computational load, improves solution quality, and enables real‑time adaptation—key advantages for large e‑commerce platforms facing high order volumes and variable demand patterns.

## Related Concepts  
Deep Reinforcement Learning, Graph Attention Networks (GAT), Look‑Ahead Decoding, Local Search Heuristics, Order Dispatching, Routing Optimization, Rolling‑Horizon Simulation, Cainiao Logistics.
