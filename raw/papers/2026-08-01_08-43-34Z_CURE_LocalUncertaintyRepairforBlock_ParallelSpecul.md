---
title: CURE: Local Uncertainty Repair for Block-Parallel Speculative Decoding
published: 2026-08-01T08:43:34Z
authors: Aofan Liu, Jingxiang Meng, Fangxin Liu, Yongbiao Chen
url: http://arxiv.org/abs/2608.00531v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CURE: Local Uncertainty Repair for Block-Parallel Speculative Decoding

## Abstract
Speculative decoding mitigates the latency of sequential generation in autoregressive Large Language Models (LLMs) by interleaving draft generation with target verification. However, existing parallel drafting backends often suffer from rapid accuracy degradation over long horizons, leading to high rejection rates during verification and suboptimal wall-clock speedups. We observe that drafting errors are not uniformly distributed but typically stem from localized high-uncertainty tokens that destabilize downstream generation trajectories. Motivated by this token error pattern, we propose CURE, a budget-aware dynamic repair tree designed to repair errors at uncertainty focal points without incurring prohibitive tree-verification overheads. Specifically, our method uses predictive confidence margins to dynamically locate candidate error tokens within a block-parallel draft, expands bounded repair paths only at these fragile nodes, and employs a novel repair resynchronization mechanism to realign draft states post-verification. Evaluations on code-generation benchmarks (HumanEval, MBPP, and LiveCodeBench-lite) and mathematical reasoning benchmark (GSM8K) demonstrate that CURE increases the average accepted length by 4.2-7.5% over parallel baselines without repair, translating to an end-to-end speedup of $2.66-3.49\times$ over target-only decoding. Furthermore, we provide a plug-and-play repair module compatible with standard parallel drafting frameworks. We also characterize the trade-off between draft compute and verification efficiency.

## Metadata
- **Published**: 2026-08-01T08:43:34Z
- **Authors**: Aofan Liu, Jingxiang Meng, Fangxin Liu, Yongbiao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00531v1)