# Summary: 2026-08-05_08-53-16Z_WhenAbsenceIsEvidence_EvaluatingCompleteness_Sensi.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_08-53-16Z_WhenAbsenceIsEvidence_EvaluatingCompleteness_Sensi.md
Model: None

---

## Summary  
Large language models are frequently asked whether a piece of information is absent from a given record, yet they often produce a negative answer even when the evidence does not fully cover the query. This paper introduces **completeness‑sensitive negative reasoning** and evaluates it on three LLM families using a controlled paired core (CROWN‑Synth) and real‑document contrast sets (CROWN‑Real). The authors demonstrate that models exhibit unstable closure judgments, over‑closing (giving a negative answer when evidence is incomplete) and under‑closing (failing to give a negative answer when evidence is complete), with systematic errors traced to mischaracterization of evidence coverage.  

## Key Contributions  
- **Finding 1:** LLM closure judgments are unstable; they over‑close or under‑close depending on how the query’s scope relates to the observed facts, leading to unreliable “Certified‑Negative” vs. “Unknown” outputs.  
- **Finding 2:** The CROWN‑Synth synthetic core reveals an asymmetric failure mode: models treat implicitly partial evidence as if it fully covers the query, causing systematic over‑closure.  
- **Finding 3:** Real‑document evaluation (CROWN‑Real) confirms that this asymmetry persists on genuine data, though its strength and the balance between over‑ and under‑closure vary across model families, prompts, and source documents.  

## Methodology  
The authors construct CROWN‑QA, a framework that isolates the effect of evidence coverage by fixing the question and observed facts while varying only how much of the query is covered by the evidence. **CROWN‑Synth** creates paired examples where one side has full coverage (Certified‑Negative) and the other has partial or implicit coverage (Unknown). **CROWN‑Real** builds a contrast set from real documents, generating similar coverage variants for each model family. The evaluation measures closure accuracy, over‑closure rate, under‑closure rate, and error distribution across the three families.  

## Results  
Across all models, closure judgments are highly variable: some produce “Certified‑Negative” even when evidence is incomplete (over‑closure), while others give “Unknown” despite complete coverage (under‑closure). Certificate analysis shows that most over‑closures stem from mischaracterizing implicit partial evidence as fully covering the query. In CROWN‑Real, the asymmetry remains robust; however, model A shows strong over‑closure, Model B a near‑balanced split, and Model C predominantly under‑closes. Prompting shifts errors between over‑ and under‑closure rather than eliminating them.  

## Significance  
The findings highlight a critical gap in current LLMs: they lack true completeness‑sensitive negative reasoning, which can lead to unsafe or misleading answers when information is missing or only partially relevant. Addressing this issue is essential for reliable knowledge integration, safety‑critical applications, and any system that must distinguish “no evidence” from “evidence insufficient.”  

## Related Concepts  
- Negative reasoning (asserting absence)  
- Closure judgment in LLMs  
- Evidence coverage (full vs. partial vs. implicit)  
- Certification of knowledge claims  
- CROWN‑QA framework for systematic evaluation
