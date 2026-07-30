# Summary: 2026-07-29_11-26-33Z_SkillRise_AgenticReinforcementLearningforCross_Tas.md
Saved: 2026-07-29 20:32
Source: 2026-07-29_11-26-33Z_SkillRise_AgenticReinforcementLearningforCross_Tas.md
Model: None

---

## Summary  
SkillRise proposes a unified reinforcement‑learning framework that enables large language model agents to learn and evolve reusable skills across multiple related tasks. By treating task instances as stages of a progressive sequence, the method uses a single policy to both solve each task and curate an evolving skill document for future tasks. The approach decouples credit assignment between solving and curating, allowing the agent to reap benefits from downstream tasks without repeated sampling. Experiments demonstrate that SkillRise outperforms strong baselines by 2.3–8.5 percentage points on Pass@1 across ALFWorld, WebShop, and ScienceWorld.

## Key Contributions  
- [Finding 1] SkillRise introduces a single‑policy reinforcement learning framework that learns skills across tasks via an evolving skill document passed between stages.  
- [Finding 2] The method decouples credit assignment: solving is supervised by immediate task outcomes while curating receives discounted rewards from future tasks, enabling cross‑task supervision.  
- [Finding 3] SkillRise achieves the strongest Pass@1 performance and reduces pipeline runtime compared to multi‑stage skill extraction pipelines.

## Methodology  
The authors organize related instances into progressively challenging sequences, letting a shared policy alternate between solving the current task and updating a skill document that is fed directly to the next task. Credit assignment is split: the reward for solving the present episode is immediate, whereas rewards for curating are delayed by a discount factor reflecting downstream tasks. This decoupling allows the agent to learn transferable representations without needing repeated attempts on the same task.

## Results  
Across ALFWorld, WebShop, and ScienceWorld, SkillRise reaches Pass@1 scores that exceed the strongest baseline by 2.3–8.5 percentage points. The learned curation policy remains effective even when tasks are revisited repeatedly, indicating stable skill reuse. Moreover, performance improves with longer sequences of related tasks even if each task is attempted only once, suggesting efficient transfer rather than mere sampling.

## Significance  
SkillRise provides a simple and efficient training paradigm that enables LLM agents to extract, refine, and reuse transferable skills across diverse tasks, reducing the overhead of multi‑stage pipelines. This work advances agentic reinforcement learning by showing how skill evolution can be learned end‑to‑end with minimal extra computation.

## Related Concepts  
- Reinforcement Learning (RL)  
- Skill extraction / skill representation  
- Cross‑task transfer learning  
- Decoupled credit assignment  
- Progressive task sequencing
