# Summary: 2026-08-08_14-10-51Z_LongSKILLComplianceasLogicalReasoning_Closure_Grou.md
Saved: 2026-08-10 22:56
Source: 2026-08-08_14-10-51Z_LongSKILLComplianceasLogicalReasoning_Closure_Grou.md
Model: None

---

## Summary  
The paper tackles the challenge of detecting compliance in long SKILL documents within large‑scale agent systems, where inference costs and model capacity clash. It introduces SkillCDG—a graph‑based framework that encodes policies as a two‑layer constraint dependency graph for efficient retrieval and closure‑grounded judgment. The approach cuts token consumption by up to 64 % while boosting detection F1 scores by up to 12.8 %. Moreover, it reveals a scaling trend linking policy‑graph complexity, model size, and performance that can be leveraged for adaptive training.

## Key Contributions  
- [Finding 1] SkillCDG introduces a two‑layer constraint dependency graph that indexes SKILL descriptions at the upper layer and captures atomic constraints at the lower layer.  
- [Finding 2] The framework reduces token usage by up to 64.3 % while improving detection F1 scores by as much as 12.8 % across three enterprise datasets and two public benchmarks.  
- [Finding 3] A consistent scaling trend is identified: end‑to‑end detection correctness follows a complexity‑differentiated pattern, enabling on‑policy distillation to boost small models.

## Methodology  
The authors model complex business policies as graphs where the upper layer routes scenarios via SKILL descriptions and the lower layer encodes dependencies among atomic constraints. During inference, two‑level retrieval selects relevant policy fragments, followed by dependency closure that validates compliance and provides traceability. To handle scale, they analyze how graph complexity interacts with model size and use this insight to select training samples adaptively, then apply on‑policy distillation to transfer knowledge from larger checkpoints to smaller ones.

## Results  
Experiments on three enterprise datasets and two controlled public variants show SkillCDG outperforms baselines in F1 by up to 12.8 % with a maximum token reduction of 64.3 %. Comparative checks across four model checkpoints confirm that detection correctness scales non‑linearly with graph complexity, and the derived complexity metric predicts performance gains for smaller models.

## Significance  
By decoupling policy representation from inference cost, SkillCDG enables scalable compliance checking in resource‑constrained environments, allowing enterprises to deploy high‑accuracy detectors without prohibitive token usage. The identified scaling trend also provides a principled guide for model selection and training strategies, fostering more efficient AI systems.

## Related Concepts  
- SKILL documents  
- Constraint dependency graph (two‑layer)  
- Closure‑grounded detection  
- On‑policy distillation  
- Graph‑based policy representation  
- Complexity‑differentiated scaling  
- Token consumption reduction
