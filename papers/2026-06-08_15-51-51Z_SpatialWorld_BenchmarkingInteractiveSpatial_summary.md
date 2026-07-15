---
title: "Summary: 2026-06-08_15-51-51Z_SpatialWorld_BenchmarkingInteractiveSpatialReasoni.md"
date: 2026-06-08
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-08_15-51-51Z_SpatialWorld_BenchmarkingInteractiveSpatialReasoni.md


**Source**: [Original Paper](http://arxiv.org/abs/2606.09669v1)
Saved: 2026-06-08 22:00
Source: 2026-06-08_15-51-51Z_SpatialWorld_BenchmarkingInteractiveSpatialReasoni.md
Model: None

---


## Summary  
SpatialWorld is a benchmark that evaluates the interactive spatial reasoning of multimodal agents in complex real‑world tasks. It moves beyond static VQA or simulator‑specific tests by requiring agents to act under vision‑only partial observability and to express decisions via a unified text‑based action interface. The study integrates eight heterogeneous simulation backends, creating 760 human‑annotated tasks across domains such as household routines, travel, and social collaboration. Evaluation of 15 advanced agents shows that even top models achieve only modest success rates.

## Key Contributions  
- [Finding 1] SpatialWorld provides a unified, simulator‑agnostic benchmark that tests active spatial reasoning in heterogeneous real‑world domains.  
- [Finding 2] The benchmark reveals a persistent gap between task success and execution efficiency, highlighting challenges of long‑horizon planning and active exploration.  
- [Finding 3] Evaluation shows that even state‑of‑the‑art models like GPT‑5 achieve only ~17% average task success rate.

## Methodology  
The authors assembled eight simulation backends—household routines, travel, social collaboration, etc.—under a shared protocol. Each task supplies an initial state, a reference trajectory, and a terminal verifier to ensure reliability. Agents receive vision‑only input and must propose actions through a unified text interface compatible with multimodal large language models (MLLMs). Human annotators validated the states and trajectories before testing.

## Results  
Across 760 tasks, GPT‑5 succeeded on average 17.4% of the time, while Qwen‑3.5 performed at 14.1%. Success correlates weakly with task complexity, and agents often fail due to inefficient exploration or misinterpretation of spatial cues.

## Significance  
SpatialWorld exposes critical limitations in current multimodal agents’ spatial reasoning, offering a rigorous testbed for future research on active perception, planning, and generalization across domains.

## Related Concepts  
multimodal large language models (MLLMs), interactive spatial reasoning, partial observability, active exploration, long‑horizon planning, benchmark evaluation, simulation backends, text‑based action interface.

[[SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks]]