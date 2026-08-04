---
title: GraphIR: Architecture-Level Search States for LLM-Guided Neural Architecture Evolution
url: http://arxiv.org/abs/2608.01633v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-06-58Z_GraphIR_Architecture_LevelSearchStatesforLLM_Guide.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GraphIR, an architecture-aware intermediate representation that bridges the gap between executable neural network programs and large language model‑guided search. By providing a mutation‑aligned candidate state, GraphIR improves NAS performance across multiple benchmarks while keeping model size comparable to existing methods.

## Key Takeaways
- GraphIR creates three complementary views for each architecture candidate: a computation skeleton that describes tensor flow, a mutation surface exposing editable modules and operations, and a validity envelope that captures interface contracts and propagated shapes.  
- The method excels at pinpointing exact producer occurrences, tracing dependency propagation, and diagnosing interface or failure risks within the NAS‑Dependency benchmark.  
- Integrated into OpenEvolve, GraphIR yields the best overall search performance across six downstream benchmarks without sacrificing model efficiency.

## Context
Neural architecture search (NAS) relies on LLMs to generate code, yet LLMs cannot directly reason about mutable components or tensor dependencies, limiting their usefulness. This work addresses that limitation by providing a structured representation that enables precise reasoning during mutation.

## Implications
GraphIR offers practitioners a reliable way to guide LLM‑driven NAS toward valid, efficient architectures, reducing costly failures and improving search speed in industry‑scale model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01633v1)
