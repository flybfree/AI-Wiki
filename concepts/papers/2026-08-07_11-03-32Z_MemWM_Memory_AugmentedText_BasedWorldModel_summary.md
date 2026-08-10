# Summary: 2026-08-07_11-03-32Z_MemWM_Memory_AugmentedText_BasedWorldModel.md
Saved: 2026-08-09 22:54
Source: 2026-08-07_11-03-32Z_MemWM_Memory_AugmentedText_BasedWorldModel.md
Model: None

---

## Summary  
The paper proposes MemWM, a memory‑augmented text‑based world model that corrects systematic prediction errors in environment state transitions. It introduces a curated memory bank containing transition rules, state caches and hard facts to condition next‑state imagination. Evaluation shows factual fidelity improves dramatically compared with standard SFT baselines. Memory‑conditioned agents achieve higher downstream performance across multiple benchmark worlds.  

## Key Contributions  
- Finding 1: MemWM’s memory‑augmented training boosts Structured State Fidelity (SSF) by up to 206.3% over SFT.  
- Finding 2: In full planning, frozen policy models benefit from task‑level skills and step‑wise corrective guidance retrieved from memory.  
- Finding 3: Memory retrieval improves downstream success rates with up to a 65.4% relative gain on ALFWorld, WebShop, ScienceWorld.  

## Methodology  
The authors design MemWM by augmenting the world model’s text generation with a structured memory bank that stores transition rules, state caches and fact entries. During training, the model is conditioned on retrieved memory passages to generate next‑state descriptions. In planning, the policy remains frozen while memory supplies task‑level skills and corrective actions at each step.  

## Results  
Experiments across three benchmark worlds (ALFWorld, WebShop, ScienceWorld) demonstrate that MemWM agents outperform SFT models in factual state preservation (SSF scores) and downstream task success. Memory‑augmented agents achieve up to 65.4% relative improvement in success rates compared with baseline SFT models.  

## Significance  
By correcting systematic prediction errors through explicit memory, MemWM provides a practical path toward more reliable world‑model agents that can plan accurately without retraining the policy. This bridges the gap between text generation and robust environmental simulation, enabling safer and more efficient autonomous planning.  

## Related Concepts  
Memory‑augmented models, Structured State Fidelity (SSF), transition rules, state caches, task‑level skills, step‑wise corrective guidance, world modeling, planning agents.
