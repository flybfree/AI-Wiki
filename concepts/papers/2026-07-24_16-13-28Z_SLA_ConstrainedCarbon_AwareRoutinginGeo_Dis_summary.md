# Summary: 2026-07-24_16-13-28Z_SLA_ConstrainedCarbon_AwareRoutinginGeo_Distribute.md
Saved: 2026-07-27 23:23
Source: 2026-07-24_16-13-28Z_SLA_ConstrainedCarbon_AwareRoutinginGeo_Distribute.md
Model: None

---

## Summary  
The paper addresses the challenge of routing serverless workloads across geo‑distributed cloud regions while respecting both latency Service Level Agreements (SLAs) and real‑time carbon intensity measurements. By formulating a constrained optimization problem, it proposes an SLA‑constrained carbon‑aware routing policy that minimizes emissions without violating any SLA thresholds. The model leverages actual carbon intensity data from five AWS deployments to evaluate the trade‑off between latency and environmental impact. Experimental results demonstrate significant carbon savings while preserving user experience.

## Key Contributions  
- [Finding 1] A novel constrained optimization framework that simultaneously satisfies SLA latency constraints and minimizes carbon emissions across multiple geographic regions.  
- [Finding 2] Empirical evidence that the proposed policy can achieve up to 46.8 % carbon reduction while maintaining zero SLA violations for a range of service‑level thresholds.  
- [Finding 3] A scalability analysis showing average carbon savings rise from 27.4 % to 47.5 % as routing flexibility expands across 12 AWS regions spanning six continents.

## Methodology  
The authors model the routing decision as a mixed‑integer linear program where each request is assigned to a cloud region based on its latency, carbon intensity, and SLA constraints. Real‑time carbon intensity data from five primary AWS deployments are fed into the optimizer, which computes the optimal region assignment for each request while respecting predefined latency budgets. The system incurs minimal routing overhead (less than 0.02 % of total request latency) because the decision is made locally at the edge without heavy central coordination.

## Results  
Under mixed workloads across the five AWS deployments, the policy reduces carbon emissions by an average of 27.4 %. When evaluated against all SLA thresholds, the routing never exceeds the allowed latency, resulting in zero violations. The scalability study across 12 regions demonstrates that extending routing flexibility yields higher savings, reaching up to 46.8 % reduction. The overhead remains negligible, confirming practical applicability.

## Significance  
This work directly contributes to SDG 13 (Climate Action) and SDG 7 (Affordable and Clean Energy) by enabling cloud services to lower their carbon footprint without compromising user experience. By integrating real‑world carbon intensity data into routing decisions, the approach offers a scalable pathway for large‑scale cloud operators to meet sustainability targets while maintaining performance guarantees.

## Related Concepts  
- Service Level Agreement (SLA) latency constraints  
- Carbon intensity measurement in power grids  
- Geo‑distributed serverless architecture  
- Mixed‑integer linear programming for constrained optimization  
- Real‑time data integration and edge computing
