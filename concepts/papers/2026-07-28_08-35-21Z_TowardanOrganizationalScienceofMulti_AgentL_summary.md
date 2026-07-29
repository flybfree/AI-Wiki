# Summary: 2026-07-28_08-35-21Z_TowardanOrganizationalScienceofMulti_AgentLLMSyste.md
Saved: 2026-07-28 20:22
Source: 2026-07-28_08-35-21Z_TowardanOrganizationalScienceofMulti_AgentLLMSyste.md
Model: None

---

## Summary  
The paper proposes IMACS, an organizational science framework that decouples the three dimensions of multi‑agent LLM systems—who (roles), how (coordination), and which algorithm (collaboration protocol)—into orthogonal layers. It introduces a common interface for six collaboration algorithms while making roles, coordination, and accountability independently configurable. The authors conduct controlled experiments varying assignments while holding the algorithm constant, and they also develop Adaptive Org Routing, a meta‑protocol that learns optimal protocols per task via contextual bandits. This work advances the field by providing an experimental basis for organizational design in LLM teams.  

## Key Contributions  
- IMACS decouples who, how, which algorithm into orthogonal layers.  
- Controlled experiments show organizational assignments affect outcomes when the protocol routes deliverables through the accountable agent.  
- Adaptive Org Routing meta‑protocol outperforms fixed protocols and learns optimal protocol per task.  

## Methodology  
The authors built IMACS as a layered system where each layer (roles, coordination, accountability) is configurable independently; they expose six algorithms via a common interface. They performed controlled comparisons varying assignments while holding the algorithm constant, and they implemented Adaptive Org Routing using contextual bandits to select protocols based on quality‑cost tradeoff, training online on benchmark and LLM‑judge rewards.  

## Results  
In experiments with a fixed protocol, moving the accountable role altered outcomes; across model families, optimal placement varied. Adaptive Org Routing achieved higher average reward (≈12 % improvement) over the best fixed protocol in the controlled study, with online learning converging to near‑optimal selection within few episodes.  

## Significance  
This work demonstrates that organizational design is not static but must be validated or learned per model family; it provides a reusable framework for LLM team coordination and opens a path to automated optimization of collaboration protocols.  

## Related Concepts  
Multi‑agent frameworks, Large Language Models (LLMs), Belbin roles, Mintzberg coordination models, RACI accountability, contextual bandits, meta‑protocols, organizational science, algorithmic fusion.
