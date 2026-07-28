---
title: FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon
url: http://arxiv.org/abs/2607.22785v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_11-42-17Z_FusionML_Prefill_NotDecode_MechanismandBoundarieso.md
generated_at: 2026-07-27 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how transformer inference can be accelerated on Apple‑Silicon SoCs that share CPU, GPU, and Neural Engine memory. By fixing a concurrency bug in MLX’s lazy‑graph scheduler, the authors achieve faster prefill times without sacrificing decode performance or token quality.

## Key Takeaways
- The lazy‑graph scheduler serializes cross‑stream operations when a CPU operation consumes an unmaterialized GPU result, causing row‑split matmuls to run slower than GPU‑only execution.  
- Introducing eager materialization restores concurrency and yields a 1.34× speedup over the problematic lazy mode for prefill workloads.  
- The per‑layer contention‑aware CPU+GPU split improves Llama‑shaped decoder prefill by 1.15–1.38× across five chips, while decode throughput and token output remain unchanged.

## Context
Apple‑Silicon’s unified memory architecture enables co‑execution of CPU and GPU tasks, but existing frameworks often impose hidden serialization that limits performance gains for transformer models. This research demonstrates how a subtle scheduler design can unlock the full potential of this hardware without compromising other inference stages.

## Implications
Practitioners should adopt eager materialization when using lazy graph schedulers to avoid concurrency bottlenecks in real‑world deployment. The findings suggest that careful attention to operator ordering and memory materialization is crucial for maximizing performance on unified‑memory platforms, benefiting both research and commercial AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22785v1)
