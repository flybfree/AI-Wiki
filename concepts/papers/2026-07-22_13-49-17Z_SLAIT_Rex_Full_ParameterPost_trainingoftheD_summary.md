# Summary: 2026-07-22_13-49-17Z_SLAIT_Rex_Full_ParameterPost_trainingoftheDeepSeek.md
Saved: 2026-07-24 01:52
Source: 2026-07-22_13-49-17Z_SLAIT_Rex_Full_ParameterPost_trainingoftheDeepSeek.md
Model: None

---

## Summary  
The paper presents a full‑parameter post‑training pipeline for trillion‑parameter mixture‑of‑experts (MoE) models on the Ascend NPU SuperPOD, targeting the DeepSeek‑V4 family. By integrating model‑level parallelism, communication orchestration, and low‑level kernel execution, the authors achieve a 34.22 % Model FLOPs Utilization with a 2.93× improvement over open‑source baselines while preserving training stability. They then apply this infrastructure to construct CPT and SFT pipelines for complex Operations Research (OR) tasks using domain‑specific data, producing a Flash model that reaches the highest zero‑shot Pass@1 score of 71.81 % among evaluated systems.

## Key Contributions  
- [Finding 1] A hierarchical optimization framework that boosts MoE FLOPs Utilization to 34.22 % on Ascend SuperPOD, delivering a 2.93× speed‑up compared with standard recipes.  
- [Finding 2] End‑to‑end CPT and SFT workflows for OR problems that combine real domain resources with solver‑verified synthetic documents, yielding a high‑quality 10 K sample set across four task categories.  
- [Finding 3] The resulting Flash model outperforms GPT‑5.4‑Mini (71.81 % Pass@1) and the base DeepSeek‑V4‑Flash (11.27 pp improvement), demonstrating superior zero‑shot reasoning for mathematical optimization.

## Methodology  
The authors tackled memory pressure, non‑overlapped communication overhead, and inefficient kernel execution by designing a three‑tier architecture: (1) model‑level parallelism to distribute the trillion‑parameter MoE across Ascend NPUs; (2) computation‑communication orchestration that schedules FLOPs and reduces redundant data movement; (3) low‑level kernels tuned for the Ascend hardware stack, including custom attention and MoE routing kernels. This pipeline enables full‑parameter training without sacrificing stability.

## Results  
The optimized system achieves 34.22 % Model FLOPs Utilization, a 2.93× improvement over baseline. The specialized Flash model attains an average zero‑shot Pass@1 of 71.81 %, surpassing GPT‑5.4‑Mini by 3.98 points and the base DeepSeek‑V4‑Flash by 11.27 points, confirming superior performance on OR reasoning tasks.

## Significance  
This work establishes a complete end‑to‑end pathway from efficient trillion‑parameter post‑training on Ascend infrastructure to domain‑specialized Flash models for complex mathematical modeling, pushing the frontier of large‑scale MoE training and showcasing how specialized data pipelines can unlock higher reasoning capabilities beyond generic benchmarks.

## Related Concepts  
- Full‑parameter post‑training  
- Mixture‑of‑Experts (MoE) models  
- Ascend NPU SuperPOD hardware stack  
- DeepSeek‑V4 family of LLMs  
- CPT and SFT workflows for Operations Research  
- Solver‑verified synthetic optimization documents  
- Model FLOPs Utilization (MFU) metric  
- Communication overhead reduction techniques
