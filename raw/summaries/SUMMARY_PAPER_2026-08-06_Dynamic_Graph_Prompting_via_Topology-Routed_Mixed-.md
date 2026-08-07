---
title: Dynamic Graph Prompting via Topology-Routed Mixed-Curvature Experts
url: http://arxiv.org/abs/2608.06031v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_13-37-52Z_DynamicGraphPromptingviaTopology_RoutedMixed_Curva.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CurvPrompt, a framework that addresses the geometry under‑adaptation problem in dynamic graph prompting by recognizing that local topology and degree heterogeneity cause temporal shifts in edge curvature. The authors propose a mixed‑curvature expert bank with learnable prompts, guided by a topology‑aware routing gate to generate personalized representations for each node‑time instance. Experiments on four benchmark datasets demonstrate significant improvements in few‑shot link prediction while maintaining strong performance on node classification tasks.

## Key Takeaways
- The optimal representation geometry evolves over time due to local clustering and degree heterogeneity, leading to a mismatch between static embeddings and dynamic topology.
- CurvPrompt solves this by maintaining multiple curvature‑diverse Riemannian experts, each paired with a prompt, and routing nodes via a soft pre‑training gate that later becomes hard Top‑K routing.
- The approach achieves strong few‑shot link prediction results while delivering consistent node classification performance, validating the necessity of geometry‑adaptive prompting.

## Context
Dynamic graph prompting aims to adapt pre‑trained temporal backbones to label‑scarce tasks with minimal compute. Existing methods assume a fixed embedding space, which often fails as graph topology changes across time steps. This work contributes by formalizing and mitigating geometry under‑adaptation, offering a principled way to align prompt design with evolving local structures.

## Implications
For practitioners, CurvPrompt provides a scalable solution that can be integrated into existing few‑shot learning pipelines without retraining the entire model. In industry, it enables more robust recommendation systems where user interaction graphs shift over time, improving personalization while conserving resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06031v1)
