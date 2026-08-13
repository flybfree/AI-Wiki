---
title: Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem
url: http://arxiv.org/abs/2608.11654v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_04-54-26Z_TowardsaFormalDefinitionofAgentMemory_Basis_Span_O.md
generated_at: 2026-08-12 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a formal framework that defines memory as a basis of knowledge and answerability as a coverage problem. It introduces optimal memory as the capacity‑constrained maximizer of expected coverage and shows how this yields a utility–capacity frontier for comparison. The framework also models memory in a sequential MDP, linking biological analogy to computational agents.

## Key Takeaways
- Memory is treated as a basis that generates knowledge through a span, with answerability defined by whether any single item in the span covers a query.
- Optimal memory maximizes expected coverage under capacity constraints, creating a utility‑capacity frontier used to benchmark systems.
- The framework extends to noisy environments where write policies must infer truth, and it is applied concretely to Homer’s Odyssey to illustrate the concepts.

## Context
This work addresses the lack of unified definitions in large‑model agents that rely on memory, which remain largely empirical. By providing a formal metric—coverage versus precision—the paper bridges theory and practice, offering tools for evaluating and improving memory systems.

## Implications
Practitioners can now measure how well an agent’s memory performs relative to its capacity, guiding design choices. The framework also clarifies the trade‑off between storing more information and maintaining high answerability, informing both research and industry efforts to build reliable AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11654v1)
