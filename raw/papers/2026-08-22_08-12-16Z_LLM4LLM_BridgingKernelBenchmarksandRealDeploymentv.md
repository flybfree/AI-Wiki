---
title: LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization
published: 2026-08-22T08:12:16Z
authors: Hui Zeng, Pengfei Yang, Yanxin Chen, Fusong Ju, Xinran Wei
url: http://arxiv.org/abs/2608.21836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization

## Abstract
Large language models have become increasingly capable agents for low-level code and kernel optimization, but isolated kernel benchmarks provide only a proxy for the deployment behavior that matters in language-model inference. We identify a benchmark-to-deployment gap: candidate kernels that appear correct and fast in standalone harnesses can exhibit different performance, safety, or phase behavior after integration into a real inference workload. We introduce LLM4LLM, a deployment-aware closed-loop optimization framework that starts from a target inference script, extracts phase-aware optimization tasks, searches with an experience-guided episodic agent, and accepts patches through in-model validation. Across ten language-model inference workloads on A100 and H100 GPUs, LLM4LLM improves end-to-end latency for every evaluated model, achieving 3.91$\times$/6.98$\times$ geometric-mean speedups on A100/H100; as supporting kernel-level evidence, it also attains up to 2.745$\times$ GeoMean speedup on KernelBench Level 2.

## Metadata
- **Published**: 2026-08-22T08:12:16Z
- **Authors**: Hui Zeng, Pengfei Yang, Yanxin Chen, Fusong Ju, Xinran Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21836v1)