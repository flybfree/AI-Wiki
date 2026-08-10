---
title: HLSmith: An Expert-Guided Agentic Framework for C/C++-to-HLS Translation
published: 2026-08-07T04:27:04Z
authors: Yuebo Luo, Ahmad Sedigh Baroughi, Philip Stachura, Le Chen, Venkatram Vishwanath, Zhenman Fang, Caiwen Ding
url: http://arxiv.org/abs/2608.06791v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HLSmith: An Expert-Guided Agentic Framework for C/C++-to-HLS Translation

## Abstract
Application-specific FPGA accelerators offer substantial performance and energy-efficiency gains across many application domains, but developing them is costly, often requiring months of specialized effort. Even with high-level synthesis (HLS), designers still need extensive hardware expertise to build high-performance accelerators. Although large language models (LLMs) have demonstrated strong software-generation capabilities, even frontier models lack the hardware intuition and procedural knowledge needed to reliably translate baseline C/C++ programs into high-performance HLS designs: they struggle to identify effective architectures, follow the optimization processes used by HLS experts, and apply hardware transformations consistently across diverse kernels. We present HLSmith, an expert-guided framework for translating C/C++ programs into optimized HLS accelerators. HLSmith combines three components: an HLS optimization expertise library that encodes guarded transformation recipes, their applicability and prerequisite conditions, and unsafe cases to avoid; a staged, feedback-driven orchestration flow modeled on expert HLS development practice that guides agents through synthesis, bottleneck analysis, and optimization; and a tool-grounded model-adaptation pipeline that converts optimization trajectories from commercial frontier models into training data for fine-tuning open-weight LLMs. We evaluate HLSmith on PolyBench against ChatHLS, a leading prior agent-orchestration framework for HLS accelerator development. HLSmith achieves a geometric mean speedup of 4.24x over ChatHLS while producing functionally correct designs, in both software and RTL simulation, for every benchmark, compared with ChatHLS's 57% valid-design rate. It further reaches speedups of up to 252x and 138x with commercial frontier models and open-weight models, respectively.

## Metadata
- **Published**: 2026-08-07T04:27:04Z
- **Authors**: Yuebo Luo, Ahmad Sedigh Baroughi, Philip Stachura, Le Chen, Venkatram Vishwanath, Zhenman Fang, Caiwen Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06791v1)