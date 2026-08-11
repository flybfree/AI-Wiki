# Summary: 2026-08-08_09-21-47Z_TheAuthorityExpectancyEffectinMulti_UserConflict.md
Saved: 2026-08-10 22:52
Source: 2026-08-08_09-21-47Z_TheAuthorityExpectancyEffectinMulti_UserConflict.md
Model: None

---

## Summary  
This paper investigates how social‑authority signals (SA) interact with severity‑based prioritization in large language models, treating each axis as a model‑elicited baseline – the triage hierarchy and the SA hierarchy. Across four LLMs (Claude, Gemini, GPT, Grok) and three experimental phases (resource allocation, fault attribution, multi‑turn dispute mediation), the authors discover that occupational authority, institutional documentation, and relational congruence can restructure model judgments in ways that cannot be explained by simple additive reweighting. They formalize this pattern as the Authority Expectancy Effect (AEE) and characterize it through three distinct properties: reference‑dependence, evidential reinterpretation, and direction sensitivity.

## Key Contributions  
- [Finding 1] The AEE emerges across multiple LLMs and experimental conditions, demonstrating that authority signals have a non‑additive impact on model decisions.  
- [Finding 2] The effect is reference‑dependent: it is defined only relative to a pre‑authority baseline and changes when the authority signal is introduced or removed.  
- [Finding 3] Direction sensitivity produces opposite outcomes depending on whether the authority position aligns with evidentiary cues.

## Methodology  
The authors operationalize social authority as observable signals (e.g., occupational titles, institutional documentation) and severity‑based prioritization as a model‑elicited baseline. They compare two competing hierarchies – the triage hierarchy (severity‑driven) and the SA hierarchy (authority‑driven) – across four large language models (Claude, Gemini, GPT, Grok) in three experimental phases: resource allocation decisions, fault attribution tasks, and multi‑turn dispute mediation. The design isolates how authority cues reshape judgments beyond simple weighting.

## Results  
Across the experiments, the AEE is consistently observed. Its reference‑dependence means that identical content yields different inferential implications when an authority signal is present versus absent. Evidential reinterpretation shows that the same textual evidence can be interpreted as supporting one party or the other depending on which party bears the SA signal. Direction sensitivity reveals opposite outcomes: alignment of authority position and cues leads to one resolution, while misalignment flips the decision. These findings are not captured by additive reweighting models.

## Significance  
The AEE challenges the assumption that model outputs can be explained by linearly combining authority and severity signals. It highlights a more complex interplay where authority expectations reshape evidential processing, with implications for AI alignment, ethical decision‑making frameworks, and any system that relies on hierarchical judgments. Understanding this effect is crucial for designing robust, trustworthy AI agents.

## Related Concepts  
Social authority, severity‑based prioritization, triage hierarchy, SA hierarchy, Authority Expectancy Effect (AEE), reference‑dependence, evidential reinterpretation, direction sensitivity.
