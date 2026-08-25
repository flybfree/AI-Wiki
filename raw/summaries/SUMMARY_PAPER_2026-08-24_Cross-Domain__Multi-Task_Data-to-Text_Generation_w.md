---
title: Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data
url: http://arxiv.org/abs/2608.23391v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_15-37-19Z_Cross_Domain_Multi_TaskData_to_TextGenerationwitho.md
generated_at: 2026-08-24 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles cross-domain data-to-text generation when neither in‑domain training texts nor test references are available, and it shows that a distillation method outperforms both fine‑tuning and zero‑shot inference on five benchmarks. At a fixed model size of 1.7 billion parameters, the distilled models consistently beat the alternatives.

## Key Takeaways
- The DDKD approach consistently outperforms fine‑tuning and zero‑shot inference across all five datasets, achieving best results at a 1.7B parameter budget.
- Structure‑preserving augmentation via subsampling and perturbation is more effective than scaling real inputs for cross‑domain distillation.
- Small distilled models match or exceed performance of larger finetuned models on two domains while being cost‑efficient.

## Context
Data-to-text generation remains limited to single tasks, requiring domain‑specific corpora. This work demonstrates that knowledge can be transferred across unrelated domains using model distillation and augmentation, reducing reliance on large labeled datasets.

## Implications
Practitioners can deploy compact, high‑performing text generators for diverse data sources without extensive fine‑tuning. The method lowers computational cost and enables rapid adaptation to new domains, aligning with trends toward efficient AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23391v1)
