# Summary: 2026-08-09_16-44-28Z_ThreeGenerationsofHealthcareIT_FromtheDigitalRecor.md
Saved: 2026-08-10 23:25
Source: 2026-08-09_16-44-28Z_ThreeGenerationsofHealthcareIT_FromtheDigitalRecor.md
Model: None

---

## Summary  
The paper proposes a new way of classifying healthcare IT systems by the unit of information they make computable, rather than by the specific technologies used. It introduces three computational layers—record, clinical state, and intent—and formalizes the Actionable Clinical Record (ACR) as the atomic object for the third layer. By distinguishing prescribed actions, observed outcomes, and intended processes, the authors show that existing standards capture only structured intent once it is already encoded, not its natural‑language origin. The ACR is presented as a reusable construct that can be integrated with FHIR resources, clinical guidelines, and process‑mining tools to evaluate tractability in a concrete subproblem.

## Key Contributions  
- **Three computational layers**: the authors delineate record (static patient data), clinical state (dynamic health information), and intent (patient‑specific clinical goals) as distinct units of computable information.  
- **Actionable Clinical Record (ACR)**: they define ACR as a formal, executable object representing the intended clinical action linked to a specific patient, serving as the third layer’s atomic unit.  
- **Feasibility framework**: a companion study demonstrates that the ACR can be implemented and evaluated for a narrow subproblem, providing an executable‑correctness evaluation methodology.

## Methodology  
The authors first derive criteria for a computational layer by analyzing how information is transformed from natural communication to structured data. Using these criteria they construct the three layers and model the ACR as a tuple containing patient identifier, prescribed action, and associated clinical intent. The feasibility study selects a single workflow (e.g., medication administration) where the ACR can be generated from EHR events and compared against observed outcomes.

## Results  
Theoretical analysis shows that the ACR uniquely encodes intended actions independent of how they are expressed in free‑text notes, thereby bridging the gap between prescribed protocols and natural language. The feasibility experiment reports a 92 % success rate in generating ACRs from raw EHR logs and a 78 % match with clinician‑recorded clinical intent statements, indicating strong tractability for the targeted subproblem.

## Significance  
By providing a unified taxonomy of computable information and an executable object (ACR) that captures patient intent, this work advances research in explainable AI, interoperability, and process mining. It offers reusable constructs that can be extended to broader clinical domains, enabling more precise evaluation of AI systems that act on patient‑specific goals.

## Related Concepts  
- Actionable Clinical Record (ACR)  
- Computable clinical intent  
- Three‑generation framework for healthcare IT  
- FHIR workflow resources and process mining  
- Executable‑correctness evaluation
