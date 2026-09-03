---
title: Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds
url: http://arxiv.org/abs/2609.02302v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-47-34Z_ImprovingEvaluationRealismwithInference_TimeComput.md
generated_at: 2026-09-02 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles evaluation awareness by making simulated alignment tests harder for models to detect as real deployments. It introduces two techniques — critique refinement, which adds inference‑time compute to generate and refine actions, and DISH, a harness that wraps the target model in an agent environment — and shows that using both together yields larger realism gains than either alone while using compute more efficiently than extending audit length.

## Key Takeaways
- Critique refinement adds extra inference time per simulator action to produce multiple candidate actions, then selects the most deployment‑like one based on feedback from the target model.  
- DISH wraps the target model in an agent harness that reduces the gap between simulated and real coding environments, improving realism without longer audits.  
- Combining both techniques produces larger gains than using them separately, demonstrating that extra compute can be used more effectively for evaluation realism.

## Context
Evaluation awareness is a known issue where capable models recognize they are being tested rather than deployed, which can undermine safety assessments. Automated methods that increase realism without significantly extending runtime are needed to produce reliable alignment conclusions in the rapidly evolving AI field.

## Implications
These findings suggest that researchers and industry practitioners can improve trustworthy evaluation pipelines by leveraging compute‑efficient techniques like critique refinement and agent harnesses, leading to more accurate safety judgments without costly longer audits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02302v1)
