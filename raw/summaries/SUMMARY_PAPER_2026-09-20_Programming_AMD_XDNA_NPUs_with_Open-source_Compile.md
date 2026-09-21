---
title: Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study
url: http://arxiv.org/abs/2609.21264v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_03-22-12Z_ProgrammingAMDXDNANPUswithOpen_sourceCompilerTools.md
generated_at: 2026-09-20 20:09
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates the optimization of FlashAttention on AMD's XDNA spatial NPU architecture using open-source compiler tools such as IRON and MLIR-AIR. The study demonstrates that strategically mapping multi-stage workloads—specifically by keeping intermediate tensors in local compute-tile memory rather than returning them to shared memory—significantly improves both throughput and energy efficiency compared to standard GPU implementations.

## Key Takeaways
- The researchers evaluated four distinct reference designs on XDNA 1 and XDNA 2 hardware, ranging from executing operators individually to a fully fused kernel that keeps $QK^T$ scores in local compute-tile memory to avoid unnecessary data movement.
- On the XDNA 2 architecture, the fused kernel achieved a throughput of 3.62 TFLOP/s over end-to-end execution, which is double the performance of the standard IRON design and offers 5.3 to 7.2 times better energy efficiency than the integrated GPU at 2K tokens and above.
- Roofline analysis revealed that XDNA 1 reaches a compute-bound regime earlier than XDNA 2, meaning the same fusion techniques that double throughput on newer hardware may be less effective on older generations due to lower ridge points.
- The authors propose a predictive rule of thumb for developers: compare a mapping's operational intensity against each memory level's ridge point to determine exactly when to stop fusing kernels before any code is written, providing a systematic approach to hardware optimization.

## Context
As the industry moves toward more efficient and specialized AI hardware, understanding how to map complex algorithms like FlashAttention onto non-von Neumann architectures is critical for scaling. This paper addresses a major bottleneck in deploying large-scale models by focusing on the interplay between software compiler tools and specific hardware memory hierarchies.

## Implications
This work provides a clear methodology for practitioners to optimize LLM inference on specialized silicon, moving beyond trial-and-error toward a predictable engineering process. By providing open-source reference designs and a framework based on roofline analysis, it empowers the community to better utilize NPU hardware for high-performance AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21264v1)
