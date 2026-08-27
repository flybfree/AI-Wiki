---
title: TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving
published: 2026-08-26T08:33:10Z
authors: Hongqiu Ni, Han Tian, Chi Zhang, Guopeng Li, Haisheng Tan
url: http://arxiv.org/abs/2608.25523v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving

## Abstract
Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing schedulers tend to prioritize either immediate prefix locality or overall workflow progress. However, under a shared KV cache budget, optimizing either objective in isolation can prolong tasklevel job completion time (JCT) through downstream delays or frequent prefix replacement. To strike a balance, we here propose TOPAS, a Task-Oriented Prefix-Aware Scheduler that jointly decides which agent prefixes to keep in the cache and which requests to schedule for execution. TOPAS scores candidate post-decision states by trading off the expected reduction in each task's longest remaining service path against the near-term benefit of downstream prefix reuse, accounting for the costs of prefix movement and preemption. A task-level aging mechanism is also incorporated to prevent starvation. We implement TOPAS within the SGLang framework and assess its performance on three synthetic DAGs and two MetaGPT software-development workflows. Compared with the best performing baseline for each workload and metric, TOPAS reduces the mean/p99 JCT by up to 39.8%/49.4% on the synthetic workloads, while lowering mean JCT by 9.8% on MetaGPT-SOP and mean/p99 JCT by 22.0%/26.6% on MetaGPT-TL.

## Metadata
- **Published**: 2026-08-26T08:33:10Z
- **Authors**: Hongqiu Ni, Han Tian, Chi Zhang, Guopeng Li, Haisheng Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25523v1)