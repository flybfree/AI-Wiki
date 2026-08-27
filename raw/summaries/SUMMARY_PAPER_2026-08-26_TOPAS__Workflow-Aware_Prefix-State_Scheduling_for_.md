---
title: TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving
url: http://arxiv.org/abs/2608.25523v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_08-33-10Z_TOPAS_Workflow_AwarePrefix_StateSchedulingforMulti.md
generated_at: 2026-08-26 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TOPAS, a task‑oriented scheduler that balances prefix caching and workflow execution in multi‑agent LLM serving. By jointly optimizing the trade‑off between keeping prefixes cached for reuse and minimizing downstream delays, TOPAS reduces mean and p99 job completion times by up to 49.4% on synthetic workloads compared with baselines. The approach also improves performance on real software‑development workflows such as MetaGPT‑SOP and MetaGPT‑TL.

## Key Takeaways
- TOPAS scores candidate post‑decision states by trading the expected reduction in each task’s longest remaining service path against the near‑term benefit of downstream prefix reuse, accounting for movement and preemption costs.  
- A task‑level aging mechanism prevents starvation, ensuring that long tasks receive timely scheduling even when their prefixes are evicted.  
- The scheduler is evaluated within the SGLang framework on three synthetic DAGs and two MetaGPT workflows, achieving up to 39.8% mean reduction in JCT across all workloads.

## Context
In multi‑agent LLM serving, the shared GPU memory for KV caches creates a fundamental bottleneck that affects both latency and throughput. Existing schedulers either favor immediate locality or overall workflow progress, leading to suboptimal resource utilization. This paper addresses that imbalance by introducing a scheduler that explicitly considers task‑level service paths and prefix reuse.

## Implications
TOPAS provides a practical framework for cloud operators seeking higher efficiency in large language model deployments without sacrificing responsiveness. Practitioners can adopt the aging‑aware scoring mechanism to improve fairness and reduce resource waste, ultimately lowering operational costs and enhancing user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25523v1)
