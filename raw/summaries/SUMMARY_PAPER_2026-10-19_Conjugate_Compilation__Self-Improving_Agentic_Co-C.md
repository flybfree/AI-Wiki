---
title: Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding
url: http://arxiv.org/abs/2610.25012v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-18_04-46-51Z_ConjugateCompilation_Self_ImprovingAgenticCo_Compi.md
generated_at: 2026-10-19 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Conjugate Compilation, a novel approach that reframes speculative decoding as a cross-model compilation problem, jointly optimizing the draft and target models within their shared execution rather than compiling them in isolation. The authors demonstrate that treating the co-located execution of both models as a single optimization target, guided by a self-improving agentic search system using LLMs and Monte Carlo tree search, yields a geometric-mean per-round speedup of 1.37x over conventional execution, with interleaved kernels pushing performance to 1.45x and up to 1.59x in the best case across multiple GPU configurations.

## Key Takeaways
- The core insight is that cross-model compilation must be informed by the measured performance of the co-located shared execution it produces: an optimization that improves a kernel in isolation need not improve the models when they execute together. This challenges the conventional compiler paradigm where each model is optimized independently, leaving the shared execution boundary unexploited.
- The authors devise operand layouts that interleave blocks from both the draft and target models within common tiles, co-locating GEMM and non-GEMM work while preserving mathematical correctness. This interleaving strategy is what elevates speedup from 1.37x to 1.45x, demonstrating that physical co-location of computation across models unlocks additional optimization opportunities invisible to single-model compilers.
- The optimization is realized through a self-improving agentic search system where an LLM edits cross-model optimization plans using the compiler and GPU execution as its environment. Each proposed plan is compiled, executed, and scored through its co-located shared execution, with kernel-level verdicts, compiler feedback, and Monte Carlo tree search accumulating rewards to guide subsequent exploration, creating a closed-loop feedback system for compiler optimization.

## Context
Speculative decoding has become a critical technique for scaling LLM serving throughput by pairing a small draft model with a larger target model, yet existing compilation pipelines treat each model as an independent compilation unit. This paper sits at the intersection of compiler optimization, agentic AI systems, and GPU systems engineering, addressing a gap where the shared execution boundary between two co-located models remains outside any single compiler's optimization scope. As GPU capacity becomes increasingly constrained and heterogeneous, unlocking stranded resources through cross-model co-compilation represents a systems-level approach to squeezing more performance from existing hardware rather than simply deploying more GPUs.

## Implications
For practitioners deploying speculative decoding in production, Conjugate Compilation offers a path to 1.37x–1.59x speedups and 1.46x–1.50x improved GPU utilization on widely available hardware like the RTX 5090 and B300, directly reducing serving costs and latency without requiring new hardware. For the compiler and AI systems research community, the agentic search paradigm—where an LLM iteratively proposes, compiles, and evaluates cross-model optimization plans against real GPU execution—suggests a broader methodology for compiler optimization that could extend beyond speculative decoding to any multi-model serving pipeline, potentially transforming how compilers are designed for heterogeneous, multi-model workloads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25012v1)
