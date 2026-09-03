---
title: CoMerge: Conflict-Driven Preference Optimization for Multi-Task Model Merging
url: http://arxiv.org/abs/2609.02273v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-21-28Z_CoMerge_Conflict_DrivenPreferenceOptimizationforMu.md
generated_at: 2026-09-02 20:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoMerge, a conflict‑driven preference optimization method for merging multi‑task large language models without full retraining. By treating merging as a preference problem and using self‑supervised defect pairs as hard negatives, CoMerge refines tensor‑wise coefficients to reduce interference while preserving task abilities. Experiments show an average normalized performance of 0.9968 on MergeBench, surpassing all data‑free baselines.

## Key Takeaways
- CoMerge treats model merging as a preference optimization problem using self‑supervised conflict pairs derived from naive merging defects.
- The method optimizes only 1,445 scalar coefficients, yielding comparable results to full fine‑tuning despite lightweight updates.
- On Llama‑3.1‑8B‑Instruct, CoMerge improves instruction following and safety tasks while maintaining competitive performance.

## Context
Model merging is a key technique for efficiently building multi‑task LLMs without retraining entire networks. Existing approaches often rely on heuristic adjustments or external annotations to mitigate interference, limiting their adaptability to new tasks.

## Implications
CoMerge offers a scalable framework that can be applied across various model architectures with minimal computational overhead. Practitioners can leverage this method to enhance task performance and safety in deployed systems without the cost of full fine‑tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02273v1)
