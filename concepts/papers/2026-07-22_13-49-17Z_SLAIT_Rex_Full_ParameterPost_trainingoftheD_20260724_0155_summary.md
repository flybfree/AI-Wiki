# Summary: 2026-07-22_13-49-17Z_SLAIT_Rex_Full_ParameterPost_trainingoftheDeepSeek.md
Saved: 2026-07-24 01:55
Source: 2026-07-22_13-49-17Z_SLAIT_Rex_Full_ParameterPost_trainingoftheDeepSeek.md
Model: None

---

## Summary  
The paper demonstrates that full‑parameter post‑training of trillion‑parameter MoE models can be executed efficiently on the Ascend NPU SuperPOD by introducing a hierarchical optimization framework called SLAI T‑Rex. This system tackles severe memory pressure, non‑overlapped communication overhead, and inefficient kernel execution through model‑level parallelism, computation‑communication orchestration, and low‑level kernel tuning. The authors also create CPT/SFT pipelines for complex Operations Research tasks using the DeepSeek‑V4‑Flash model, producing a high‑quality dataset of 10 K synthetic optimization documents. Their integrated approach yields state‑of‑the‑art zero‑shot Pass@1 performance (71.81%) that surpasses GPT‑5.4‑Mini and the base DeepSeek‑V4‑Flash model.

## Key Contributions  
- [Finding 1] Full‑parameter post‑training of trillion‑parameter MoE models on Ascend SuperPOD is feasible with a hierarchical optimization framework (SLAI T‑Rex).  
- [Finding 2] The framework achieves 34.22 % Model FLOPs Utilization, a 2.93× improvement over the open‑source baseline while preserving training stability.  
- [Finding 3] DeepSeek‑V4‑Flash reaches the highest zero‑shot Pass@1 score (71.81 %), outperforming GPT‑5.4‑Mini by 3.98 pp and the base model by 11.27 pp.

## Methodology  
The authors approached the problem by building a three‑layer optimization pipeline: first, they organized model‑level parallelism to distribute the massive MoE parameters across Ascend NPUs; second, they orchestrated computation and communication with low‑overlap kernels to maximize FLOPs Utilization; third, they constructed CPT (Continued Pre‑Training) and SFT (Supervised Fine‑Tuning) workflows that fuse domain resources with solver‑verified synthetic optimization documents. The resulting dataset comprises 10 K high‑quality SFT samples spanning four task categories and three problem representations.

## Results  
The experimental results show a Model FLOPs Utilization of 34.22 %, which is 2.93 times higher than the baseline recipe, and training remains stable throughout. The DeepSeek‑V4‑Flash model trained on this pipeline attains an average zero‑shot Pass@1 score of 71.81 %, beating GPT‑5.4‑Mini by 3.98 percentage points and the base DeepSeek‑V4‑Flash model by 11.27 percentage points.

## Significance  
This work provides a full‑stack pathway from efficient trillion‑parameter post‑training on NPU infrastructure to domain‑specialized Flash models for complex reasoning, pushing frontier‑model systems forward in both scalability and specialized application performance.

## Related Concepts  
Full‑parameter post‑training, Mixture of Experts (MoE), Ascend SuperPOD, hierarchical optimization framework SLAI T‑Rex, Model FLOPs Utilization, CPT/SFT pipelines, zero‑shot Pass@1 evaluation, Operations Research tasks, solver‑verified synthetic documents.
