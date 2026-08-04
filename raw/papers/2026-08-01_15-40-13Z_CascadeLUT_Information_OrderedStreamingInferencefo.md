---
title: CascadeLUT: Information-Ordered Streaming Inference for Bandwidth-Constrained FPGAs
published: 2026-08-01T15:40:13Z
authors: Oliver Cassidy, Marta Andronic, George A. Constantinides
url: http://arxiv.org/abs/2608.00720v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CascadeLUT: Information-Ordered Streaming Inference for Bandwidth-Constrained FPGAs

## Abstract
Mapping neural networks to FPGAs enables low-latency, energy-efficient inference, particularly for lookup table (LUT)-based models that eliminate multipliers and map directly to reconfigurable fabric. While prior work achieves high compute efficiency, it typically assumes full-sample availability, causing pipeline stalls in bandwidth-limited streaming scenarios. Here, the bottleneck shifts from computation to data movement, as large input transfers limit throughput and energy efficiency. We present CascadeLUT, an information-structured inference framework organized around bandwidth constraints. Instead of buffering the full input, features are partitioned into ordered subsets and predictions are progressively refined as subsets arrive. The cascade statically controls which layers consume incoming features, enabling deterministic streaming inference without runtime branching. By co-designing feature scheduling with hardware dataflow, CascadeLUT reduces data movement while maintaining accuracy. Across datasets, it achieves 4.0 to 12.5 times lower latency, 3.0 to 5.0 times higher throughput and up to 13.8 times lower energy/sample than prior LUT baselines, using 1.2 to 4.4 times the LUTs of the smallest DWN baseline per task. We also demonstrate on-device input quantization integrated with LUT-based inference and present end-to-end FPGA results on real-world workloads, with 5 times reductions in quantization overhead.

## Metadata
- **Published**: 2026-08-01T15:40:13Z
- **Authors**: Oliver Cassidy, Marta Andronic, George A. Constantinides
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00720v1)