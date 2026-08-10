---
title: Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models
url: http://arxiv.org/abs/2608.06901v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_07-36-19Z_PruneOnce_Retraining_FreeTask_AgnosticPruningforVi.md
generated_at: 2026-08-09 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents PORTA, a retraining‑free pruning method that works for vision‑language models without any task‑specific data. By estimating feature importance from generic calibration data and allocating sparsity adaptively to layers with high output variability, PORTA achieves strong compression while preserving performance across diverse VLM architectures.

## Key Takeaways
- PORTA derives a task‑agnostic importance measure using activation variation extracted from generic calibration data, enabling pruning without any downstream task information.  
- The framework uses an adaptive sparsity allocation mechanism that assigns higher pruning ratios to layers with greater output feature variability, avoiding uniform sparsity and mitigating performance loss at high compression levels.  
- Extensive experiments on CLIP, BLIP, and Qwen2‑VL show that PORTA maintains competitive downstream performance under substantial model size reduction without requiring any retraining.

## Context
Vision‑language models have become central to multimodal AI systems, but their large parameter counts limit deployment in resource‑constrained settings. Traditional pruning approaches often rely on task‑specific knowledge or fine‑tuned importance scores, which are impractical when the same model must serve multiple tasks. PORTA addresses this gap by providing a generic, retraining‑free solution that can be applied broadly across VLM families.

## Implications
For industry practitioners, PORTA offers a practical way to shrink large multimodal models for edge devices or low‑power environments without sacrificing accuracy. For researchers, the method opens avenues for standardizing model compression pipelines and reducing reliance on task‑specific fine‑tuning, fostering more versatile and deployable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06901v1)
