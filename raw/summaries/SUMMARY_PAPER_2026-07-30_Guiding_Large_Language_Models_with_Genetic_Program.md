---
title: Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling
url: http://arxiv.org/abs/2607.27698v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_05-30-09Z_GuidingLargeLanguageModelswithGeneticProgramming_E.md
generated_at: 2026-07-30 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a hybrid approach that uses genetic programming‑evolved heuristic rules to guide large language model decisions in dynamic multi‑mode project scheduling. By extracting knowledge from high‑quality GP rules and injecting it through four mechanisms, the authors improve LLM performance while reducing token usage and enhancing decision stability.

## Key Takeaways
- The extracted GP rules provide a compact source of scheduling knowledge that can be applied directly to online LLM decisions via Feature Selection, Feature Hint, Rule Reference, and Rule Follow.  
- Simplified decision contexts or explicit logic yield better results than merely highlighting important features, with Feature Selection offering the highest token efficiency.  
- Guidance from GP rules stabilizes LLMs’ output and shifts the rationale toward more relevant scheduling attributes.

## Context
Dynamic project scheduling involves uncertain durations, multiple execution modes, and resource limits, making heuristic design challenging for AI systems. Large language models offer flexible interpretation but often lack domain knowledge when operating zero‑shot, leading to high token consumption and unstable outputs. Integrating GP‑derived rules addresses this gap by providing structured, efficient guidance.

## Implications
Practitioners can leverage GP‑evolved heuristics to make LLM‑driven scheduling decisions faster and more reliable without extensive manual rule engineering. This hybrid method could become a standard tool for automating complex project planning workflows in industry settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27698v1)
