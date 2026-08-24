---
title: AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification
published: 2026-08-21T03:34:22Z
authors: Ji Liu, Puyuan Yang, Rongzhang Zheng, Fan Wang, Jinglin Wang, Muhammad A. Awad, Mortis Huang, Andy Chang, Zekai Li, Zeping Li, Zihao An, Yue Liu, Yuchen Yang, Jianghui Wang, Chushi Chen, Ziqiong Liu, Fuwei Yang, Dong Li, Wen Heng Chung, Shengcai Liu, Emad Barsoum
url: http://arxiv.org/abs/2608.20711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification

## Abstract
High-performance ML systems increasingly rely on GPU kernels whose editable source is unavailable, generated, or too distant from final machine code to expose remaining optimizations. Existing LLM kernel optimizers and autotuners mainly operate on CUDA, Triton, HIP, or tensor-program source and validate against reference implementations. We study a stricter setting: optimizing an already compiled AMDGPU code object, where the deployed binary is the only behavioral oracle.   We present AsmEvo, an agentic assembly-level optimizer for AMD GPU kernels. Given an AMDGPU code object K0, AsmEvo reconstructs a reassemblable representation, proposes low-level edits with a long-horizon agent, rebuilds an ABI-preserving optimized object, and accepts candidates only after differential verification against K0 under identical launches. AsmEvo combines code-object recovery, metadata-aware rebuilding, profiling-guided hot-window editing, correctness-gated timing, and conservative in-place patch fallback.   We conduct extensive experiments with AsmEvo on various AMD GPU kernels. On MI308X, AsmEvo improves 29 of 30 selected KernelBench kernels, reaching 1.35x geometric-mean and 3.88x maximum speedup. On MI300X production workloads, it improves all evaluated AITer binaries and vLLM/SGLang Triton assembly kernels, reaching 1.09x/1.31x and 1.18x/1.34x geometric-mean/maximum speedups, respectively, while preserving functional equivalence.

## Metadata
- **Published**: 2026-08-21T03:34:22Z
- **Authors**: Ji Liu, Puyuan Yang, Rongzhang Zheng, Fan Wang, Jinglin Wang, Muhammad A. Awad, Mortis Huang, Andy Chang, Zekai Li, Zeping Li, Zihao An, Yue Liu, Yuchen Yang, Jianghui Wang, Chushi Chen, Ziqiong Liu, Fuwei Yang, Dong Li, Wen Heng Chung, Shengcai Liu, Emad Barsoum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20711v1)