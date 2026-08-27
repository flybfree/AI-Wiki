---
title: Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels
published: 2026-08-25T18:43:43Z
authors: Amir Taherin, Sana Taghipour Anvari, Charles Amante, Yixiao Chen, Ruben Noroian, Zlatan Feric, Nicolas Bohm Agostini, Pu Zhao, José Cano, Bin Ren, Yanzhi Wang, David Kaeli
url: http://arxiv.org/abs/2608.25053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels

## Abstract
Edge LLM deployment is shaped by more than model size and precision: inference backend, hardware platform, memory traffic, and power management all affect latency and efficiency. We present Hydra, a common-schema, phase-aware workload characterization framework for LLM inference on edge SoCs. Hydra instruments HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema and fuses those records with hardware telemetry, enabling a multi-dimensional characterization of performance, system-resource utilization, and efficiency across prefill and decode phases. Using Hydra, we evaluate three consecutive edge System-on-Chip (SoC) generations (AGX Xavier, AGX Orin, and AGX Thor), 13 instruction-tuned LLMs from seven families, five execution formats, and consider input/output-length sensitivity. The resulting artifact contains roughly 107K per-prompt records and is publicly released with Hydra. Our analysis shows that aggregate latency alone hides key deployment effects: backend structure changes where latency is introduced, quantization reduces memory traffic and energy but does not predict power monotonically, and SoC generation changes how utilization and efficiency should be interpreted. By connecting phase-level timing with system-resource utilization and efficiency metrics, Hydra enables reproducible, phase-aware characterization of edge LLM inference. Hydra's source code and the collected per-prompt trace corpus are available open-source at: https://github.com/amirtaherin/hydra

## Metadata
- **Published**: 2026-08-25T18:43:43Z
- **Authors**: Amir Taherin, Sana Taghipour Anvari, Charles Amante, Yixiao Chen, Ruben Noroian, Zlatan Feric, Nicolas Bohm Agostini, Pu Zhao, José Cano, Bin Ren, Yanzhi Wang, David Kaeli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25053v1)