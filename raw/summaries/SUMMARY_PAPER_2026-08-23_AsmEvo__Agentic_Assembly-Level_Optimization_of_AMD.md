---
title: AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification
url: http://arxiv.org/abs/2608.20711v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_03-34-22Z_AsmEvo_AgenticAssembly_LevelOptimizationofAMDGPUKe.md
generated_at: 2026-08-23 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
AsmEvo is an agentic assembly‑level optimizer that works on already compiled AMDGPU kernels, reconstructing a reassemblable representation and proposing low‑level edits while guaranteeing functional equivalence. It uses profiling to edit only hot windows and falls back conservatively when correctness cannot be ensured. The method achieves geometric‑mean speedups of up to 3.88× on MI308X and comparable gains on production workloads.

## Key Takeaways
- AsmEvo reconstructs a reassemblable representation from the compiled AMDGPU code object K0, enabling optimization without access to source or intermediate representations.
- It proposes low‑level edits within a hot window guided by profiling and only accepts candidates after differential verification against K0 under identical launches.
- The optimizer combines metadata‑aware rebuilding, correctness‑gated timing checks, and an in‑place patch fallback to ensure ABI preservation when edits cannot be applied.

## Context
In AI inference pipelines, GPU kernels often become black boxes after compilation, limiting opportunities for performance improvements. Existing autotuning tools require source or high‑level representations, making them unsuitable for real‑world deployed binaries.

## Implications
This work demonstrates that assembly‑level optimization can be applied to proprietary and third‑party kernels, expanding the scope of GPU acceleration beyond open‑source projects. Practitioners can expect measurable gains in latency without sacrificing correctness or requiring vendor cooperation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20711v1)
