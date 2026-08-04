# Summary: 2026-08-01_22-12-02Z_AssumingYouKnew_FixinganEpistemicSemanticsforFlowP.md
Saved: 2026-08-03 21:29
Source: 2026-08-01_22-12-02Z_AssumingYouKnew_FixinganEpistemicSemanticsforFlowP.md
Model: None

---

## Summary  
The paper aims to provide a robust epistemic semantics for flow policies, addressing the challenge of selective downgrading in security requirements. It builds on the earlier CSF 2018 work “Assuming You Know” and presents a corrected formalization machine‑checked in Rocq. The framework unifies relational annotations with epistemic logic, enabling precise policy enforcement. By integrating these fixes, the paper demonstrates that epistemic semantics can be both precise and practical for high‑level security policies.  

## Key Contributions  
- [Finding 1] The authors introduced a corrected formalization of the epistemic semantics for flow policies, resolving gaps in the original CSF 2018 presentation.  
- [Finding 2] They machine‑checked this formalization using Rocq, establishing correctness proofs that validate the framework’s soundness and completeness.  
- [Finding 3] The unified model enables systematic comparison of different policy specification styles and facilitates automated enforcement via existing verification tools.  

## Methodology  
The authors approached the problem by revisiting the epistemic semantics introduced in “Assuming You Know”, identifying the original formalization as incomplete, and then constructing a corrected version. They leveraged an agentic AI coding assistant to generate and refine the Rocq code, ensuring that all relational annotations are properly encoded within the epistemic framework. The process combined theoretical analysis with practical AI‑assisted coding to produce a verifiable artifact.  

## Results  
The main theoretical result is that the corrected model captures selective downgrading exactly, preserving both preservation and weakening properties of flow policies under epistemic operators. Additionally, the machine‑checked proof demonstrates that the formalization is sound with respect to the intended semantics. These results show that the framework scales to complex programs and integrates seamlessly with existing verification pipelines.  

## Significance  
This work matters because it provides a reliable, general framework for expressing security‑related information flows in programs, moving beyond ad‑hoc or sketchy formalisms. By integrating AI assistance with formal verification, it lowers the barrier for practitioners to adopt precise policy specifications and compare them objectively. Future work could explore extensions to dynamic policies and larger language ecosystems.  

## Related Concepts  
epistemic logic, relational annotations, flow policies, selective downgrading, CSF 2018 “Assuming You Know”, Rocq proof assistant, agentic AI coding assistants
