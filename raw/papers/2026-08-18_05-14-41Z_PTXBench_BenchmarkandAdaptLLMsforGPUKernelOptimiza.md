---
title: PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX
published: 2026-08-18T05:14:41Z
authors: Genghan Zhang, Yixin Dong, Chengze Fan, Zhichen Zeng, Yueming Yuan, Shaowei Zhu, Kunle Olukotun
url: http://arxiv.org/abs/2608.17379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX

## Abstract
We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads, and executing the target instructions does not necessarily translate into competitive performance. No evaluated model consistently matches frontier libraries across the suite. We further adapt Qwen3.6-27B using supervised fine-tuning. Repair-conditioned training improves several tasks, but generalization remains uneven; data coverage, balance, and the quality of the reasoning teacher matter in addition to dataset size. PTXBench provides an auditable testbed for measuring and improving LLMs' ability to exploit evolving GPU architectures.

## Metadata
- **Published**: 2026-08-18T05:14:41Z
- **Authors**: Genghan Zhang, Yixin Dong, Chengze Fan, Zhichen Zeng, Yueming Yuan, Shaowei Zhu, Kunle Olukotun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17379v1)