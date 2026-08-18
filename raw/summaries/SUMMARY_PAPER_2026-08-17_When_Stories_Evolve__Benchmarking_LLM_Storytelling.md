---
title: When Stories Evolve: Benchmarking LLM Storytelling Across Agent Architectures in Open-Ended World Simulations
url: http://arxiv.org/abs/2608.15654v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_09-46-45Z_WhenStoriesEvolve_BenchmarkingLLMStorytellingAcros.md
generated_at: 2026-08-17 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces WSE-bench, a benchmark that evaluates large language models on open‑ended storytelling in evolving world simulations by measuring three distinct capacities: sustained generation, canonical coherence, and meaningful development. Across frontier models, the relationship between consistency and richness is non‑concave, indicating multiple non‑dominated configurations where neither metric dominates.

## Key Takeaways  
- Consistency and Richness do not form a smooth trade‑off; their empirical Pareto frontier is non‑concave with several non‑dominated intermediate configurations.  
- Model scale chiefly improves sustained generation but does not yield reliable gains in canonical coherence or meaningful development.  
- Added structure can enrich trajectories, yet it may shorten them and does not uniformly improve coherence.

## Context  
Open‑ended storytelling demands that models retain facts, relationships, causal dependencies, and character states as the simulated world changes. Existing evaluation often focuses on final story quality, overlooking the dynamic processes that generate those stories in real time.

## Implications  
The findings reveal that sustained generation, canonical coherence, and meaningful development are distinct and sometimes competing abilities, challenging the assumption of a single linear improvement metric. Practitioners should adopt multi‑objective, process‑aware evaluation to guide model design and avoid over‑reliance on superficial trade‑off optimizations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15654v1)
