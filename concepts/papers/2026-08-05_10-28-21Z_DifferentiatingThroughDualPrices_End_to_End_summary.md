# Summary: 2026-08-05_10-28-21Z_DifferentiatingThroughDualPrices_End_to_EndPolicyL.md
Saved: 2026-08-05 22:26
Source: 2026-08-05_10-28-21Z_DifferentiatingThroughDualPrices_End_to_EndPolicyL.md
Model: None

---

## Summary  
The paper tackles the problem of learning assignment policies for scarce social services—such as housing assistance or hospital interventions—that must respect hard capacity constraints while processing arrivals one‑by‑one. Traditional approaches treat outcomes and prices separately (decision‑blind regression), but the authors propose an end‑to‑end optimization that jointly learns outcome models and dual prices to enforce feasibility. They introduce both an exact nonconvex formulation and a convex relaxation that guarantees expected capacity compliance with bounded suboptimality. Experiments on queueing simulations across six datasets show these methods outperform decision‑blind baselines, especially when capacities are binding.

## Key Contributions  
- The authors propose an exact nonconvex optimization problem that jointly learns outcome models and dual prices to enforce capacity constraints.  
- They develop a convex relaxation of this problem whose optimum satisfies capacity constraints in expectation with suboptimality linear in the smoothing temperature and logarithmic in the number of arms.  
- Empirically, the end‑to‑end approaches achieve superior policy values across all delay costs, outperforming decision‑blind baselines, especially on large real‑world datasets such as a 70 k patient hospital cohort.

## Methodology  
The authors treat resource assignment as an off‑policy learning problem where each arrival must be assigned immediately. They train outcome models and dual prices jointly using gradient‑based optimization, formulating the exact problem as maximizing expected value minus the sum of dual price times capacity usage. For tractability they relax to a convex program that enforces expected feasibility. The training pipeline uses logged observational data without ground‑truth labels for outcomes.

## Results  
Across six simulated datasets with varying arrival rates and capacities, both end‑to‑end formulations achieve the top deployment‑adjusted value index at every delay cost, including zero delay. When capacity constraints are active, decision‑blind baselines often violate them leading to longer queues. On the largest dataset (70 k patients), end‑to‑end training yields a significant improvement over capacity‑matched neural baselines. Flexible regression remains stronger when outcomes are measurable but is irrelevant in truly scarce resource settings.

## Significance  
This work bridges off‑policy learning with hard feasibility constraints, offering a principled way to learn allocation policies that respect real‑world scarcity without violating operational limits. It demonstrates that end‑to‑end training can outperform standard regression pipelines, highlighting the importance of capacity‑aware optimization in resource management.

## Related Concepts  
- Off‑policy learning  
- Dual pricing  
- Convex relaxation  
- Queueing theory  
- Capacity constraints  
- Deployment‑adjusted value index  
- Nonconvex optimization  
- Smoothing temperature
