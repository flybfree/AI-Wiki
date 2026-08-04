# Summary: 2026-08-03_17-51-58Z_CoWAM_CoordinationContractsforSelectivePolicyInter.md
Saved: 2026-08-04 00:53
Source: 2026-08-03_17-51-58Z_CoWAM_CoordinationContractsforSelectivePolicyInter.md
Model: None

---

## Summary  
CoWAM introduces a selective intervention layer that augments bimanual robot policies with World Action Models (WAMs) to coordinate actions safely. The framework defines coordination contracts—comprising typed admissibility checks, event‑conditioned verification, and calibrated gates—that replace the nominal action only when an alternative satisfies all obligations and offers a low‑risk improvement; otherwise it abstains. This approach is evaluated across eight simulated bimanual tasks, demonstrating measurable gains in both selection quality and closed‑loop success while keeping harmful interventions below 1 %.  

## Key Contributions  
- CoWAM defines a formal framework of coordination contracts that combine typed admissibility checks with event‑conditioned verification.  
- It introduces calibrated intervention gates that select alternative actions only when they satisfy every active obligation and provide a clear, low‑risk improvement.  
- The method separates selector quality from proposal quality by operating on identical candidate pools and committing decisions before shared oracle labeling.  

## Methodology  
The authors first augment existing bimanual policies with WAMs, which predict action‑conditioned futures for each possible move. A selection layer then evaluates a set of coordination contracts: each contract is expressed as a typed admissibility condition (e.g., no collision) and an event‑conditioned verification (e.g., synchronization). A calibrated gate decides whether to intervene; if the nominal action remains inadmissible or no alternative improves safety, the system abstains. All methods share the same candidate pool of actions, ensuring that selector decisions are based on a common set rather than differing proposals.  

## Results  
Across eight simulated bimanual tasks, CoWAM improved coordination‑valid selection by 16.7 percentage points relative to the contract‑only baseline and raised closed‑loop success by 9.6 percentage points above the strongest selective baseline. Crucially, harmful interventions remained below 1 %, indicating that the intervention layer is highly conservative. These gains confirm that CoWAM can reliably select better actions while preserving safety.  

## Significance  
CoWAM establishes coordination contracts as an effective interface for conservative policy intervention in tasks where robots must coordinate complex bimanual motions. By grounding interventions in predictive futures and explicit obligations, the method enables safe, selective changes without sacrificing performance or incurring frequent unsafe moves. This work provides a template for integrating safety‑aware selection into reinforcement learning pipelines that rely on predicted world models.  

## Related Concepts  
- World Action Models (WAMs) – action‑conditioned predictions of future states.  
- Typed admissibility checks – formal conditions ensuring an action is safe or feasible.  
- Event‑conditioned verification – confirming that specific events occur in the predicted future.  
- Calibration gates – decision thresholds that balance intervention and abstention.  
- Selection layers – components of policy networks that choose among candidate actions.  
- Collaborative robotics – multi‑robot or bimanual tasks requiring coordination.
