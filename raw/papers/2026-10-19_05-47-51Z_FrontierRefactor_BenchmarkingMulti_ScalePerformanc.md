---
title: FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring
published: 2026-10-19T05:47:51Z
authors: Shijian Wang, Fanqing Meng, Jiajun Chen, Qiguang Chen, Linxin Song, Runhao Fu, Shuhang Zheng, Shuai Shao, Qizhe Xie, Jieyu Zhao, Mengkang Hu
url: http://arxiv.org/abs/2610.25834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring

## Abstract
Autonomous codebase refactoring requires coding agents to restructure working software while strictly preserving externally observable behavior and prioritizing execution performance and compute efficiency over stylistic preference. Existing benchmarks: refactoring benchmarks assess functional correctness while overlooking runtime regressions, whereas code performance benchmarks target isolated micro-kernels that ignore codebase-scale complexity. We observe that refactoring scale is governed by the scope of the observable contract, the caller-visible interface fixing behavioral invariants while freeing private implementations for optimization. Building on this insight, we introduce FrontierRefactor, a benchmark of 60 qualified engineering tasks spanning four scales, from computational kernels to full repositories, across in-place optimization and cross-language rewriting. Evaluating frontier coding agents through a reference-free cascaded protocol across 1,080 execution runs reveals that correctness and speedup are largely decoupled: 41.2% of submissions satisfy functional equivalence yet fail to deliver verified performance improvements, with 19.3% suffering performance regressions and 21.9% trapped in measurement noise. Refactoring paradigms reveal orthogonal engineering bottlenecks: while cross-language rewrites gain speedups from native compilation after passing functional checks, agents struggle with contract fidelity, with pass rates dropping from 65.0% on modules to 32.6% at package scale; conversely, in-place optimization reliably preserves behavioral contracts at 86.5% but rarely achieves acceleration without physical performance profiling. Trajectory analysis shows that agents fall victim to uncalibrated micro-benchmarking illusions, an operational blind spot that multi-turn execution-timing feedback directly resolves, raising strict success from 16.0% to 40.0%.

## Metadata
- **Published**: 2026-10-19T05:47:51Z
- **Authors**: Shijian Wang, Fanqing Meng, Jiajun Chen, Qiguang Chen, Linxin Song, Runhao Fu, Shuhang Zheng, Shuai Shao, Qizhe Xie, Jieyu Zhao, Mengkang Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25834v1)