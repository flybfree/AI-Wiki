---
title: Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs
published: 2026-08-22T00:01:18Z
authors: Afsara Benazir, Chen Chen, Rongxiao Qu, Jiabo Huang, Jingtao Li, Lingjuan Lyu
url: http://arxiv.org/abs/2608.21693v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs

## Abstract
Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware. Practical deployment often requires stacking multiple compression techniques: expert pruning removes redundant experts, weight quantization lowers model memory footprint, and KV-cache compression reduces long-context memory pressure. However, these techniques are typically evaluated in isolation, leaving open how they interact when applied together in realistic deployment pipelines.   In this work, we present MoEXBench, a systematic benchmark for evaluating composable MoE compression as an end-to-end deployment workflow. MoEXBench studies 10 MoE models ranging from 30B to 235B total parameters across standard-attention, hybrid linear-attention, and sliding window attention architectures. It evaluates 20%-50% expert pruning rates, 1 to 16 bit weight-quantization schemes, and multiple KV-cache precision settings, applied both individually and in combination.   MoEXBench introduces an eight-module evaluation suite that jointly measures composable-compression quality, workload and architecture robustness, pruning/quantization/KV cache sensitivity, and deployment efficiency on commodity hardware. Our results reveal non-trivial interactions among compression methods: composable compression cannot be predicted from standalone techniques, compression rate alone does not reliably predict quality loss or runtime gain, expert pruning is the dominant degradation source, and average quality can hide workload and architecture-specific failures. By releasing normalized module scores, compressed artifacts, and reproducible scripts, MoEXBench enables practical accuracy-memory-latency comparison across MoE families and hardware backends.

## Metadata
- **Published**: 2026-08-22T00:01:18Z
- **Authors**: Afsara Benazir, Chen Chen, Rongxiao Qu, Jiabo Huang, Jingtao Li, Lingjuan Lyu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21693v1)