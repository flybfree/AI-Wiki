---
title: Task-Specific Prompt with Global Context for Multi-Task Graph Pre-Training
url: http://arxiv.org/abs/2609.00047v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-30_04-28-51Z_Task_SpecificPromptwithGlobalContextforMulti_TaskG.md
generated_at: 2026-09-01 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TPGC, a dual-prior prompt initialization method for multi-task graph pre-training that aligns prompts with both task objectives and structural features. By integrating a task‑prior injection module and a structure‑prior injection module, TPGC improves alignment and transferability of prompt representations across tasks. Experiments on six benchmarks demonstrate superior few‑shot performance compared to state‑of‑the‑art baselines.

## Key Takeaways
- The Task-Prior Injection Module performs short homologous multi-task pre-training on an auxiliary graph to initialize prompts with optimization preferences from multiple pretext tasks.
- The Structure-Prior Injection Module extracts global structural context and converts it into layer-wise prompt vectors by aggregating node embeddings that capture structural information.
- TPGC yields consistently better few‑shot performance, requires fewer downstream tunable parameters, and reduces runtime compared to existing approaches.

## Context
Graph prompt learning aims to adapt pre-trained graph models efficiently in low‑resource settings. This work advances the field by providing a principled way to align prompts with both task relevance and structural properties, moving beyond random initialization toward structured, task‑aware representations.

## Implications
For practitioners, TPGC offers a practical solution that enhances model performance without increasing complexity or inference time. In industry applications where graph data is abundant but downstream tasks are scarce, this method can deliver measurable gains in accuracy while maintaining computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00047v1)
