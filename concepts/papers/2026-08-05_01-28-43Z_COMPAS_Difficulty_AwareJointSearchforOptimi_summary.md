# Summary: 2026-08-05_01-28-43Z_COMPAS_Difficulty_AwareJointSearchforOptimizingCod.md
Saved: 2026-08-05 22:22
Source: 2026-08-05_01-28-43Z_COMPAS_Difficulty_AwareJointSearchforOptimizingCod.md
Model: None

---

## Summary  
The paper addresses the challenge of optimizing code generation by jointly tuning model selection, prompts, and decoding settings across tasks, discovering that these choices interact and that optimal configurations vary with task difficulty. It proposes COMPAS, a difficulty‑aware framework that learns group‑specific quality‑cost frontiers through low‑cost model selection and joint prompt‑decoding search, enabling online routing to the best configuration per task without further search. The method is evaluated on LiveCodeBench and SWE‑bench, achieving notable improvements in pass@1 and task resolution rates while drastically reducing cost.

## Key Contributions  
- [Finding 1] Joint interactions between model selection, prompts, and decoding settings affect code generation performance.  
- [Finding 2] Optimal configurations vary by task difficulty, requiring a difficulty‑aware optimization approach.  
- [Finding 3] COMPAS learns group‑specific quality‑cost frontiers via low‑cost model selection and joint prompt‑decoding search.

## Methodology  
The authors adopt a multi‑stage optimization pipeline. First, they conduct a global search over a limited set of models to identify cost‑effective candidates. Then, for each candidate model, they perform a joint search over prompts and decoding parameters using low‑cost sampling, constructing quality‑cost curves per task group. Finally, at inference time, tasks are routed to the front that maximizes pass@1 while staying within budget, avoiding repeated searches.

## Results  
On LiveCodeBench, COMPAS raises pass@1 from 45.9% (best baseline) to 52.8%, and reduces total cost from $36.57 to $4.92. On SWE‑bench repository‑level generation, it resolves 76.0% of tasks versus 70.0% for the best baseline.

## Significance  
The work demonstrates that a unified, difficulty‑aware optimization can dramatically improve code generation efficiency and scalability, offering a practical path to lower costs while maintaining higher quality across diverse tasks.

## Related Concepts  
Code generation, large language models (LLMs), prompt engineering, decoding strategies, cost‑effective search, group‑specific optimization, pass@1 metric, SWE‑bench benchmark, LiveCodeBench.
