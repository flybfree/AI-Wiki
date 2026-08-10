---
title: Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking
url: http://arxiv.org/abs/2608.07077v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-29-19Z_TransformersStruggletoUseTheirEmergentWorldModels_.md
generated_at: 2026-08-09 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large reasoning models succeed on the Tower of Hanoi but falter when the goal state is not restricted to a single peg, revealing that they build an emergent world model which decays during planning. Small Transformers trained from scratch develop a geometrically faithful Sierpinski triangle representation that guides solving, while frontier LLMs encode this model perfectly at the end of the prompt yet lose it mid‑task.

## Key Takeaways
- Small Transformers develop a linearly decodable, geometrically faithful representation of the puzzle’s state space (the Sierpinski triangle) that is causally involved in solving.  
- Large LLMs encode the same world model near‑perfectly at the end of the prompt but fail on tasks with more than three rings because the representation decays during planning.  
- Injecting the prompt‑time representation at inference can restore performance, indicating the failure is due to loss of the required representation rather than its absence.

## Context
This work highlights that emergent world models are not stable in large language models; they decay over time and affect reasoning tasks beyond standard benchmarks. It challenges assumptions about LLMs maintaining knowledge across prompts and suggests a need for more nuanced evaluation.

## Implications
For practitioners, the findings imply designing systems to preserve or restore world model representations rather than relying on them persisting naturally. This could inform training strategies and inference‑time interventions in reasoning models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07077v1)
