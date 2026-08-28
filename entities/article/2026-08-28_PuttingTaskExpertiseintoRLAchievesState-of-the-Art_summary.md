# Summary: 2026-08-28_PuttingTaskExpertiseintoRLAchievesState-of-the-Art.md
Saved: 2026-08-28 09:38
Source: 2026-08-28_PuttingTaskExpertiseintoRLAchievesState-of-the-Art.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The article shows that embedding human‑level task expertise into reinforcement learning can let a model reach human performance on text‑to‑SQL without using scaffolding. By fine‑tuning the model with expert‑verified data and carefully shaped rewards, it attains BIRD scores of 92.96%, matching the benchmark that humans achieve.

## Key Takeaways  
- Human expertise can be encoded into RL rewards to close the performance gap between AI and human experts.  
- Using an expert‑verified training set removes label errors that could poison reinforcement learning.  
- Reward shaping addresses two common failure modes, enabling the model to perform at human level.

## Context  
Text‑to‑SQL remains a critical task for enterprises that rely on relational databases, yet LLM scores have lagged behind human performance despite abundant training data. Benchmarks such as BIRD measure translation accuracy, and current state‑of‑the‑art models score in the mid‑80s at high cost. Traditional approaches like OpenHands or MetaGPT use agentic scaffolding, but they still fall short of human capability.

## Implications  
This work demonstrates that moving beyond prompt engineering toward experience‑based training can unlock practical, high‑volume applications where latency and cost are prohibitive. It signals a shift from static prompting to dynamic reinforcement learning pipelines that better reflect real‑world problem solving.
