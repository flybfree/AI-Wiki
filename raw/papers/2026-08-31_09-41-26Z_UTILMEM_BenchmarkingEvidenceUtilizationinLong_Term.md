---
title: UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory
published: 2026-08-31T09:41:26Z
authors: Peijun Qing, Fobo Shi, Soroush Vosoughi
url: http://arxiv.org/abs/2608.30508v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory

## Abstract
Long-term memory is increasingly important for conversational agents, yet existing benchmarks primarily measure memory through pointwise factual recall: whether a system can recover isolated facts or event-level details from prior interactions. Real-world memory use, however, often requires a more demanding capability: integrating distributed, implicit, and noisy evidence across extended interaction histories into coherent, task-oriented outputs. We call this capability memory utilization. Here, we introduce UtilMem, a diagnostic benchmark comprising 1,717 instances across five domains, designed to evaluate four underexplored aspects of memory utilization: reasoning over dense histories, identifying implicitly relevant memories, synthesizing distributed evidence into summaries, analyses, or plans, and resisting interference from semantically similar distractors. Evaluating a diverse set of retrieval-based and memory-augmented systems, we find that strong performance on conventional factual-memory benchmarks does not reliably translate into effective memory utilization. Moreover, retrieval alone is insufficient: even when relevant evidence is successfully recovered, systems frequently fail to integrate information across sessions or to distinguish useful evidence from plausible distractors. These findings expose a substantial gap between accessing stored information and using it effectively, and suggest that progress in long-term conversational memory will require architectures that explicitly support evidence integration and robustness to retrieval interference. Code is available at https://github.com/peijunallin/UtilMem.

## Metadata
- **Published**: 2026-08-31T09:41:26Z
- **Authors**: Peijun Qing, Fobo Shi, Soroush Vosoughi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30508v1)