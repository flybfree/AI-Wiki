# Summary: 2026-07-27_16-04-24Z_EvaluatingtheImpactofExplainableAIonTrustinAI_Assi.md
Saved: 2026-07-27 23:05
Source: 2026-07-27_16-04-24Z_EvaluatingtheImpactofExplainableAIonTrustinAI_Assi.md
Model: None

---

## Summary  
This paper investigates how the level of Explainable AI (XAI) support influences developers’ trust in AI‑generated code review feedback. By comparing three LLM‑based review systems that provide detailed explanations, only feedback, or no explanation, the authors aim to uncover whether richer XAI improves both trust and agreement with recommendations. The study contributes empirical evidence on how XAI can be tuned to balance perceived reliability with willingness to accept AI suggestions.  

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Full explanations (Condition A) yield the highest perceived trust scores (M = 3.99/5) but not the highest agreement, indicating that more detail may prompt developers to question recommendations.  
- Moderate explanations (Condition B) achieve the highest agreement rate (89.22%), suggesting a sweet‑spot where enough rationale encourages acceptance without excessive doubt.  
- No explanations (Condition C) produce the lowest trust and agreement, confirming that XAI is essential for mitigating skepticism in AI‑assisted code review.  

## Methodology  
The authors conducted a within‑subjects user study with 34 participants who evaluated real‑world code change requests alongside three LLM‑generated reviews under the three conditions. Trust perception was measured on a 5‑point Likert scale, agreement was recorded as binary acceptance of the AI recommendation, and reviewers were asked to provide reasoning for each decision. Review time was also logged to assess any impact of explanation level on processing speed.  

## Results  
Trust scores increased monotonically with explanation depth (C < B < A), while agreement peaked at moderate explanations (B). The effect on review duration was non‑significant, indicating that richer XAI does not slow developers’ workflows. The most frequently cited reasons for AI decisions were code readability and correctness.  

## Significance  
These findings highlight the critical role of XAI in shaping developer trust and acceptance of automated code reviews, offering designers a clear trade‑off between transparency and responsiveness. They inform future research on human factors in AI‑assisted software development and guide the creation of more reliable, user‑friendly review tools.  

## Related Concepts  
- Explainable AI (XAI)  
- Trust in AI systems  
- Code review automation  
- Large language models (LLMs) for feedback generation  
- Within‑subjects experimental design
