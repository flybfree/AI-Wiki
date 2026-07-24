# Summary: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Saved: 2026-07-24 03:02
Source: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Model: None

---

## Summary  
The paper introduces SPORD (Simulation‑Propose‑then‑OR‑Dispose) to integrate simulation and optimization for supply‑chain planning, directly confronting three longstanding barriers: operational fragmentation, computational intractability, and a lack of executive trust. By decoupling the generation of all feasible candidate paths through an accelerated simulation layer from the selection of the globally optimal subset via integer programming, SPORD produces executable plans that can be trusted and acted upon. The approach is realized in JD.com’s NetSim platform, delivering measurable operational gains across thousands of suppliers.

## Key Contributions  
- [Finding 1] A parallelized, matrix‑vectorized simulation framework that enumerates the full set of operationally valid candidate paths at scale.  
- [Finding 2] An integer program that selects the optimal subset from those candidates, solving the combinatorial problem efficiently.  
- [Finding 3] An intelligent diagnosis engine and closed‑loop system that continuously validates performance and refines plans.

## Methodology  
The authors built NetSim by first constructing a simulation layer that models complex routing, inventory, and service logic; this layer is accelerated using GPU/CPU parallelism to achieve 10–100× speedups over serial methods. Input data are fed into an integer‑programming solver which outputs the best subset of paths. The process is embedded in an intelligent diagnosis engine that monitors key metrics (e.g., fulfillment rate, carbon emissions) and adjusts parameters as needed, creating a feedback loop between simulation and optimization.

## Results  
Since 2025 NetSim has optimized end‑to‑end services for over 20,000 suppliers. The cross‑regional fulfillment rate fell from 6.1 % to 4.9 %, and the average monthly carbon reduction is approximately 5,745 tCO₂e. List scheduling reduces coupled‑order processing time from hours to minutes, demonstrating both operational efficiency and environmental benefit.

## Significance  
SPORD bridges simulation and optimization, turning opaque models into transparent, executable outputs that executives can trust. The modular architecture means future planning tasks require only configuration changes rather than model reconstruction, fostering faster decision cycles and deeper stakeholder engagement in supply‑chain improvement.

## Related Concepts  
Simulation‑based optimization (SBO), integer programming, supply‑chain planning, decoupling of generation versus selection, carbon footprint reduction, e‑commerce logistics, modular architecture.
