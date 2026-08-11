# Summary: 2026-08-10_11-58-04Z_WhenDoTaskVectorsInterfere_MappingtheValidityBound.md
Saved: 2026-08-10 23:47
Source: 2026-08-10_11-58-04Z_WhenDoTaskVectorsInterfere_MappingtheValidityBound.md
Model: None

---

## Summary  
The paper investigates the limits of task‑vector arithmetic in weight space, asking when fine‑tuning displacements become predictable functional changes rather than mere parameter additions. It maps the validity boundaries of weight‑space composition by measuring pairwise functional non‑additivity across a two‑dimensional surface that combines input distribution and task vectors. The authors demonstrate that certain prompt combinations (code + safety) exhibit stronger interference than matched controls, while other pairs (math prompts) show little effect. Their analysis predicts the sign of eight high‑versus‑low comparisons in an expansion to six tasks and shows this ordering survives across multiple fine‑tuning regimes.

## Key Contributions  
- [Finding 1] Code + safety prompts produce greater non‑additivity than a matched code + math control on both code and instruction inputs, but not on math prompts alone.  
- [Finding 2] In a prospective six‑task expansion, all eight high‑versus‑low pairwise comparisons of unseen task pairs retain the predicted sign, indicating robust ordering in the task‑vector surface.  
- [Finding 3] The primary ordering persists under full‑parameter fine‑tuning at 0.5 B, LoRA up to 7 B, and a Llama‑3.1 cross‑architecture audit; external validation further sharpens the boundary between raw prompts and wrapper‑style instructions.

## Methodology  
The authors separate parameter geometry from functional geometry by constructing a two‑dimensional task‑vector surface that pairs an input distribution with a fine‑tuning displacement. They evaluate pairwise functional non‑additivity using a first‑token predictive‑distribution interaction ratio, normalizing the response to norm‑matched controls. Experiments run with three training seeds and response‑only fine‑tuning to isolate composition effects.

## Results  
Code + safety prompts show higher non‑additive scores than code + math controls on both code and instruction tasks, while math prompts alone do not differ significantly. The eight high‑versus‑low comparisons of unseen task pairs all align with the predicted sign in the six‑task expansion. This ordering remains consistent across full‑parameter fine‑tuning at 0.5 B, LoRA up to 7 B, and a Llama‑3.1 cross‑architecture test. External validation reveals that raw public code, instruction, or safety prompts preserve the contrast, whereas an instruction‑style wrapper collapses it on identical code prompts; EvalPlus pass@1 interactions also fail to reproduce the effect.

## Significance  
Understanding when task vectors interfere helps practitioners avoid unintended degradation of model behavior during fine‑tuning. By mapping these boundaries, designers can select prompt formats and adaptation methods that preserve functional integrity across scales and architectures, supporting more reliable transfer learning in large language models.

## Related Concepts  
task arithmetic, weight‑space composition, functional geometry vs. parameter geometry, non‑additivity, first‑token predictive distribution interaction ratio, fine‑tuning regimes (full‑parameter, LoRA), EvalPlus pass@1, cross‑architecture audit
