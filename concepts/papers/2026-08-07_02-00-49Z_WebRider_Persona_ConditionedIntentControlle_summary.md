# Summary: 2026-08-07_02-00-49Z_WebRider_Persona_ConditionedIntentControllersforLi.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_02-00-49Z_WebRider_Persona_ConditionedIntentControllersforLi.md
Model: None

---

## Summary  
WebRider addresses a critical flaw in current live‑web assistants: they frequently finish tasks but ignore the policy constraints that define the delegation. The authors formalize this delegated policy as an *intent contract* and introduce a hierarchical controller that separates action realization from the final answer, enabling auditable, persona‑consistent assistance. Their system is evaluated on 4,096 live contracts across 42 public websites, showing that while task completion remains high (≈ 99 %), policy fidelity drops sharply (≈ 38 %). By treating the browsing path as a first‑class object and using it as a training signal for an 8B action‑policy model, WebRider demonstrates a learnable controller that outperforms baseline executables.  

## Key Contributions  
- **Finding 1:** Live‑web agents complete tasks at high rates but only about one‑third of the time respect the full delegated policy, revealing a gap between output and constraint adherence.  
- **Finding 2:** WebRider introduces an *intent contract* that records goals, constraints, evidence obligations, answer form, and persona controls, providing a formal, auditable representation of delegation.  
- **Finding 3:** The guarded middle interface serves as a high‑quality training signal; an 8B action‑policy model trained on this interface outperforms executable‑only baselines under the same controller.  

## Methodology  
WebRider adopts a three‑layer architecture: (1) a top‑layer controller that maintains the intent contract, (2) a middle layer that realizes intentions as *guarded* executable actions, and (3) a tool layer that executes those actions via browser, search, or map APIs. The authors evaluate this design on RiderBench, a benchmark comprising 4,096 live contracts across 42 public websites. Each contract is audited for both internal contract state and visible user experience to verify policy preservation and persona consistency. The browsing path is treated as an object that can be inspected and logged throughout the interaction.  

## Results  
Task completion on RiderBench remains robust at 99.2 %, but only 38.8 % of runs honor every contract clause, confirming the fidelity gap. Training a 8B action‑policy model using the guarded middle interface yields higher performance than executing actions directly (≈ 15 % improvement in policy adherence). Human judges also rate the WebRider system as more trustworthy because the audit trail is explicit and persona‑consistent.  

## Significance  
WebRider bridges the disconnect between action realization and final answer, offering a framework where policies are first‑class objects that survive page changes. By separating execution from output, it enables auditable, human‑judgeable assistance and allows learning without conflating what is done with what is returned. This work paves the way for truly responsible live‑web agents that respect user intent beyond mere task completion.  

## Related Concepts  
- Intent contract  
- Hierarchical controller (top/middle/tool layers)  
- Guarded executable actions  
- Persona conditioning  
- Live‑audit methodology  
- RiderBench dataset
