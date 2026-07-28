---
title: ParasGB: A Graph Benchmark Suite for Parasitic Estimation on AMS Circuits
url: http://arxiv.org/abs/2607.23225v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_14-23-27Z_ParasGB_AGraphBenchmarkSuiteforParasiticEstimation.md
generated_at: 2026-07-27 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
ParasGB is an open‑source benchmark suite designed to evaluate GNN models for predicting parasitic capacitance and resistance in analog mixed‑signal circuits before physical implementation. The authors release large, heterogeneous RC networks extracted from tape‑out designs together with a standardized evaluation protocol that measures node‑level ground capacitance, edge‑level resistance, and edge‑level coupling capacitance.

## Key Takeaways
- ParasGB provides the first publicly available high‑fidelity RC benchmarks for early‑stage parasitic estimation on circuit graphs.  
- The suite includes diverse GNN architectures evaluated under a unified training pipeline that exposes challenges such as extreme label imbalance, long‑tailed parasitic distributions, and strong structural heterogeneity.  
- All datasets, preprocessing scripts, and configurations are openly available in the GitHub repository.

## Context
This work addresses a critical gap in AI research where deep learning models for circuit design lack reliable evaluation data. By creating a physically grounded benchmark, ParasGB enables reproducible studies of how graph neural networks learn to capture parasitic effects that are essential for accurate analog circuit simulation and optimization.

## Implications
For industry practitioners, ParasGB offers a practical tool to assess the performance of their own GNN‑based models before committing costly layout iterations. For researchers, the benchmark fosters fair comparison across model architectures and guides the development of more robust, physically informed AI solutions in AMS design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23225v1)
