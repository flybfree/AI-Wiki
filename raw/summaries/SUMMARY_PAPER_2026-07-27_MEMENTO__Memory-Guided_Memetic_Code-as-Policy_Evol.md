---
title: MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution
url: http://arxiv.org/abs/2607.22832v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_18-16-35Z_MEMENTO_Memory_GuidedMemeticCode_as_PolicyEvolutio.md
generated_at: 2026-07-27 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper presents MEMENTO, a memory‑guided single‑elite memetic framework that evolves executable code‑as‑policy for long‑horizon embodied tasks. It demonstrates that the evolved policies achieve higher task success and better generalization than existing evolutionary baselines on Robosuite Tower‑of‑Hanoi and AI2‑THOR.  

## Key Takeaways  
- MEMENTO first evolves a rollout evaluator that maps policy executions to scalar fitness and structured feedback, using this to select candidates and the next elite.  
- The framework combines memory‑guided hill‑climbing, macro‑mutation, and crossover, with feedback metrics conditioning each proposal generation step.  
- Ablations reveal that zero‑shot generation and unevolved evaluators cannot solve either domain, and removing policy‑search branches degrades performance.  

## Context  
Long‑horizon embodied tasks demand policies that perform many dependent actions before success is observed. Code‑as‑policy allows inspection and revision of decision logic after rollout evaluation. Evolutionary search with large language models can generate variants, but most methods stop at independent generation without a sequential local improvement phase. MEMENTO fills this gap by integrating an evaluator into the evolutionary loop.  

## Implications  
The results show that evolution guided by execution feedback can produce policies suitable for real robot deployment, bridging sim‑to‑real transfer. Practitioners may adopt memory‑guided memetic loops to iteratively improve code‑based agents, reducing reliance on manual engineering and accelerating adaptation across diverse environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22832v1)
