---
title: How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning
url: http://arxiv.org/abs/2607.21351v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
generated_at: 2026-07-23 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how much a low-rank adapter actually modifies the underlying frozen model during parameter-efficient fine-tuning, measuring this in bits rather than counting parameters. It finds that adapters write far fewer bits per trainable weight than full fine‑tuning would suggest and that the amount of memory written depends on where the adapter is placed within the network. The study also shows a clear distinction between supervised and reinforcement learning: supervised adapters replicate model knowledge, while reward‑based adapters do not.

## Key Takeaways
- Adapters store only a couple of bits per trainable parameter, far less than the full model’s budget, indicating that compression is more effective than expected.  
- The capacity of an adapter is strongly affected by its location in the network; moving the same budget from attention to MLP increases stored information nearly twofold, while removing the frozen base structure collapses it.  
- Privacy leakage correlates with the bits written rather than the number of parameters, and supervised fine‑tuning produces verbatim copies that are recorded, whereas reinforcement learning adapters record nothing.

## Context
In AI research, parameter-efficient fine‑tuning methods like LoRA promise to reduce compute and memory usage while preserving performance. This paper moves beyond theoretical compression by directly quantifying the physical impact of these adaptations on model weights, providing a measurable metric that can guide design choices. The findings help clarify why certain architectures benefit more from adapter placement than others.

## Implications
For practitioners, knowing exactly how many bits an adapter writes allows them to set realistic limits on privacy exposure and resource consumption. It also informs the development of safer fine‑tuning pipelines where reinforcement learning adaptations are not inadvertently leaking sensitive data. The paper’s bit‑level measurement offers a concrete benchmark for evaluating model updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21351v1)
