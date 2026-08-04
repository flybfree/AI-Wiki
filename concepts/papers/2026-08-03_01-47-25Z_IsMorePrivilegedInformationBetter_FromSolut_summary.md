# Summary: 2026-08-03_01-47-25Z_IsMorePrivilegedInformationBetter_FromSolutionTrac.md
Saved: 2026-08-03 23:17
Source: 2026-08-03_01-47-25Z_IsMorePrivilegedInformationBetter_FromSolutionTrac.md
Model: None

---

## Summary  
The paper investigates why on‑policy self‑distillation (OPSD) can be limited when the teacher’s token‑level targets rely on reference‑specific information that is unavailable at inference time. To address this, the authors introduce Problem‑Space‑Guided OPSD (PS‑OPSD), which replaces the full solution with a concise trajectory‑grounded guide that captures only the essential problem space: initial state, goal conditions, constraints, and a selected transition path. The student rollout and OPSD objective remain unchanged; PS‑OPSD therefore supplies a more compact, inference‑compatible representation of privileged information. Across three mathematical reasoning benchmarks and model scales from 1.7 B to 8 B, PS‑OPSD achieves the highest aggregate question‑only accuracy among all compared methods.

## Key Contributions  
- **Finding 1:** Problem‑Space‑Guided OPSD improves performance by using a reduced, problem‑space‑focused guidance instead of the complete solution.  
- **Finding 2:** The relevance of the guidance and its path coherence directly explain the observed accuracy gains.  
- **Finding 3:** PS‑OPSD consistently outperforms alternative approaches on multiple benchmarks and model scales.

## Methodology  
The authors adopt a teacher‑student rollout framework unchanged from standard OPSD. Instead of feeding the student the full reference solution, they generate a trajectory‑grounded guide that encodes: (i) the initial state of the problem, (ii) the goal conditions to be achieved, (iii) any constraints governing the transition, and (iv) a selected path through the state space. This guide is conditioned on the teacher’s reference solution but is far less verbose than the full trace. The student model receives only this lightweight guidance plus the raw question, preserving the original OPSD loss objective while mitigating reliance on unavailable token‑level targets.

## Results  
Experiments are conducted on three mathematical reasoning benchmarks (e.g., arithmetic word problems, logical deduction tasks). Model sizes ranging from 1.7 B to 8 B parameters are evaluated. PS‑OPSD attains the highest aggregate question‑only accuracy across all models and datasets, surpassing baseline OPSD, full‑solution distillation, and other state‑of‑the‑art methods. Controlled ablation studies confirm that (a) guidance relevance—how much of the problem space is captured—correlates with performance improvements, and (b) path coherence (logical consistency of the transition sequence) further boosts accuracy.

## Significance  
This work demonstrates that representing privileged information as a compact problem‑space guide rather than a full solution trace can be both effective and efficient. It clarifies a key design choice in OPSD: how much teacher knowledge to expose to the student, balancing completeness with inference feasibility. The findings suggest that future self‑distillation frameworks should prioritize guidance relevance over exhaustive solution copying.

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Token‑level targets and reference solutions  
- Problem space representation  
- Trajectory‑grounded guidance  
- Solution traces vs. problem‑space guides  
- Model scaling effects on reasoning performance
