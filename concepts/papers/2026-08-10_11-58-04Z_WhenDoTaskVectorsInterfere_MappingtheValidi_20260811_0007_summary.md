# Summary: 2026-08-10_11-58-04Z_WhenDoTaskVectorsInterfere_MappingtheValidityBound.md
Saved: 2026-08-11 00:07
Source: 2026-08-10_11-58-04Z_WhenDoTaskVectorsInterfere_MappingtheValidityBound.md
Model: None

---

## Summary  
The paper investigates when task vectors—displacements in weight space that represent fine‑tuning for different tasks—interfere with each other, i.e., when their composition does not predictably alter model behavior. It maps the validity boundaries of weight‑space composition across models and adaptation methods by measuring functional non‑additivity on a two‑dimensional task‑vector surface using controlled prompts and norm‑matched controls.

## Key Contributions  
- Finding 1: Code+safety fine‑tuning shows higher pairwise functional non‑additivity than code+math control on code and instruction prompts, but not on math prompts.  
- Finding 2: In a six‑task expansion, all eight high‑vs‑low comparisons of unseen task pairs have the predicted sign, indicating consistent ordering across tasks.  
- Finding 3: The primary ordering persists under full‑parameter fine‑tuning at 0.5B, LoRA up to 7B, and Llama‑3.1‑8B cross‑architecture audit.

## Methodology  
The authors separate parameter geometry from functional geometry; they measure pairwise functional non‑additivity over a two‑dimensional task‑vector surface using the first‑token predictive‑distribution interaction ratio conditioned on an input distribution, with norm‑matched controls, three training seeds, and response‑only fine‑tuning. Experiments evaluate Qwen2.5‑1.5B across code+safety vs matched code+math prompts, a six‑task expansion, full‑parameter tuning at 0.5B, LoRA scales up to 7B, and a Llama‑3.1‑8B cross‑architecture audit.

## Results  
Code+safety is more non‑additive than code+math on code and instruction prompts; math prompts show no difference. All eight high‑vs‑low unseen task pair comparisons have the predicted sign in the six‑task expansion, confirming a robust ordering. The primary ordering remains valid under full‑parameter fine‑tuning at 0.5B, LoRA up to 7B, and across Llama‑3.1‑8B, demonstrating that weight‑space composition supports input‑ and format‑conditioned functional statements rather than being a universal predictor of merging performance.

## Significance  
This work provides a principled boundary for when task vectors interfere, offering guidance for multi‑task adaptation by clarifying that composition is sensitive to input type and fine‑tuning method rather than universally diminishing model performance. It helps practitioners design robust training pipelines and understand the limits of task arithmetic in large language models.

## Related Concepts  
Task arithmetic, weight‑space composition, functional non‑additivity, parameter geometry vs functional geometry, fine‑tuning displacement, LoRA, full‑parameter fine‑tuning, cross‑architecture audit.
