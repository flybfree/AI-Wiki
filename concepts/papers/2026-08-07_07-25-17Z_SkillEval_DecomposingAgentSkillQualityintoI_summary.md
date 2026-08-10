# Summary: 2026-08-07_07-25-17Z_SkillEval_DecomposingAgentSkillQualityintoInterpre.md
Saved: 2026-08-09 22:45
Source: 2026-08-07_07-25-17Z_SkillEval_DecomposingAgentSkillQualityintoInterpre.md
Model: None

---

## Summary  
The paper introduces **SkillEval**, an interpretable framework that decomposes the quality of a reusable agent‑skill document into several distinct, measurable signals rather than relying solely on downstream task performance. By learning fixed scoring directions from positive and negative skill pairs in the model’s hidden representation space, SkillEval produces transparent scores for each property (e.g., clarity, relevance) while filtering out irrelevant factors such as length or formatting. The framework enables reliable discrimination between high‑ and low‑quality skills, early prediction of task success, and targeted revisions that improve both the decomposed signals and downstream outcomes.

## Key Contributions  
- [Finding 1] General document properties (structure, clarity, relevance) are primary drivers of skill quality, not just their impact on specific tasks.  
- [Finding 2] SkillEval learns interpretable, fixed scoring directions from controlled positive‑negative skill pairs in the hidden representation space to isolate each property’s contribution.  
- [Finding 3] Guided revisions based on SkillEval scores raise targeted property scores and increase downstream task pass rates.

## Methodology  
SkillEval treats a skill document as a vector embedded by a language model. The authors train a supervised model on pairs of high‑quality (positive) and low‑quality (negative) skills, extracting direction vectors that align with the desired quality properties. A new skill is scored by projecting its hidden representation onto these pre‑computed directions, yielding a scalar for each property. To keep scores meaningful, the projection discards irrelevant document features such as length or formatting through dimensionality reduction before projection.

## Results  
In controlled tests, SkillEval consistently separates high‑quality skills from low‑quality ones with high precision and recall. The decomposed scores correlate strongly (r ≈ 0.78) with downstream task pass rates, indicating early validity. When authors revise a skill according to the lowest‑scoring property identified by SkillEval, the revised document improves that specific score and raises overall task success from 62 % to 79 %. The framework also reduces variance caused by surface features like formatting, yielding stable scores across different document templates.

## Significance  
SkillEval bridges the gap between opaque downstream evaluation and transparent skill quality assessment. It provides a reusable, property‑level metric that can be applied to any skill documentation without retraining models, allowing rapid feedback loops for improvement. By isolating which aspects of a skill are weak, it enables targeted revisions that directly boost performance, reducing costly full re‑evaluation cycles.

## Related Concepts  
- Agent skills (procedural knowledge)  
- Decomposable evaluation metrics  
- Hidden representation space  
- Interpretable scoring directions  
- Document‑level skill documentation (SKILL.md)  
- Downstream task performance correlation  
- Feature filtering and dimensionality reduction
