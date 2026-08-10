---
title: HLSmith: An Expert-Guided Agentic Framework for C/C++-to-HLS Translation
url: http://arxiv.org/abs/2608.06791v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_04-27-04Z_HLSmith_AnExpert_GuidedAgenticFrameworkforC_C___to.md
generated_at: 2026-08-09 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HLSmith, an expert-guided framework that translates C/C++ code into high-performance HLS accelerators by integrating a library of transformation recipes, a staged feedback orchestration flow, and a model-adaptation pipeline. Evaluated on PolyBench against ChatHLS, HLSmith achieves higher geometric mean speedup and functional correctness rates across benchmarks.

## Key Takeaways
- The framework’s expertise library encodes transformation rules with applicability conditions and unsafe cases, enabling systematic optimization of HLS designs.
- A staged feedback orchestration mimics expert practice, guiding agents through synthesis, bottleneck analysis, and iterative tuning to improve design quality.
- Model adaptation converts commercial model trajectories into training data, allowing open-weight LLMs to learn hardware‑aware generation.

## Context
Current AI tools for high‑level synthesis lack deep procedural knowledge of FPGA hardware constraints. Existing systems often produce designs that are either incorrect or suboptimal, limiting adoption in time‑critical and energy‑sensitive applications.

## Implications
HLSmith demonstrates that expert‑driven guidance can significantly boost the reliability and performance of AI‑generated accelerators, offering a path toward scalable, cost‑effective hardware design pipelines for industry and research alike.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06791v1)
