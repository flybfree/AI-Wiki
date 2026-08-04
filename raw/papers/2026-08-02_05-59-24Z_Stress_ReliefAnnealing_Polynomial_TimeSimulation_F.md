---
title: Stress-Relief Annealing: Polynomial-Time Simulation-Free Layout Optimization for Automated Warehouses
published: 2026-08-02T05:59:24Z
authors: Xiangjie Luo, Yulun Zhang, Miyuki Koshimura, Makoto Yokoo, Jiaoyang Li
url: http://arxiv.org/abs/2608.01024v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stress-Relief Annealing: Polynomial-Time Simulation-Free Layout Optimization for Automated Warehouses

## Abstract
We study the problem of optimizing physical layouts for automated warehouses, where hundreds to thousands of robots are coordinated to transport packages. Previous works have shown that optimizing the warehouse layout (e.g., the physical location of the storage shelves) significantly improves throughput. However, state-of-the-art layout optimization approaches are based on evolutionary optimization methods, which treat the entire warehouse as a black box and rely on random mutation to search for high-quality layouts. While the optimization outcomes are promising, these methods require a massive number of simulations to evaluate candidate solutions, making them sample-inefficient. In this paper, we present Stress-Relief Annealing (SRA), a polynomial-time simulation-free layout optimization algorithm. SRA turns the task demand into a per-vertex \emph{stress field} that predicts where traffic will concentrate in the warehouse; the field's peak provably caps the throughput.   Our experimental results show that (1) SRA improves both the throughput and the scalability of a human-designed warehouse, roughly doubling the number of robots it can sustain, (2) it matches or exceeds the throughput of the evolutionary baselines while taking only $19$ minutes on one CPU core, against their $25{,}000$ simulations and $25$ hours on a $64$-core machine, and (3) the gain generalizes across different Multi-Agent Path Finding algorithms, non-uniform task demands, and a warehouse with doubled dimensions.

## Metadata
- **Published**: 2026-08-02T05:59:24Z
- **Authors**: Xiangjie Luo, Yulun Zhang, Miyuki Koshimura, Makoto Yokoo, Jiaoyang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01024v1)