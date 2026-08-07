---
title: Hypothesis Testing with Conditional Queries: Learnability and the Value of Interaction
url: http://arxiv.org/abs/2608.06262v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_16-54-10Z_HypothesisTestingwithConditionalQueries_Learnabili.md
generated_at: 2026-08-06 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates a conditional‑query model that must decide which distribution classes to test and how many fixed queries are needed before any response is observed. It proves that learnability occurs only when two classes have positive separation in their pairwise conditional probabilities, otherwise the worst‑case error stays at 1/2. The authors also show that interaction can cut query requirements by a quadratic factor, while non‑adaptive procedures require Ω(N²) queries.

## Key Takeaways
- Learnability is equivalent to having positive separation between the two distribution classes in their conditional probabilities; without it the optimal error remains exactly 1/2 for any finite number of queries.  
- A randomized non‑adaptive procedure using O(N²(T + log(1/ρ))) pair queries can approximate an adaptive transcript within total variation ρ, demonstrating that interaction does not give exponential query advantage despite apparent branching.  
- The gap between fixed and adaptive query complexities is Θ_ε(N²), meaning interaction reduces the required number of tests by a quadratic factor.

## Context
The work addresses a fundamental challenge in AI model evaluation: balancing adaptivity with computational cost when queries must be predetermined. It contributes to theoretical understanding of how conditional probabilities affect test design, offering insights for scalable testing frameworks.

## Implications
For practitioners, this research suggests that designing fixed‑query tests can still achieve near‑optimal performance if the underlying distributions are well separated, reducing the need for costly interactive evaluation loops. The quadratic improvement in query efficiency may enable more reliable and cost‑effective model assessment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06262v1)
