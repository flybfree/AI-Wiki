---
title: Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study
published: 2026-09-18T03:22:12Z
authors: Erwei Wang, Ephrem Wu, Victor J. B. Jung, Jiajie Li, Andre Rosti, Joseph Melber, Samuel Bayliss
url: http://arxiv.org/abs/2609.21264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study

## Abstract
Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software. Mapping a multi-stage workload onto such a device is largely a question of where the intermediate tensors live. We report what we learned making those choices for FlashAttention with the open-source IRON and MLIR-AIR flows.   We compare four reference designs on XDNA 1 and XDNA 2: one runs each operator separately, two stream between operators on chip, and one fuses all three attention stages into a single kernel. The fused kernel holds the $\boldsymbol{QK}^{\mathsf T}$ scores in compute-tile local memory and reduces partial results over the cascade interconnect, so the scores never return to shared MemTile memory. On XDNA 2, it reaches 3.62 TFLOP/s over complete end-to-end execution, twice the IRON design, with 5.3 to 7.2 times the energy efficiency of the integrated GPU on the same chip at 2K tokens and above. It covers twelve LLM configurations, from BERT to DeepSeek, up to 128K tokens.   Roofline analysis at each memory level explains this result and shows when to stop. XDNA 1 has lower ridge points, so streaming on chip already reaches the compute-bound regime: the same fusion that doubles throughput on XDNA 2 is nearly wasted on XDNA 1. Comparing a mapping's operational intensity against each level's ridge point predicts which case applies before writing any code. Fuse until the mapping clears that ridge point, then stop. We release the reference designs as maintained open source.

## Metadata
- **Published**: 2026-09-18T03:22:12Z
- **Authors**: Erwei Wang, Ephrem Wu, Victor J. B. Jung, Jiajie Li, Andre Rosti, Joseph Melber, Samuel Bayliss
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21264v1)