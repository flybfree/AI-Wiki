---
title: From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models
url: http://arxiv.org/abs/2610.21165v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_03-24-36Z_FromLongContexttoSelectiveMemory_ASurveyofMemory_C.md
generated_at: 2026-10-15 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This survey reframes long-context compression for large language models as a unified memory-management problem, distinguishing between compute-active memory that directly participates in model computation and compute-inactive memory that can be stored, retrieved, updated, or forgotten outside the computation path. The paper introduces a budgeted cost model and an information lifecycle framework that unifies previously isolated research areas—prompt compression, KV-cache management, retrieval augmentation, and agent memory—into a single coherent account of how information flows between storage and computation during inference.

## Key Takeaways
- The survey establishes a critical taxonomy separating compute-active memory (directly participating in model computation) from compute-inactive memory (stored, retrieved, updated, or forgotten outside the computation path), while characterizing offloaded KV caches, persistent prefix caches, and precomputed KV states as intermediate states on the activation path. This distinction reveals that existing literature on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory has been discussed in isolation, leaving the information flow between storage and computation poorly understood.
- The paper formulates eight state transitions—writing, offloading, recall, retrieval-and-injection, materialization, eviction, consolidation, and forgetting—as components of an information lifecycle, and introduces a budgeted cost model that places all these operations within a single cost account. This framework unifies short-term context compression with long-term memory management and the transitions between them, showing that the central challenge is not merely reducing information volume but deciding which information should participate in costly inference, when, and in what form.
- The authors identify evaluation dimensions, benchmark gaps, and open challenges, arguing that future research must move from static, pointwise compression techniques toward dynamic, governable, lifecycle-aware memory management systems that can adaptively allocate inference-time resources.

## Context
This survey addresses a critical gap in the LLM research landscape, where work on prompt compression, KV-cache optimization, retrieval-augmented generation, and agent memory systems has developed largely in parallel without a unifying theoretical framework. As context windows expand to hundreds of thousands of tokens and agentic systems require persistent memory across sessions, the computational, storage, and information-selection pressures at inference time have become the dominant bottleneck rather than raw model capacity. By treating these disparate techniques as state transitions within a single information lifecycle, the paper provides the conceptual scaffolding that the field has lacked for building coherent, end-to-end memory architectures.

## Implications
For practitioners building production LLM systems, this framework offers a principled way to reason about trade-offs between context length, inference cost, and information fidelity, enabling more systematic design of serving infrastructure and agent memory pipelines. For the research community, the call to move from static compression toward dynamic, governable memory management suggests that future breakthroughs will come not from compressing more aggressively but from intelligently deciding what to retain, when to materialize it into active computation, and when to let it be forgotten. Industry deployments of long-context models and autonomous agents stand to benefit directly from lifecycle-aware resource allocation strategies that this survey makes explicit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21165v1)
