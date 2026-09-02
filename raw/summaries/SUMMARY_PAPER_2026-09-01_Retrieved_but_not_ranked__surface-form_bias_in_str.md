---
title: Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories
url: http://arxiv.org/abs/2609.01556v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-19-57Z_Retrievedbutnotranked_surface_formbiasinstructural.md
generated_at: 2026-09-01 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates surface‑form bias in embedding retrieval by comparing two domains: mathematics problem solving and embodied agent trajectories. The authors find that strict Hit@1 is zero for both production embedders when the correct answer is hidden, while lexical similarity often wins instead of true structural relevance.

## Key Takeaways
- In mathematics, strict Hit@1 is 0.0% with a bootstrap CI [0.0, 0.0] and the correct item appears in the top 10 almost always, yet many misses are driven by lexically similar but structurally irrelevant answers.
- Retrieval performance drops to or below hypergeometric chance when gold requires a different object or receptacle, indicating models latch onto literal tokens rather than task structure.
- An LLM reranker recovers between 5% and 76% of the gap across both domains, showing that surface variation can be adversarial in trajectories but less so in mathematics.

## Context
The study highlights how retrieval systems often prioritize surface cues over underlying semantics, a problem relevant to any domain where meaning is encoded in embeddings. It underscores the need for evaluation beyond simple accuracy metrics and consideration of lexical bias.

## Implications
For practitioners, this research suggests that improving retrieval may require mitigating surface‑form bias through rerankers rather than relying solely on embedding quality. In industry applications, such mitigation can lead to more accurate matching in knowledge bases and autonomous agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01556v1)
