---
title: Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning
url: http://arxiv.org/abs/2607.27766v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_07-03-18Z_Gradient_freeTask_ConditionedRetrievalforOn_Device.md
generated_at: 2026-07-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Conditional Retrieval Alignment (CoRA), a gradient‑free method for on‑device in‑context learning that selects task‑specific demonstrations from local memories without fine‑tuning the retriever. By aligning candidate input representations to an output‑derived conditioning space using ridge regression and low‑rank factorization, CoRA builds a compact retrieval index that can be constructed offline and used at inference time with only the query input. Experiments on textual and multimodal benchmarks show effective task‑conditioned retrieval without backpropagation or target‑model calls.

## Key Takeaways
- CoRA converts a frozen encoder into a task‑conditioned retriever by pairing candidate inputs and outputs, constructing an output‑derived conditioning space that is aligned to query inputs via closed‑form ridge regression.  
- The framework creates a low‑rank factorization of the fitted representation, allowing offline index construction while keeping query‑time retrieval lightweight and requiring only the query input and precomputed index.  
- CoRA’s rank‑constrained basis is mathematically optimal for compressing the output‑conditioned fitted representation, enabling exact streaming construction that avoids storing the full matrix.

## Context
On‑device in‑context learning faces strict constraints on computation, memory, and data exposure, making efficient retrieval crucial. This work advances the field by providing a zero‑gradient, low‑rank solution that integrates seamlessly with existing frozen models, supporting multimodal tasks without additional training pipelines.

## Implications
For industry practitioners, CoRA enables faster deployment of task‑specific assistants on resource‑constrained devices like Raspberry Pi 5, reducing latency and power consumption. The method’s compatibility with large language models such as Llama‑3.2‑1B and MobileLLM‑Pro opens pathways for personalized AI services without retraining the core model.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27766v1)
