# Summary: 2026-08-09_16-44-28Z_ThreeGenerationsofHealthcareIT_FromtheDigitalRecor.md
Saved: 2026-08-10 23:25
Source: 2026-08-09_16-44-28Z_ThreeGenerationsofHealthcareIT_FromtheDigitalRecor.md
Model: None

---

## Summary  
The paper argues that healthcare IT should be organized by the computational layers it creates rather than by the technologies used, focusing on making patient‑specific clinical intent computable. It introduces a third layer of “intent” beyond traditional records and clinical state, formalizes the Actionable Clinical Record (ACR) as its atomic object, and shows how this framework complements existing standards such as FHIR.

## Key Contributions  
- The authors devise a three‑generation framework that categorizes healthcare IT into record, clinical state, and intent layers.  
- They formalize the Actionable Clinical Record (ACR) as an atomic computational object representing patient‑specific clinical intent.  
- They demonstrate tractability of computing intent from natural communication using process mining and propose an executable‑correctness evaluation framework.

## Methodology  
The researchers first derive criteria for a computational layer, then map existing standards to the record and clinical state layers, after which they introduce the intent layer. The ACR is defined as the atomic unit that embodies this intent; feasibility is illustrated by applying process mining to a narrow subproblem within a healthcare workflow.

## Results  
The study shows that intent can be reliably extracted from unstructured communication using process‑mining techniques, and that the ACR framework enables an executable‑correctness evaluation which passes for the test case. The results confirm that the proposed construct is computationally feasible and can be evaluated systematically.

## Significance  
By shifting research attention to computable clinical intent, the paper provides a reusable construct that moves healthcare IT from merely storing data or enforcing workflows toward aligning systems with patient‑specific goals, offering a foundation for future extensions, evaluations, or falsifications of this direction.

## Related Concepts  
Actionable Clinical Record (ACR), computational layer, FHIR, process mining, executable‑correctness evaluation, prescribed/observed/intended processes.
