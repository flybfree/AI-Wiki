# Summary: 2026-08-07_16-40-03Z_PACE_Primitive_AwareCodeEvolutionforAutomatedAlgor.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_16-40-03Z_PACE_Primitive_AwareCodeEvolutionforAutomatedAlgor.md
Model: None

---

## Summary  
The paper addresses the limitation of LLM‑based automated algorithm design, which treats algorithms as whole programs and discards valuable local logic. To overcome this, PACE introduces a primitive‑aware framework that isolates reusable logical units into persistent Executable Algorithmic Primitives (EAPs). The framework enables code‑level transfer by maintaining a dynamic set of EAPs across program generations. Primitive‑aware operators are used to evolve algorithms while guaranteeing the retention and cross‑program transfer of these components.

## Key Contributions  
- [Finding 1] Decouples local logic from complete programs, representing it as persistent Executable Algorithmic Primitives (EAPs).  
- [Finding 2] Introduces primitive‑aware operators that structurally guarantee retention and cross‑program transfer of EAPs.  
- [Finding 3] Uses Thompson sampling based on parent‑relative performance improvements to select primitives without requiring extra evaluation datasets.

## Methodology  
The authors approached the problem by first identifying reusable algorithmic snippets as EAPs, then designing a dynamic set that persists across evolution steps. Evolution is driven by primitive‑aware operators that enforce structural integrity of these components. For operator selection, they applied Thompson sampling conditioned on parent‑relative performance gains, allowing the system to choose primitives from the existing set without needing additional benchmark data.

## Results  
Experiments on four benchmark tasks show that PACE discovers competitive algorithms while preserving valuable algorithmic components. The primitive‑aware operators maintain high transferability of EAPs across generations, and the Thompson sampling strategy efficiently guides selection without extra datasets, achieving performance comparable to or better than baseline whole‑program methods.

## Significance  
This work matters because it mitigates the loss of code snippets that would otherwise be discarded in whole‑program algorithm design. By preserving and transferring EAPs, PACE enables a more granular evaluation of component contribution and improves the robustness of automated algorithm generation.

## Related Concepts  
- LLM‑based automated algorithm design  
- Whole‑program perspective  
- Executable Algorithmic Primitives (EAPs)  
- Thompson sampling  
- Primitive‑aware operators  
- Dynamic set of EAPs  
- Code‑level transfer
