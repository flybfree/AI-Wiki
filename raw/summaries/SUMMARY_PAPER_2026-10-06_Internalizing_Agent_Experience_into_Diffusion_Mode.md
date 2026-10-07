---
title: Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context Distillation
url: http://arxiv.org/abs/2610.07250v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_18-50-09Z_InternalizingAgentExperienceintoDiffusionModelWeig.md
generated_at: 2026-10-06 21:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper proposes Diffusion On-Policy Context Distillation (D-OPCD) to transfer the benefits of an agentic text-to-image harness into the diffusion model weights. Instead of relying on external memory, skills, workflow orchestration, verification, and iterative prompt refinement at inference time, the method treats the agent-improved prompt as privileged context and distills that knowledge into the generator. The result is a model that can produce better images from the original query alone, while also enabling the harness to evolve further after saturated skills are removed.

## Key Takeaways
- Agentic harnesses can substantially improve text-to-image generation by constructing and revising prompts through memory, skills, workflow orchestration, result verification, and iterative refinement, but these gains are normally external to the diffusion model and disappear when the harness is not used.
- D-OPCD addresses this limitation by using the agent-improved prompt as privileged context and distilling the harness’s learned behavior into the diffusion model weights, allowing the model to retain part of the harness benefit when conditioned only on the original query.
- With an agent equipped with Auto Skill Evolver, D-OPCD raises average direct-generation scores from 60.52 to 65.09 across four benchmarks, and a second evolution round on the updated generator improves a skill-free harness by 1.83 points, suggesting continual co-evolution between model and harness.

## Context
This work sits at the intersection of diffusion models, agentic systems, and knowledge distillation. It matters because many recent gains in generative AI come from external scaffolding rather than from stronger base models, limiting deployment efficiency and making improvements dependent on complex runtime infrastructure. By internalizing agent experience into model weights, the paper explores a path toward more self-contained generators that can benefit from agentic reasoning without requiring the full harness at inference time.

## Implications
For practitioners, D-OPCD suggests a practical way to compress the value of agent workflows into deployable model weights, potentially reducing latency, cost, and dependence on elaborate orchestration systems. For the field, it points toward co-evolving systems where harnesses teach models, models become stronger, and harnesses can then shed obsolete skills and continue improving. This could influence future text-to-image pipelines, model training loops, and agent-model integration strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07250v1)
