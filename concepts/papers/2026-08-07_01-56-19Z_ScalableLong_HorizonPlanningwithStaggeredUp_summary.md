# Summary: 2026-08-07_01-56-19Z_ScalableLong_HorizonPlanningwithStaggeredUpdatesfo.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_01-56-19Z_ScalableLong_HorizonPlanningwithStaggeredUpdatesfo.md
Model: None

---

## Summary  
The paper addresses the challenge of generating collision‑free paths for thousands of agents over long horizons while meeting real‑time constraints, which reactive rule‑based planners lack due to temporal myopia and full‑horizon planners suffer from high planning overhead. By introducing Path Updates over Staggered Horizons (PUSH), PUSH merges the scalability of PIBT/EPIBT with the windowed reasoning of RHCR and the subset‑planning efficiency of TP, enabling long‑horizon coordination across general maps without restrictive assumptions. The method plans only a subset of agents at each timestep using staggered planning windows while integrating EPIBT‑style priority inheritance, backtracking, and anytime improvements to sustain throughput in congested scenarios.  

## Key Contributions  
- PUSH combines the key advantages of PIBT, RHCR, and TP into a single framework for scalable long‑horizon LMAPF.  
- It reduces computational complexity by planning only subsets of agents at each timestep using staggered horizons, unlike TP which is limited to structured maps.  
- The integration of EPIBT‑inspired priority inheritance, backtracking, and anytime improvements maintains high system throughput in congested environments.  

## Methodology  
PUSH operates by dividing the agent fleet into planning windows that advance over a multi‑step horizon. At each step it selects a subset of agents whose future positions are most uncertain or critical, computes RHCR‑style windowed paths using a general map representation, and updates their trajectories while deferring less urgent updates to later windows. The planner employs priority inheritance so higher‑priority agents can preempt lower ones, backtracking when deadlocks arise, and anytime improvements allow early termination if the current solution satisfies constraints.  

## Results  
Experiments on two realistic MAPF scenarios requiring long‑horizon reasoning show that PUSH scales to 10 k agents in under one second, matching EPIBT’s capacity but delivering higher system throughput than PIBT, RHCR, TP, and EPIBT. The planner also achieves superior path quality with fewer replanning events.  

## Significance  
This work bridges the gap between reactive scalability and long‑horizon reasoning, providing a practical solution for fleet coordination in dynamic environments where both speed and foresight are essential.  

## Related Concepts  
PIBT, Enhanced PIBT (EPIBT), RHCR, TP, windowed planning, staggered horizons, priority inheritance, anytime improvements, collision‑free path generation, multi‑agent path finding.
