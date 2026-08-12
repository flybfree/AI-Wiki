---
title: SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training
published: 2026-08-11T15:12:14Z
authors: Zhuang Wang
url: http://arxiv.org/abs/2608.11034v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training

## Abstract
In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin. Existing diagnosis often relies on in-process monitors that cannot report after the trainer blocks or terminates, or on post-mortem logs that preserve only synchronized symptoms; offline health tests lose the workload and operating conditions that triggered the failure. We present SCOUT, a unified runtime failure-localization framework built on one design principle: identify outliers through strict-majority consensus among equivalent replicas. SCOUT aligns replica progress, timing, and numerical evidence, then uses its Consensus Collective Communication (C3) abstraction to identify ranks whose compact signatures disagree with their peers. An out-of-band CPU observer remains responsive when training hangs, whereas in-situ replay exercises recurring stragglers and silent data corruption (SDC) beside the live job with its model state, kernels, allocations, communication path, and thermal and memory pressure present. Collective fingerprints expose rank-local protocol divergence. Clean replay coverage certifies checkpoint numerical integrity, preventing recovery from selecting state corrupted by SDC. SCOUT integrates with PyTorch, TorchTitan, Megatron-Core, and DeepSpeed without training-loop or framework-source modifications. SCOUT is open source at https://github.com/LMResiliency/lm-resiliency.

## Metadata
- **Published**: 2026-08-11T15:12:14Z
- **Authors**: Zhuang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11034v1)