# Summary: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Saved: 2026-07-24 02:46
Source: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md
Model: None

---

## Summary  
The paper introduces SPORD—a Simulation‑Propose‑then‑OR‑Dispose framework that tackles three persistent problems in e‑commerce supply chain planning: operational fragmentation, computational intractability, and executive distrust. By integrating a high‑speed simulation engine with an integer‑programming optimizer, SPORD generates all operationally valid candidate paths and then selects the globally optimal subset, delivering transparent outputs that can be acted upon without model reconstruction. This approach is deployed as JD.com’s NetSim platform, which has already optimized services for thousands of suppliers.

## Key Contributions  
- SPORD decouples simulation (proposal) from optimization (dispose), enabling scalable candidate generation across millions of SKUs and complex routing logic.  
- Matrix‑vectorized CPU/GPU acceleration provides a 10–100× speedup over serial methods, while list scheduling reduces coupled‑order processing from hours to minutes.  
- An intelligent diagnosis engine creates a closed‑loop system that continuously improves fulfillment rates and carbon reduction.

## Methodology  
The authors built NetSim, which first simulates the full set of feasible operationally valid paths using matrix‑vectorized computations that capture all business‑specific logic. The simulation outputs are fed into an integer program that formulates a global optimum selection problem. A list‑scheduling algorithm then orders these selected paths for execution, allowing rapid reconfiguration without rebuilding models.

## Results  
Since 2025 NetSim has optimized end‑to‑end services for over 20,000 suppliers, lowering the cross‑regional fulfillment rate from 6.1 % to 4.9 %. The system also achieves an average monthly carbon reduction of approximately 5,745 tCO₂e. Computational experiments demonstrate a 10–100× speedup in simulation versus serial approaches and cut processing time for coupled orders from hours to minutes.

## Significance  
SPORD shifts simulation from passive monitoring to active planning, turning skeptical executives into engaged collaborators through transparent, verifiable outputs. Its modular architecture ensures that future planning tasks require only configuration changes rather than full model reconstruction, fostering long‑term adoption and continuous improvement across the supply chain.

## Related Concepts  
- Simulation‑based optimization  
- Integer programming (IP) for route selection  
- List scheduling algorithms  
- Closed‑loop supply‑chain management  
- Carbon footprint reduction metrics  
- E‑commerce fulfillment rate improvement
