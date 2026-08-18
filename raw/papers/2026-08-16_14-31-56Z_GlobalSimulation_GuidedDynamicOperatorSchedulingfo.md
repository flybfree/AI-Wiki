---
title: Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving
published: 2026-08-16T14:31:56Z
authors: Weinan Liu, Zeyuan Ding, Dian Ding, Chengcheng Wan, Lu Tang, Guangtao Xue, Jiwu Shu, Yiming Zhang
url: http://arxiv.org/abs/2608.15762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving

## Abstract
Container-granularity scheduling leaves abundant short-lived idle slices within containers unexploited. Reallocating containers is too heavyweight to utilize such fine-grained opportunities under SLA constraints, and operator-level scheduling requires reasoning about dependencies, memory safety, and cluster-wide execution dynamics in real time.   In this paper, we present SliceScheduler, a dynamic operator-level scheduling system for multi-tenant model serving. The key idea is to expose cluster-wide operator execution state and enable what-if reasoning over scheduling decisions. SliceScheduler consists of four key components. First, we introduce the Global Mapping Graph (GMG), a unified abstraction that captures operator dependencies, tensor shapes, resource mappings, and execution states, providing a real-time, cluster-wide view with explicit resource semantics. Second, we build a global simulator on top of GMG to predict operator-level execution and memory evolution under candidate placements. Third, we design an incremental, simulation-based scheduling module that selects placements to exploit fragmented idle slices while avoiding memory violations and preserving SLA. Finally, we develop an operator executor that materializes scheduling decisions on GPUs and coordinates computation and cross-accelerator transfers. We implement SliceScheduler as a PyTorch backend and evaluate it using production trace replay. Experimental results show that SliceScheduler improves token throughput by 1.10--2.29$\times$ compared to existing approaches, while maintaining SLA violations within 9\%. SliceScheduler demonstrates that operator-level scheduling is a practical and effective approach to improving GPU utilization for multi-tenant LLM serving.

## Metadata
- **Published**: 2026-08-16T14:31:56Z
- **Authors**: Weinan Liu, Zeyuan Ding, Dian Ding, Chengcheng Wan, Lu Tang, Guangtao Xue, Jiwu Shu, Yiming Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15762v1)