---

title: "PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs"
url: http://arxiv.org/abs/2605.23883v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_17-45-01Z_PGT_ProcedurallyGeneratedTasksforimprovingvisualgr.md
generated_at: "2026-06-11 10:46"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces Procedurally Generated Tasks (PGT), a lightweight data‑driven method that augments multimodal large language models with geometric primitives to improve fine‑grained visual grounding. Experiments show PGT boosts performance on relational, quantitative, and 3D benchmarks by up to 20 % on What’sUp and 13.3 % on CV‑Bench‑2D when instruction‑tuned. Fine‑tuning state‑of‑the‑art MLLMs yields further gains of +5.5 % and +8.3 % respectively, indicating that richer supervision can overcome perception bottlenecks.

## Key Takeaways
- PGT adds dense geometric supervision by overlaying unambiguous primitives on images, separating visual grounding from semantic priors.
- Instruction‑tuned MLLMs using LLaVA‑v1.5‑Instruct with PGT data achieve up to +20 % improvement on What’sUp and +13.3 % on CV‑Bench‑2D.
- Fine‑tuning existing MLLMs on PGT data yields additional gains of +5.5 % on What’sUp and +8.3 % on CV‑Bench‑2D, proving the method works across architectures.

## Context
Visual grounding remains a persistent challenge for multimodal models despite advances in large language capabilities. Providing explicit geometric cues can help align perception with model training signals, reducing reliance on implicit or noisy supervision.

## Implications
Practitioners can integrate PGT as a low‑cost diagnostic and improvement tool without retraining massive datasets. This approach offers a scalable way to enhance visual reasoning across diverse MLLM deployments in industry and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23883v1)
