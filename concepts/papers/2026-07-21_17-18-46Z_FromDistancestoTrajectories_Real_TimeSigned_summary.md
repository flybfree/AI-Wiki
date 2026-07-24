# Summary: 2026-07-21_17-18-46Z_FromDistancestoTrajectories_Real_TimeSignedDistanc.md
Saved: 2026-07-24 01:05
Source: 2026-07-21_17-18-46Z_FromDistancestoTrajectories_Real_TimeSignedDistanc.md
Model: None

---

## Summary  
The paper proposes a unified real‑time pipeline that simultaneously maps an environment and plans safe UAV trajectories using a single signed distance function (SDF) representation. By encoding the exact distance to each obstacle, the SDF supplies richer information than binary occupancy grids for both mapping and collision checking. The authors introduce two novel components: OREN, a fast octree‑based residual network that reconstructs SDFs online from point clouds, and Bubble*, a search‑driven planner that grows maximal collision‑free “bubbles” with formal termination guarantees. Together they enable safe corridor generation in cluttered indoor settings within seconds.

## Key Contributions  
- OREN improves SDF estimation by 22 % compared to baselines while preserving real‑time efficiency and differentiability.  
- Bubble* constructs maximal collision‑free bubbles, providing formal guarantees of termination, completeness, and failure detection.  
- The integrated OREN–Bubble* pipeline yields trajectories spanning ~90 m in 1–3 s, outperforming grid‑based A* baselines that require up to 10 s.

## Methodology  
The authors treat mapping and planning as co‑designed tasks around an SDF. Mapping is performed by OREN, which fuses a structured octree prior with a differentiable neural residual to estimate distances from point‑cloud observations in real time. Planning uses Bubble* to generate a graph of maximal safe bubbles; the planner searches this graph for a feasible corridor and then optimizes the trajectory within it, eliminating the need for repeated binary collision checks.

## Results  
Experiments on a quadrotor navigating an unseen indoor cluttered environment demonstrate that OREN’s SDF reconstruction is 22 % more accurate than state‑of‑the‑art baselines. Bubble* finds feasible trajectories in 1–3 seconds, whereas A*‑based methods take up to 10 seconds. The combined system runs onboard with limited compute resources, achieving both high accuracy and rapid response.

## Significance  
By unifying mapping and planning around an SDF, the approach reduces computational load, improves safety through richer distance information, and enables real‑time navigation in dynamic cluttered spaces—critical for autonomous UAVs operating in unseen environments. The work advances the field of embodied AI by showing how neural reconstruction can be tightly coupled with geometric planners without sacrificing performance.

## Related Concepts  
Signed Distance Function (SDF), Octree Residual Network (OREN), Bubble* planner, collision‑free ball growth, graph search, trajectory optimization, volumetric mapping, A*.
