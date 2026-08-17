---
title: Ontology-Grounded Project Memory for Coding Agents
url: http://arxiv.org/abs/2608.13662v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_18-03-00Z_Ontology_GroundedProjectMemoryforCodingAgents.md
generated_at: 2026-08-16 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MOOSEDev, a system that gives coding agents structured project memory grounded in an ontology. The knowledge graph is exposed through a Model Context Protocol and queried by a neurosymbolic engine called MOOSE, achieving near‑perfect recall on supersession and set‑completeness questions compared with a vector‑memory baseline.

## Key Takeaways
- MOOSEDev’s ontology‑grounded memory yields 0.98–1.00 answer accuracy on supersession, set‑completeness, and negation queries, while the baseline’s top‑k retrieval succeeds only between 6% and 27%.  
- Relevance recall and token cost are comparable between MOOSEDev and the vector‑memory approach, indicating similar computational efficiency.  
- The system supports lifecycle status, provenance, and supersession links, enabling agents to understand why changes were made.

## Context
The rapid generation of code by coding agents creates a flood of changes that is hard to trace, limiting reproducibility and debugging. Traditional memory systems rely on dense vector embeddings, which often lose the structured reasoning needed for project‑level questions. This work bridges that gap with an explicit knowledge graph and a symbolic engine.

## Implications
For software teams, MOOSEDev can improve traceability of code changes, reducing bugs caused by undocumented decisions. In AI research, it demonstrates that neurosymbolic systems can match or exceed vector‑based retrieval in domain‑specific tasks, encouraging broader adoption of structured memory in coding agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13662v1)
