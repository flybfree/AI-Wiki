---
title: Trident: Unifying Guarded Dispatch and Host Execution for PyTorch Triton Workloads
published: 2026-09-29T10:57:15Z
authors: Jinjie Liu, Xiaoyan Liu, Shuhan Zhang, Wenjia Sun, Ruilin Yang, Chunlei Men, Yonghua Lin, Shaohua Li
url: http://arxiv.org/abs/2609.37241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trident: Unifying Guarded Dispatch and Host Execution for PyTorch Triton Workloads

## Abstract
User-written Triton kernels enable high-performance GPU computation within PyTorch, but their end-to-end latency can remain dominated by host-side orchestration, especially when device execution is short. Although torch.compile can generate native host wrappers for captured graphs, each invocation still passes through runtime-managed specialization lookup, guard evaluation, and preparation before reaching the wrapper. We present Trident, a compiler backend that removes this recurring overhead from the specialization cache-hit path. Trident introduces the Specialization Cache Module (SCM), which compiles guarded specialization selection, argument and execution-environment preparation, and host execution for multiple specializations into a single executable module. An invocation enters the SCM once, remains in compiled code when a specialization matches, and returns to Python only when a new specialization must be compiled. Built on Torch-MLIR, Trident lowers guards and host-side orchestration to native code while retaining calls to optimized runtime implementations of supported ATen operators. Our evalu- ation on two LLMs shows that Trident achieves up to a 1.47x speedup in model-level end-to-end latency over eager execution and up to 1.68x over torch.compile.

## Metadata
- **Published**: 2026-09-29T10:57:15Z
- **Authors**: Jinjie Liu, Xiaoyan Liu, Shuhan Zhang, Wenjia Sun, Ruilin Yang, Chunlei Men, Yonghua Lin, Shaohua Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37241v1)