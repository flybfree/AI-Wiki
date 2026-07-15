title: "Summary: 2026-06-25_17-44-48Z_EmpoweringGUIAgentsviaAutonomousExperienceExplorat.md"
# Summary: 2026-06-25_17-44-48Z_EmpoweringGUIAgentsviaAutonomousExperienceExplorat.md
Saved: 2026-06-25 22:00
Source: 2026-06-25_17-44-48Z_EmpoweringGUIAgentsviaAutonomousExperienceExplorat.md
Model: None

---


## Summary  
The paper proposes a method to empower GUI agents through autonomous experience exploration and hindsight experience utilization for task planning. It introduces the PEEU (planning experience exploration and utilization) framework that autonomously explores environments, discovers raw experiences, and synthesizes strictly aligned high‑level training data from them. A hierarchical analysis framework called TDHAF is introduced to evaluate compositional generalization across three granularities: low, middle, and high task levels. Experiments on real‑world benchmarks show a 7B model achieving 30.6% accuracy, outperforming the larger Qwen2.5‑VL‑32B model.

## Key Contributions  
- PEEU method autonomously explores environments to discover experiences and synthesizes hindsight experience for strictly aligned high‑level training data.  
- TDHAF framework systematically studies compositional generalization across low, middle, and high task granularities.  
- Empirical results demonstrate that small MLLMs can achieve strong OOD planning performance when trained with hindsight high‑level tasks.

## Methodology  
The authors first let the agent interact autonomously within GUI environments to collect raw experiences. These are then processed into structured examples using a retrieval‑augmented generation pipeline that generates hindsight‑aligned high‑level task descriptions. TDHAF decomposes each task into atomic, intermediate, and composite levels, measuring performance at each level via accuracy metrics.

## Results  
On real‑world benchmarks, the 7B PEEU model reaches 30.6% accuracy, outperforming Qwen2.5‑VL‑32B (which is larger but less effective). The analysis shows high‑level training yields stronger OOD generalization than low‑level skill mastery alone.

## Significance  
This work bridges the gap between small, privacy‑preserving LLMs and practical GUI automation by providing a scalable training paradigm that leverages hindsight experience. It offers a clear path to improve planning competence without massive compute resources.

## Related Concepts  
Autonomous exploration, hindsight experience synthesis, task decomposition, compositional generalization, OOD (out‑of‑distribution) generalization, multimodal web agents, small open‑source LLMs, task planning, hierarchical analysis framework.
