# Summary: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Saved: 2026-07-24 02:57
Source: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Model: None

---

## Summary  
The paper introduces SPORD (Simulation‑Propose‑then‑OR‑Dispose) as a framework that integrates high‑fidelity simulation with integer programming to solve supply‑chain planning problems at scale. By separating the generation of all operationally valid candidate paths through simulation from the selection of the globally optimal subset via an integer program, SPORD addresses three longstanding barriers: operational fragmentation, computational intractability, and lack of executive trust. The authors demonstrate that this decoupling enables rapid, transparent planning on JD.com’s NetSim platform, delivering measurable improvements in fulfillment rates and carbon emissions.  

## Key Contributions  
- [Finding 1] Decoupling simulation‑driven candidate generation from integer‑programming selection creates a modular pipeline that eliminates the need to rebuild models for each new planning task.  
- [Finding 2] Matrix‑vectorized CPU/GPU accelerated simulation achieves a 10–100× speedup over serial methods, making large‑scale routing feasible within minutes rather than hours.  
- [Finding 3] The closed‑loop intelligent diagnosis engine continuously validates plan feasibility and automatically proposes corrective actions, resulting in a cross‑regional fulfillment rate drop from 6.1 % to 4.9 % and an average monthly carbon reduction of ~5,745 tCO₂e.  

## Methodology  
SPORD follows three stages: (1) **Simulation** – NetSim runs a vectorized simulation that enumerates every feasible path respecting SKU‑level attributes, network topology, and routing constraints; (2) **Propose** – the full set of candidate paths is stored as a matrix‑vector product for fast access; (3) **OR‑Dispose** – an integer linear program selects the optimal subset from this candidate pool, discarding suboptimal routes. The process is orchestrated by a list‑scheduling algorithm that compresses coupled‑order processing from hours to minutes.  

## Results  
Since 2025 NetSim has optimized end‑to‑end services for over 20,000 suppliers. Key quantitative results include: (i) fulfillment error reduction from 6.1 % to 4.9 %; (ii) monthly carbon emissions cut by ~5,745 tCO₂e; (iii) computational throughput improvement of 10–100× via GPU‑accelerated simulation and minutes‑scale list scheduling.  

## Significance  
SPORD transforms supply‑chain planning from a series of isolated, trust‑deficient projects into an active, self‑correcting system where executives see transparent simulations before committing to decisions. The modular architecture ensures future tasks require only configuration changes, not model reconstruction, fostering rapid adaptation and sustainable operations across global networks.  

## Related Concepts  
Simulation, integer programming (ILP), decoupled optimization pipelines, matrix‑vectorized computation, GPU acceleration, list scheduling, closed‑loop feedback, NetSim platform, supply‑chain planning, carbon accounting, fulfillment rate, SKU assortment planning.
