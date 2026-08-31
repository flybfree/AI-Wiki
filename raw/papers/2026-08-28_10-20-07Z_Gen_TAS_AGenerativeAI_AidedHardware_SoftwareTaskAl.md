---
title: Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems
published: 2026-08-28T10:20:07Z
authors: Mary Kong, Yuqin Zhao, Semih Vazgecen, Cristian Sestito, Themis Prodromakis
url: http://arxiv.org/abs/2608.28160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems

## Abstract
FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware. However, determining which application tasks should execute on the GPP or FPGA requires extensive expertise and design-space exploration, particularly when user objectives vary across latency, communication, resource utilisation, and power. This paper proposes Gen-TAS, a knowledge-grounded LLM framework for user-specific FPGA-GPP task allocation. By combining task-graph analysis with RAG, Gen-TAS grounds LLM reasoning in historical implementation knowledge and generates multiple explainable strategies tailored to the specified objectives. Human-in-the-loop selection and a deterministic backend connect LLM-generated decisions to reproducible FPGA SoC implementations. Experiments on CNN and SDR workloads across multiple LLMs demonstrate stable, requirement-driven allocation. Under latency-oriented objectives, implementations following the selected strategies achieve speedups of up to 2.45$\times$ and 92.53$\times$, respectively, relative to the corresponding all-GPP baselines while other objectives select strategies that trade some acceleration performance for FPGA-GPP communication, resource utilisation, or FPGA power.

## Metadata
- **Published**: 2026-08-28T10:20:07Z
- **Authors**: Mary Kong, Yuqin Zhao, Semih Vazgecen, Cristian Sestito, Themis Prodromakis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28160v1)