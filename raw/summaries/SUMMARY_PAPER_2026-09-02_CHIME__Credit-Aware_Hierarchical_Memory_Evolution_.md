---
title: CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning
url: http://arxiv.org/abs/2609.02074v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_03-59-21Z_CHIME_Credit_AwareHierarchicalMemoryEvolutionforLo.md
generated_at: 2026-09-02 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Credit-Aware Hierarchical Memory Evolution (CHIME), a self‑evolving memory framework that separates planning and execution experiences into distinct banks, thereby solving the credit assignment problem in prior approaches. Experiments on four long‑horizon agent benchmarks show CHIME outperforms both training‑based and existing self‑evolving baselines, accumulating effective memory with fewer items while preserving faithful utility of learned values.

## Key Takeaways
- CHIME maintains separate planning and execution banks, updating only the relevant bank after attributing outcomes to plan, execution, both, or neither.  
- The framework accumulates a highly effective memory using far fewer memory entries than prior methods.  
- Downstream utility is reflected in learned memory values: high‑quality planning memories are more valuable than execution memories.

## Context
Self‑evolving memory aims to improve agents’ long‑horizon planning without costly parameter updates, but current solutions suffer from noisy feedback that conflates plan quality with execution errors. CHIME’s credit‑aware design offers a principled way to separate these influences, aligning with the broader goal of scalable, continual learning in AI.

## Implications
For practitioners, CHIME enables more efficient training loops and reduces reliance on large labeled datasets, lowering computational costs. The framework’s ability to transfer memory across models suggests a path toward modular, reusable planning components that can be integrated into diverse AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02074v1)
