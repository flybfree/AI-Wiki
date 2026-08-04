---
title: Celty: SpMspV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference
url: http://arxiv.org/abs/2608.01536v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_23-10-04Z_Celty_SpMspVGPUKernelandSIMTCo_DesignforEfficientD.md
generated_at: 2026-08-03 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Celty, a co‑designed sparse format and GPU kernel for dual‑sparse LLM inference. It achieves up to 5.3× speedup over cuBLAS at high sparsity levels.

## Key Takeaways  
- RLC‑CSC compresses weight columns into run‑length compressed CSC, enabling vectorized loading of only non‑zero entries and skipping zeroed memory accesses.  
- Shared memory is used to accumulate partial products while the kernel ignores unnecessary loads, reducing bandwidth traffic.  
- The Sparse SIMT Core pipelines the RLC decoder and reuses local registers for accumulation, operating directly on the same RLC‑CSC layout without requiring data reshuffling.

## Context  
LLM inference relies heavily on matrix multiplication, yet most GPU kernels assume a single sparsity source. Dual‑sparsity workloads—combining weight pruning with runtime activation sparsity—are rarely supported by existing hardware, limiting practical deployment of such models.

## Implications  
Hardware acceleration for dual‑sparse LLM inference can dramatically lower latency and cost, encouraging broader adoption of sparse architectures in production systems. This research opens a path toward more efficient AI services that balance model size and performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01536v1)
