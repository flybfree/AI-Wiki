# Summary: 2026-07-21_17-18-46Z_FromDistancestoTrajectories_Real_TimeSignedDistanc.md
Saved: 2026-07-24 01:21
Source: 2026-07-21_17-18-46Z_FromDistancestoTrajectories_Real_TimeSignedDistanc.md
Model: None

---

## Summary  
This paper proposes a unified framework that simultaneously maps the environment into a signed distance function (SDF) and generates collision‑free trajectories in real time for autonomous UAVs. By integrating an efficient neural SDF estimator with a search‑based bubble planner, the authors achieve both high geometric accuracy and rapid computation on limited onboard hardware. The contributions lie not only in the new OREN network but also in Bubble$^\star$, which exploits distance information to construct maximal collision‑free “bubbles” and yields provable guarantees of termination and completeness.

## Key Contributions  
- **Finding 1:** A single SDF representation replaces binary occupancy maps, providing richer geometric data for both mapping and planning.  
- **Finding 2:** OREN, an Octree REsidual Network, reconstructs SDFs online from point‑cloud observations with the speed of volumetric methods while retaining neural accuracy and differentiability.  
- **Finding 3:** Bubble$^\star$, a search‑based planner that grows maximal collision‑free bubbles, reduces collision checks dramatically compared to grid‑based A* and produces a safe corridor for trajectory optimization.

## Methodology  
The authors tackled the problem by first designing a co‑optimized mapping‑planning pipeline around an SDF. OREN combines an explicit octree prior with an implicit residual network, allowing it to predict distances to obstacles from sparse point clouds in real time. The resulting SDF is fed into Bubble$^\star$, which constructs a graph of maximal collision‑free bubbles using the distance field as a cost function. This bubble graph enables a fast A*‑style search that only evaluates edges between adjacent bubbles, cutting the number of explicit collision tests from thousands to a few hundred. The integrated system runs on a quadrotor in unseen indoor cluttered environments while respecting tight compute constraints.

## Results  
Experimental evaluation shows OREN improves SDF estimation accuracy by roughly 22 % relative to baseline methods such as classic octree or pure neural estimators. Bubble$^\star$ finds traversable corridors of about 90 m in a cluttered indoor space within 1–3 seconds, whereas conventional A*‑based planners require up to 10 seconds for the same task. The combined OREN‑Bubble$^\star$ pipeline demonstrates real‑time performance on a quadrotor with limited onboard processing power.

## Significance  
By merging geometric mapping and planning into one SDF‑centric workflow, the framework reduces both computational load and safety risk. Fewer collision checks translate to lower latency and higher reliability in dynamic environments, making autonomous flight feasible for practical applications such as inspection drones or search‑and‑rescue missions.

## Related Concepts  
- Signed distance function (SDF) – a continuous field encoding signed distances to obstacles.  
- Octree – a hierarchical spatial partitioning structure used for volumetric data storage and retrieval.  
- Residual networks – neural architectures that add a learned correction term to an explicit prior.  
- Bubble planner – a search‑based method that constructs maximal collision‑free regions (bubbles) from distance information.  
- A* search – a classic pathfinding algorithm often applied on grid or graph representations of environments.
