---
title: CoEvoKG: Co-Evolving Knowledge Graphs with Self-Evolving Search Agents
url: http://arxiv.org/abs/2608.01904v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_08-39-16Z_CoEvoKG_Co_EvolvingKnowledgeGraphswithSelf_Evolvin.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoEvoKG, a framework that integrates a knowledge graph as both the source of verifiable multihop questions and a persistent evidence memory for self‑evolving search agents. By jointly training a task generator and an agent, CoEvoKG closes the loop between model improvement and knowledge accumulation, achieving significant accuracy gains on multiple QA benchmarks.

## Key Takeaways
- CoEvoKG creates multihop questions from entity chains sampled from a knowledge graph, providing verifiable training tasks that are grounded in factual evidence.  
- The system dedupes successful search results and writes the corresponding evidence back into graph nodes and edges, ensuring future rounds reuse enriched information.  
- Experiments show macro average accuracy improvements of +11.2 to +11.6 points on Qwen2.5‑3B‑Instruct, Qwen2.5‑7B‑Instruct, and Llama‑3.1‑8B‑Instruct compared with baseline models.

## Context
This work tackles a longstanding issue in reinforcement learning for search agents: the tendency to forget learned knowledge after each episode. By embedding persistent evidence into the training loop, CoEvoKG demonstrates how structured graph data can serve as both curriculum and memory, enabling continuous self‑improvement without sacrificing performance.

## Implications
The approach offers a scalable method for continuously enriching AI models with factual knowledge, which is valuable across domains where structured information matters. Practitioners can adopt CoEvoKG to boost search agent accuracy while maintaining realistic training budgets, fostering more reliable and up‑to‑date reasoning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01904v1)
