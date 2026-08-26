---
title: More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving
url: http://arxiv.org/abs/2608.23962v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_01-42-08Z_MoreGPUsoraSmallerCache_TensorParallelismversusKVC.md
generated_at: 2026-08-25 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper compares tensor parallelism and KV compression as strategies for alleviating memory limits in LLM serving, finding that compression is consistently cheaper per million tokens while tensor parallelism offers latency gains only when the model exceeds a device‑memory threshold. Across models up to 70B parameters, three GPU types, and various cache settings, no cost‑equivalence crossover was observed; compression dominates below ~36B parameters and extra GPUs become wasteful.

## Key Takeaways
- Compression is cheaper by 1.20x to 2.00x compared with adding GPUs for memory relief, meaning it multiplies capacity per dollar more than an eightfold GPU spend.
- The decision boundary between strategies hinges on model size relative to device memory, roughly at 36B parameters for an 80 GB card; below this wall compression dominates and extra GPUs are largely wasted.
- Tensor parallelism improves latency (by reducing batching contention) while KV compression worsens per‑token latency by 8–93%, making it a trade‑off between cost and speed.

## Context
LLM serving is constrained by limited GPU memory, forcing practitioners to choose between scaling hardware or shrinking data structures. This work empirically aligns these two approaches on a single cost axis, offering a practical benchmark for resource allocation in production systems.

## Implications
For industry and researchers, the findings suggest prioritizing KV compression unless serving extremely large models that cannot fit even with tensor parallelism, thereby avoiding unnecessary GPU spend. Practitioners should also weigh latency impacts, as compression can degrade throughput despite saving memory.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23962v1)
