---
title: Experience Graphs: The Data Foundation for Self-Improving Agents
url: http://arxiv.org/abs/2606.29823v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-06-29_06-02-20Z_ExperienceGraphs_TheDataFoundationforSelf_Improvin.md
generated_at: 2026-07-23 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Trellis, a database foundation that treats the experience graph of an agent as first‑class state. By storing artifacts, tool outputs, rewards, sibling comparisons, and causal lineage in a structured database, Trellis enables queries across sessions and materialized views for training data. The authors demonstrate that this approach yields crash recovery, horizontal scaling, and a closed‑loop training flywheel.

## Key Takeaways  
- Experience graphs capture artifacts, tool outputs, rewards, sibling comparisons, and causal lineage across agent steps, forming a structured object rather than disposable JSON checkpoints.  
- Trellis governs these graphs as a durable database state, allowing cross‑session reuse via vector‑seeded graph retrieval and materialized views for training data extraction.  
- The design makes agents stateless compute, resulting in 10× faster cross‑session speedup with 52% lower token cost at Meta’s KernelEvolve accelerator.

## Context  
Long‑horizon AI tasks such as code generation and scientific discovery require persistent memory of exploration history that cannot be captured by ephemeral logs. Existing frameworks treat this experience as disposable state, limiting scalability and the ability to reuse knowledge across sessions or integrate it into training pipelines. Trellis reframes the problem as a database access pattern, aligning AI search with relational data management.

## Implications  
Treating experience graphs as queryable databases transforms inference‑time search from temporary computation to a reliable institutional asset. Practitioners can build cumulative agents that survive crashes and scale horizontally, accelerating research cycles and reducing operational costs in large language model deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.29823v1)
