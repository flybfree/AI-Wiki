# Summary: 2026-08-06_16-07-26Z_ContinualLearninginTransition.md
Saved: 2026-08-06 22:19
Source: 2026-08-06_16-07-26Z_ContinualLearninginTransition.md
Model: None

---

## Summary  
The paper proposes a tri‑axial framework to characterize the shift in continual learning from parameter‑centric to system‑level adaptation. It surveys how, when and where learning occurs across off‑policy, on‑policy and beyond‑gradient mechanisms, pre‑training/post‑training/inference stages, and internal versus external constraints. The authors trace this transition, identify challenges, and outline future research directions.

## Key Contributions  
- Introduces a tri‑axial taxonomy (When, How, Where) to systematically analyze the evolution of continual learning.  
- Conducts a comprehensive survey of representative methods across all three dimensions, highlighting their interplay and limitations.  
- Discusses key challenges and broader implications of moving from parameter adaptation to system‑level adaptation.

## Methodology  
The authors adopt a conceptual taxonomy that partitions continual learning into three orthogonal axes: temporal (When), mechanistic (How), and structural (Where). By mapping each axis onto existing paradigms—off‑policy vs on‑policy, pre‑training/post‑training/inference training, internal parameter updates versus external memory/skill libraries—they create a matrix for comparison. The survey is organized around this matrix, allowing systematic tracing of the transition from classic parameter‑centric approaches to newer system‑level strategies.

## Results  
The analysis reveals that most existing CL systems still operate primarily within the internal‑parameter space while neglecting external harness components; however, recent works on test‑time training and on‑policy updates demonstrate early adoption of the Where dimension. The survey also shows a growing diversity of How mechanisms, yet off‑policy methods remain under‑explored relative to their theoretical promise.

## Significance  
This shift from parameter‑centric to system‑level adaptation redefines model design, deployment, and evaluation criteria for continual learning tasks. It opens avenues for integrating external memory and skill libraries, but also introduces challenges in consistency, forgetting, and scalability across heterogeneous environments.

## Related Concepts  
Continual Learning (CL), on‑policy vs off‑policy learning, test‑time training, internal parameter adaptation, external harness components (memory, skill libraries), pre‑training/post‑training/inference stages, system‑level adaptation, tri‑axial taxonomy.
