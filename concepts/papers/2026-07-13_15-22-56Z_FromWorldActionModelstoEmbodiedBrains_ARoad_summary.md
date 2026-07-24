# Summary: 2026-07-13_15-22-56Z_FromWorldActionModelstoEmbodiedBrains_ARoadmapforO.md
Saved: 2026-07-23 23:41
Source: 2026-07-13_15-22-56Z_FromWorldActionModelstoEmbodiedBrains_ARoadmapforO.md
Model: None

---

## Summary  
The paper reviews the evolution of artificial agents that can reason and act in the physical world, emphasizing World Action Models (WAMs) as a promising bridge between candidate interventions and their predicted consequences. It identifies three inter‑related gaps—model roles and representations, objectives and standardization, and system composition—that fragment current progress toward embodied intelligence. The authors propose a co‑evolution roadmap centered on an *embodied brain* that issues state‑transition or capability requests rather than direct actuator commands, integrating multimodal context, candidate interventions, and verification through tools. This framework aims to create a modular physical‑intelligence stack capable of adaptive, self‑improving agents.

## Key Contributions  
- [Finding 1] WAMs link candidate actions with predicted consequences but suffer from incompatible action spaces and prediction targets across research.  
- [Finding 2] Current datasets and tasks use divergent conventions, hindering reuse and evaluation of models.  
- [Finding 3] Runtime systems expose limited interfaces, preventing integration into a unified physical harness.

## Methodology  
The authors conducted a systematic literature review to map the state‑of‑the‑art in WAMs, then organized identified limitations into three coupled gaps. They proposed a co‑evolution roadmap that prioritizes an embodied brain architecture and a physical harness composed of tools, controllers, verification, and trace logging.

## Results  
While no new experiments are reported, the paper presents a theoretical decomposition showing how each component—WAM prototype, harness, shared contracts, and closed‑loop post‑training—can be combined to form a modular stack. It argues that this integration enables self‑improving embodied agents by converting verified interaction into reusable experience.

## Significance  
This roadmap addresses fragmentation in physical AI research, offering a clear pathway toward general physical intelligence and facilitating scalable, reusable systems across domains such as robotics, simulation, and real‑world control.

## Related Concepts  
World Action Models (WAMs), embodied brain, multimodal context, candidate interventions, state‑transition requests, capability requests, tool harness, verification, trace logging, shared contracts, closed‑loop learning, modular stack.
